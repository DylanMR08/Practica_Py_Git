from __future__ import annotations

from typing import List
from pydantic import BaseModel, EmailStr

class GatitoValidator(BaseModel):
    id: int | None = None
    name: str
    raza: str
    owner_id: int

class PersonaValidator(BaseModel):
    id: int | None = None
    name: str
    lastname: str
    email: EmailStr

    gatitos: List[GatitoValidator] = []

    class Config:
        orm_mode = True