from fastapi import APIRouter, HTTPException
from models.phone_model import TelefoneRequest
from services.phone_service import (
    criar_telefone,
    listar_telefones,
    remover_telefone
)

phone_router = APIRouter(prefix="/phones", tags=["Telefones"])
#user id para testes
USER_ID_FIXO = "123"

@phone_router.post("/add-phone")
async def novo_telefone(data: TelefoneRequest):
    try:
        return criar_telefone(data.numero, USER_ID_FIXO)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@phone_router.get("/list-phones")
async def listar():
    return listar_telefones(USER_ID_FIXO)


@phone_router.delete("/{telefone_id}")
async def deletar(telefone_id: str):
    try:
        return remover_telefone(telefone_id, USER_ID_FIXO)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))