# the code to demonstrate the Cross origin Resource Sharing through FastAPI 
# security feature implemented by browsers which restricts the web apps running under one domain from making requests 
# to another domain. 

# FastAPI provides built-in support for CORS and pre-flight request Options and content headers to validate the 
# HTTP request headers before triggering the actual request. 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# initialize the app variable with FastAPI object 

app = FastAPI()

# CORS (cross-origin resource sharing) middleware configuration 

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://www.microsoft.com",
    "https://www.google.com",
    "https://aws.amazon.com",

]

# invoking the add_middleware method to allow origins and methods for FastAPI 
# FastAPI supports the following types of arguments - 

# - allow_origins -> list of origins should be permitted to make cross-origin requests. The wildcard is supported but not recommended. 
# - allow_origin_regex -> a regex string to match against origins which should be permitted to make cross-origin requests. 
# - allow_headers -> list of HTTP headers which should be allowed to support for cross-origin requests. 
# - allow_credentials -> defines the cookies to be supported for cross-origin request, default is False. 
# - expose_headers -> indicate any response headers which should be made accessible to be browser. 
# - max_age -> Sets up a max time limit in sec for browsers to cache the CORS responses. Default is 600 sec.  


app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)

# Adding GET decorator with HTTP verb 
# 
@app.get("/")
async def main():
    return {"message-": "Hello FastAPI CORS"}

@app.get("/items/{item_id}") 
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
