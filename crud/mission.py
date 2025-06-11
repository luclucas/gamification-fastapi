from sqlalchemy.orm import Session
from db import models
from schemas import mission as schemas

def get_or_create_default(db: Session):
    default_title = "Primeiros passos"
    mission = db.query(models.Mission).filter_by(title=default_title).first()
    if not mission:
        mission = models.Mission(title=default_title, description="Complete seu perfil e leia as instruções iniciais.")
        db.add(mission)
        db.commit()
        db.refresh(mission)
    return mission