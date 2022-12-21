"""
用户表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, backref

from models.base import Base


class User(Base):
    """ 用户表 """
    __table_args__ = ({"comment": "用户表"})

    user_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='用户ID')

    username = Column(String(100), nullable=False, comment='账号')

    password = Column(String(100), nullable=False, comment='密码')

    real_name = Column(String(30), comment='真实姓名')

    avatar = Column(String(255), comment='头像地址')

    gender = Column(Enum('1', '2'), server_default='1', comment='性别(1:男 2:女)')

    email = Column(String(100), comment='邮箱')

    phone = Column(String(11), comment='电话')

    role = Column(Enum('1', '2', '3'), nullable=False, comment='用户角色')

    is_admin = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否管理员(1是 0否)')

    is_enable = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否启用(1是 0否)')

    is_delete = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否删除(1是 0否)')

    description = Column(String(500), server_default='空', comment='用户描述')
