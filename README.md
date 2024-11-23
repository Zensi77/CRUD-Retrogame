# API RESTFULL - CRUD - FASTAPI
## Descricion
API RESTFULL para el manejo de usuarios, utilizando el framework FastAPI, con las operaciones CRUD (Create, Read, Update, Delete).
Se utilizo una base de datos SQLite para el almacenamiento de los datos.
Tiene implementado autenticacion JWT (Json Web Token) para la proteccion de las rutas, asi como autorizacion de roles.
## Requerimientos
Inicio rapido
```bash
docker-compose up
pip install -r requirements.txt
```

## Usuarios
La base de datos ya posee 2 administradores, los demas se crearan mediante un endpoint de la API.
- admin1{
    username: admin, 
    password: admin, 
    role: admin
}
- admin2{
    username: juanma, 
    password: juanma, 
    role: admin
}

