# Pydantic automatic serlization 

from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float 
    is_offer: bool | None = None

@app.get("/items/{item_id}")
async def read_item(item_id: int):
     # FastAPI automatically serializes this Pydantic model instance to JSON 
     # It will return the Item, price and Offer details
     return Item(name="Foo", price=10.5, is_offer=True)