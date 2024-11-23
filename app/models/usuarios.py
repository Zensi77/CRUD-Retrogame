from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, Integer, String
from app.conf.db import Base

class User(BaseModel):
    id: Optional[int] = Field(None)
    user:str
    password:str
    name:str
    email:str
    admin:bool = False
    
class UserDB(Base):
    __tablename__='Usuarios'
    
    id=Column(Integer, primary_key=True, autoincrement=True)
    user=Column(String(255), nullable=False)
    password=Column(String(255), nullable=False)
    name=Column(String(255), nullable=False)
    email=Column(String(255), nullable=False)
    admin=Column(Boolean, default=False)
