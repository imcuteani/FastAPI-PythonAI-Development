# FastAPI code with SQLite to create database table. 

from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

# Define class with arguments SQLModel and table
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name:str

# define the SQLite db and filename

sqlite_file_name = "database_1.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

# create db & table 

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session 

# Create Session dependency in FastAPI 

SessionDep = Annotated[Session, Depends(get_session)]

# initialize the app variable with FastAPI object 

app = FastAPI()

# define the startup events 

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

async def lifespan(app: FastAPI):
    try: 

        print("database startup tasks are completed")
        yield
    finally:
        print("Closing the connection pool")
        engine.dispose()

app = FastAPI(lifespan=lifespan)            


# Define the HTTP Post decorator 

@app.post("/heroes")
def create_hero(hero: Hero, session: SessionDep) -> Hero: 
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero



