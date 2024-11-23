from fastapi import HTTPException
from app.models.categorias import CategoryDB
from sqlalchemy.orm import Session
from app.models.articulos import Item, ItemDB

def getAllArticles(db:Session)->list[Item]:
    return db.query(ItemDB).all()

def getOneArticle(id: int, db: Session)->Item:
    return db.query(ItemDB).filter(ItemDB.id == id).first()

def insertArticle(article: Item, db: Session)->Item:
    cat = db.query(CategoryDB).filter(CategoryDB.id == article.categoryId).first()
    if not cat:
        raise HTTPException(status_code=404, detail='Categoria no encontrada')
    
    new_articulo = ItemDB(**article.dict())
    db.add(new_articulo)
    db.commit()
    db.refresh(new_articulo)
    return new_articulo
    
def modifyArticle(article_mod: Item, db: Session)->bool:
    article = db.query(ItemDB).filter(ItemDB.id == article_mod.id).first()
    if article:
        article.id = article_mod.id
        article.name = article_mod.name
        article.price = article_mod.price
        article.tax = article_mod.tax
        article.description = article_mod.description
        article.image = article_mod.image
        article.stock = article_mod.stock
        article.categoryId = article_mod.categoryId
        db.commit()
        db.refresh(article)
        return True
    return False
    
def deleteArticle(id: int, db: Session)->bool:
    article = getOneArticle(id, db)
    if article:
        db.delete(article)
        db.commit()
        return True
    return False

def getArticlesByCategory(name_category: str, db: Session)->list[Item]:
    return db.query(ItemDB).join(CategoryDB).filter(CategoryDB.name==name_category).all()
