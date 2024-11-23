from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import ExpiredSignatureError, PyJWTError, encode, decode
from os import getenv
from dotenv import load_dotenv
load_dotenv()  # Carga las variables de entorno desde el archivo .env



def create_jwt_token(data: dict, role: str, id: str) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=30)
    to_encode.update({"exp": expire, "role": role, "id": id})
    encoded_jwt = encode(to_encode, key=getenv('SECRET'), algorithm='HS256')
    return encoded_jwt

def verify_jwt(token: str) -> dict[str, str]:
    try:
        decoded = decode(token, key=getenv('SECRET'), algorithms=['HS256'])
        return decoded
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
security = HTTPBearer()
async def current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict[str, str]:
    token = credentials.credentials
    payload = verify_jwt(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload
