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
OUTRO_USUARIO = {
    "nome": "outroUsuario",
    "email": "teste2@gmail.com",
    "senha": "123456"
}
LOGIN_OUTRO_USUARIO = {
    "email": "teste2@gmail.com",
    "senha": "123456"
}
TELEFONE = {
    "numero": "1123456789"
}
TELEFONE_INVALIDO =  {
    "numero": "numeroErrado"
}
def test_novo_telefone_correto():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/phones/", json=TELEFONE, headers=headers)

    esvaziar_tabelas()

    assert response.status_code == 201

def test_novo_telefone_numero_invalido():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/phones/", json=TELEFONE_INVALIDO, headers=headers)
    esvaziar_tabelas()
    assert response.status_code == 422

def test_novo_telefone_ja_existente():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    client.post("/phones/", json=TELEFONE, headers=headers)
    response = client.post("/phones/", json=TELEFONE, headers=headers)

    esvaziar_tabelas()

    assert response.status_code == 409

def test_listar_telefones():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]

    headers = {"Authorization": f"Bearer {auth_token}"}
    ##client.post("/phones/", json=TELEFONE, headers=headers)

    response = client.get("/phones/", headers=headers)

    esvaziar_tabelas()

    assert response.status_code == 200

def test_listar_telefones_token_invalido():
    auth_token_invalido = "123"
    headers = {"Authorization": f"Bearer {auth_token_invalido}"}

    response = client.get("/phones/", headers=headers)

    esvaziar_tabelas()

    assert response.status_code == 401

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

def test_deletar_telefone_token_acesso_invalido():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token_valido = resposta_login.json()["access_token"]

    headers_valido = {"Authorization": f"Bearer {auth_token_valido}"}
    client.post("/phones/", json=TELEFONE, headers=headers_valido)

    resposta_telefone = client.get("/phones/", headers=headers_valido)
    lista_telefones = resposta_telefone.json()["telefones"]
    telefone_id = lista_telefones[0]["telefone_id"]

    auth_token_invalido = "123"
    headers_invalido = {"Authorization": f"Bearer {auth_token_invalido}"}

    response = client.delete(f"/phones/{telefone_id}", headers=headers_invalido)

    esvaziar_tabelas()

    assert response.status_code == 401

def test_deletar_telefone_com_id_de_telefone_invalido():
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}

    telefone_id_invalido = "123"

    response = client.delete(f"/phones/{telefone_id_invalido}", headers=headers)

    esvaziar_tabelas()

    assert response.status_code == 404

def test_deletar_telefone_usuario_nao_contem_telefones():
    #Cria usuario 1 e adiciona um telefone na conta dele. O telefone_id deste user
    #vai ser usado posteriormente para simular uma invasão
    client.post("/auth/criar-usuario", json=USUARIO)
    resposta_login = client.post("/auth/login", json=LOGIN)
    auth_token = resposta_login.json()["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    client.post("/phones/", json=TELEFONE, headers=headers)
    resposta_telefone = client.get("/phones/", headers=headers)
    lista_telefones = resposta_telefone.json()["telefones"]
    telefone_id = lista_telefones[0]["telefone_id"]

    #Usuario 2. Ele tem um token de acesso válido, porém, está tentando apagar dados de outro user
    client.post("/auth/criar-usuario", json=OUTRO_USUARIO)
    resposta_login_outro_usuario = client.post("/auth/login", json=LOGIN_OUTRO_USUARIO)
    auth_token_outro_usuario = resposta_login_outro_usuario.json()["access_token"]
    headers_outro_usuario = {"Authorization": f"Bearer {auth_token_outro_usuario}"}

    response = client.delete(f"/phones/{telefone_id}", headers=headers_outro_usuario)

    esvaziar_tabelas()

    assert response.status_code == 404