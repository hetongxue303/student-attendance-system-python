"""
token
@Author:何同学
"""
from datetime import timedelta
from typing import List
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str | None
    expired_time: timedelta | None


class TokenData(BaseModel):
    username: str | None = None
    scopes: List[str] = []
