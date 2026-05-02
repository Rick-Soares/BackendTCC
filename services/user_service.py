from models.user_model import CriarUsuario, Usuario
from services.db_service import buscar_usuario_email, salvar_usuario

def criar_usuario(email, senha, nome):
    if buscar_usuario_email(email):
        raise FileExistsError("Email já existente.")

    data = CriarUsuario(email=email, senha=senha, nome=nome)
    usuario = Usuario.criar(data=data)

    salvar_usuario(usuario)
    return {
        "mensagem": "Usuário cadastrado com sucesso."
    }

def login_user(email, senha):
    usuario = buscar_usuario_email(email)

    if not usuario:
        raise ValueError("Usuário ou senha incorretos.")

    if usuario["senha_hash"] != senha:
        raise ValueError("Usuário ou senha incorretos.")

    return {
        "email": usuario["email"],
        "mensagem": "Login realizado com sucesso."
    }

