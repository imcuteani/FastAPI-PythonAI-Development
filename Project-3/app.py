from sqlmodel import Field, Session, SQLModel, create_engine



class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database_2.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

# SQLModel.metadata.create_all(engine)

# Create Rows and use Session - INSERT
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Create rows 
def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Super-Man", secret_name="Toby Willams") 
    hero_3 = Hero(name="Rusty_Man", secret_name="Tommy Sharp", age=48)   

    session = Session(engine)

    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)

    session.commit()

    session.close()

# main method 

def main():
    create_db_and_tables()
    create_heroes()

if __name__ == "__main__":
     main()     
    