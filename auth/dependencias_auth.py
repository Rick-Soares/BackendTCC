from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from auth.jwt_auth import decodificar_token
from exceptions import CredenciaisInvalidasError

security = HTTPBearer()

def verificar_token(credentials = Depends(security)):
    token = credentials.credentials

    try:
        user_id = decodificar_token(token)
        return user_id

    except CredenciaisInvalidasError as e:
        raise HTTPException(status_code=401, detail="Token inválido")