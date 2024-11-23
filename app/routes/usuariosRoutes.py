from app.conf.db import get_db
from app.models.usuarios import User
from fastapi import Depends, HTTPException, status, APIRouter
from app.controllers.usuariosController import createAdmin, getAllUsers, getOneUser, insertOneUser, modifyUser, deleteUser
from app.utils.jwt import current_user

userRouter=APIRouter(prefix='/api/usuarios', tags=['Usuarios'])

@userRouter.get('/', status_code=status.HTTP_200_OK, response_model=list[User])
def show_Users(db=Depends(get_db), current_user: dict[str, str] = Depends(current_user)):
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos")
        
    return getAllUsers(db)

@userRouter.get('/{id}', status_code=status.HTTP_200_OK, response_model=User)
def show_One_User(id: int, db=Depends(get_db), current_user: dict[str, str] = Depends(current_user)):
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos")

    return getOneUser(id, db)

@userRouter.post('/', status_code=status.HTTP_201_CREATED, response_model=list[User])
def create_User(user: User, db=Depends(get_db)):
    insertOneUser(user, db)
    return getAllUsers(db)

@userRouter.put('/', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def modify_User(user: User, db=Depends(get_db), current_user: dict[str, str] = Depends(current_user)):
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos")

    if modifyUser(user, db):
        return {"detail":"Usuario modificado"}
    return {"detail":"Usuario no encontrado"}

@userRouter.delete('/{id}', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def delete_User(id: int, db=Depends(get_db), current_user: dict[str, bool] = Depends(current_user)):
    if current_user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos")

    if deleteUser(id, db):
        return {"detail":"Usuario eliminado"}
    return {"detail":"Usuario no encontrado"}

@userRouter.get('/profile', status_code=status.HTTP_200_OK, response_model=User)
def show_profile(user: User, db=Depends(get_db), current_user: dict[str, str] = Depends(current_user)):
    user_db = getOneUser(current_user.get('id'), db)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user_db

@userRouter.put('/paassword', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def modify_password(password: str, db=Depends(get_db), current_user: dict[str, str] = Depends(current_user)):
    user = getOneUser(current_user.get('id'), db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    user.password = password
    if modifyUser(user, db):
        return {"detail":"Contraseña modificada"}
    
@userRouter.post('/createAdmin', status_code=status.HTTP_201_CREATED, response_model=dict[str, str])
def create_admin(user: User, db = Depends(get_db), current_user: dict[str, str] = Depends(current_user)):
    if current_user.get('rol') != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos")
    createAdmin(user, db)
