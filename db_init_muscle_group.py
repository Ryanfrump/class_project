from sqlmodel import Session
from models import MuscleGroup
from database import engine


with Session(engine) as session:
    session.add(MuscleGroup(name="upper_body"))
    session.add(MuscleGroup(name="lower_body"))
    session.add(MuscleGroup(name="rest_day"))
    session.add(MuscleGroup(name="active_rest_day"))

    session.commit()