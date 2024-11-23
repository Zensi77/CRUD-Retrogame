from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from app.conf.db import Base


class Item(BaseModel):
    id: Optional[int] = Field(None) 
    name: str
    price: float
    tax: int
    description: str
    image: str
    stock: int
    categoryId: int
    
class ItemDB(Base):
    __tablename__= "Articulos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, default = 0)
    tax = Column(Integer, default = 0)
    description = Column(String(255))
    image = Column(String(255))
    stock = Column(Integer, default=0)
    categoryId = Column(Integer, ForeignKey("Categorias.id"))
    
    def precio_final(self):
        return self.price+(self.price*self.tax/100)