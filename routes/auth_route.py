from fastapi import APIRouter, HTTPException
from services.user_service import criar_usuario, login_user
from models.user_model import CriarUsuario, LoginRequest

auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.post("/criar-usuario")
async def novo_usuario(data: CriarUsuario):
    try:
        criar_usuario(data.email, data.senha, data.nome)
    except FileExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return {
        "mensagem": "Usuário cadastrado com sucesso."
        }


@auth_router.post("/login")
async def login_usuario(data: LoginRequest):
    try:
        login_user(data.email, data.senha)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    else:
        return {
            "mensagem": "Acesso liberado."
        }