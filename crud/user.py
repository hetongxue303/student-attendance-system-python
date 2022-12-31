"""
用户业务
@Author:何同学
"""
from typing import List

import jsonpickle
from aioredis import Redis
from sqlalchemy.orm import Session

from core.security import get_password_hash, get_user
from database.mysql import get_db
from database.redis import get_redis
from models import User, User_Role
from schemas.common import Page
from schemas.user import UserDtoOut, UserDto

db: Session = next(get_db())


async def insert_user(data: UserDto):
    """
    新增用户
    :param data: 用户信息
    """
    redis: Redis = await get_redis()
    role_keys: List[str] = jsonpickle.decode(await redis.get('current-role-keys'))
    if 'admin' in role_keys:
        db.add(User(username=data.username, password=get_password_hash(data.password),
                    is_admin='1' if data.role == 1 else '0', is_enable='1' if data.is_enable else '0',
                    gender=data.gender.__str__(), nick_name=data.nick_name, email=data.email, phone=data.phone,
                    real_name=data.real_name, role=data.role.__str__(), description=data.description))
        db.commit()
        user: User = db.query(User).filter(User.username == data.username).first()
        db.add(User_Role(user_id=user.user_id, role_id=data.role))
        db.commit()


def query_user_list_page(current_page: int, page_size: int) -> Page[List[UserDtoOut]]:
    """
    分页查询用户列表
    :param current_page: 当前页
    :param page_size: 页面大小
    :return: 选课列表
    """
    return Page(total=db.query(User).filter(User.is_delete == '0').count(),
                record=db.query(User).filter(User.is_delete == '0').limit(page_size).offset(
                    (current_page - 1) * page_size).all())


def query_user_by_username(username: str):
    """
    根据用户名查询用户信息
    :param username: 用户名
    :return:用户信息
    """
    return db.query(User).filter(User.username == username).first()


def query_user_by_role(role: int) -> List[User]:
    """
    根据用户角色查询用户信息
    :param role: 用户角色
    :return: 用户信息
    """
    return db.query(User).filter(User.is_delete == '0', User.role == role).all()


def delete_user_by_id(user_id: int):
    """
    删除用户
    :param user_id: 用户ID
    """
    item: User = db.query(User).filter(User.user_id == user_id).first()
    item.is_delete = '1'
    db.query(User_Role).filter(User_Role.user_id == user_id).delete()
    db.commit()


def delete_user_by_ids(user_ids: List[int]):
    """
    批量删除用户
    :param user_ids: 用户ID
    """
    for id in user_ids:
        item: User = db.query(User).filter(User.user_id == id).first()
        item.is_delete = '1'
        db.query(User_Role).filter(User_Role.user_id == id).delete()
        db.commit()


async def update_user_by_id(data: UserDto):
    """
    更新用户
    :param data: 用户信息
    """
    item: User = db.query(User).filter(User.user_id == data.user_id).first()
    item.is_delete = '1' if data.is_delete else '0'
    item.is_enable = '1' if data.is_enable else '0'
    item.is_admin = '1' if data.is_admin else '0'
    item.password = item.password if data.password is None else get_password_hash(data.password)
    item.role = data.role.__str__()
    item.real_name = data.real_name
    item.username = data.username
    item.description = data.description
    item.avatar = data.avatar
    item.email = data.email
    item.gender = data.gender.__str__()
    item.phone = data.phone
    db.commit()
