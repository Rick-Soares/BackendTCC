from models.user_model import Usuario
from services.db_service import buscar_usuario_email, salvar_usuario


def criar_usuario(email, senha, telefone):
    if buscar_usuario_email(email):
        raise FileExistsError("Email já existente.")

    user = Usuario(email=email, senha=senha, telefone=telefone)
    salvar_usuario(user)
    return True

def login_user(email, senha):
    usuario = buscar_usuario_email(email)

    if not usuario:
        raise FileNotFoundError("Usuário ou senha incorreto.")

    if usuario["senha"] == senha:
        return True

    raise ValueError("Usuário ou senha incorreto.")