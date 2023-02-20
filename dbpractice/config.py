import pymysql

host = 'localhost'
user = 'user'
password = '1337228'
db_name = 'students'

connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        db = db_name,
        password = password,
        cursorclass = pymysql.cursors.DictCursor
        )
