# Adding some custom tags, responses and dependencies with File Structure of FastAPI 

# The prefix /items not be added nor the tags=["items"] to each path operation because it's to be added to the APIRouter. 

# But we can still more tags which will be applied to a specific path operation & also some extra responses specific to the path operation. 

from fastapi import APIRouter, Depends, HTTPException

from .dependencies import get_token_header 

# define the router object initialized from APIRouter class 

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404:{"description": "Not Found"}},
)

# define the items database 

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun Fire"}}

# Invoke the Get decorator from router object 

@router.get("/")
async def read_items():
    return fake_items_db

@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db: 
        raise HTTPException(status_code=404, detail="Item not available") 
    return {"name": fake_items_db[item_id]["name"],"item_id":item_id}   
                 

# Adding PUT decorator with the router object 
# 
@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation not allowed"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="The field only can be updated with the item: plumbus"
        )
    return {"item_id": item_id, "name": "The new Plumbus"}
