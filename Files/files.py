from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}

        