import logging
import os

from functools import lru_cache
from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()
log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT")
    testing: bool = os.getenv("TESTING")
    mongo_url: str = os.getenv("MONGO_URL")



@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading settings from the environment")
    return Settings()
