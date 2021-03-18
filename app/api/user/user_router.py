from typing import List
from app.api.user.user import User, UserData, UserResource
from fastapi import APIRouter, Request
import app.api.user.user_repo as user_repo

path = "/api/users"
user_router = APIRouter(prefix=path)


def to_user_resource(user: User, request: Request) -> UserResource:
    user_resource = UserResource(**user.dict())
    user_resource.add_self_link(path, request)
    return user_resource


@user_router.get("")
async def get_users(request: Request) -> List[UserResource]:
    users = await user_repo.find_users()
    user_resources = map(lambda user: to_user_resource(user, request), users)
    return list(user_resources)


@user_router.get("/{user_id}")
async def get_user(user_id: str, request: Request) -> UserResource:
    user = await user_repo.find_user_by_id(user_id)
    return to_user_resource(user, request)


@user_router.post("")
async def create_user(user: UserData, request: Request) -> UserResource:
    created_user = await user_repo.create_user(user)
    return to_user_resource(created_user, request)


@user_router.put("/{user_id}")
async def update_user(user_id: str, user_data: UserData, request: Request) -> UserResource:
    updated_user = await user_repo.update_user(user_id, user_data)
    return to_user_resource(updated_user, request)


@user_router.delete("/{user_id}")
async def delete_user(user_id: str):
    return await user_repo.delete_user(user_id)
