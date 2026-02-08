from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}

@app.post("/login")
async def login(data: Annotated[FormData, Form()]):
    return data

#@app.post("/login/")
#async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    #return {"username": username}

