# The APIRouter class inherits from the main fastapi module

from fastapi import APIRouter 

# initialize the router object from APIRouter() method

router = APIRouter()

# Retrive the Router Get response 

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Monty"}]

@router.get("/users/me", tags=["users"])
async def read_users_me():
    return {"username": "fakelatestuser"}

# retrieve the username with the respective users through APIRouter class 
# 
@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}        