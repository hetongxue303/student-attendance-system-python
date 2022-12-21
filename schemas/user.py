"""
用户
@Author:何同学
"""
from pydantic import BaseModel


class UserLoginDto(BaseModel):
    """
    用户登录模型
    """
    avatar: str = None
    is_admin: bool
    username: str = None

    class Config:
        orm_mode = True


class User(UserLoginDto):
    user_id: int
    password: str = None
    real_name: str = None
    gender: int
    email: str = None
    phone: str = None
    role: int
    is_enable: bool
    is_delete: bool
    description: str = None

    class Config:
        orm_mode = True
