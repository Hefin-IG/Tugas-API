# Hefin Immanuel Ginting
# 18220065

from http.client import HTTPException
import json
from fastapi import FastAPI
from pydantic import BaseModel

class student_item(BaseModel):
    Nama: str
    NIM: int

data = []

with open("student.json", "r") as read_file: 
    data = json.load(read_file)

app = FastAPI()
@app.get('/student/{NIM}')
async def read_student(NIM: int):
    for student in data['student']:
        if student['NIM'] == NIM:
            return student
    raise HTTPException(
        status_code=404, detail=f'Item not found')

@app.post("/student")
async def add_student(student_new: student_item):
    new_student = [
        {
            "NIM": student_new.NIM,
            "NAMA": student_new.Nama
        }
    ]
    data['student'].append(new_student)
    return data