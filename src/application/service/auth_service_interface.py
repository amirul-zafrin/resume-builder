from abc import ABC, abstractmethod

from fastapi.security import OAuth2PasswordRequestForm

from domain.entity import User

from ..model.pydantic import TokenModel, UserPatchModel, UserPostModel


class AuthServiceInterface(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> User:
        ...

    @abstractmethod
    def create(self, data: UserPostModel) -> User:
        ...

    @abstractmethod
    def update(self, data: UserPatchModel) -> User:
        ...

    @abstractmethod
    def delete(self, id: int) -> bool:
        ...

    @abstractmethod
    def get_by_username(self, username: str) -> User:
        ...

    @abstractmethod
    def signup(self, data: UserPostModel) -> bool:
        ...

    @abstractmethod
    def login(self, data: OAuth2PasswordRequestForm) -> TokenModel:
        ...
