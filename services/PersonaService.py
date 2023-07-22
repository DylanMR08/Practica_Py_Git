from models.models import Persona
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from schemas.PersonaSchema import PersonaValidator
from typing import List

class PersonaService:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_all(self, db: Session) -> List[Persona]:
        values = db.query(Persona).all()
        return [person for person in values]

    @classmethod
    def get_by(self, id: int, db: Session) -> Persona:
        value = db.query(Persona).get(id)
        return value

    @classmethod
    def delete(self, id: int, db: Session) -> bool:
        try:
            value = db.query(Persona).get(id)
            if value is not None:
                db.delete(value)
                db.commit()
                return True
        except Exception as e:
            db.rollback()
            print(e)
        return False

    @classmethod
    def create(self, person: PersonaValidator, db: Session) -> bool:
        try:
            persona = Persona(**person.model_dump())
            persona.password = self.pwd_context.hash(persona.password)
            db.add(persona)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(e)
        return False
    
    @classmethod
    def update(self, person: PersonaValidator, db: Session) -> bool:
        try:
            persona = db.query(Persona).get(person.id)
            persona.name = person.name
            persona.lastname = person.lastname
            db.commit()
            db.refresh(persona)
            return True
        except Exception as e:
            db.rollback()
            print(e)
        return False