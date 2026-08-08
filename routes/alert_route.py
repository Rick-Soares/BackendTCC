from fastapi import APIRouter, HTTPException, Depends, status
from exceptions import RecursoNaoEncontradoError, CredenciaisInvalidasError
from services.alerta_service import alerta_queda, listar_alertas
from models.alert_model import AlertaRequest
from auth.dependencias_auth import verificar_token

alert_router = APIRouter(prefix="/alerta", tags=["Alerta"])

@alert_router.post("/", status_code=status.HTTP_200_OK)
def gerar_alerta(data: AlertaRequest):
    try:
        resposta = alerta_queda(data.device_id, data.device_token)
    except RecursoNaoEncontradoError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CredenciaisInvalidasError as e:
        raise HTTPException(status_code=401, detail=str(e))
    else:
        return resposta

@alert_router.get("/", status_code=status.HTTP_200_OK)
def alertas(user_id: str = Depends(verificar_token)):
    try:
        return listar_alertas(user_id)
    except CredenciaisInvalidasError as e:
        raise HTTPException(status_code=401, detail=str(e))