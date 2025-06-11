from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    xp_to_next_level = Column(Integer, default=100)  # NOVO: quanto precisa para subir
    missions = relationship("UserMission", back_populates="user")

class Mission(Base):
    __tablename__ = 'missions'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    xp_reward = Column(Integer, default=100) 
    users = relationship("UserMission", back_populates="mission")

class UserMission(Base):
    __tablename__ = "user_missions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    mission_id = Column(Integer, ForeignKey("missions.id"))
    completed = Column(Boolean, default=False)

    user = relationship("User", back_populates="missions")
    mission = relationship("Mission", back_populates="users")