import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BANCO = BASE_DIR.parent / "database" / "db.json"

def carregar_db():
    with open(BANCO, 'r') as arquivo:
        return json.load(arquivo)

def salvar_db(novo_banco):
    with open(BANCO, "w", encoding="utf-8") as arq:
        json.dump(novo_banco, arq, ensure_ascii=False, indent=4, default=str)
        return True

def salvar_usuario(user):
    db = carregar_db()
    db["users"].append(user.model_dump())
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

def salvar_dispositivo(dispositivo):
    db = carregar_db()
    db["devices"].append(dispositivo.model_dump())
    salvar_db(db)

    return True