from fastapi import APIRouter
from app.crud import get_student

router = APIRouter()

@router.get("/status/{student_id}")
async def status(student_id: str):
    student = await get_student(student_id)
    if not student:
        return {"error": "Student not found"}
    return student
