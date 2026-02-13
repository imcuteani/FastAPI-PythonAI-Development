
from fastapi import APIRouter
from app.crud import create_student



router = APIRouter()

@router.post("/register")
async def register(name: str):
    student = await create_student(name)
    return {"student_id": student.id, "message": f"Welcome, {student.name}!"}
