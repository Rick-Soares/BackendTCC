from fastapi import APIRouter, HTTPException
from models.phone_model import TelefoneRequest
from services.phone_service import (
    criar_telefone,
    listar_telefones,
    remover_telefone
)
from pydantic import BaseModel

phone_router = APIRouter(prefix="/phones", tags=["Telefones"])

