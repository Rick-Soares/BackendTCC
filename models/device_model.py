from uuid import uuid4
import secrets
from pydantic import BaseModel, ConfigDict
from datetime import datetime, UTC

class CriarDevice(BaseModel):
    device_name: str
    device_type: str

    model_config = ConfigDict(extra="forbid")

class Device(BaseModel):
    device_id: str
    device_name: str
    device_type: str
    device_token: str
    user_id: str
    created_at: str | datetime

    @classmethod
    def criar(cls, data: CriarDevice, user_id: str = None, id_dispositivo = None, token_dispositivo = None, criado_em = None):
        return cls(
            device_id = id_dispositivo or str(uuid4()),
            device_name = data.device_name,
            device_type = data.device_type,
            device_token = token_dispositivo or secrets.token_hex(16),
            user_id = user_id,
            created_at = criado_em or datetime.now(UTC)
        )