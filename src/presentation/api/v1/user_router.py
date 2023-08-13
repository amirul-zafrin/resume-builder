from fastapi import APIRouter, Depends

from application.model import UserPatchModel, UserPostModel, UserResponseModel
from application.service import UserService

user_router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@user_router.get(
    "/",
    response_model=list[UserResponseModel],
)
async def get_all_user(
    service: UserService = Depends(),
):
    users = service.get_all()
    return users


@user_router.get(
    "/{user_id}",
    response_model=UserResponseModel,
)
async def get_user_by_id(
    user_id: int,
    service: UserService = Depends(),
):
    user = service.get_by_id(id=user_id)
    return user
