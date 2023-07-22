
from models.models import Gatito
from sqlalchemy.orm import Session
from typing import List
from schemas.GatitoSchema import GatitoValidator


class GatitoService:
    @classmethod
    def get_all(self, db:Session) -> List[Gatito]:
        values = db.query(Gatito).all()
        print(values)
        return [gato for gato in values]

    @classmethod
    def get_by_id(self, id:int, db:Session) -> Gatito:
        value = db.query(Gatito).get(id)
        return value

    @classmethod
    def delete(self, id:int, db:Session) -> bool:
        try:
            values = db.query(Gatito).get(id)
            if values is not None:
                db.delete(values)
                db.commit()
                return True
        except Exception as e:
            db.rollback()
            print(e)
        return False
    
    @classmethod
    def create(self, gatito:GatitoValidator, db:Session) -> bool:
        try:
           gatito = Gatito(**gatito.model_dump())
           db.add(gatito)
           db.commit()
           return True
        except Exception as e:
            db.rollback()
            print(e)
        return False
    
    @classmethod
    def update(self, gatito:GatitoValidator, db:Session) -> bool:
        try:
           gatitos = db.query(Gatito).get(gatito.id)
           gatitos.name = gatito.name
           gatitos.raza = gatito.raza
           db.commit()
           db.refresh(gatitos)
           return True
        except Exception as e:

            db.rollback()
            print(e)
        return False