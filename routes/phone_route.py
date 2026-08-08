from fastapi import APIRouter, HTTPException, Depends, status
from exceptions import RecursoJaExisteError, RecursoNaoEncontradoError, DadoInvalidoError, CredenciaisInvalidasError
from models.phone_model import TelefoneRequest
from services.phone_service import (
    criar_telefone,
    listar_telefones,
    remover_telefone
)
from auth.dependencias_auth import verificar_token

phone_router = APIRouter(prefix="/phones", tags=["Telefones"])

@phone_router.post("/", status_code=status.HTTP_201_CREATED)
async def novo_telefone(data: TelefoneRequest, user_id: str = Depends(verificar_token)):
    try:
        return criar_telefone(data.numero, user_id)
    except RecursoJaExisteError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except DadoInvalidoError as e:
        raise HTTPException(status_code=422, detail=str(e))


@phone_router.get("/", status_code=status.HTTP_200_OK)
async def listar(user_id: str = Depends(verificar_token)):
    try:
        resposta = listar_telefones(user_id)
    except CredenciaisInvalidasError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return resposta


@phone_router.delete("/{telefone_id}", status_code=status.HTTP_200_OK)
async def deletar(telefone_id: str, user_id: str = Depends(verificar_token)):
    try:
        return remover_telefone(telefone_id, user_id)
    except RecursoNaoEncontradoError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CredenciaisInvalidasError as e:
        raise HTTPException(status_code=401, detail=str(e))