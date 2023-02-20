import pymysql
from config import host, user, password, db_name
from pymysql.cursors import DictCursor

try:
    connection = pymysql.connect(
    host = host,
    port = 3306,
    user = user,
    db = db_name,
    password = password,
    cursorclass = pymysql.cursors.DictCursor
    )
    print('Connected successfully')

    try:

        # create table
        #with connection.cursor() as cursor:
        #    cursor.execute('DROP TABLE IF EXISTS student')
        #    createTable = '''CREATE TABLE student(
        #        id INT AUTO_INCREMENT PRIMARY KEY,
        #        name VARCHAR(32),
        #        faculty VARCHAR(32)
        #        )'''
        #    cursor.execute(createTable)
        #    print('Table created successfully') 

        # insert data
        #with connection.cursor() as cursor:
        #    inputname = input('Name>>> ')
        #    inputfaculty = input('Faculty>>> ')
        #   insertData = f'INSERT INTO `student`(name, faculty) VALUES ("{inputname}", "{inputfaculty}")'
        #    cursor.execute(insertData)
        #    connection.commit()
        #    print('Data inserted successfully')

        # get names by faculty
        with connection.cursor() as cursor:
            inputquery = input('(get) Faculty>>> ')
            getNamesByFaculty = f'SELECT * FROM student WHERE faculty=\'{inputquery}\''
            cursor.execute(getNamesByFaculty)
            rows = cursor.fetchall()
            for row in rows:
                print(row['name'])
            print('Success')

    finally:
        connection.close()

except Exception as ex:
    print('Connection failed')
    print(ex)

