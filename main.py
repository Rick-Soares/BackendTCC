from fastapi import FastAPI

app = FastAPI()

from routes.phone_route import phone_router
from routes.auth_route import auth_router
from routes.device_route import device_router

app.include_router(phone_router)
app.include_router(auth_router)
app.include_router(device_router)