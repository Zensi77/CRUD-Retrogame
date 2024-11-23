from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.conf.db import get_db
from app.controllers.categoriasController import deleteCategory, getAllCategories, getOneCategory, insertCategory, modifyCategory
from app.models.categorias import Category
from app.utils.jwt import current_user

categoriasRoutes = APIRouter(prefix='/api/categorias', tags=['Categorias'])

@categoriasRoutes.get('/', status_code=status.HTTP_200_OK, response_model=list[Category])
def show_Categorias(db= Depends(get_db))->list[Category]:
    return getAllCategories(db)

@categoriasRoutes.get('/{id}', status_code=status.HTTP_200_OK, response_model=Category)
def get_Categoria(id: int, db= Depends(get_db))->Category:
    res = getOneCategory(id, db)
    if res:
        return res
    raise HTTPException(status_code=404, detail='Categoria no encontrada')

@categoriasRoutes.post('/', status_code=status.HTTP_201_CREATED, response_model=Category)
def create_Categoria(category: Category, db= Depends(get_db), current_user: dict=Depends(current_user))->Category:
    print(current_user)
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail='No tienes permisos para realizar esta accion')
        
    return insertCategory(category, db)

@categoriasRoutes.delete('/{id}', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def borrar_Categoria(id: int, db= Depends(get_db), current_user: dict=Depends(current_user))->dict[str, str]:
    print(current_user)
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail='No tienes permisos para realizar esta accion')
        
    if deleteCategory(id, db):
        return {'detail':'Tarea borrada con exito'}
    raise HTTPException(status_code=404, detail='Categoria no encontrada')


@categoriasRoutes.put('/', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def modify_Categoria(categoria: Category, db= Depends(get_db), current_user: dict=Depends(current_user))->dict[str, str]:
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail='No tienes permisos para realizar esta accion')
        
    res = modifyCategory(categoria, db)
    if res:
        return {'detail':'Tarea modificada con exito'}
    raise HTTPException(status_code=404, detail='Categoria no encontrada')