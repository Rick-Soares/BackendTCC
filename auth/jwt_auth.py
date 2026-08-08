from datetime import datetime, timedelta, UTC
from jose import jwt,JWTError
from dotenv import load_dotenv
import os
from exceptions import CredenciaisInvalidasError

load_dotenv()

chave_secreta = os.getenv("SECRET_KEY")
algoritmo = os.getenv("ALGORITHM")
expira_em = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def gerar_token(user_id: str) -> str:
    expire = datetime.now(UTC) + timedelta(minutes=expira_em)

    payload = {
        "sub": user_id,   # subject (quem é o usuário)
        "exp": expire     # tempo de expiração
    }

    token = jwt.encode(payload, chave_secreta, algorithm=algoritmo)

    return token


def decodificar_token(token: str) -> str:
    try:
        payload = jwt.decode(token, chave_secreta, algorithms=[algoritmo])

        user_id = payload.get("sub")

        if user_id is None:
            raise CredenciaisInvalidasError("Token inválido")

        return user_id

    except JWTError:
        raise CredenciaisInvalidasError("Token inválido ou expirado")

