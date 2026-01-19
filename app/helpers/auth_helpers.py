
from datetime import datetime, timedelta
import os
from argon2 import PasswordHasher
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from app.models.user import User


ph = PasswordHasher()


SECRET_TOKEN=os.getenv("SECRET_KEY","CHANGE_ME_DEV")
ALGORITHM="HS256"
bearer_scheme=HTTPBearer()

ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_TOKEN, algorithm=ALGORITHM)
    return token

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if not credentials:
        raise HTTPException(status_code=401, detail="Authorization token missing")

    token = credentials.credentials
    try:
        decoded = jwt.decode(token, SECRET_TOKEN, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = await User.get_or_none(id=decoded.get("user_id"))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

 
def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return ph.verify(hashed_password, password)

