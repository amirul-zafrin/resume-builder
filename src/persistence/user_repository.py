from typing import Optional

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

    def get_all(self) -> list[Optional[User]]:
        users = self.session.query(User).all()
        return users

    def get_by_id(self, id: int) -> Optional[User]:
        user = self.session.query(User).get(id)
        return user

    def get_by_username(self, username: str) -> Optional[User]:
        user = self.session.query(User).filter(User.username == username).scalar()
        return user

    def create(
        self,
        data: dict,
    ) -> User:
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def update(
        self,
        id: int,
        data: dict,
        target: User,
    ) -> User:
        for key, val in data.items():
            setattr(target, key, val)
        self.session.commit()
        self.session.refresh(target)
        return target

    def delete(
        self,
        id: int,
        target: User,
    ) -> bool:
        self.session.delete(target)
        self.session.commit()
        return True
