"""
菜单模型
@Author:何同学
"""
from schemas.common import Common


class MenuDto(Common):
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

    class Config:
        orm_mode = True
