from os import replace
from motor.core import AgnosticCollection
from pydantic.utils import Obj
from app.api.user.user import User, UserData
from app.database import get_database
from typing import List
from bson import ObjectId
import logging


def get_collection() -> AgnosticCollection:
    return get_database()['playground']['users']

async def find_users() -> List[User]:
    user_collection = get_collection()
    users = []

    async for user in user_collection.find():
        users.append(User(**user))

    return users

async def find_user_by_id(id: str) -> User:
    user_by_id = await get_collection().find_one({ '_id': ObjectId(id) })

    return User(**user_by_id)


async def create_user(data: UserData) -> User:
    user_collection = get_collection()

    result = await user_collection.insert_one(data.dict())

    return User(**data.dict(), id=result.inserted_id)


async def update_user(user_id: str, user_data: UserData) -> User:
    user_collection = get_collection()

    await user_collection.replace_one({ '_id': ObjectId(user_id) }, user_data.dict())

    return User(**user_data.dict(), id=ObjectId(user_id))


async def delete_user(user_id: str):
    result = await get_collection().delete_one({ '_id': ObjectId(user_id) })

    return { 
        "deletedDocuments": result.deleted_count,
        "acknowledged": result.acknowledged
     }