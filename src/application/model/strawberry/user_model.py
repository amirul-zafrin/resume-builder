from datetime import datetime

import strawberry


@strawberry.type
class User:
    user_id: int
    username: str
    password: str
    user_date_created: datetime
    user_date_last_modified: datetime
