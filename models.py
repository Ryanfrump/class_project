from sqlmodel import Field, SQLModel, Session, create_engine

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int

class Workout(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    set: int
    rep: int

class Reward(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item_name: str
    
    
class Punishment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    punishment_name: str
    punishment: str
    #implement later punishment_severity: int

class Date(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    day: str
    

class Schedual(SQLModel, table=True):
    day: str
    wourkout_id: int = Field(foreign_key="workout.id", primary_key=True)
    is_completed: bool
    #set up composite key for date and workout id
