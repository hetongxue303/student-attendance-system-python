"""
账户表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger, Enum

from models.base import Base


class Account(Base):
    """ 账户表 """
    __table_args__ = ({"comment": "账户表"})

    account_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='账户ID')

    username = Column(String(100), nullable=False, comment='用户名')

    password = Column(String(200), nullable=False, comment='用户密码')

    status = Column(Enum('0', '1'), nullable=False, server_default='1', comment='是否启用(1是 0否)')

    del_flag = Column(Enum('0', '1'), nullable=False, server_default='1', comment='是否删除(1是 0否)')
