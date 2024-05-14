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
async def get_schedual(db: Session = Depends(get_db)) -> list[Schedual]:
    return db.exec(select(Schedual)).all()

@app.get("/muscle_group")
async def get_muscle_group(db: Session = Depends(get_db)) -> list[MuscleGroup]:
    return db.exec(select(MuscleGroup)).all()

@app.get("/user/{user_id}/schedual")
async def get_schedual_for_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    schedual = db.query(Schedual).filter(Schedual.user_id == user_id).all()
    return schedual

@app.get("/workouts/{muscle_group_id}")
async def get_workouts_for_muscle_group(muscle_group_id: int, db: Session = Depends(get_db)):
    muscle_group = db.get(MuscleGroup, muscle_group_id)
    if muscle_group is None:
        raise HTTPException(status_code=404, detail="Muscle Group not found")

    workouts = db.query(Workout).filter(Workout.muscle_group_id == muscle_group_id).all()
    return workouts

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





#PUT
@app.put("/user/{user_id}")
async def update_user(user_id: int, updated_user: User,  db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    
    user_data = updated_user.model_dump(exclude_unset=True)
    user.sqlmodel_update(user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


#delete
@app.delete("/user/{user_id}")
async def remove_user(user_id: int, db: Session = Depends(get_db)):
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
        return {"ok": True}
    

