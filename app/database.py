import logging
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import Settings, get_settings
from fastapi import FastAPI, Depends

class Database:
    client: AsyncIOMotorClient = None


db = Database()


def get_database() -> AsyncIOMotorClient:
    return db.client


async def connect_to_mongo():
    settings = get_settings()
    db.client = AsyncIOMotorClient(settings.mongo_url)
    logging.getLogger("uvicorn").info("Connection to mongodb established")


async def close_mongo_connection():
    db.client.close()