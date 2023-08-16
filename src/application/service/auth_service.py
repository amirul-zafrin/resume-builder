from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from domain.entity import User
from infrastructure.authentication import crypt_context, oauth2_scheme
from persistence import UserRepository
from settings import expiration_minute, jwt_hash_algo, secret_key

from ..exception import EntryNotFoundError, UnauthorizedError
from ..model import TokenModel, TokenData, UserPatchModel, UserPostModel
from .auth_service_interface import AuthServiceInterface


class AuthService(AuthServiceInterface):
    def __init__(
        self,
        repository: UserRepository = Depends(),
    ) -> None:
        self.repository = repository

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
        data: UserPatchModel,
    ) -> User:
        return super().update(data)

    def delete(
        self,
        id: int,
    ) -> bool:
        return super().delete(id)

    def get_by_username(
        self,
        username: str,
    ) -> User:
        user = self.repository.get_by_username(username=username)
        if not user:
            raise EntryNotFoundError
        return user

    def signup(
        self,
        data: UserPostModel,
    ) -> User:
        data.password = self._hash_password(data.password)
        created_user = self.create(data=data)
        return created_user

    def login(
        self,
        data: OAuth2PasswordRequestForm,
    ) -> TokenModel:
        username = data.username
        plain_password = data.password
        user = self.get_by_username(username=username)
        verificaton_status = self._verify_password(
            plain_password=plain_password,
            hashed_password=user.password,
        )
        if verificaton_status:
            jwt_token = self._generate_access_token(
                username=user.username,
                user_id=user.user_id,
            )
            return TokenModel(access_token=jwt_token)
        else:
            raise UnauthorizedError

    @classmethod
    def validate_user(
        cls,
        token: str = Depends(oauth2_scheme),
    ):
        token_data = TokenData(
            **jwt.decode(
                token=token,
                key=secret_key,
                algorithms=jwt_hash_algo,
            )
        )
        if (expire := token_data.expire) > (now := datetime.utcnow()):
            return token_data
        elif expire < now:
            raise UnauthorizedError("Token expired")

    def _verify_password(
        self,
        plain_password: str,
        hashed_password: str,
    ) -> bool:
        verification_status = crypt_context.verify(
            secret=plain_password,
            hash=hashed_password,
        )
        return verification_status

    def _hash_password(
        self,
        plain_password: str,
    ) -> str:
        hashed_password = crypt_context.hash(secret=plain_password)
        return hashed_password

    def _generate_access_token(
        self,
        username: str,
        user_id: int,
    ) -> str:
        expire = datetime.utcnow() + timedelta(minutes=expiration_minute)
        token_dict = {
            "user_id": user_id,
            "username": username,
            "expire": str(expire),
        }
        jwt_token = jwt.encode(
            token_dict,
            key=secret_key,
            algorithm=jwt_hash_algo,
        )
        return jwt_token
