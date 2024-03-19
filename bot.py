import telebot
from keyboards import KeyboardsAll
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
kb = KeyboardsAll()


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     'Здравствуй, добрый человек!\n'
                     'Добро пожаловать в бота приюта "Верность"\n'
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
            'Выберите породу',
            reply_markup=kb.cats_kb())
