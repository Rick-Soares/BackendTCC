from fastapi import APIRouter, HTTPException, Depends
from services.alerta_service import alerta_queda, listar_alertas
from models.alert_model import AlertaRequest
from auth.dependencias_auth import verificar_token

alert_router = APIRouter(prefix="/alerta", tags=["Alerta"])

@alert_router.post("/")
def gerar_alerta(data: AlertaRequest):
    try:
        resposta = alerta_queda(data.device_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return resposta

@alert_router.get("/alertas")
def alertas(user_id: str = Depends(verificar_token)):
    try:
        return listar_alertas(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))