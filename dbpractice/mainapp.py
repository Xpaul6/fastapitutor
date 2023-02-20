from fastapi import FastAPI
from config import host, user, password, db_name
import pymysql
from pymysql.cursors import DictCursor
import databaserequests



app = FastAPI()
connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        db = db_name,
        password = password,
        cursorclass = pymysql.cursors.DictCursor
        )

@app.get('/get-students')
async def get_students():
    return databaserequests.get_students(connection)

@app.get('/get-student-by-id/{studentId}')
async def get_student_by_id(studentId: int):
    return databaserequests.get_student_by_id(connection, studentId)
