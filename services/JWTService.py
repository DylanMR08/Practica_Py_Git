import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models.models import Persona
load_dotenv(".env")

class JWTService:

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/person/login")
    tokenDependency = Annotated[str, Depends(oauth2_scheme)]
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def verify_password(self, password, hashed_password) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    @classmethod
    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    @classmethod
    def authenticate_user(self, email: str, password: str, db: Session):
        user = db.query(Persona).filter(Persona.email == email).first()
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user

    @classmethod
    def create_access_token(self, data):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=float(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
        return encoded_jwt

    @classmethod
    async def get_current_user(self, token: tokenDependency) -> str:
        try:
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=os.getenv('ALGORITHM'))
            data = payload.get("sub")
            if data is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            return data
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"}
            )