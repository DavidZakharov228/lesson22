import vk_api
from vk_api import longpoll
import random
import requests
from bs4 import BeautifulSoup

# Авторизация в VK API
vk_session = vk_api.VkApi(token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
vk = vk_session.get_api()

# Функция для получения города для хода бота
def get_city(last_letter):
    url = f'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cities = []
    for link in soup.find_all('a'):
        if link.has_attr('title'):
            city = link.get('title')
            if city.startswith(last_letter.upper()):
                cities.append(city)
    return random.choice(cities)

# Функция для проверки, является ли слово городом
def is_city(word):
    url = f'https://ru.wikipedia.org/wiki/{word}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    if 'не найдена' in title:
        return False
    else:
        categories = soup.find_all('div', {'class': 'mw-normal-catlinks'})
        for category in categories:
            if 'города' in category.text:
                return True
    return False

# Функция для игры в города
def play_game(peer_id):
    vk.messages.send(peer_id=peer_id, message='Начинаем игру в города!\nВведите город:')
    last_letter = ''
    while True:
        response = vk.messages.get(peer_id=peer_id)
        message = response['items'][0]['text']
        if message.lower() == 'стоп':
            vk.messages.send(peer_id=peer_id, message='Игра окончена')
            break
        if not is_city(message):
            vk.messages.send(peer_id=peer_id, message='Это не город\nВведите город:')
            continue
        if last_letter and message[0].lower() != last_letter:
            vk.messages.send(peer_id=peer_id, message=f'Город должен начинаться на букву "{last_letter}"\nВведите город:')
            continue
        last_letter = message[-1].lower()
        vk.messages.send(peer_id=peer_id, message=f'Мой ход: {get_city(last_letter)}\nВведите город:')

# Основной цикл программы
while True:
    longpoll = vk_api.longpoll.VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == vk_api.longpoll.EventType.MESSAGE_NEW and event.to_me:
            peer_id = event.peer_id
            message = event.text.lower()
            if message == 'играть в города':
                play_game(peer_id)