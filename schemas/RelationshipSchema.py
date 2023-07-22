from pydantic import BaseModel, EmailStr
from typing import List

class PersonaResponse(BaseModel):
    id: int
    name: str
    lastname: str
    email: EmailStr

    gatitos: List["GatitoResponse"] = []

class GatitoResponse(BaseModel):
    id: int
    name: str
    raza: str

    owner : PersonaResponse

PersonaResponse.model_rebuild()