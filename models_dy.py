from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import List

class Persona(Base):
    __tablename__ = "persona"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    lastname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)

    gatitos: Mapped[List["Gatito"]] = relationship(back_populates="owner")

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.lastname = kwargs.get("lastname")
        self.email = kwargs.get("email")
        
    def __repr__(self) -> str:
        return f"User: <Id: {self.id}, name: {self.name}>"