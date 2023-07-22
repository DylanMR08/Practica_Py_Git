from pydantic import BaseModel

class GatitoValidator(BaseModel):
    id: int | None = None
    name: str
    raza: str
    owner_id: int