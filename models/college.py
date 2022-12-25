"""
学院表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum

from models.base import Base


class College(Base):
    """ 学院表 """
    __table_args__ = ({"comment": "学院表"})

    college_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='学院ID')

    college_name = Column(String(100), nullable=False, comment='学院名称')

    is_delete = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否删除(1是 0否)')

    description = Column(String(500), server_default='空', comment='学院描述')
