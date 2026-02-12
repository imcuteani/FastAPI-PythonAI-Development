# Create a oath2_scheme to check the token URL for JWT password beaer token

# Importing FastAPI security packages from fastapi.security module
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer 

# initialize the app variable with FastAPI object 

app = FastAPI()

# define the oath2_scheme 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# HTTP Get method 
@app.get("/items")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
