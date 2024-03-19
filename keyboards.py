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
        btn1 = types.InlineKeyboardButton(
            'Крупная', callback_data='Big')
        btn2 = types.InlineKeyboardButton(
            'Средняя', callback_data='Average')
        btn3 = types.InlineKeyboardButton(
            'Мелкая', callback_data='Small')
        dog_kb.add(btn1, btn2, btn3)
        return dog_kb

    def dog_big_maintenance_kb(self):
        """
        Клавиатура вида содержания собаки
        """
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Дворовое', callback_data='yard_big')
        btn2 = types.InlineKeyboardButton(
            'Квартирное', callback_data='apartment_big')
        keyboard.add(btn1, btn2)
        return keyboard

    def dog_average_maintenance_kb(self):
        """
        Клавиатура вида содержания собаки
        """
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Дворовое', callback_data='yard_average')
        btn2 = types.InlineKeyboardButton(
            'Квартирное', callback_data='apartment_average')
        keyboard.add(btn1, btn2)
        return keyboard

    def dog_small_maintenance_kb(self):
        """
        Клавиатура вида содержания собаки
        """
        maintenance = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Дворовое', callback_data='yard_small')
        btn2 = types.InlineKeyboardButton(
            'Квартирное', callback_data='apartment_small')
        maintenance.add(btn1, btn2)
        return maintenance

    def cats_kb(self):
        """
        Клавиатура выбора цвета котов
        """
        color_kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Породистые', callback_data='Purebred_cat')
        btn2 = types.InlineKeyboardButton(
            'Дворовые', callback_data='Ordinary_cat')
        color_kb.add(btn1, btn2)
        return color_kb
