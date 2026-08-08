from fastapi import APIRouter, HTTPException, Depends, status
from exceptions import CredenciaisInvalidasError
from services.device_service import criar_dispositivo, listar_dispositivo
from models.device_model import CriarDevice
from auth.dependencias_auth import verificar_token

device_router = APIRouter(prefix="/devices", tags=["Dispositivo"])

@device_router.post("/", status_code=status.HTTP_201_CREATED)
async def novo_dispositivo(data: CriarDevice, user_id : str = Depends(verificar_token)):
    try:
        resposta = criar_dispositivo(data.device_name, data.device_type, user_id)
    except CredenciaisInvalidasError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return resposta

@device_router.get("/", status_code=status.HTTP_200_OK)
async def dispositivos(user_id : str = Depends(verificar_token)):
    try:
        resposta = listar_dispositivo(user_id=user_id)
    except CredenciaisInvalidasError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return resposta
