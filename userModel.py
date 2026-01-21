from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Genero(str, Enum):
    masculino: "masculino"
    femenino:"femenino"

class Role(str, Enum):
    admin: "admin"
    user: "user"
    invitado: "invitado"

class Usuario(BaseModel):
    id: Optional[UUID]=uuid4()
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]