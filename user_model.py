"""
Módulo que define los modelos de datos para usuarios.
Incluye las clases Usuario, Genero y Role.
"""
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel

class Genero(str, Enum):
    """Enumeración para el género del usuario."""
    MALE = "Masculino"
    FEMALE = "Femenino"

class Role(str, Enum):
    """Enumeración para los roles de usuario."""
    ADMIN = "Admin"
    USER = "User"
    GUEST = "Guest"

class Usuario(BaseModel):
    """Modelo de datos para un usuario del sistema."""
    id: Optional[UUID] = uuid4()
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
