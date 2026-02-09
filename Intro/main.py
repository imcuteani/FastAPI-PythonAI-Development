# Import FastAPI

from fastapi import FastAPI

app = FastAPI()

# The HTTP Get method invoked 

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}