# The upload file operation in FstAPI 

import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException, status

app = FastAPI() 

# Specifying Max file size 

MAX_FILE_SIZE = 100 * 1024 * 1024 # 100 MB of file size 

# posting the HTTP POST decorator 

@app.post("/upload-file")
async def create_upload_file(file: UploadFile = File(...)):
    # optional: check of Content-header for early rejection 
    # robust way to check if file uploading is done in the streaming loop 

    file_path = f"uploads/{file.filename}"
    try: 
        size = 0
        with open(file_path, "wb") as buffer: 
            while chunk := await file.read(1024*1024): # read 1 MB of chunks 
              size += len(chunk)
              if size > MAX_FILE_SIZE: 
                raise HTTPException(
                    status_code=status.HTTP_413_CONTENT_TOO_LARGE,
                    detail=f"File is too large.Maximum size is {MAX_FILE_SIZE / 1024 / 1024} MB"
                )
            buffer.write(chunk)
    except HTTPException: 
        # Clean up the file if an error is encountered during upload 
        import os
        if os.path.exists(file_path):
            os.remove(file_path)
        raise
    finally:
        await file.close()

        return {"filename": file.filename, "size": size}             
