from typing import Annotated, List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database.database import get_db
from services.GatitoService import GatitoService
DBSession = Annotated[Session, Depends(get_db)]

gatitoRoute = APIRouter(prefix="/gatito", tags=["Gatitos"])

@gatitoRoute.get("/")
async def index(dbCom: DBSession) -> List:
    response = GatitoService.get_all(db=dbCom)
    return response

@gatitoRoute.get("/{id}")
async def getById(id:int, dbCom: DBSession) -> List:
    response = GatitoService.get_by_id(id=id, b=dbCom)
    return response

@gatitoRoute.delete("/{id}")
async def getById(id:int, dbCom: DBSession):
    response = GatitoService.delete(id=id, b=dbCom)
    return "Gatito Eliminado" if response is True else "Error al eliminar"

@gatitoRoute.post("/")
async def getById(gatito: GatitoValidator, dbCom: DBSession):
    response = GatitoService.create(gatito=gatito, b=dbCom)
    return "Gatito Agregado" if response is True else "Error al agregar"

@gatitoRoute.put("/")
async def getById(gatito: GatitoValidator, dbCom: DBSession):
    response = GatitoService.update(gatito=gatito, b=dbCom)
    return "Gatito actualizado" if response is True else "Error al actualizar"