"""
角色表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum
from sqlalchemy.orm import relationship

from models.base import Base


class Role(Base):
    """ 角色表 """
    __table_args__ = ({"comment": "角色表"})

    role_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='角色ID')

    role_name = Column(String(50), nullable=False, comment='角色名称')

    role_key = Column(String(100), nullable=False, comment='角色key值')

    status = Column(Enum('0', '1'), nullable=False, server_default='1', comment='是否启用(1是 0否)')

    is_enable = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否启用(1是 0否)')

    is_delete = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否删除(1是 0否)')

    description = Column(String(500), server_default='空', comment='角色描述')
