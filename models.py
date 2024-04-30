from sqlmodel import Field, SQLModel, create_engine

class user(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int

class Workout(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    set: int
    rep: int
    help_video: str

class Reward(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item_name: str
    item_value: str
    user_item: int = Field(foreign_key="user.id")

class Punishment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    punishment_name: str
    punishment: str
    punishment_item: int = Field(foreign_key="user.id") 

class Days(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    day: str







postgres_url = "postgresql://postgres:Packers0192!@localhost:5432/class_project"

engine = create_engine(postgres_url, echo = True)