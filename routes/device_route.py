from fastapi import APIRouter, HTTPException
from services.user_service import criar_dispositivo

device_router = APIRouter(prefix="/order", tags=["Dispositivo"])

@device_router.post("/registrar-dispositivo")
async def novo_dispositivo(nome_dispositivo: str, tipo_dispositivo: str):
    try:
        criar_dispositivo(nome_dispositivo, tipo_dispositivo)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return {
            "mensagem": "Dispositivo cadastrado com sucesso."
        }
