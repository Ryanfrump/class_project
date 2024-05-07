from sqlmodel import Session
from models import Reward
from database import engine





with Session(engine) as session:
    session.add(Reward(item_name="Chocolate milk"))
    session.add(Reward(item_name="Apple juice"))
    session.add(Reward(item_name="Orange juice"))
    session.add(Reward(item_name="Monster"))
    session.add(Reward(item_name="Smoothie"))
    session.add(Reward(item_name="Go play mini golf"))
    session.add(Reward(item_name="go bowling"))
    session.add(Reward(item_name="Go to the arcade"))
    session.add(Reward(item_name="Indoor Rock climbing"))
    session.add(Reward(item_name="Go to the movies"))
    session.add(Reward(item_name="Buy new clothes"))
    session.add(Reward(item_name="Buy new video game"))
    session.add(Reward(item_name="Purchase a udemy course"))
    session.add(Reward(item_name="Get a new phone case"))
    session.add(Reward(item_name="Get some fast food"))
    session.add(Reward(item_name="Steak dinner"))
    session.add(Reward(item_name="Go get ice cream"))
    session.add(Reward(item_name="Go to a Baseball game"))
    session.add(Reward(item_name="Go to a hockey game"))
    session.add(Reward(item_name="Go to the pool"))
    session.commit()
