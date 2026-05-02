from fastapi import APIRouter, HTTPException
from services.db_service import registrar_dispositivo

device_router = APIRouter(prefix="/order", tags=["Dispositivo"])

@device_router.post("/registrar-dispositivo")
async def novo_dispositivo(email_usuario: str):
    try:
        registrar_dispositivo(email_usuario)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return {
            "mensagem": "Dispositivo cadastrado com sucesso."
        }
