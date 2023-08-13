from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func, DATETIME


class User(Base):
    __tablename__ = "USER"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    user_date_created: Mapped[datetime] = mapped_column(
        DATETIME,
        default=func.now(),
    )
    user_date_last_modified: Mapped[datetime] = mapped_column(
        DATETIME,
        default=func.now(),
        onupdate=func.now(),
    )
