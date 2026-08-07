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
def test_novo_usuario():
    response = client.post("/auth/criar-usuario", json=USUARIO)
    esvaziar_tabelas()
    assert response.status_code == 200

def test_login_usuario():
    client.post("/auth/criar-usuario", json=USUARIO)
    response = client.post("/auth/login", json=LOGIN)
    esvaziar_tabelas()
    assert response.status_code == 200