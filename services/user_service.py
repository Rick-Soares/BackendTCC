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
        raise ValueError("Usuário ou senha incorretos.")

    if usuario["senha"] != senha:
        raise ValueError("Usuário ou senha incorretos.")

    return {
        "email": usuario["email"],
        "mensagem": "Login realizado com sucesso."
    }