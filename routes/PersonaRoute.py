from typing import Annotated, List
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.RelationshipSchema import PersonaResponse
from schemas.PersonaSchema import PersonaValidator
from schemas.AuthSchema import Login
from services.PersonaService import PersonaService
from services.JWTService import JWTService

DBSession = Annotated[Session, Depends(get_db)]
tokenDependency = Depends(JWTService.get_current_user)

personRoute = APIRouter(prefix="/person", tags=["Personas"])

@personRoute.get("/", dependencies=[tokenDependency])
async def index(dbConn: DBSession) -> List[PersonaResponse]:
    response = PersonaService.get_all(db=dbConn)
    if response:
        return response
    raise HTTPException(status.HTTP_400_BAD_REQUEST, "No hay registros almacenados")

@personRoute.get("/{id}", dependencies=[tokenDependency])
async def getById(id: int, dbConn: DBSession) -> PersonaResponse:
    response = PersonaService.get_by(id=id, db=dbConn)
    if response:
        return response
    raise HTTPException(status.HTTP_400_BAD_REQUEST, f"No hay persona con id {id}")

@personRoute.delete("/{id}", dependencies=[tokenDependency])
async def delete(id: int, dbConn: DBSession):
    if PersonaService.delete(id=id, db=dbConn):
        return JSONResponse("Persona eliminada existosamente", status.HTTP_200_ACCEPTED)
    raise HTTPException(status.HTTP_400_BAD_REQUEST, f"Error al eliminar persona con id {id}")

@personRoute.post("/")
async def create(persona: PersonaValidator, dbConn: DBSession):
    if PersonaService.create(person=persona, db=dbConn):
        return JSONResponse("Persona agregada existosamente", status.HTTP_200_ACCEPTED)
    raise HTTPException(status.HTTP_400_BAD_REQUEST, f"Error al registrar persona con id {id}")

@personRoute.put("/", dependencies=[tokenDependency])
async def update(persona: PersonaValidator, dbConn: DBSession):
    if PersonaService.update(person=persona, db=dbConn):
        return JSONResponse("Persona modificada existosamente", status.HTTP_201_CREATED)
    raise HTTPException(status.HTTP_400_BAD_REQUEST, f"Error al modificar persona con id {id}")

@personRoute.post("/login", name="login")
async def login_for_access_token(credentials: Login, dbConn: DBSession) -> str:
    person = JWTService.authenticate_user(credentials.email, credentials.password, dbConn)
    if not person:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = JWTService.create_access_token(data={"sub": person.email})
    return access_token