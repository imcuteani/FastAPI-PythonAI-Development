# Adding WebSockets route so that await for messages and can send messages 

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

# initialize the app variable with FastAPI object 

app = FastAPI()

# adding client side HTML code 
html= """
<!DOCTYPE html>
<html>
 <head>
 <title> Chat application with FastAPI Websockets</title>
 </head>
 <body>
  <h1> Websocket CHAT with FastAPI <h1>
  <form action=" " onsubmit="sendMessage(event)">
  <input type="text" id="messageText" autocomplete="off" />
  <button> Send Chat </button>
  </form>
  <ul id='messages'>
  </ul>
  <script>
  var ws = new WebSocket("ws://localhost:8000/ws");
  ws.onmessage = function(event){
  var messages = document.getElementById('messages')
  var message = document.createElement('li)
  var content = document.createTextNode(event.data)
  message.appendChild(content)
  message.appendChild(message)
  };
  function sendMessage(event){
  var input = document.getElementById('messageText')
  ws.send(input.value)
  input value = ' '
  event.preventDefault()
  }
  </script>
  </body>
  </html>
  """

# Adding GET decorator for retrieving CHAT responses 
@app.get("/")
async def get():
    return HTMLResponse(html)

# Adding WebSockets endpoint 
# 
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message Sent Text was: {data}")    
