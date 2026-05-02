from services.db_service import carregar_db

def alerta_queda(device_id):
    db = carregar_db()

    for dispositivo in db["devices"]:
        if dispositivo["device_id"] == device_id:
            user_id = dispositivo["user_id"]
            lista = []
            for telefone in db["telefones"]:
                if telefone["user_id"] == user_id:
                    lista.append(f"ALERTA! ligando para {telefone["numero"]}")
            return lista
        raise ValueError("Device_id nao encontrado.")
    return False
alerta_queda("785e2214-1283-4992-a280-ff750947f5cf")