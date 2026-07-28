from datetime import datetime, UTC
from pydantic import BaseModel
from uuid import uuid4

class CriarTelefone(BaseModel):
    numero: str

class Telefone(BaseModel):
    telefone_id: str
    user_id: str
    numero: str
    created_at: datetime | str

    @classmethod
    def criar(cls, data: CriarTelefone, id_telefone = None, user_id: str = None, criado_em = None):
        return cls(
            telefone_id = id_telefone or str(uuid4()),
            user_id = user_id,
            numero = data.numero,
            created_at = criado_em or datetime.now(UTC)
        )

class TelefoneRequest(BaseModel):
    numero: str