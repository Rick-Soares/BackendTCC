from fastapi import APIRouter, HTTPException
from services.device_service import criar_dispositivo
from models.device_model import CriarDevice

device_router = APIRouter(prefix="/devices", tags=["Dispositivo"])

@device_router.post("/registrar-dispositivo")
async def novo_dispositivo(data: CriarDevice):
    try:
        resposta = criar_dispositivo(data.device_name, data.device_type)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return resposta