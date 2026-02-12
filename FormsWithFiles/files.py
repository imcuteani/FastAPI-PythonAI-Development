# Creating a file and form parameters the same way as body and Query parameters in FastAPI 

from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile

# initialize the app variable with FastAPI object 

app = FastAPI()

# Adding the POST method 

@app.post("/files")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return{
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type
    }