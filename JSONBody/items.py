# Update the JSON encoding of FastAPI with HTTP PUT operation 

# You can use the jsonable_encoder to convert the input data to the data which can be stored as JSON (e.g. with a NOSQL db)
# for e.g. conversion of datetime to str type etc. 

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

# Declaration of class 

class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5 
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2}, 
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.5, "tax": 10.5, "tag": []}, 
} 

# Decleration of Get decorator 

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]