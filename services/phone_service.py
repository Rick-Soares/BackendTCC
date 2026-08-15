from exceptions import RecursoJaExisteError, RecursoNaoEncontradoError, DadoInvalidoError
from models.phone_model import CriarTelefone, Telefone
from services.db_service import salvar_telefone, verificar_telefone, buscar_telefones_por_usuario, deletar_telefone

def criar_telefone(numero, user_id):
    numero_tratado = numero.strip()
    if not numero_tratado.isdigit():
        raise DadoInvalidoError("Telefone inválido. O telefone deve conter apenas números")
    if len(numero_tratado) != 13:
        raise DadoInvalidoError("Telefone inválido. O telefone deve conter exatamente 13 digitos.")
    if not numero_tratado.startswith("55"):
        raise DadoInvalidoError("Telefone inválido. O número deve conter DDI '55'")
    if not verificar_telefone(numero_tratado):
        raise RecursoJaExisteError("Telefone já cadastrado.")

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
    telefones_do_usuario = buscar_telefones_por_usuario(user_id)
    if not telefones_do_usuario:
        raise RecursoNaoEncontradoError("Usuário não tem telefones cadastrados")

    for telefone in telefones_do_usuario:
        if telefone_id == telefone.telefone_id:
            deletar_telefone(telefone_id)
            return {
                "mensagem": "Telefone removido com sucesso."
            }

    raise RecursoNaoEncontradoError("Telefone não encontrado.")


