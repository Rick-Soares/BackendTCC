from uuid import uuid8
from pydantic import BaseModel, Field

class Device(BaseModel):
    device_id: str = Field(default_factory=uuid8)
    email_usuario: str

    def to_dict(self):
        return {
            "device_id": self.device_id,
            "email_usuario": self.email_usuario,
        }
