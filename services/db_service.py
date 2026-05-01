import json
BANCO = "../database/db.json"

def carregar_db():
    with open(BANCO, 'r') as arquivo:
        return json.load(arquivo)

def salvar_db(novo_banco):
    with open(BANCO, "w", encoding="utf-8") as arq:
        json.dump(novo_banco, arq, ensure_ascii=False, indent=4, default=str)
        return True

def salvar_usuario(user):
    db = carregar_db()
    db["users"].append(user)
    salvar_db(db)
    return True

def buscar_usuario_email(email):
    db = carregar_db()
    for usuario in db["usuarios"]:
        if usuario["email"] == email:
            return usuario
    return False

def deletar_por_email(email):
    db = carregar_db()
    for usuario in db["usuarios"]:
        if usuario["email"] == email:
            db["usuarios"].remove(usuario)
            salvar_db(db)
            return True
    return False
