from fastapi import APIRouter, HTTPException, Depends
from services.device_service import criar_dispositivo
from models.device_model import CriarDevice
from auth.dependencias_auth import verificar_token

device_router = APIRouter(prefix="/devices", tags=["Dispositivo"])

@device_router.post("/registrar-dispositivo")
async def novo_dispositivo(data: CriarDevice, user_id : str = Depends(verificar_token)):
    try:
        resposta = criar_dispositivo(data.device_name, data.device_type, user_id)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return resposta