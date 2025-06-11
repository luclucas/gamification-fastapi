from pydantic import BaseModel

class UserMission(BaseModel):
    user_id: int
    mission_id: int
    completed: bool

    class Config:
        orm_mode = True