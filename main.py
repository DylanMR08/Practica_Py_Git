import uvicorn
from typing import Annotated
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db

DBSession = Annotated[Session, Depends(get_db)]

app = FastAPI()

@app.get("/")
async def index(request: Request, db: DBSession) -> JSONResponse:
    return JSONResponse(content="HOLA", status_code=200)

@app.get("/bye")
async def index(request: Request) -> JSONResponse:
    return JSONResponse(content="Adios", status_code=200)

if __name__ == "__main__":
    uvicorn.run(app)