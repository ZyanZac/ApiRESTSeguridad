"""
API REST para gestión de usuarios.
Implementa operaciones CRUD (Create, Read, Update, Delete).
"""
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from user_model import Genero, Role, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Zyanya",
        apellidos="Zacatenco",
        genero=Genero.FEMALE,
        roles=[Role.ADMIN]
    )
]


@app.get("/")
async def root():
    """Endpoint raíz de la API."""
    return {"Saludo": "Holi ñom ñom ñom"}
    ##fastapi dev main.py
    ##pip install pydantic


@app.get("/api/v1/users")
async def get_users():
    """Obtiene la lista de todos los usuarios."""
    return db


@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: UUID):
    """Obtiene un usuario específico por su ID."""
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario NO encontrado")


@app.post("/api/v1/users")
async def create_user(usuario: Usuario):
    """Crea un nuevo usuario en la base de datos."""
    db.append(usuario)
    return {"mensaje": "Usuario creado exitosamente", "usuario": usuario}


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, usuario_actualizado: Usuario):
    """Actualiza un usuario existente por su ID."""
    for index, user in enumerate(db):
        if user.id == user_id:
            usuario_actualizado.id = user_id
            db[index] = usuario_actualizado
            return {"mensaje": "Usuario actualizado exitosamente",
                    "usuario": usuario_actualizado}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    """Elimina un usuario de la base de datos por su ID."""
    for index, user in enumerate(db):
        if user.id == user_id:
            db.pop(index)
            return {"mensaje": "Usuario eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
