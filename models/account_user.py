"""
账户信息表
@Author:何同学
"""
from sqlalchemy import BigInteger, Column, ForeignKey

from models.base import Base


class Account_User(Base):
    """ 账户信息表 """
    __table_args__ = ({"comment": "账户信息表"})

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='ID')

    account_id = Column(BigInteger, ForeignKey('account.account_id'), comment='账户ID')

    user_id = Column(BigInteger, ForeignKey('user.user_id'), comment='用户ID')
