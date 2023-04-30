import vk_api
import datetime
import wikipedia
import re
from vk_api.longpoll import VkLongPoll, VkEventType


# Функция для отправки сообщения пользователю
def send_message(chat_id, message):
    vk.messages.send(
        chat_id=chat_id,
        message=message,
        random_id=vk_api.utils.get_random_id()
    )


# Функция для обработки сообщений
def handle_message(chat_id, message):
    # Проверяем, есть ли в сообщении слово "сейчас"
    if "сейчас" in message:
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
        response = f"Сегодня {now.strftime('%d.%m.%Y')}\nТекущее время: {now.strftime('%H:%M:%S')}\nДень недели: {now.strftime('%A')}"
        send_message(chat_id, response)
    # Проверяем, есть ли в сообщении слово "википедия"
    elif "википедия" in message.lower():
        try:
            page = wikipedia.page(query)
            summary = wikipedia.summary(query)
            send_message(event.peer_id, summary)
        except:
            send_message(event.peer_id,
                         'Извините, я не смог найти информацию по вашему запросу')

        send_message(event.peer_id, 'Хотите узнать что-то еще? (Да/Нет)')

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                answer = event.text.lower()

                if answer == 'да':
                    break
                else:
                    send_message(event.peer_id, 'Спасибо за обращение!')
                    break
    # Проверяем, является ли сообщение примером
    elif re.match(r'\d+\s*[+*\/-]\s*\d+', message):
        result = eval(message)
        send_message(chat_id, f"{message} = {result}")
    # Если ничего не подошло, просто приветствуем пользователя
    else:
        name = vk.users.get(user_id=event.user_id)[0]['first_name']
        city = vk.users.get(user_id=event.user_id, fields='city')[0].get('city', {}).get('title')
        message = f"Привет, {name}!"
        if city:
            message += f" Как поживает {city}?"
        vk.messages.send(
            peer_id=event.peer_id,
            message=message,
            random_id=0
        )


# Авторизуемся в ВКонтакте
vk_session = vk_api.VkApi(
    token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
vk = vk_session.get_api()

# Получаем Long Poll сервер
long_poll = vk_api.longpoll.VkLongPoll(vk_session)

# Обрабатываем новые сообщения
for event in long_poll.listen():
    if event.type == vk_api.longpoll.VkEventType.MESSAGE_NEW:
        chat_id = event.chat_id
        message = event.text
        handle_message(chat_id, message)
