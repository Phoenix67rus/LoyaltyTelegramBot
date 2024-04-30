"""
Модуль осуществляет поиск в базе данных по заданным характеристикам
"""
from SQL import connection


def dogs_choice(type_: str, characteristics: str, maintenance: str) -> tuple:
    """
    Функция принимает в качестве аргументов данные с различных клавиатур
    и осуществляет выбор собак по заданным параметрам

    Args:
        type_: данные с клавиатуры выбора вида животного(стартовая клавиатура),
        characteristics: данные с клавиатуры выбора размера собаки(dogs_kb),
        maintenance: данные с клавиатуры содержания собаки.

    Returns:
        tuple: хранит в себе данные из строк таблицы с заданными параметрами
    """
    cur = connection.cursor()
    cur.execute(
        f"SELECT * FROM Animals WHERE type = '{type_}' AND characteristics = "
        f"'{characteristics}' AND maintanance = '{maintenance}'")
    dog = cur.fetchall()
    return dog


def cats_choice(type_: str, characteristics: str) -> tuple:
    """
    Функция принимает в качестве аргументов данные с различных клавиатур
    и осуществляет выбор кошек по заданным параметрам

    Args:
        type_: данные с клавиатуры выбора вида животного(стартовая клавиатура),
        characteristics: данные с клавиатуры выбора породы кошки(cats_kb),

    Returns:
        tuple: хранит в себе данные из строк таблицы с заданными параметрами
    """
    cur = connection.cursor()
    cur.execute(
        f"SELECT * FROM Animals WHERE type = '{type_}' AND characteristics = "
        f"'{characteristics}'")
    cat = cur.fetchall()
    return cat
