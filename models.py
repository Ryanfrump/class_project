from sqlmodel import Field, SQLModel

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
    muscle_group_id: int = Field(foreign_key="musclegroup.id")

class MuscleGroup(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

class Reward(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item_name: str
    
    
class Punishment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    punishment_name: str
    punishment: str
    #implement later punishment_severity: int

class Schedual(SQLModel, table=True):
    sunday: int = Field(foreign_key="musclegroup.id")
    monday: int = Field(foreign_key="musclegroup.id")
    tuesday: int = Field(foreign_key="musclegroup.id")
    wednesday: int = Field(foreign_key="musclegroup.id")
    thursday: int = Field(foreign_key="musclegroup.id")
    friday: int = Field(foreign_key="musclegroup.id")
    satuday:int = Field(foreign_key="musclegroup.id")
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    is_completed: bool
    #set up composite key for date and workout id
