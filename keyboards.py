"""
В данном файле собраны клавиатуры, используемые в данном проекте
"""
from telebot import types


class KeyboardsAll:
    def main_kb(self):
        """
        Выбор вида животного (стартовая клавиатура)
        """
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Собаки')
        btn2 = types.KeyboardButton('Кошки')
        kb.row(btn1, btn2)
        return kb

    def dogs_kb(self):
        """
        Выбор размера собаки
        """
        dog_kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Крупная', callback_data='Big')
        btn2 = types.InlineKeyboardButton('Средняя', callback_data='Middle')
        btn3 = types.InlineKeyboardButton('Мелкая', callback_data='Small')
        dog_kb.add(btn1, btn2, btn3)
        return dog_kb

    def dog_maintenance_kb(self):
        """
        Клавиатура вида содержания собаки
        """
        maintenance = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Дворовое', callback_data='yard')
        btn2 = types.InlineKeyboardButton('Квартирное', callback_data='apartment')
        maintenance.add(btn1, btn2)
        return maintenance

    def cats_kb(self):
        """
        Клавиатура выбора цвета котов
        """
        color_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Одноцветные')
        btn2 = types.KeyboardButton('Цветные')
        color_kb.row(btn1, btn2)
        return color_kb
