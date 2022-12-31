"""
用户相关
@Author:何同学
"""
import typing
from typing import List

from fastapi import APIRouter, Body, Security

from core.security import check_permissions
from crud.college import delete_college_by_id
from crud.user import query_user_by_role, query_user_list_page, delete_user_by_id, delete_user_by_ids, \
    update_user_by_id, insert_user
from schemas.common import Page, BatchDto
from schemas.result import Success
from schemas.user import UserDtoOut, up_password, up_email, UserDto

router = APIRouter()


@router.get('/get/all', summary='查询用户(All)')
async def select_all():
    pass


@router.get('/get/all/{role}', response_model=Success[List[UserDtoOut]], summary='查询用户(All)')
async def select_all(role: int):
    users = query_user_by_role(role=role)
    return Success(data=users, message='查询成功')


@router.get('/get/page', response_model=Success[Page[List[UserDtoOut]]], summary='查询用户(Page)',
            dependencies=[Security(check_permissions)])
async def select_page(currentPage: int, pageSize: int):
    users = query_user_list_page(current_page=currentPage, page_size=pageSize)
    return Success(data=users, message='查询成功')


@router.post('/insert', response_model=Success[typing.Any], summary='新增用户',
             dependencies=[Security(check_permissions)])
async def insert_one(data: UserDto):
    await insert_user(data)
    return Success(message='增加成功')


@router.delete('/delete/{id}', response_model=Success[typing.Any], summary='删除用户',
               dependencies=[Security(check_permissions)])
async def delete_one(id: int):
    delete_user_by_id(id)
    return Success(message='删除成功')


@router.delete('/delete/batch', response_model=Success[typing.Any], summary='批量删除用户',
               dependencies=[Security(check_permissions)])
async def delete_batch(data: BatchDto):
    print(data)
    # delete_user_by_ids(data)
    return Success(message='删除成功')


@router.put('/update', response_model=Success[typing.Any], summary='修改用户',
            dependencies=[Security(check_permissions)])
async def update_one(data: UserDto):
    await update_user_by_id(data)
    return Success(message='修改成功')


@router.put('/update/password', response_model=Success[typing.Any], summary='修改密码')
async def update_password(data: up_password):
    print(data.new_password)
    print(data.old_password)
    print(data.confirm_password)


@router.put('/update/email', response_model=Success[typing.Any], summary='修改邮箱')
async def update_email(data: up_email):
    print(data.email)
    print(data.code)
    print(data.password)


@router.get('/center', response_model=Success[typing.Any], summary='个人中心')
async def get_center_info(username: str):
    delete_college_by_id(1)
    return Success(data=None)
