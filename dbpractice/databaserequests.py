def get_students(connection):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM student')
        return cursor.fetchall()

def get_student_by_id(connection, studentId):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM student WHERE id={studentId}')
        return cursor.fetchall()

def create_student(connection, new_student):
    with connection.cursor() as cursor:
        cursor.execute(f'INSERT INTO student (name, faculty) VALUES ("{new_student.name}","{new_student.faculty}")')
        connection.commit()
        return {'Successfully':'added'}
