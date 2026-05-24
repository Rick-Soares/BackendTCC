from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Backend TCC",
    version="1.0.0"
)

from routes.phone_route import phone_router
from routes.auth_route import auth_router
from routes.device_route import device_router
from routes.alert_route import alert_router

app.include_router(phone_router)
app.include_router(auth_router)
app.include_router(device_router)
app.include_router(alert_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "online"}