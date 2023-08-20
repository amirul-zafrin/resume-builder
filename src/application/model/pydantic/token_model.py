from pydantic import BaseModel
from datetime import datetime


class TokenModel(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class TokenData(BaseModel):
    user_id: int
    username: str
    expire: datetime
