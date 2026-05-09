from fastapi import APIRouter, HTTPException, Depends
from models.phone_model import TelefoneRequest
from services.phone_service import (
    criar_telefone,
    listar_telefones,
    remover_telefone
)
from auth.dependencias_auth import verificar_token

phone_router = APIRouter(prefix="/phones", tags=["Telefones"])

@phone_router.post("/")
async def novo_telefone(data: TelefoneRequest, user_id: str = Depends(verificar_token)):
    try:
        return criar_telefone(data.numero, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@phone_router.get("/")
async def listar(user_id: str = Depends(verificar_token)):
    return listar_telefones(user_id)


@phone_router.delete("/{telefone_id}")
async def deletar(telefone_id: str, user_id: str = Depends(verificar_token)):
    try:
        return remover_telefone(telefone_id, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))