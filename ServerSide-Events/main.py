# SSE in FastAPI is typically implemented using StreamingResponse with an 
# async generator. The library required is sse_starletter library. 

from fastapi import FastAPI, Request, UploadFile, File, HTTPException, Status
from fastapi.responses import StreamingResponse
import asyncio
from datetime import datetime, timedelta
import time

app = FastAPI()

html= """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
    <script>
const eventSource = new EventSource("http://localhost:8000/stream");

eventSource.onmessage = function(event) {
  console.log("Received data:", event.data);
};

eventSource.onerror = function(error) {
  console.error("EventSource failed:", error);
  eventSource.close();
};
</script>
</body>
</html>
"""

MAX_FILE_SIZE = 100 * 1024 * 1024 # 100 MB of file size in bytes 

@app.get("/stream")
async def stream_events(request: Request):
    async def event_generator():
        while True:
            if await request.is_disconnected():
                break
            # Send a real time update 
            data = f"event: message\ndata: The current time is {time.strftime('%X')}\n\n"
            yield data 
            await asyncio.sleep(1) # Send update every 1 second

    return StreamingResponse(event_generator(), media_type="text/event-stream")         