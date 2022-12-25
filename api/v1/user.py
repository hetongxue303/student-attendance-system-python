"""
用户相关
@Author:何同学
"""
import typing
from typing import List

from fastapi import APIRouter, Body

from crud.college import delete_college_by_id
from crud.user import query_user_by_role
from schemas.result import Success
from schemas.user import UserDtoOut

router = APIRouter()


@router.get('/getAll', summary='查询用户(All)')
async def select_all():
    pass


@router.get('/getAll/{role}', response_model=Success[List[UserDtoOut]], summary='查询用户(All)')
async def select_all(role: int):
    users = query_user_by_role(role=role)
    return Success(data=users, message='查询成功')


@router.get('/getPage', summary='查询用户(Page)')
async def select_page(data=Body(None)):
    pass


@router.get('/getOne/{id}', summary='查询用户(ById)')
async def select_one(id: int):
    pass


@router.post('/insert', summary='新增用户')
async def insert_one(data=Body(None)):
    pass


@router.delete('/delete/{id}', summary='删除用户')
async def delete_one(id: int):
    pass


@router.put('/update/{id}', summary='修改用户')
async def update_one(id: int):
    pass


@router.get('/center', response_model=Success[typing.Any], summary='个人中心')
async def get_center_info(username: str):
    delete_college_by_id(1)
    return Success(data=None)
