from sqlmodel import Field, SQLModel, create_engine

class Hero(SQLModel, table=True):
    id: int | None = Field(default = None, primary_key = True)
    first_name: str
    last_name: str
    age: int

postgres_url = "postgresql://postgres:Packers0192!@localhost:5432/class_project"

engine = create_engine(postgres_url, echo = True)