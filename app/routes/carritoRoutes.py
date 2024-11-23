from fastapi import APIRouter, status, HTTPException, Depends

from app.conf.db import get_db
from app.models.carrito import Cart, CartDB
from app.utils.jwt import current_user


carritoRoutes = APIRouter(prefix="/api/carrito", tags=["Carrito"])

@carritoRoutes.get("/", status_code=status.HTTP_200_OK, response_model=list[Cart])
def get_carrito(db = Depends(get_db), current_user = Depends(current_user)):
    return db.query(CartDB).filter(CartDB.userId == current_user.id).all()

@carritoRoutes.post("/", status_code=status.HTTP_201_CREATED, response_model=dict[str, str])
def add_carrito(register: Cart, db = Depends(get_db), current_user = Depends(current_user)):
    nuevo = CartDB(
        articuloId = register.articuloId,
        userId = current_user.get('id'),
        amount = register.amount               
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"detail":"Articulo añadido al carrito"}
        
@carritoRoutes.put("/", status_code=status.HTTP_200_OK, response_model=dict[str, str])
def modify_cart(cart: Cart, db = Depends(get_db), current_user = Depends(current_user)):
    registro = db.query(CartDB).filter(CartDB.articuloId == cart.articuloId and CartDB.userId == current_user.get('id')).first()
    if not registro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Articulo no encontrado")
    registro.amount = cart.amount
    db.commit()
    return {"detail":"Carrito modificado"}

@carritoRoutes.delete("/{id_item}", status_code=status.HTTP_200_OK, response_model=dict[str, str])
def delete_item(id_item: int, db = Depends(get_db), current_user = Depends(current_user)):
    registro = db.query(CartDB).filter(CartDB.articuloId == id_item and CartDB.userId == current_user.get('id')).first()
    if registro: 
        db.delete(registro)
        db.commit()
        return {"detail":"Articulo eliminado"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Articulo no encontrado")


@carritoRoutes.get('/pedido', status_code=status.HTTP_200_OK, response_model=list[Cart])
def pedido(db = Depends(get_db), current_user = Depends(current_user)):
    lista = db.query(CartDB).filter(CartDB.userId == current_user.get('id')).all()
    if lista:
        for item in lista:
            db.delete(item)
        db.commit()
        return lista
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrito vacio")