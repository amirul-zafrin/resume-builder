from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserResponseModel(BaseModel):
    user_id: int
    username: str
    password: str
    user_date_created: datetime
    user_date_last_modified: datetime


class UserPostModel(BaseModel):
    username: str
    password: str


class UserPatchModel(BaseModel):
    username: Optional[str]
    password: Optional[str]
