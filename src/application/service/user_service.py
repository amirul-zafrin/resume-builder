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
        dict_data = data.model_dump()
        created_user = self.repository.create(data=dict_data)
        return created_user

    def update(
        self,
        id: int,
        data: UserPatchModel,
    ) -> User:
        target_user = self.get_by_id(id=id)
        dict_data = data.model_dump(exclude_unset=True)

        if not dict_data:
            return target_user

        updated_user = self.repository.update(
            id=id,
            data=dict_data,
            target=target_user,
        )
        return updated_user

    def delete(
        self,
        id: int,
    ) -> User:
        target_user = self.get_by_id(id=id)
        delete_status = self.repository.delete(
            id=id,
            target=target_user,
        )
        return delete_status
