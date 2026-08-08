from fastapi.testclient import TestClient
from main import app
from services.db_service import esvaziar_tabelas

client = TestClient(app)
USUARIO = {"nome": "Ricardo2",
            "email": "teste@gmail.com",
            "senha": "123456"}
USUARIO_EMAIL_INVALIDO = {
    "nome": "Ricardo22",
    "email": "teste",
    "senha": "123"
}
LOGIN = {
    "email": "teste@gmail.com",
    "senha": "123456"
}
LOGIN_EMAIL_INVALIDO = {
    "email": "teste_errado@gmail.com",
    "senha": "123456"
}
LOGIN_SENHA_INVALIDO = {
    "email": "teste_errado@gmail.com",
    "senha": "senhaErrada"
}

def test_novo_usuario_correto():
    response = client.post("/auth/criar-usuario", json=USUARIO)
    esvaziar_tabelas()
    assert response.status_code == 201

def test_novo_usuario_email_invalido():
    response = client.post("/auth/criar-usuario", json=USUARIO_EMAIL_INVALIDO)
    assert response.status_code == 422

def test_novo_usuario_email_ja_existente():
    response1 = client.post("/auth/criar-usuario", json=USUARIO)
    response2 = client.post("/auth/criar-usuario", json=USUARIO)
    esvaziar_tabelas()

    assert response1.status_code == 201
    assert response2.status_code == 409

def test_login_correto():
    client.post("/auth/criar-usuario", json=USUARIO)
    response = client.post("/auth/login", json=LOGIN)
    esvaziar_tabelas()
    assert response.status_code == 200

def test_login_email_invalido():
    response1 =client.post("/auth/criar-usuario", json=USUARIO)
    response2 = client.post("/auth/login", json=LOGIN_EMAIL_INVALIDO)
    esvaziar_tabelas()

    assert response1.status_code == 201
    assert response2.status_code == 401

def test_login_senha_invalida():
    response1 = client.post("/auth/criar-usuario", json=USUARIO)
    response2 = client.post("/auth/login", json=LOGIN_SENHA_INVALIDO)
    esvaziar_tabelas()

    assert response1.status_code == 201
    assert response2.status_code == 401