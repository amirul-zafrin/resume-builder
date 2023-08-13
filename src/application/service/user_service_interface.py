from domain.entity import User

from ..model import UserPatchModel, UserPostModel, UserResponseModel
from .core import GenericServiceInterface


class UserServiceInterface(
    GenericServiceInterface[
        User,
        UserPostModel,
        UserPatchModel,
    ]
):
    pass
