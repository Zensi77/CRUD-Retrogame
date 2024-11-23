from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint

from app.conf.db import Base



class Cart(BaseModel):
    articuloId: Optional[int] = None
    userId: Optional[int] = None
    amount: Optional[int] = None
    
class CartDB(Base):
    __tablename__="Carrito"
    __table_args__ = (
        # Anado una clave primaria compuesta para que no se repitan los articulos en el carrito
        PrimaryKeyConstraint('articuloId', 'userId'),
    )

    articuloId=Column(Integer, ForeignKey('Articulos.id'))
    userId=Column(Integer, ForeignKey('Usuarios.id'))
    amount = Column(Integer)