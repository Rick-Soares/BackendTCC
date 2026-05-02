from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4

class Usuario(BaseModel):
    email: EmailStr
    senha: str
    telefone: str
    id_usuario: UUID = Field(default_factory=uuid4)

    def to_dict(self):
        return {
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
            "id_usuario": self.id_usuario
        }

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str