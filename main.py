import uvicorn
from typing import Annotated
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db
from services.GatitoService import GatitoService

DBSession = Annotated[Session, Depends(get_db)]
app = FastAPI()

@app.get("/")
async def index(request: Request, db: DBSession) -> JSONResponse:
    response = GatitoService.get_all(db=db)
    return response, 200


@app.get("/bye")
async def index(request: Request) -> JSONResponse:
    return JSONResponse(content="Adios", status_code=200)



if __name__ == "main":
    uvicorn.run(app)