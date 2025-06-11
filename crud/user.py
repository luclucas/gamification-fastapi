from sqlalchemy.orm import Session
from db import models
from schemas import user as schemas
from core.config import XP_PER_MISSION, LEVEL_UP_XP

def create_user(db: Session, user: schemas.UserCreate, default_mission: models.Mission):
    db_user = models.User(username = user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    user_mission = models.UserMission(user_id=db_user.id, mission_id=default_mission.id)
    db.add(user_mission)
    db.commit()
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def complete_mission(db: Session, user_id: int, mission_id: int):
    user_mission = db.query(models.UserMission).filter_by(user_id=user_id, mission_id=mission_id).first()
    if user_mission and not user_mission.completed:
        user_mission.completed = True
        user = db.query(models.User).get(user_id)
        user.experience += XP_PER_MISSION
        if user.experience >= LEVEL_UP_XP:
            user.level += 1
            user.experience = 0
        db.commit()
        return user_mission
    return None