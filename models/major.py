"""
专业表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum
from sqlalchemy.orm import relationship

from models.base import Base


class Major(Base):
    """ 专业表 """
    __table_args__ = ({"comment": "专业表"})

    major_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='专业ID')

    major_name = Column(String(100), nullable=False, comment='专业名称')

    is_delete = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否删除(1是 0否)')

    description = Column(String(255), server_default='空', comment='专业描述')
