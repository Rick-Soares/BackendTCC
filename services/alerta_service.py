from services.db_service import carregar_db

def alerta_queda(device_id):
    db = carregar_db()

    for dispositivo in db["devices"]:
        if dispositivo["device_id"] == device_id:
            user_id = dispositivo["user_id"]

            for usuario in db["users"]:
                if usuario["user_id"] == user_id:
                    print(f"ALERTA! Queda detectada, ligando para {usuario["nome"]}")
                    return True
    return False