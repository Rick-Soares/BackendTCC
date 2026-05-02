from services.db_service import carregar_db, salvar_db
from datetime import datetime, UTC
from uuid import uuid4

def alerta_queda(device_id):
    db = carregar_db()
    dispositivo = None

    for d in db["devices"]:
        if d["device_id"] == device_id:
            dispositivo = d
            break
    if not dispositivo:
        raise ValueError("Dispositivo nao encontrado.")

    user_id = dispositivo["user_id"]
    telefones = []

    for telefone in db["telefones"]:
        if telefone["user_id"] == user_id:
            telefones.append(telefone["numero"])

    if not telefones:
        return {"mensagem": "Alerta recebido, mas nenhum telefone cadastrado."}

    alerta_registro = {
        "alerta_id": str(uuid4()),
        "device_id": device_id,
        "user_id": user_id,
        "timestamp": datetime.now(UTC),
        "telefones_notificados": telefones
    }
    db["alertas"].append(alerta_registro)
    salvar_db(db)

    return {
        "mensagem": "Alerta processado com sucesso.",
        "telefones_notificados": telefones
    }
