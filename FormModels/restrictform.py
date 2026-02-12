# This code will decomstrate how to restrict the form fields to only those fields declared in the Pydantic model. 
# Any extra fields will be forbidden. 
# 
# We can use the Pydantic's model configuration's to forbid any extra / additional form fields. 

from typing import Annotated
from fastapi import FastAPI, Form 
from pydantic import BaseModel 

# Initialize the app variable with FastAPI object 

app = FastAPI()

# Class with FormData inherited from the BaseModel class with UserName and Password fields and should restrict any extra fields

class FormData(BaseModel): 
    username: str 
    password: str 
    model_config = {"extra": "forbid"}

# HTTP post method to define the form data 
# 
@app.post("/restrictform")
async def restrictform(data: Annotated[FormData, Form()]):
    return data    
  