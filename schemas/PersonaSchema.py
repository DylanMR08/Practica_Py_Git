from pydantic import BaseModel, EmailStr

class PersonaValidator(BaseModel):
    id: int | None = None
    name: str
    lastname: str
    email: EmailStr