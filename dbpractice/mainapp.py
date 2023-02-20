from fastapi import FastAPI
from config import host, user, password, db_name, connection
import databaserequests


app = FastAPI()

@app.get('/get-students')
async def get_students():
    return databaserequests.get_students(connection)

@app.get('/get-student-by-id/{studentId}')
async def get_student_by_id(studentId: int):
    return databaserequests.get_student_by_id(connection, studentId)
