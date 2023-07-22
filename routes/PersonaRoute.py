from typing import Annotated, List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.RelationshipSchema import PersonaResponse
from schemas.PersonaSchema import PersonaValidator
from services.PersonaService import PersonaService

DBSession = Annotated[Session, Depends(get_db)]

personRoute = APIRouter(prefix="/person", tags=["Personas"])

@personRoute.get("/")
async def index(dbConn: DBSession) -> List[PersonaResponse]:
    response = PersonaService.get_all(db=dbConn)
    return response

@personRoute.get("/{id}")
async def getById(id: int, dbConn: DBSession) -> PersonaResponse:
    response = PersonaService.get_by(id=id, db=dbConn)
    return response

@personRoute.delete("/{id}")
async def delete(id: int, dbConn: DBSession):
    response = PersonaService.delete(id=id, db=dbConn)
    return "Eliminado correctamente" if response is True else "Error al eliminar"

@personRoute.post("/")
async def create(persona: PersonaValidator, dbConn: DBSession):
    response = PersonaService.create(person=persona, db=dbConn)
    return "Agregado correctamente", 200 if response is True else "Error al agregar", 400

@personRoute.put("/")
async def update(persona: PersonaValidator, dbConn: DBSession):
    response = PersonaService.update(person=persona, db=dbConn)
    return "Modificado correctamente" if response is True else "Error al modificar"