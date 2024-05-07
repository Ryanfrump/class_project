from sqlmodel import Session
from models import Punishment
from database import engine



with Session(engine) as session:
    session.add(Punishment(punishment_name="1 extra workout", punishment="Assigned 1 extra workout for tomorrow"))
    session.add(Punishment(punishment_name="2 extra workouts", punishment="Assigned 2 extra workouts for tomorrow"))
    session.add(Punishment(punishment_name="3 extra wourkouts", punishment="Assigned 3 extra workouts for tomorrow"))
    session.add(Punishment(punishment_name="No reward", punishment="You get no reward when tomorrows workouts are finished"))
    session.add(Punishment(punishment_name="Push ups", punishment="Drop and give me 25 push-ups right now slacker"))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.add(Punishment(punishment_name="", punishment=""))
    session.commit()