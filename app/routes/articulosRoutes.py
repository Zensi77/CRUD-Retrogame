from app.conf.db import get_db
from app.controllers.articulosController import deleteArticle, getAllArticles, getArticlesByCategory, getOneArticle, insertArticle, modifyArticle
from app.models.articulos import Item
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.utils.jwt import current_user

itemRoutes = APIRouter(prefix='/api/articulos', tags=['Articulos'])

@itemRoutes.get('/', status_code=status.HTTP_200_OK, response_model=list[Item])
def get_items(db = Depends(get_db)):
    return getAllArticles(db)

@itemRoutes.get('/{id}', status_code=status.HTTP_200_OK, response_model=Item)
def get_item_id(id:int, db=Depends(get_db)):
    return getOneArticle(id, db)

@itemRoutes.post('/', status_code=status.HTTP_201_CREATED, response_model=Item)
def create_article(article: Item, db= Depends(get_db), current_user: dict=Depends(current_user))->Item:
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='No tienes permisos para realizar esta accion')

    return insertArticle(article, db)

@itemRoutes.put('/', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def modify_Article(article: Item, db=Depends(get_db), current_user: dict=Depends(current_user))->dict[str, str]:
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='No tienes permisos para realizar esta accion')

    if modifyArticle(article, db):
        return {'detail':'Articulo modificado con exito'}
    raise HTTPException(status_code=404, detail='Articulo no encontrado')

@itemRoutes.delete('/{id}', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def delete_Article(id: int, db=Depends(get_db), current_user: dict=Depends(current_user))->dict[str, str]:
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='No tienes permisos para realizar esta accion')

    if deleteArticle(id, db):
        return {'detail':'Articulo borrado con exito'}
    raise HTTPException(status_code=404, detail='Articulo no encontrado')

@itemRoutes.get('/items-category/{name_category}', status_code=status.HTTP_200_OK, response_model=list[Item])
def get_articles_by_category(name_category: str, db=Depends(get_db))->list[Item]:
    print(name_category)
    return getArticlesByCategory(name_category, db)