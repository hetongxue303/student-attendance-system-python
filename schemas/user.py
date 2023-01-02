"""
用户模型
@Author:何同学
"""
from datetime import datetime

from pydantic import BaseModel

from schemas.menu import MenuDto


class LoginDto(BaseModel):
    """
    用户登录模型
    """
    avatar: str = None
    is_admin: bool = None
    username: str = None
    menus: list[MenuDto] = None
    permissions: list[str] = None
    roles: list[str] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserDtoOut(BaseModel):
    user_id: int = None
    username: str = None
    nick_name: str = None
    real_name: str = None
    avatar: str = None
    gender: int = None
    email: str = None
    phone: str = None
    role: int = None
    is_admin: bool = None
    is_enable: bool = None
    is_delete: bool = None
    description: str = None
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserDto(UserDtoOut):
    password: str = None


class up_email(BaseModel):
    email: str = None
    code: str = None
    password: str = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class up_password(BaseModel):
    old_password: str = None
    new_password: str = None
    confirm_password: str = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class CurrentUserInfo(BaseModel):
    menu_id: list[int] = None
    menu_data: list[MenuDto]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
