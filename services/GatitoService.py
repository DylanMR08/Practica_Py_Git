
from models.models import Gatito
from sqlalchemy.orm import Session
from typing import List


class GatitoService:
    @classmethod
    def get_all(self, db:Session) -> List[Gatito]:
        values = db.query().all()
        return [gato for gato in values]
