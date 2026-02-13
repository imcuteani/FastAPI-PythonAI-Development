from app.database import student_collection
from app.models import Student
from uuid import uuid4

async def create_student(name: str):
    student_id = str(uuid4())
    student = Student(id=student_id, name=name)
    await student_collection.insert_one(student.dict())
    return student

async def get_student(student_id: str):
    return await student_collection.find_one({"id": student_id})

async def update_progress(student_id: str, week: str):
    await student_collection.update_one(
        {"id": student_id},
        {"$set": {f"progress.{week}": True}}
    )
    return await get_student(student_id)
