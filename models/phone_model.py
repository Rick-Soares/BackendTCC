from datetime import datetime, UTC
from pydantic import BaseModel
from uuid import uuid4

class CriarTelefone(BaseModel):
    numero: str

class Telefone(BaseModel):
    telefone_id: str
    user_id: str
    numero: str
    created_at: datetime

    @classmethod
    def criar(cls, data: CriarTelefone, user_id: str):
        return cls(
            telefone_id = str(uuid4()),
            user_id = user_id,
            numero = data.numero,
            created_at = datetime.now(UTC)
        )

class TelefoneRequest(BaseModel):
    numero: str