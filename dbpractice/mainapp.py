from fastapi import FastAPI
from pydantic import BaseModel
from config import connection
import databaserequests

class Student(BaseModel):
    name: str
    faculty: str


app = FastAPI()

@app.get('/')
async def index():
    return {'index':'page'}

@app.get('/get-students')
async def get_students():
    return databaserequests.get_students(connection)

@app.get('/get-student-by-id/{studentId}')
async def get_student_by_id(studentId: int):
    return databaserequests.get_student_by_id(connection, studentId)

@app.post('/create-student')
async def create_student(new_student: Student):
    return databaserequests.create_student(connection, new_student)
