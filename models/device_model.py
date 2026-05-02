from uuid import uuid4
import secrets
from pydantic import BaseModel
from datetime import datetime, UTC

class CriarDevice(BaseModel):
    device_name: str
    device_type: str

class Device(BaseModel):
    device_id: str
    device_name: str
    device_type: str
    device_token: str
    user_id: str
    created_at: datetime

    @classmethod
    def criar(cls, data: CriarDevice, user_id: str):
        return cls(
            device_id = str(uuid4()),
            device_name = data.device_name,
            device_type = data.device_type,
            device_token = secrets.token_hex(16),
            user_id = user_id,
            created_at = datetime.now(UTC),
        )