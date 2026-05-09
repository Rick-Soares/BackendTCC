from models.device_model import CriarDevice, Device
from services.db_service import salvar_dispositivo, buscar_dispositivos_por_usuario


def criar_dispositivo(nome_dispositivo, tipo_dispositivo, user_id):
    data = CriarDevice(device_name=nome_dispositivo, device_type=tipo_dispositivo)
    dispositivo = Device.criar(data=data, user_id=user_id)

    salvar_dispositivo(dispositivo)

    return {
        "mensagem": "Dispositivo criado com sucesso."
    }

def listar_dispositivo(user_id):
    dispositivos = buscar_dispositivos_por_usuario(user_id=user_id)

    return {"devices": dispositivos}