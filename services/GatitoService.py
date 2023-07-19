
from models.models import Gatito
from sqlalchemy.orm import Session
from typing import List


class GatitoService:
    @classmethod
    def get_all(self, db:Session) -> List[Gatito]:
        values = db.query().all()
        return [gato for gato in values]

    @classmethod
    def get_by_id(self, id:int, db:Session) -> bool:
        values = db.query(Gatito).get(id)
        return [gato for gato in values]

    @classmethod
    def delete(self, id:int, db:Session) -> List[Gatito]:
        try:
            values = db.query(Gatito).get(id)
            if values is not None:
                db.delete(values)
                db.commit()
            return False
        except Exception as e:

            db.rollback()
            print(e)
        return False
    
    @classmethod
    def create(self, gatito:GatitoValidator, db:Session) -> List[Gatito]:
        try:
           gatito = Gatito(**gatito.model_dump())
           db.add(gatito)
           db.commit()


        except Exception as e:

            db.rollback()
            print(e)
        return False
    
    @classmethod
    def update(self, gatito:GatitoValidator, db:Session) -> List[Gatito]:
        try:
           gatito = db.query(gatito).get()
           db.add(gatito)
           db.commit()
           

        except Exception as e:

            db.rollback()
            print(e)
        return False