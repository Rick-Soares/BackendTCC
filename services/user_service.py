from db_service import salvar_db, carregar_db
from models.user_model import Usuario

def criar_usuario(email, senha, telefone):
    usuario = Usuario(email, senha, telefone)
    return True
