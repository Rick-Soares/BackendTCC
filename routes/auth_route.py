from fastapi import APIRouter, HTTPException, status
from exceptions import RecursoJaExisteError, CredenciaisInvalidasError
from services.user_service import criar_usuario, login_user
from models.user_model import CriarUsuario, LoginRequest

auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.post("/criar-usuario", status_code=status.HTTP_201_CREATED)
async def novo_usuario(data: CriarUsuario):
    try:
        resultado = criar_usuario(data.email, data.senha, data.nome)
    except RecursoJaExisteError as e:
        raise HTTPException(status_code=409, detail=str(e))
    else:
        return resultado

@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login_usuario(data: LoginRequest):
    try:
        resposta = login_user(data.email, data.senha)
    except CredenciaisInvalidasError as e:
        raise HTTPException(status_code=401, detail=str(e))
    else:
        return resposta