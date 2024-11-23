from sqlalchemy.orm import Session
from app.models.usuarios import User, UserDB
from app.utils.password import Hash


def getAllUsers(db:Session)->list[User]:
    return db.query(UserDB).all()

def getOneUser(id: int, db: Session)->User:
    return db.query(UserDB).filter(UserDB.id==id).first()
    
def insertOneUser(user: User, db: Session):
    new_user = UserDB(
        user=user.user,
        password=Hash.getPasswordHash(user.password),
        name=user.name,
        email=user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    
def modifyUser(user: User, db: Session)->bool:
    usuario = getOneUser(user.id, db)
    if usuario:
        usuario.id=user.id
        usuario.user=user.user
        usuario.password=Hash.getPasswordHash(user.password)
        usuario.name=user.name
        usuario.email=user.email
        usuario.admin=user.admin
        db.commit()
        db.refresh(usuario)
        return True
    return False
    
    
def deleteUser(id: int, db: Session)->bool:
    user = getOneUser(id, db)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
    
def createAdmin(user: User, db: Session)->bool:
    admin = UserDB(
        user=user.user,
        password=Hash.getPasswordHash(user.password),
        name=user.name,
        email=user.email,
        admin=True
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return True