from pydantic import BaseModel

class MissionBase(BaseModel):
    title: str
    description: str
    xp_reward: int = 100

class MissionCreate(MissionBase):
    pass

class Mission(MissionBase):
    id: int
    class Config:
        orm_mode = True

class UserMission(BaseModel):
    mission: Mission
    completed: bool

    class Config:
        orm_mode = True