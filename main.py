"""
Модуль осуществляет запуск бота.
"""

if __name__ == '__main__':
    from bot import bot

    print('Бот запущен!')
    bot.infinity_polling()
