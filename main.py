# in the main router file mainrouter.py

from fastapi import FastAPI 
from routers import users

app = FastAPI()

# the include_router method to organize the API into seperate, modular files which're required for fullstack FastAPI apps
app.include_router(users.router)