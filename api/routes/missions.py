from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.deps import get_db
from crud import user as crud_user

router = APIRouter()

@router.post("/complete/{user_id}/{mission_id}")
def complete(user_id: int, mission_id: int, db: Session = Depends(get_db)):
    result = crud_user.complete_mission(db, user_id, mission_id)
    if not result:
        raise HTTPException(status_code=404, detail="Missão não encontrada ou já completada")
    return {"message": "Missão completada com sucesso!"}