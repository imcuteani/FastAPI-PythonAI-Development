# Declare the header parameter using the same structure as with PAth, uery and Cookie param. 

from fastapi import FastAPI, Header
from typing import Annotated

# initialize the app variable with FastAPI 

app = FastAPI()

# inject the HTTP GET decorator with endpoint function 

@app.get("/headers")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}