"""
用户相关
@Author:何同学
"""
import typing

import jsonpickle
from aioredis import Redis
from fastapi import APIRouter, Security
from sqlalchemy.orm import Session

from core.security import check_permissions, verify_password, get_password_hash
from crud.user import query_user_by_role, query_user_list_page, delete_user_by_id, update_user_by_id, insert_user
from database.mysql import get_db
from database.redis import get_redis
from exception.custom import UpdateException
from models import User
from schemas.common import Page, BatchDto
from schemas.result import Success
from schemas.user import UserDtoOut, up_password, up_email, UserDto, LoginDto

router = APIRouter()
db: Session = next(get_db())


@router.get('/get/all', summary='查询用户(All)', dependencies=[Security(check_permissions)])
async def select_all():
    pass


@router.get('/get/all/{role}', response_model=Success[list[UserDtoOut]], summary='查询用户(All)',
            dependencies=[Security(check_permissions)])
async def select_all(role: int):
    users = query_user_by_role(role=role)
    return Success(data=users, message='查询成功')


@router.get('/get/page', response_model=Success[Page[list[UserDtoOut]]], summary='查询用户(Page)',
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


@router.put('/update/password', response_model=Success[typing.Any], summary='修改密码',
            dependencies=[Security(check_permissions)])
async def update_password(data: up_password):
    redis: Redis = await get_redis()
    login_user: LoginDto = jsonpickle.decode(await redis.get('current-user'))
    user: User = db.query(User).filter(User.username == login_user.username).first()
    if not verify_password(data.old_password, user.password):
        raise UpdateException(message='原密码不正确')
    user.password = get_password_hash(data.new_password)
    db.commit()
    return Success(message='修改成功')


@router.get('/center', response_model=Success[typing.Any], summary='个人中心',
            dependencies=[Security(check_permissions)])
async def get_center_info(username: str):
    user: User = db.query(User).filter(User.username == username).first()
    return Success(data=user)
