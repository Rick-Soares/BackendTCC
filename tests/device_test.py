from fastapi.testclient import TestClient
from main import app
from services.db_service import esvaziar_tabelas

client = TestClient(app)

USUARIO = {"nome": "Ricardo2",
            "email": "teste@gmail.com",
            "senha": "123456"}
LOGIN = {
    "email": "teste@gmail.com",
    "senha": "123456"
}

DISPOSITIVO = {
    "device_name": "Dispositivo Teste",
    "device_type": "Detector de Queda"
}

def test_novo_dispositivo_correto():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/devices/", json=DISPOSITIVO, headers=headers)

    esvaziar_tabelas()
    assert response.status_code == 201

def test_novo_dispositivo_token_invalido():
    auth_token_invalido = "123"
    headers = {"Authorization": f"Bearer {auth_token_invalido}"}

    response = client.post("/devices/", json=DISPOSITIVO, headers=headers)

    assert response.status_code == 401

def test_exibir_dispositivos():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    ##client.post("/devices/", json=DISPOSITIVO, headers=headers) --> cria dispositivo para exemplo
    response = client.get("/devices/", headers=headers)

    esvaziar_tabelas()

    assert response.status_code == 200
    assert response.status_code == 200

def test_exibir_dispositivos_token_invalido():
    auth_token_invalido = "123"
    headers = {"Authorization": f"Bearer {auth_token_invalido}"}

    response = client.get("/devices/", headers=headers)

    assert response.status_code == 401




