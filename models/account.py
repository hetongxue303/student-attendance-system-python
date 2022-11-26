"""
账户表
@Author:何同学
"""
from sqlalchemy import Column, String, BigInteger, Enum, DateTime, func
from sqlalchemy.orm import relationship

from models.base import Base


class Account(Base):
    """ 账户表 """
    __table_args__ = ({"comment": "账户表"})

    account_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='账户ID')

    username = Column(String(100), nullable=False, comment='用户名')

    password = Column(String(200), nullable=False, comment='用户密码')

    status = Column(Enum('0', '1'), nullable=False, server_default='1', comment='是否启用(1是 0否)')

    del_flag = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否删除(1是 0否)')

    last_login_ip = Column(String(100), server_default='0.0.0.0', comment='最后登录IP')

    last_login_time = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(),
                             comment='最后登录时间')

    # 多对多
    role = relationship('Role', secondary='account_role', back_populates='account')

    user = relationship('User', secondary='account_user', back_populates='account')
