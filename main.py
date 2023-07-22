import uvicorn
from typing import Annotated
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db
from routes.PersonaRoute import personRoute
from routes.GatitoRoute import gatitoRoute

app = FastAPI()

app.include_router(router=gatitoRoute, prefix="/api")
app.include_router(router=personRoute, prefix="/api")


@app.get("/")
async def index() -> JSONResponse:
    return JSONResponse(content="HOLA", status_code=200)

if __name__ == "__main__":
    uvicorn.run(app)