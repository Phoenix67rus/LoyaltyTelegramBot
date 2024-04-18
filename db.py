from SQL import connection


def dogs_choice(type, characteristics, maintanance):
    cur = connection.cursor()
    cur.execute(
        f"SELECT * FROM Animals WHERE type = '{type}' AND characteristics = "
        f"'{characteristics}' AND maintanance = '{maintanance}'")
    dog = cur.fetchall()
    return dog


def cats_choice(type, characteristics):
    cur = connection.cursor()
    cur.execute(
        f"SELECT * FROM Animals WHERE type = '{type}' AND characteristics = "
        f"'{characteristics}'")
    cat = cur.fetchall()
    return cat
