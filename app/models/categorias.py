from typing import Optional
from app.conf.db import Base
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String


class Category(BaseModel):
    id: Optional[int] = Field(None) 
    name: str
    
class CategoryDB(Base):
    __tablename__="Categorias"
    
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(150), nullable=False)