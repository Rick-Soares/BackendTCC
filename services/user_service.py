from db_service import salvar_db, carregar_db, salvar_usuario
from models.user_model import Usuario
from services.db_service import buscar_usuario_email


def criar_usuario(email, senha, telefone):
    if buscar_usuario_email(email):
        raise FileExistsError("Email já existente.")

    user = Usuario(email=email, senha=senha, telefone=telefone)
    salvar_usuario(user)
    return True

def login_user(email, senha):
    db = carregar_db()

    for usuario in db["users"]:
        if usuario["email"] == email and usuario["senha"] == senha:
            return True

    return False