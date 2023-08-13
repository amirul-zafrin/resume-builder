from fastapi import Depends
from sqlalchemy.orm import Session

from domain.entity.user import User
from domain.interface import UserRepostoryInterface
from infrastructure.database import get_session


class UserRepository(UserRepostoryInterface):
    def __init__(
        self,
        session: Session = Depends(get_session),
    ) -> None:
        super().__init__()
        self.session = session

    def get_all(self) -> list[User]:
        users = self.session.query(User).all()
        return users

    def get_by_id(
        self,
        id: int,
    ) -> User:
        user = self.session.query(User).get(id)
        return user

    def create(
        self,
        data: dict,
    ) -> User:
        return super().create(data)

    def update(
        self,
        id: int,
        data: dict,
    ) -> User:
        return super().update(id, data)

    def delete(
        self,
        id: int,
    ) -> bool:
        return super().delete(id)
