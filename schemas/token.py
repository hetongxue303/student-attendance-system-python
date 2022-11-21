"""
token实体
@Author:何同学
"""
from datetime import timedelta

from pydantic import BaseModel


class Token(BaseModel):
    token: str | None
    expired_time: timedelta
