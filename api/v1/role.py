"""
角色相关
@Author:何同学
"""
from typing import List

from fastapi import APIRouter, Body, Security

from core.security import check_permissions
from crud.role import query_role_list_all
from schemas.common import Page
from schemas.result import Success
from schemas.role import RoleDto

router = APIRouter()


@router.get('/get/all', response_model=Success[Page[List[RoleDto]]], summary='查询角色(All)',
            dependencies=[Security(check_permissions)])
async def select_all():
    roles = query_role_list_all()
    return Success(data=roles, message='查询成功')


@router.get('/get/page', summary='查询角色(Page)')
async def select_page(data=Body(None)):
    pass


@router.get('/getOne/{id}', summary='查询角色(ById)')
async def select_one(id: int):
    pass


@router.post('/insert', summary='新增角色')
async def insert_one(data=Body(None)):
    pass


@router.delete('/delete/{id}', summary='删除角色')
async def delete_one(id: int):
    pass


@router.put('/update/{id}', summary='修改角色')
async def update_one(id: int):
    pass
