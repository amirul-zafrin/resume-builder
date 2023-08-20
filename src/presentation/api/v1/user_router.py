from fastapi import APIRouter, Depends, Path

from application.model.pydantic import UserPatchModel, UserPostModel, UserResponseModel
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
    """get all registered user"""
    users = service.get_all()
    return users


@user_router.get(
    "/{user_id}",
    response_model=UserResponseModel,
)
async def get_user_by_id(
    user_id: int = Path(ge=1),
    service: UserService = Depends(),
):
    """Get registered user by user_id"""
    user = service.get_by_id(id=user_id)
    return user


@user_router.post(
    "/",
    response_model=UserResponseModel,
)
async def create_new_user(
    data: UserPostModel,
    service: UserService = Depends(),
):
    created_user = service.create(data=data)
    return created_user


@user_router.patch(
    "/{user_id}",
    response_model=UserResponseModel,
)
async def update_user(
    data: UserPatchModel,
    user_id: int = Path(ge=1),
    service: UserService = Depends(),
):
    updated_user = service.update(
        id=user_id,
        data=data,
    )
    return updated_user


@user_router.delete(
    "/{user_id}",
    response_model=bool,
)
async def delete_user(
    user_id: int = Path(ge=1),
    service: UserService = Depends(),
):
    delete_status = service.delete(id=user_id)
    return delete_status
