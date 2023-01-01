"""
角色相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Body, Security
from sqlalchemy.orm import Session

from core.security import check_permissions
from crud.role import query_role_list_all
from database.mysql import get_db
from models import Role
from schemas.common import Page, BatchDto
from schemas.result import Success
from schemas.role import RoleDto

router = APIRouter()
db: Session = next(get_db())


@router.get('/get/all', response_model=Success[Page[list[RoleDto]]], summary='查询角色(All)',
            dependencies=[Security(check_permissions)])
async def select_all():
    roles = query_role_list_all()
    return Success(data=roles, message='查询成功')


@router.get('/get/page', response_model=Success[Page[list[RoleDto]]], summary='查询角色(Page)',
            dependencies=[Security(check_permissions)])
async def select_page(currentPage: int, pageSize: int):
    """
    分页查询角色信息
    :param currentPage: 当前页
    :param pageSize: 页面大小
    :return:
    """
    data = Page(total=db.query(Role).filter(Role.is_delete == '0').count(),
                record=db.query(Role).filter(Role.is_delete == '0').limit(pageSize).offset(
                    (currentPage - 1) * pageSize).all())
    return Success(data=data, message='查询成功')


@router.get('/getOne/{id}', summary='查询角色(ById)')
async def select_one(id: int):
    pass


@router.post('/insert', response_model=Success[typing.Any], summary='新增角色',
             dependencies=[Security(check_permissions)])
async def insert_one(data: RoleDto):
    db.add(Role(role_name=data.role_name, role_key=data.role_key, description=data.description))
    db.commit()
    return Success(message='新增成功')


@router.delete('/delete/{role_id}', response_model=Success[typing.Any], summary='删除角色',
               dependencies=[Security(check_permissions)])
async def delete_one(role_id: int):
    """
    删除角色信息
    :param role_id: 角色ID
    :return:
    """
    item = db.query(Role).filter(Role.role_id == role_id).first()
    item.is_delete = '1'
    db.commit()
    return Success(message='删除成功')


@router.delete('/delete/batch', response_model=Success[typing.Any], summary='批量删除角色',
               dependencies=[Security(check_permissions)])
async def delete_batch(data: BatchDto):
    pass


@router.put('/update', response_model=Success[typing.Any], summary='修改角色',
            dependencies=[Security(check_permissions)])
async def update_one(data: RoleDto):
    """
    修改角色信息
    :param data:
    :return:
    """
    item = db.query(Role).filter(Role.role_id == data.role_id).first()
    item.role_name = data.role_name
    item.role_key = data.role_key
    item.description = data.description
    item.is_enable = '1' if data.is_enable else '0'
    item.is_delete = '1' if data.is_delete else '0'
    db.commit()
    return Success(message='修改成功')
