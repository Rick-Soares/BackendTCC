from models.device_model import CriarDevice, Device
from db_service import salvar_dispositivo


def criar_dispositivo(nome_dispositivo, tipo_dispositivo):
    data = CriarDevice(device_name=nome_dispositivo, device_type=tipo_dispositivo)
    dispositivo = Device.criar(data=data, user_id="123")

    salvar_dispositivo(dispositivo)

    return {
        "mensagem": "Dispositivo criado com sucesso."
    }
