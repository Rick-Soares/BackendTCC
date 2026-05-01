import json
from models.device_model import Device
BANCO = "database/db.json"

def carregar_db():
    with open(BANCO, 'r') as arquivo:
        return json.load(arquivo)

def salvar_db(novo_banco):
    with open(BANCO, "w", encoding="utf-8") as arq:
        json.dump(novo_banco, arq, ensure_ascii=False, indent=4, default=str)
        return True

def salvar_usuario(user):
    db = carregar_db()
    db["users"].append(user.to_dict())
    salvar_db(db)
    return True

def buscar_usuario_email(email):
    db = carregar_db()
    for usuario in db["users"]:
        if usuario["email"] == email:
            return usuario
    return False

def deletar_usuario_por_email(email):
    db = carregar_db()
    for usuario in db["users"]:
        if usuario["email"] == email:
            db["users"].remove(usuario)
            salvar_db(db)
            return True
    return False

def registrar_dispositivo(email_usuario):
    if not buscar_usuario_email(email_usuario):
        raise FileNotFoundError("Email não encontrado.")
    db = carregar_db()

    dispositivo = Device(email_usuario=email_usuario)
    db["devices"].append(dispositivo.to_dict())

    salvar_db(db)
    return True

