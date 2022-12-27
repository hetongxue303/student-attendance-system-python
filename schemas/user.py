"""
用户模型
@Author:何同学
"""
from typing import List

from pydantic import BaseModel

from schemas.common import Common
from schemas.menu import MenuDto


class LoginDto(BaseModel):
    """
    用户登录模型
    """
    avatar: str = None
    is_admin: bool
    username: str = None
    menus: List[MenuDto] = None
    permissions: List[str] = None
    roles: List[str] = None

    class Config:
        orm_mode = True


class UserDtoOut(Common):
    user_id: int
    username: str = None
    real_name: str = None
    avatar: str = None
    gender: int
    email: str = None
    phone: str = None
    role: int
    is_admin: bool
    is_enable: bool
    is_delete: bool
    description: str = None


class UserDto(UserDtoOut):
    password: str = None


class up_email(BaseModel):
    email: str = None
    code: str = None
    password: str = None

    class Config:
        orm_mode = True


class up_password(BaseModel):
    old_password: str = None
    new_password: str = None
    confirm_password: str = None

    class Config:
        orm_mode = True


class CurrentUserInfo(BaseModel):
    menu_id: List[int] = None
    menu_data: List[MenuDto]

    class Config:
        orm_mode = True
