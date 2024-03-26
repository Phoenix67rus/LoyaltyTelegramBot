import pymysql

connection = pymysql.connect(host='147.45.105.54',
                             user='gen_user',
                             password='mfohmdu%E3$b\k',
                             database='LoyaltyBase',
                             port=3306)
def dogs_choice(type, size, maintanance):
    with connection:
        cur = connection.cursor()
        cur.execute(f"SELECT * FROM Animals WHERE type = '{type}' AND size = "
                    f"'{size}' AND maintanance = '{maintanance}'")
        dog = cur.fetchall()
        return dog

