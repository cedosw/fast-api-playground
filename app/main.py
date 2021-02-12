from app.api.health import health
import os

from app.config import Settings, get_settings
from fastapi import FastAPI, Depends
from app.api import health


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(health.router)

    return application


app = create_application()