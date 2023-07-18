from models.models import Persona
from sqlalchemy.orm import Session
from typing import List

class PersonaService:

    @classmethod
    def get_all(self, db: Session) -> List[Persona]:
        values = db.query(Persona).all()
        return [person for person in values]
