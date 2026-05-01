from db_service import carregar_db

def alerta_queda(device_id):
    db = carregar_db()

    for dispositivo in db["devices"]:
        if dispositivo["id"] == device_id:
            email_usuario = dispositivo["email"]

            for usuario in db["usuarios"]:
                if usuario["email"] == email_usuario:
                    telefone = usuario["telefone"]

                    print(f"ALERTA! Queda detectada, ligando para {telefone}")
                    return True
    return False