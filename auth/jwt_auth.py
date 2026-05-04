from datetime import datetime, timedelta, UTC
from jose import jwt,JWTError

# (jogar em.env)
chave_secreta = "segredo-completo"
algoritmo = "HS256"
expira_em = 60


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
            raise Exception("Token inválido")

        return user_id

    except JWTError:
        raise Exception("Token inválido ou expirado")

