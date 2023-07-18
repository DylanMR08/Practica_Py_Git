from models.models import Base
from database.database import engine
from models.models import Persona, Gatito
from pydantic import BaseModel, validator
from sqlalchemy.orm import Session


class PersonaValidator(BaseModel):
    name: str
    lastname: str
    email: str | None = "example@gmail.com"

    @validator("email")
    def email_val(value: str):
        if not value.__contains__("@"):
            raise ValueError("No es un email valido")
        return value

    class Config:
        orm_mode = True

def insert_persona():
    try:
        db = Session(engine)
        data = {"name":"Dylan", "lastname":"Mejia", "email":"dylan@gmail.com"}
        validator = PersonaValidator(**data)
        persona = Persona(name="Dylan", lastname="Mejia", email="dylan@gmail.com")
        print(persona)
        db.add(persona)
        db.commit()
        db.refresh(persona)
        return f"Persona agregada con exito"
    except Exception as e:
        db.rollback()
        return f"Error"
    finally:
        db.close()

def insert_gatitos():
    try:
        db = Session(engine)
        data = {"name":"Cualquiera", "raza":"Cualquiera", "owner_id":3}
        gatito = Gatito(**data)
        db.add(gatito)
        db.commit()
        db.refresh(gatito)
        return f"gatito agregado con exito"
    except Exception as e:
        db.rollback()
        print(e)
        return f"Error"
    finally:
        db.close()

def select_personas():
    db = Session(engine)
    values = db.query(Persona).all()
    return values

def select_gatitos():
    db = Session(engine)
    values = db.query(Gatito).all()
    return values

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
    print(insert_gatitos())
    print(insert_gatitos())

    print(select_personas())
    print(select_gatitos())