import pymysql
from config import host, user, password, db_name
from pymysql.cursors import DictCursor

try:
    connection = pymysql.connect(
    host = host,
    port = 3306,
    user = user,
    password = password,
    db = db_name,
    cursorclass = pymysql.cursors.DictCursor
    )
    print('Connected successfully')

    try:
        with connection.cursor() as cursor:
            getCityList = 'SELECT * FROM sakila.city'
            cursor.execute(getCityList)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        connection.close()

except Exception as ex:
    print('Connection failed')
    print(ex)

