from typing import Annotated 

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file: 
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}