from fastapi import APIRouter
app = APIRouter()
@app.get("/")
async def hello() -> dict:
    return {
    "message": "Hello World"
    }
student_list = []
@app.post("/student")
async def add_student(student: dict) -> dict:
student_list.append(student)
return {"message": "Sucess"}
@app.get("/student")
async def get_student() -> dict:
return {"student": student_list}