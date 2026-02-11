# Cookie parameters can be used as same way to define Query & Path params

# import the Cookie 
from typing import Annotated
from fastapi import Cookie, FastAPI

# initialize the app variable with FastAPI object 
app = FastAPI()

# Inject the HTTP GET model function in the endpoint function

@app.get("/cookies")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}