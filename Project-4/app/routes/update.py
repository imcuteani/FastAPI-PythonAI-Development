from fastapi import APIRouter
from app.crud import update_progress



router = APIRouter()

@router.post("/update/{student_id}")
async def update(student_id: str, week: str):
    student = await update_progress(student_id, week)
    return {"message": f"Progress updated for {week}", "student": student}
