import json
BANCO = "BackendTCC/database/db.json"

def carregar_db():
    with open(BANCO, 'r') as arquivo:
        return json.load(arquivo)

def salvar_db(novo_banco):
    with open(BANCO, "w", encoding="utf-8") as arq:
        json.dump(novo_banco, arq, ensure_ascii=False, indent=4, default=str)
        return True