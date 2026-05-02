from fastapi import APIRouter
from services.user_service import criar_usuario, login_user
from services.db_service import registrar_dispositivo
from fastapi import HTTPException
from models.user_model import Usuario

auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.post("/criar-usuario")
async def novo_usuario(data: Usuario):
    try:
        criar_usuario(data.email, data.senha, data.telefone)
    except FileExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return {
        "mensagem": "Usuário cadastrado com sucesso."
        }

@auth_router.post("/registrar-dispositivo")
async def novo_dispositivo(email_usuario: str):
    try:
        registrar_dispositivo(email_usuario)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return {
            "mensagem": "Dispositivo cadastrado com sucesso."
        }

@auth_router.post("/login")
async def login_usuario(email: str, senha: str):
    try:
        login_user(email, senha)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return {
            "mensagem": "Acesso liberado."
        }