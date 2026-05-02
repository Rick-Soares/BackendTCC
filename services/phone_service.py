from models.phone_model import CriarTelefone, Telefone
from services.db_service import salvar_telefone, verificar_telefone, buscar_telefones_por_usuario, deletar_telefone

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

def listar_telefones(user_id):
    telefones = buscar_telefones_por_usuario(user_id)

    return {
        "telefones": telefones
    }


def remover_telefone(telefone_id, user_id):
    sucesso = deletar_telefone(telefone_id, user_id)

    if not sucesso:
        raise ValueError("Telefone não encontrado.")

    return {
        "mensagem": "Telefone removido com sucesso."
    }

print(remover_telefone("9b654f5b-d514-46af-b4c8-3d54ca8d2a02", "123456"))