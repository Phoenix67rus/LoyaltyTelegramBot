"""
Основной модуль программы, содержит логику работы бота, взаимодействия его с
базой данных посредством нажатия на кнопки клавиатур
"""
import telebot
from keyboards import KeyboardsAll
from config import TOKEN
from db import dogs_choice, cats_choice

bot = telebot.TeleBot(TOKEN)
kb = KeyboardsAll()
temp_data = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    """
    Функция отлавливает команду /start, после чего выдает приветственное
    сообщение и выводит стартовую клавиатуру main_kb
    """
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
    Сохраняет выбор в словаре temp_data.
    """
    bot.send_message(message.chat.id,
                     'Отличный выбор, продолжаем!',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    if message.text == '🐕 Собака':
        bot.send_message(message.chat.id,
                         'Собаку какого размера Вы хотите?',
                         reply_markup=kb.dogs_kb())
    elif message.text == '🐈 Кошка':
        bot.send_message(
            message.chat.id,
            'Выберите породу',
            reply_markup=kb.cats_kb())
    temp_data[message.chat.id]['type'] = message.text


@bot.callback_query_handler(
    func=lambda call: call.data in ('Большая', 'Маленькая', 'Средняя'))
def get_characteristics(call):
    """
    Данная функция обрабатывает выбор с клавиатуры dogs_kb, сохраняет выбор
    в словаре temp_data
    """
    message = call.message
    bot.send_message(message.chat.id,
                     'Где планируете держать собаку?',
                     reply_markup=kb.dog_maintenance_kb())
    temp_data[message.chat.id]['characteristics'] = call.data


@bot.callback_query_handler(
    func=lambda call: call.data in ('Двор', 'Дом/квартира'))
def get_maintenance(call):
    """
    Функция принимает данные с клавиатуры dog_maintenance_kb(),
    после чего проходит циклом
    по кортежу, который возвращает функция dogs_choice, для последовательной
    отправки пользователю сообщений с информацией об имеющихся в приюте
    собаках, по выбранным пользователем параметрам
    """
    message = call.message
    for i in dogs_choice(temp_data[message.chat.id]['type'],
                         temp_data[message.chat.id]['characteristics'],
                         call.data):
        with open(i[-1], 'rb') as file:
            photo = file.read()
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, f'Имя: {i[4]}\n'
                                          f'Возраст: {i[5]}\n'
                                          f'Описание: {i[6]}\n')
    bot.send_message(message.chat.id,
                     'Выберите действие',
                     reply_markup=kb.actions_kb())


@bot.callback_query_handler(
    func=lambda call: call.data in ('Породистая', 'Простая'))
def get_cat(call):
    """
    Функция принимает данные с клавиатуры cats_kb(),
    после чего проходит циклом
    по кортежу, который возвращает функция cats_choice, для последовательной
    отправки пользователю сообщений с информацией об имеющихся в приюте
    кошках, по выбранным пользователем параметрам
    """
    message = call.message
    for i in cats_choice(temp_data[message.chat.id]['type'],
                         call.data):
        with open(i[-1], 'rb') as file:
            photo = file.read()
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, f'Имя: {i[4]}\n'
                                          f'Возраст: {i[5]}\n'
                                          f'Описание: {i[6]}\n')
    bot.send_message(message.chat.id,
                     'Выберите действие',
                     reply_markup=kb.actions_kb())


@bot.callback_query_handler(
    func=lambda call: call.data == 'На главную')
def action(call):
    """
    Принимает данные с клавиатуры действий и при нажатии клавиши "на главную",
    возвращает клавиатуру выбора типа животного
    """
    message = call.message
    bot.send_message(message.chat.id,
                     'Выберите себе любимца',
                     reply_markup=kb.main_kb())
    temp_data[message.chat.id] = {}
