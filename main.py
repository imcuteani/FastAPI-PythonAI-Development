# in the main router file mainrouter.py

from fastapi import Depends, FastAPI 
from routers import users, items
from routers.dependencies import get_query_token, get_token_header
#from routers import items, users


app = FastAPI(dependencies=[Depends(get_query_token)])

# the include_router method to organize the API into seperate, modular files which're required for fullstack FastAPI apps
# app.include_router(users.router)

app.include_router(users.router)
app.include_router(items.router)

# Adding GET Operator 

@app.get("/")
async def root():
    return{"message": "Hello From FastAPI Multiple File Structure!"}


