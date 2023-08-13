from fastapi import Depends

from application.model.user_model import UserPatchModel, UserPostModel
from domain.entity.user import User
from persistence import UserRepository

from ..exception.error import EntryNotFoundError
from .user_service_interface import UserServiceInterface


class UserService(UserServiceInterface):
    def __init__(
        self,
        repository: UserRepository = Depends(),
    ) -> None:
        self.repository = repository

    def get_all(self) -> list[User]:
        users = self.repository.get_all()
        return users

    def get_by_id(
        self,
        id: int,
    ) -> User:
        user = self.repository.get_by_id(id=id)
        if not user:
            raise EntryNotFoundError
        return user

    def create(
        self,
        data: UserPostModel,
    ) -> User:
        return super().create(data)

    def update(
        self,
        id: int,
        data: UserPatchModel,
    ) -> User:
        # target_user = self.get_by_id(id=id)
        # self.repository.update()
        ...

    def delete(
        self,
        id: int,
    ) -> User:
        return super().delete(id)
