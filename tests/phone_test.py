from services.db_service import esvaziar_tabelas
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

USUARIO = {"nome": "Ricardo2",
            "email": "teste@gmail.com",
            "senha": "123456"}
LOGIN = {
    "email": "teste@gmail.com",
    "senha": "123456"
}
TELEFONE = {
    "numero": "12345678910"
}
def test_novo_telefone():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/phones/", json=TELEFONE, headers=headers)

    esvaziar_tabelas()

    assert response.status_code == 200

def test_listar_telefones():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    ##client.post("/phones/", json=TELEFONE, headers=headers)

    response = client.get("/phones/", headers=headers)

    esvaziar_tabelas()

    assert response.status_code == 200

def test_deletar_telefone():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    client.post("/phones/", json=TELEFONE, headers=headers)

    resposta_telefone = client.get("/phones/", headers=headers)
    lista_telefones = resposta_telefone.json()["telefones"]
    telefone_id = lista_telefones[0]["telefone_id"]

    response = client.delete(f"/phones/{telefone_id}", headers=headers)
    esvaziar_tabelas()

    assert response.status_code == 200
