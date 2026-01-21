from fastapi import FastAPI
from typing import List, Optional
from uuid import UUID, uuid4
from userModel import Genero, Role, Usuario

app = FastAPI()

app = List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Zyanya",
        apellidos="Zacatenco",
        genero=Genero.femenino,
        roles=[Role.admin]
    )
]

@app.get("/")
async def root():
    return {"Saludo": "hola hijos  de su chingada madre"}
    ##fastapi dev main.py
    ##pip install pydantic

@app.get("api/v1/users")
async def get_users():
    return db