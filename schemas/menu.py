"""
菜单模型
@Author:何同学
"""
from datetime import datetime

from pydantic import BaseModel


class MenuDto(BaseModel):
    menu_id: int = None
    menu_name: str = None
    menu_title: str = None
    menu_type: int = None
    parent_id: int = None
    path: str = None
    component: str = None
    sort: int = None
    redirect: str = None
    icon: str = None
    per_key: str = None
    is_show: bool = None
    is_sub: bool = None
    is_cache: bool = None
    is_delete: bool = None
    description: str = None
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class MenuTreeDto(MenuDto):
    children: list[MenuDto] = []


class MenuPermissionDto(BaseModel):
    role_id: int = None
    data: list[int] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class MenuLazyTreeDto(BaseModel):
    id: int = None
    name: str = None
    disable: bool = None
    leaf: bool = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
