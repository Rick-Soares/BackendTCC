from pydantic import BaseModel, ConfigDict

class AlertaRequest(BaseModel):
    device_id: str
    device_token: str

    model_config = ConfigDict(extra="forbid")