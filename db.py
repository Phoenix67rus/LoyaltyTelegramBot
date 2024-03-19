import pymysql

connection = pymysql.connect(host='147.45.105.54',
                             user='gen_user',
                             password='mfohmdu%E3$b\k',
                             database='LoyaltyBase',
                             port=3306)
with connection:
    cur = connection.cursor()
