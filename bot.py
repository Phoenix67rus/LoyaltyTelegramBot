import telebot
from keyboards import KeyboardsAll
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
kb = KeyboardsAll()

animals = {
    'cats': {
        'cat1': {
            'name': 'Барсик',
            'description': 'Рыжий, пушистый, милый',
            'age': '1 год'
        },
        'cat2': {'name': 'Пышка',
                 'description': 'шкодливая, игривая кошечка, к лотку приучена',
                 'age': '3 года'
                 }
    },
    'dogs': {
        'dog1': {
            'name': 'Рекс',
            'description': 'Не большой, местис таксы, дружелюбный',
            'age': '3 года'
        },
        'dog2': {
            'name': 'Филя',
            'description': 'Игривый джек рассел, подходит для содержания дома',
            'age': '5 года'
        }
    }
}


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуй, добрый человек! Добро пожаловать в бота приюта "Верность"')


def choice(message):
    chat_id = message.chat.id