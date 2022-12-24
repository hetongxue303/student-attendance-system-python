"""
token
@Author:何同学
"""
from datetime import timedelta
from typing import List
from pydantic import BaseModel

from schemas.user import LoginDto


class Token(BaseModel):
    code: int
    message: str
    access_token: str
    expired_time: timedelta
    user: LoginDto

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    username: str | None = None
    scopes: List[str] = []

    class Config:
        orm_mode = True
