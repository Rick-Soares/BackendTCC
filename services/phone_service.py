from models.phone_model import CriarTelefone, Telefone
from services.db_service import salvar_telefone, verificar_telefone

def criar_telefone(numero, user_id):
    if not numero.isdigit():
        raise ValueError("Número inválido.")
    if not verificar_telefone(numero):
        raise ValueError("Telefone já cadastrado.")

    data = CriarTelefone(numero=numero)
    telefone = Telefone.criar(data=data, user_id=user_id)

    salvar_telefone(telefone)

    return {
    "mensagem": "Telefone cadastrado com sucesso."
}


