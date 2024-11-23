from pydantic import BaseModel
from app.models.usuarios import UserDB
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.conf.db import get_db
from app.utils.jwt import create_jwt_token
from app.utils.password import Hash

class loginData(BaseModel):
    name: str
    password: str

authRoutes = APIRouter(prefix="/api/auth", tags=["Auth"])

@authRoutes.post("/login", response_model=dict[str, str])
async def login(user: loginData, db: Session = Depends(get_db)) -> dict[str, str]:
    user_db = db.query(UserDB).filter(UserDB.user == user.name).first()
    if not user_db or not Hash.verifyPassword(user.password, user_db.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    token_data = {"usuario": user_db.name}
    if user_db.admin:
        token = create_jwt_token(token_data, role="admin", id=user_db.id)
    else:
        token = create_jwt_token(token_data, role="user", id=user_db.id)
        
    return {"token": token}
