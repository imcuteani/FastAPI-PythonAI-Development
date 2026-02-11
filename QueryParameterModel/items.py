# Declare the Query parameter with the Pydantic model 

from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field 

app = FastAPI()

# Declare the class inherting the BaseModel class in Pydantic 
# In some scenario, we can restrict the query parameters which we can specify to define in the query string. 
# In Pydantic model configuration, it can be declared to use Pydantic model config to forbid any extra field in the query parameter



class QueryParamModel(BaseModel):
    model_config = {"extra": "forbid"}
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []



# inject the model function into the final endpoint function 

@app.get("/items")
async def read_items(filter_query: Annotated[QueryParamModel, Query()]):
    return filter_query
