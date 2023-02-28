"""
菜单相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Security
from sqlalchemy import func
from sqlalchemy.orm import Session

from core.security import check_permissions
from database.mysql import get_db
from exception.custom import UpdateException, DeleteException
from models import Menu, Role_Menu, Role
from schemas.menu import MenuLazyTreeDto, MenuTreeDto, MenuDto, MenuPermissionDto
from schemas.result import Success

router = APIRouter()
db: Session = next(get_db())


@router.delete('/delete/{id}', response_model=Success, summary='删除菜单')
async def delete(id: int):
    try:
        db.delete(db.query(Menu).filter(Menu.menu_id == id).first())
        db.commit()
        return Success(message='删除成功')
    except:
        db.rollback()
        raise DeleteException(code=400, message='删除失败')


@router.put('/update/show', response_model=Success, summary='更新显示状态')
async def update_status(data: MenuDto):
    try:
        item = db.query(Menu).filter(Menu.menu_id == data.menu_id).first()
        item.is_show = '1' if data.is_show else '0'
        db.commit()
        return Success(message='更新成功')
    except:
        db.rollback()
        raise UpdateException(code=400, message='更新失败')


@router.put('/update/permission', response_model=Success, summary='修改权限',
            dependencies=[Security(check_permissions)])
async def update_one(temp: MenuPermissionDto):
    print(temp)
    try:
        role_id = temp.role_id
        menu_ids = temp.data
        item = db.query(Role).filter(Role.role_id == role_id).first()
        ids_all = [i.menu_id for i in db.query(Role_Menu).filter(Role_Menu.role_id == role_id).all()]
        add_ids = [i for i in (menu_ids + ids_all) if i not in ids_all]
        delete_ids = [i for i in ids_all if i not in [x for x in menu_ids if x in ids_all]]
        if delete_ids:
            db.query(Role_Menu).filter(Role_Menu.menu_id.in_(delete_ids), Role_Menu.role_id == role_id).delete()
        for id in add_ids:
            db.add(Role_Menu(role_id=role_id, menu_id=id))
        if add_ids or delete_ids:
            item.update_time = func.now()
        db.commit()
        return Success(message='更新成功')
    except:
        db.rollback()
        raise UpdateException(code=400, message='更新失败')


@router.get('/tree', response_model=Success[list[MenuTreeDto]], summary='获取菜单(树)')
async def get_tree(menu_title: str = None):
    if menu_title:
        return Success(
            data=db.query(Menu).filter(Menu.menu_title.like('%{0}%'.format(menu_title))).all(),
            message='查询成功')
    return Success(data=filter_menu(data=db.query(Menu).all()), message='查询成功')


def filter_menu(data: list[Menu], parent_id: int = 0) -> list[MenuTreeDto]:
    tree_data: list[MenuTreeDto] = []
    for item in data:
        if item.parent_id == parent_id:
            temp: MenuTreeDto | Menu = item
            temp.children = filter_menu(data=data, parent_id=item.menu_id)
            tree_data.append(temp)
    return tree_data


@router.get('/get/one', response_model=Success[list[MenuDto]], summary='查询菜单(通过角色ID)',
            dependencies=[Security(check_permissions)])
async def select_one(role_id: int = None):
    """
    通过角色ID查询角色菜单信息
    :param role_id:
    :return:
    """
    role_menus = db.query(Role_Menu).filter(Role_Menu.role_id == role_id).all()
    rms: list[int] = []
    for rm in role_menus:
        rms.append(rm.menu_id)
    return Success(data=db.query(Menu).filter(Menu.menu_id.in_(rms)).all(), message='查询成功')


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
