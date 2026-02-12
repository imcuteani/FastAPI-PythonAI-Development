# While working with FastAPI Form fields, we need install the package "python-multipart"

# Define Form Fields and Parameters for FastAPI web applications 

from typing import Annotated
from fastapi import FastAPI, Form
# initialize the app variable with FastAPI object

app = FastAPI()

# HTTP POST decorator for login form in FastAPI 

@app.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}