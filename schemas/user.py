from pydantic import BaseModel
from typing import List

from schemas.user_mission import UserMission

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    level: int
    experience: int
    xp_to_next_level: int
    missions: List[UserMission] = []

    class Config:
        orm_mode = True