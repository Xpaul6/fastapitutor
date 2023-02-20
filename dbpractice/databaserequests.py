from pymysql.cursors import DictCursor

def get_students(connection):
    with connection.cursor() as cursor:
        getAllStudents = 'SELECT * FROM student'
        cursor.execute(getAllStudents)
        rows = cursor.fetchall()
        return rows

def get_student_by_id(connection, studentId):
    with connection.cursor() as cursor:
        getStudentById = f'SELECT * FROM student WHERE id={studentId}'
        cursor.execute(getStudentById)
        row = cursor.fetchall()
        return row