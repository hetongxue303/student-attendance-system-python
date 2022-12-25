"""
用户业务
@Author:何同学
"""
from typing import List

from sqlalchemy.orm import Session

from database.mysql import get_db
from models import User

db: Session = next(get_db())


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
