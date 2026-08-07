from exceptions import RecursoNaoEncontradoError, CredenciaisInvalidasError
from services.db_service import busca_dispositivo_por_id, buscar_telefones_por_usuario, salvar_alerta, lista_alertas
from datetime import datetime, UTC
from uuid import uuid4

def alerta_queda(device_id, device_token):
    dispositivo = busca_dispositivo_por_id(device_id)
    if not dispositivo:
        raise RecursoNaoEncontradoError("Dispositivo nao encontrado.")

    if dispositivo.device_token != device_token:
        raise CredenciaisInvalidasError("Token do dispositivo inválido")

    user_id = dispositivo.user_id
    telefones = buscar_telefones_por_usuario(user_id= user_id)
    numeros_notificados = []
    for telefone in telefones:
        numeros_notificados.append(telefone.numero)

    salvar_alerta(id_alerta=str(uuid4()),
                  id_dispositivo=str(device_id),
                  id_usuario=str(user_id),
                  data=str(datetime.now(UTC)),
                  telefones=str(numeros_notificados),
                  nome_dispositivo=str(dispositivo.device_name))

    if not telefones:
        return {"mensagem": "Alerta recebido, mas nenhum telefone cadastrado."}
    return {
        "mensagem": "Alerta processado com sucesso.",
        "telefones_notificados": telefones
    }

def listar_alertas(user_id):
    alertas = lista_alertas(id_usuario= user_id)
    return {
        "alertas": alertas
    }