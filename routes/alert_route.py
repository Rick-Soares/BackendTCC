from fastapi import APIRouter, HTTPException
from services.alerta_service import alerta_queda
alert_router = APIRouter(prefix="/alerta", tags=["Alerta"])

@alert_router.post("/gerar-alerta")
def gerar_alerta(device_id):
    try:
        resposta = alerta_queda(device_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return resposta