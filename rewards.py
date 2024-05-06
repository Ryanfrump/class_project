from sqlmodel import SQLModel, Session, create_engine
from models import Reward


postgres_url = "postgresql://postgres:Packers0192!@localhost:5432/class_project"

engine = create_engine(postgres_url, echo = True)


reward_1 = Reward(item_name="Drink", item_value="Chocolate Milk")



with Session(engine) as session:
    session.add(reward_1)
    session.commit()
