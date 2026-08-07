from models.user_model import CriarUsuario, Usuario
from services.db_service import buscar_usuario_email, salvar_usuario
from auth.jwt_auth import gerar_token
from auth.security_utils import gerar_hash, verificar_senha
from exceptions import *

def criar_usuario(email, senha, nome):
    if buscar_usuario_email(email):
        raise RecursoJaExisteError("Email já existente.")

    senha_hash = gerar_hash(senha)

    data = CriarUsuario(email=email, senha=senha_hash, nome=nome)
    usuario = Usuario.criar(data=data)

    salvar_usuario(usuario)
    return {
        "mensagem": "Usuário cadastrado com sucesso."
    }

def login_user(email, senha):
    usuario = buscar_usuario_email(email)

    if not usuario:
        raise CredenciaisInvalidasError("Usuário ou senha incorretos.")

    if not verificar_senha(senha, usuario.senha_hash):
        raise CredenciaisInvalidasError("Usuário ou senha incorretos.")

    token = gerar_token(usuario.user_id)
    return {
  "access_token": token,
  "token_type": "bearer"
}