# Automatic Conversion through HTTP Header Param with FastAPI 

# By default, headers will convert the parameter names character from underscore(_) to hyphen(-) in order to extract 
# and document the headers. 

# HTTP headers are case-insensitive, so we can declare them with standard python style 

# So, when we can use user_agent in normal python code, instead of requiring the put in Upper case User-Agent like similar 

# If for some reason if you need to disable the automatic conversion of underscores to hyphens, then set the parameter 
# convert_underscores of Header to False: 

from typing import Annotated
from fastapi import FastAPI, Header

# initialize the app variable with FastAPI object 

app = FastAPI()

# Inject the HTTP Get decorator with endpoint function

@app.get("/items")

# Added the "convert_underscores as False just to disable the header user agent from automated conversion of underscores to hyphen"
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None, 

): 
    return {"strange_header": strange_header}
