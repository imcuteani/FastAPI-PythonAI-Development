from pydantic import BaseModel
from typing import Optional, Dict

class Student(BaseModel):
    id: str
    name: str
    progress: Dict[str, bool] = {}
