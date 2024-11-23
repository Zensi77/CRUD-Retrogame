<p align="center">
    <img src="https://cosasdedevs.com/media/sections/images/fastapi.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">CRUD-RETROGAME</h1></p>
<p align="center">
	<em><code>❯Proyecto realizado para la  asignatura Desarrollo Web Servidor</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/Zensi77/CRUD-Retrogame?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Zensi77/CRUD-Retrogame?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Zensi77/CRUD-Retrogame?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Caracteristicas](#-Caracteristicas)
- [📁 Estructura de proyecto](#-Estructura-del-proyeco)
- [🚀 Inicio rapido](#-Inicio-rapido)
  - [☑️ Prerequisitos](#-Prerequisitos)
  - [⚙️ Instalacion](#-Instalacion)
  - [🤖 Uso](#🤖-Uso)
    - [Documentación](#Documentación)
    - [🔒 Roles](#-Roles)
---

## 📍 Caracteristicas

- Autenticación JWT: Protección de endpoints con tokens seguros.
- Autorización por roles: Control de acceso granular (usuarios y administradores).
- Gestión de recursos: CRUD para usuarios, artículos, categorías y carritos.
- OpenAPI: Documentación generada automáticamente con Swagger.
- Contenedores: Compatible con Docker para implementación ágil.

---

## 📁 Estructura del proyeco

```sh
└── CRUD-Retrogame/
    ├── README.md
    ├── __pycache__
    │   ├── main.cpython-311.pyc
    │   ├── main.cpython-312.pyc
    │   └── main.cpython-313.pyc
    ├── app
    │   ├── conf
    │   ├── controllers
    │   ├── models
    │   ├── routes
    │   └── utils
    ├── docker-compose.yml
    ├── main.py
    ├── openapi.json
    ├── requirements.txt
    └── shop.db
```


---
## 🚀 Inicio rapido

### ☑️ Prerequisitos

Before getting started with CRUD-Retrogame, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


### ⚙️ Instalacion

Install CRUD-Retrogame using one of the following methods:

**Build from source:**

1. Clone the CRUD-Retrogame repository:
```sh
❯ git clone https://github.com/Zensi77/CRUD-Retrogame
```

2. Navigate to the project directory:
```sh
❯ cd CRUD-Retrogame
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker compose up
```

### 🤖 Uso
Replace the `.env.example` file with your own environment variables.

Run CRUD-Retrogame using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python main.py
```


#### **Usuarios**
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

#### Documentación
La documentación de la API se encuentra en la ruta `/docs` y `/redoc`.

#### 🔒 Roles

|  Accion |  Invitado | Registrado  | Admin  |
|---|---|---|---|
| Hacer Login  | Si  | No  | No  |
| Registrarse  |  Si |  No | No  |
|  Ver perfil |  No |  Si | Si  |
| Cambiar contraseña  | No  | Si  | Si  |
|  Ver videojuegos | Si  |  Si |  Si |
| Ver categorias  | Si  |  SI | Si  |
| Añadir categorias y juegos  | No  | No  | Si  |
|  Modificar borrar categorias |  No | No  |  Si |


