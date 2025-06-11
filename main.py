from fastapi import FastAPI
from db.base import Base
from db.sessions import engine
from api.routes import users, missions

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(missions.router, prefix="/missions", tags=["Missions"])
