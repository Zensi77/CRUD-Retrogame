from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.conf.db import engine
from app.models import articulos, carrito, categorias, usuarios

app = FastAPI(
    title="API Retrogame", 
    description="API REST para la gestión de una tienda de videojuegos, con autenticacion y autorización de usuarios", 
    version="1.0.0"
)

# Importar rutas
from app.routes import articulosRoutes, authRoutes, carritoRoutes, categoriasRoutes, usuariosRoutes
app.include_router(articulosRoutes.itemRoutes)
app.include_router(authRoutes.authRoutes)
app.include_router(carritoRoutes.carritoRoutes)
app.include_router(categoriasRoutes.categoriasRoutes)
app.include_router(usuariosRoutes.userRouter)

# Crear tablas
articulos.Base.metadata.create_all(bind=engine) 
carrito.Base.metadata.create_all(bind=engine) 
categorias.Base.metadata.create_all(bind=engine) 
usuarios.Base.metadata.create_all(bind=engine) 

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
if (__name__ == "__main__"):
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True) # Corre el servidor en el puerto 8000