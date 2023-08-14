from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from .core import BasePatchModel, BasePostModel


class UserResponseModel(BaseModel):
    """Response data for '/user' endpoint"""

    user_id: int
    username: EmailStr
    password: str
    user_date_created: datetime
    user_date_last_modified: datetime


class UserPostModel(BasePostModel):
    """Input data for user creation"""

    username: EmailStr
    password: str


class UserPatchModel(BasePatchModel):
    """Input data for user updation"""

    username: Optional[EmailStr] = None
    password: Optional[str] = None
