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
    bot.send_message(message.chat.id,
                     'Здравствуй, добрый человек!\nДобро пожаловать в бота приюта "Верность"\n'
                     'Выберите себе любимца',
                     reply_markup=kb.main_kb())

@bot.message_handler()
def get_data_with_main_kb(message):
    """
               Принимает данные из стартовой клавиатуры.
               Осуществляет связь со следующими функциями и клавиатурами.
               """
    if message.text == 'Собаки':
        bot.send_message(message.chat.id,
                         'Собаку какого размера Вы хотите?',
                         reply_markup=kb.dogs_kb())
    elif message.text == 'Кошки':
        bot.send_message(
            message.chat.id,
            'Выберите окрас',
            reply_markup=kb.cats_kb())
