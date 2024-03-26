import telebot
from keyboards import KeyboardsAll
from config import TOKEN
from db import dogs_choice

bot = telebot.TeleBot(TOKEN)
kb = KeyboardsAll()
temp_data = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     'Здравствуй, добрый человек!\n'
                     'Добро пожаловать в бота приюта "Верность"\n'
                     'Выберите себе любимца',
                     reply_markup=kb.main_kb())
    temp_data[message.chat.id] = {}

@bot.message_handler()
def get_data_with_main_kb(message):
    """
    Принимает данные из стартовой клавиатуры.
    Осуществляет связь со следующими функциями и клавиатурами.
    """
    if message.text == 'Собака':
        bot.send_message(message.chat.id,
                         'Собаку какого размера Вы хотите?',
                         reply_markup=kb.dogs_kb())
    elif message.text == 'Кошка':
        bot.send_message(
            message.chat.id,
            'Выберите породу',
            reply_markup=kb.cats_kb())
    temp_data[message.chat.id]['type'] = message.text

@bot.callback_query_handler(func=lambda call: call.data in ('Большая', 'Маленькая', 'Средняя'))
def get_size(call):
    message = call.message
    bot.send_message(message.chat.id,
                     'Где планируете держать собаку?',
                     reply_markup=kb.dog_maintenance_kb())
    temp_data[message.chat.id]['size'] = call.data


@bot.callback_query_handler(func=lambda call: call.data in ('Двор', 'Дом/квартира'))
def get_maintanance(call):
    message = call.message
    for i in dogs_choice(temp_data[message.chat.id]['type'], temp_data[message.chat.id]['size'], call.data):
        bot.send_message(message.chat.id, f'{i[4]} {i[6]}')
