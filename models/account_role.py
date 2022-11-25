"""
账户角色表
@Author:何同学
"""
from sqlalchemy import BigInteger, Column, ForeignKey

from models.base import Base


class Account_Role(Base):
    """ 账户角色表 """
    __table_args__ = ({"comment": "账户角色表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='ID')

    account_id = Column(BigInteger, ForeignKey('account.account_id'), comment='账户ID')

    role_id = Column(BigInteger, ForeignKey('role.role_id'), comment='角色ID')
