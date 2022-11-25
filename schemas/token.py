"""
token实体
@Author:何同学
"""
from datetime import timedelta
from typing import List
from pydantic import BaseModel


class Token(BaseModel):
    token: str | None
    expired_time: timedelta


class TokenData(BaseModel):
    username: str | None = None
    scopes: List[str] = []
