from app.database import close_mongo_connection, connect_to_mongo
from app.api.health import health
import logging

from app.config import Settings, get_settings
from fastapi import FastAPI, Depends, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.api import health
from app.api.user.user_router import user_router


def create_application() -> FastAPI:
    application = FastAPI()

    application.add_middleware(CORSMiddleware, allow_origins=["*"])

    application.include_router(health.router)
    application.include_router(user_router)

    application.add_event_handler("startup", connect_to_mongo)
    application.add_event_handler("shutdown", close_mongo_connection)

    return application


app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message was {data}")
