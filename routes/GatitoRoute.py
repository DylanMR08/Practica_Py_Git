from typing import Annotated, List
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db
from services.GatitoService import GatitoService
from schemas.GatitoSchema import GatitoValidator
from schemas.RelationshipSchema import GatitoResponse
from services.JWTService import JWTService



DBSession = Annotated[Session, Depends(get_db)]
tokenDependency = Depends(JWTService.get_current_user)

gatitoRoute = APIRouter(prefix="/gatito", tags=["Gatitos"], dependencies=[tokenDependency])

@gatitoRoute.get("/")
async def index(dbCom: DBSession):
    response = GatitoService.get_all(db=dbCom)
    if response: 
        return response
    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="No existen registros")

@gatitoRoute.get("/{id}")
async def getById(id:int, dbCom: DBSession):
    response = GatitoService.get_by_id(id=id, db=dbCom)
    if response:
        return response
    raise HTTPException(status.HTTP_400_BAD_REQUEST,  detail=f"No existe un registro con id: {id}")

@gatitoRoute.delete("/{id}")
async def delete(id:int, dbCom: DBSession):
    if  GatitoService.delete(id=id, db=dbCom):
        return JSONResponse("Gatito Eliminado", status.HTTP_200_OK)
    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"No existe un gatito con id {id}")

@gatitoRoute.post("/")
async def create(gatito: GatitoValidator, dbCom: DBSession):
    if GatitoService.create(gatito=gatito, db=dbCom):
        return JSONResponse("Gatito Agrgedo", status.HTTP_201_CREATED)
    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Error al agregar")

@gatitoRoute.put("/")
async def update(gatito: GatitoValidator, dbCom: DBSession):
    if GatitoService.update(gatito=gatito, db=dbCom):
         return JSONResponse("Gatito MOdificado", status.HTTP_202_ACCEPTED)
    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Error al modificar")