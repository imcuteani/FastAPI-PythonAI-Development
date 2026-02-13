# put them in their own dependencies module (./dependencies.py)

from typing import Annotated
from fastapi import Header, HTTPException

# define the get_token_header method

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "harry":
        raise HTTPException(status_code=400, detail="No Harry token provided")