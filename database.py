from sqlmodel import create_engine, Session

postgres_url = "postgresql://postgres:Packers0192!@localhost:5432/class_project"
engine = create_engine(postgres_url, echo = True)

def get_db():
    with Session(engine) as session:
        yield session