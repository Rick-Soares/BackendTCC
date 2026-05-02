from models.device_model import CriarDevice, Device
from services.db_service import salvar_dispositivo

USER_ID_FIXO = "123"

def criar_dispositivo(nome_dispositivo, tipo_dispositivo):
    data = CriarDevice(device_name=nome_dispositivo, device_type=tipo_dispositivo)
    dispositivo = Device.criar(data=data, user_id=USER_ID_FIXO)

    salvar_dispositivo(dispositivo)

    return {
        "mensagem": "Dispositivo criado com sucesso."
    }