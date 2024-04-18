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
        btn1 = types.KeyboardButton('Собака')
        btn2 = types.KeyboardButton('Кошка')
        kb.row(btn1, btn2)
        return kb

    def dogs_kb(self):
        """
        Выбор размера собаки
        """
        dog_kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Крупная', callback_data='Большая')
        btn2 = types.InlineKeyboardButton(
            'Средняя', callback_data='Средняя')
        btn3 = types.InlineKeyboardButton(
            'Мелкая', callback_data='Маленькая')
        dog_kb.add(btn1, btn2, btn3)
        return dog_kb

    def dog_maintenance_kb(self):
        """
        Клавиатура вида содержания собаки
        """
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Дворовое', callback_data='Двор')
        btn2 = types.InlineKeyboardButton(
            'Квартирное', callback_data='Дом/квартира')
        keyboard.add(btn1, btn2)
        return keyboard

    def cats_kb(self):
        """
        Клавиатура выбора котов
        """
        color_kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'Породистые', callback_data='Породистая')
        btn2 = types.InlineKeyboardButton(
            'Дворовые', callback_data='Простая')
        color_kb.add(btn1, btn2)
        return color_kb

    def actions_kb(self):
        """
        Клавиатура выбора действий
        """
        act_kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            'На главную', callback_data='На главную')
        btn2 = types.InlineKeyboardButton(
            'Выбрали? Свяжитесь с нами!', url='https://vk.com/vernosttv')
        act_kb.add(btn1, btn2)
        return act_kb
