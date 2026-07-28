from pydantic import BaseModel, EmailStr, ConfigDict
from uuid import uuid4
from datetime import datetime, UTC

class CriarUsuario(BaseModel):
    email: EmailStr
    senha: str
    nome: str

    model_config = ConfigDict(extra="forbid")

class Usuario(BaseModel):
    user_id: str
    nome: str
    email: str
    senha_hash: str
    created_at: datetime

    @classmethod
    def criar(cls, data: CriarUsuario, id_usuario = None, criado_em = None):
        return cls(
            user_id = id_usuario or str(uuid4()),
            nome = data.nome,
            email = str(data.email),
            senha_hash = data.senha,
            created_at = criado_em or datetime.now(UTC),
        )

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str