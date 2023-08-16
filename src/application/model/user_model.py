from datetime import datetime
from typing import Optional

from pydantic import EmailStr, constr

from .core import BasePatchModel, BasePostModel, BaseResponseModel


class UserResponseModel(BaseResponseModel):
    """Response data for '/user' endpoint"""

    user_id: int
    username: EmailStr
    # password: str
    user_date_created: datetime
    user_date_last_modified: datetime


class UserPostModel(BasePostModel):
    """Input data for user creation"""

    username: EmailStr
    password: constr(min_length=7)


class UserPatchModel(BasePatchModel):
    """Input data for user updation"""

    username: Optional[EmailStr] = None
    password: Optional[str] = None
