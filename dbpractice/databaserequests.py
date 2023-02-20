def get_students(connection):
    with connection.cursor() as cursor:
        getAllStudents = 'SELECT * FROM student'
        cursor.execute(getAllStudents)
        return cursor.fetchall()

def get_student_by_id(connection, studentId):
    with connection.cursor() as cursor:
        getStudentById = f'SELECT * FROM student WHERE id={studentId}'
        cursor.execute(getStudentById)
        return cursor.fetchall()
