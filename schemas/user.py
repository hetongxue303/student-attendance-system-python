"""
用户模型
@Author:何同学
"""
from pydantic import BaseModel

from schemas.common import Common


class LoginDto(Common):
    """
    用户登录模型
    """
    avatar: str = None
    is_admin: bool
    username: str = None

    class Config:
        orm_mode = True


class UserDtoOut(LoginDto):
    user_id: int
    real_name: str = None
    gender: int
    email: str = None
    phone: str = None
    role: int
    is_enable: bool
    is_delete: bool
    description: str = None


class UserDto(UserDtoOut):
    password: str = None
