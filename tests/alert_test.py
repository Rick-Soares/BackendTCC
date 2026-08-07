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

def test_gerar_alerta():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    client.post("/devices/", json=DISPOSITIVO, headers=headers)

    resposta_dispositivos = client.get("/devices/", headers=headers)
    lista_dispositivos = resposta_dispositivos.json()["devices"]
    device_id = lista_dispositivos[0]["device_id"]
    device_token = lista_dispositivos[0]["device_token"]

    response = client.post("/alerta/",
                           json={
        "device_id": device_id,
        "device_token": device_token
    })

    esvaziar_tabelas()
    assert response.status_code == 200

def test_listar_alertas():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = client.get("/alerta/", headers=headers)

    esvaziar_tabelas()
    assert response.status_code == 200