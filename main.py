from fastapi import FastAPI

app = FastAPI()

from routes.auth_route import auth_router
from routes.order_route import order_router

app.include_router(auth_router)
app.include_router(order_router)