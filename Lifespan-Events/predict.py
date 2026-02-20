# LifeSpan events for FastAPI 

# The same ML model are shared among requests, so it's not one model per request or one per user or something similar. 

# load the ML model before the request are handled but only right before the application starts receiving requests & not while the code is being loaded. 

# you can use lifespan events through lifespan parameter for startup and shutdown of FastAPI app and a "content manager"

# the lifespan() method can be invoked using yield 

from contextlib import asynccontextmanager

from fastapi import FastAPI

# here we're simulating the startup operation of loading the model by putting the false() model function in the dict with ML models before the yield object. 
# the code will be executed before the application starts taking requests during the startup. 

# then after the yield , model is uploaded, the code will be executed after the app finishes the handling requests right before the shutdown. 
# releasing resources like GPU / memory. 

def false_answer_to_everything_ml_model(x: float):
    return x * 40 

ml_models = {}

# define asynccontextmanager class & initialize it 
@asynccontextmanager
async def lifespan(app: FastAPI):
    # load the ML model
    ml_models["answer_to_everything"] = false_answer_to_everything_ml_model
    yield

    # Clean up the ML models and release the resources 
    ml_models.clear()

# lifespan parameter of the FastAPI app takes the async content manager so we can pass our new lifespan async context manager to it. 
app = FastAPI(lifespan=lifespan)   

# GET decorator added 

@app.get("/predict")
async def predict(x: float):
    result = ml_models["answer_to_everything"](x)
    return {"result": result}
