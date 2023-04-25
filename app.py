import vk_api
import requests
import re



vk_session = vk_api.VkApi(token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
vk = vk_session.get_api()

# Функция для получения списка городов по первой букве
def get_cities_by_letter(letter):
    url = f'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_{letter.upper()}_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'
    response = requests.get(url)
    cities = re.findall(r'title="([^"]+)"', response.text)
    return [city for city in cities if ',' not in city]

# Функция для получения последнего города из сообщения
def get_last_city(text):
    words = text.split()
    for i in range(len(words) - 1, -1, -1):
        if words[i].isalpha():
            return words[i]
    return None

# Функция для отправки сообщения с городом
def send_city_message(peer_id, city):
    vk.messages.send(peer_id=peer_id, message=f'Мой ход: {city}', random_id=0)

# Основной цикл бота
while True:
    # Получение новых сообщений
    response = vk.messages.getConversations(count=20, filter='unread')
    if response['count'] > 0:
        items = response['items']
        for item in items:
            message = item['last_message']
            text = message['text']
            peer_id = message['peer_id']

            # Если сообщение не является командой "город", пропускаем его
            if not text.startswith('город'):
                continue

            # Получаем последний город из сообщения игрока
            last_city = get_last_city(text)

            # Если это первый ход, выбираем случайный город
            if last_city is None:
                city = 'Москва'
            else:
                # Получаем первую букву последнего города и ищем следующий город на эту букву
                letter = last_city[-1].lower()
                cities = get_cities_by_letter(letter)
                if len(cities) == 0:
                    vk.messages.send(peer_id=peer_id, message='Я не знаю больше городов на эту букву :(', random_id=0)
                    continue
                city = cities[0]

            # Отправляем сообщение с городом
            send_city_message(peer_id, city)