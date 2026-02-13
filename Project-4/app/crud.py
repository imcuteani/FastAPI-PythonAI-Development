from app.database import student_collection
from app.models import Student
from uuid import uuid4

async def create_student(name: str):
    student_id = str(uuid4())
    student = Student(id=student_id, name=name)
    await student_collection.insert_one(student.dict())
    return student

async def get_student_progress(name: str):
    return await student_collection.find_one({"name": name})

async def update_student_progress(name: str, week: str, status: str):
    result = await student_collection.update_one(
        {"name": name},
        {"$set": {f"progress.week{week}": status}}
    )
    if result.modified_count == 0:
       return None
    return await student_collection.find_one({"name" : name})


async def count_students():
    return await student_collection.count_documents({})
