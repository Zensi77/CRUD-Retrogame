from app.models.categorias import Category, CategoryDB
from sqlalchemy.orm import Session


def getAllCategories(db: Session)->list[Category]:
    return db.query(CategoryDB).all()

def getOneCategory(id: int, db: Session)->Category:
    return db.query(CategoryDB).filter(CategoryDB.id==id).first()

def insertCategory(categoria: Category, db: Session)->Category:
    category = CategoryDB(**categoria.dict())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def deleteCategory(id: int, db: Session)->bool:
    category = getOneCategory(id, db)
    if category:
        db.delete(category)
        db.commit()
        return True
    return False
    
def modifyCategory(categoria: Category, db: Session):
    category = db.query(CategoryDB).filter(CategoryDB.id == categoria.id).first()
    if category:
        category.name = categoria.name
        db.commit()
        db.refresh(category)
        return True
    return False