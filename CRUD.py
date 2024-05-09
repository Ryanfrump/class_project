from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select

from database import get_db
from models import User, Reward, Punishment, Workout, Schedual, MuscleGroup


app = FastAPI()

#get
@app.get("/user")
async def get_user(db: Session = Depends(get_db)) -> list[User]:
    return db.exec(select(User)).all()

@app.get("/reward")
async def get_reward(db: Session = Depends(get_db)) -> list[Reward]:
    return db.exec(select(Reward)).all()

@app.get("/punishment")
async def get_punishment(db: Session = Depends(get_db)) -> list[Punishment]:
    return db.exec(select(Punishment)).all()

@app.get("/workout")
async def get_workout(db: Session = Depends(get_db)) -> list[Workout]:
    return db.exec(select(Workout)).all()

@app.get("/schedual")
async def get_schedual(db: Session = Depends(get_db)) -> Schedual:
    return db.exec(select(Schedual)).all()

@app.get("/muscle_group")
async def get_muscle_group(db: Session = Depends(get_db)) -> list[MuscleGroup]:
    return db.exec(select(MuscleGroup)).all()

#post
@app.post("/user")
async def create_user(user: User, db: Session = Depends(get_db)) -> None:
    db.add(user)
    db.commit()

@app.post("/workout")
async def create_workout(workout: Workout, db: Session = Depends(get_db)) -> None:
    db.add(workout)
    db.commit()

@app.post("/schedual")
async def create_schedual(schedual: Schedual, db: Session = Depends(get_db)) -> None:
    db.add(schedual)
    db.commit()

@app.post("/muscle_group")
async def create_muscle_group(muscle_group: MuscleGroup, db: Session = Depends(get_db)) -> None:
    db.add(muscle_group)
    db.commit()




# put
@app.delete("/user/{user-id}")
async def remove_user(user_id: int, db: Session = Depends(get_db)):
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Hero not found")
        db.delete(user)
        db.commit()
        return {"ok": True}
    

