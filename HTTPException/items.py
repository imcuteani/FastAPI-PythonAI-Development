# To return the HTTP responses with errors to the client 

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Items"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items: 
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}