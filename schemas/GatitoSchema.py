from __future__ import annotations

from pydantic import BaseModel, field_validator, EmailStr
from .PersonaSchema import PersonaValidator
from typing import List

class PersonaValidator(BaseModel):
    id: int | None = None
    name: str
    lastname: str
    email: EmailStr

class GatitoValidator(BaseModel):
    id: int | None = None
    name: str
    raza: str
    owner_id: int

    owner : PersonaValidator

    class Config:
        orm_mode = True