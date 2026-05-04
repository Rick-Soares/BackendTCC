from models.device_model import CriarDevice, Device
from services.db_service import salvar_dispositivo



def criar_dispositivo(nome_dispositivo, tipo_dispositivo, user_id):
    data = CriarDevice(device_name=nome_dispositivo, device_type=tipo_dispositivo)
    dispositivo = Device.criar(data=data, user_id=user_id)

    salvar_dispositivo(dispositivo)

    return {
        "mensagem": "Dispositivo criado com sucesso."
    }