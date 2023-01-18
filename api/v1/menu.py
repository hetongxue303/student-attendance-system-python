"""
菜单相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Security
from sqlalchemy.orm import Session

from core.security import check_permissions
from database.mysql import get_db
from models import Menu, Role_Menu
from schemas.menu import MenuLazyTreeDto
from schemas.result import Success

router = APIRouter()
db: Session = next(get_db())


@router.get('/get/one', response_model=Success[list[MenuLazyTreeDto]], summary='查询菜单(通过角色ID)',
            dependencies=[Security(check_permissions)])
async def select_one(role_id: int = None):
    """
    通过角色ID查询角色菜单信息
    :param role_id:
    :return:
    """
    menu_ids: list[int] = []
    data: list[MenuLazyTreeDto] = []
    record = db.query(Role_Menu).filter(Role_Menu.role_id == role_id).all()
    if record:
        for item in record:
            menu_ids.append(item.menu_id)
    if menu_ids:
        menus = db.query(Menu).filter(Menu.menu_id.in_(menu_ids)).all()
        if menus:
            for menu in menus:
                data.append(MenuLazyTreeDto(id=menu.menu_id, name=menu.menu_title, disable=False,
                                            leaf=True if db.query(Menu).filter(
                                                Menu.parent_id == menu.menu_id).count() == 0 else False))
    return Success(data=data, message='查询成功')


@router.get('/get/tree/lazy', response_model=Success[list[MenuLazyTreeDto]], summary='获取懒加载菜单树',
            dependencies=[Security(check_permissions)])
async def select_lazy_tree(parent_id: int = None):
    """
    获取懒加载菜单树
    :param parent_id: 父ID
    :return:
    """
    data: list[MenuLazyTreeDto] = []
    id: int = 0 if parent_id is None else parent_id
    menus = db.query(Menu).filter(Menu.parent_id == id).all()
    if menus:
        for menu in menus:
            data.append(MenuLazyTreeDto(id=menu.menu_id, name=menu.menu_title, disable=False,
                                        leaf=True if db.query(Menu).filter(
                                            Menu.parent_id == menu.menu_id).count() == 0 else False))
    return Success(data=data, message='查询成功')
