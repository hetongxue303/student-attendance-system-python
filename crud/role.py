"""
角色业务
@Author:何同学
"""
from typing import List

from sqlalchemy.orm import Session

from database.mysql import get_db
from models import Role
from schemas.common import Page
from schemas.role import RoleDto

db: Session = next(get_db())


def query_role_list_all() -> Page[List[RoleDto]]:
    """
    查询角色列表
    :return: 角色列表
    """
    return Page(total=db.query(Role).filter(Role.is_delete == '0').count(),
                record=db.query(Role).filter(Role.is_delete == '0').all())
