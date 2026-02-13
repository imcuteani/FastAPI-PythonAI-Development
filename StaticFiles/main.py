# create the Static Files with FastAPI 

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 

# initialize the app variable with FastAPI object 

app = FastAPI()

# Mount the "static" directory to the "/static" path

app.mount("/static", StaticFiles(directory="static"), name="static")

# API routes through the GET decorator

@app.get("/")
def read_root():
    return {"message": "Hello Static Files with FastAPI"}