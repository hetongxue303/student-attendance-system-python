"""
菜单表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum, Integer
from sqlalchemy.orm import relationship

from models.base import Base


class Menu(Base):
    """ 菜单表 """
    __table_args__ = ({"comment": "菜单表"})

    menu_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='菜单ID')

    menu_name = Column(String(50), comment='菜单名称')

    menu_title = Column(String(50), nullable=False, comment='菜单标题')

    menu_type = Column(Enum('1', '2', '3'), server_default='1', comment='菜单类型(1:目录 2:菜单 3:按钮)')

    parent_id = Column(BigInteger, nullable=False, server_default='0', comment='父菜单ID')

    path = Column(String(200), comment='路由地址')

    component = Column(String(255), comment='组件地址')

    sort = Column(Integer, nullable=False, comment='菜单排序')

    redirect = Column(String(200), comment='重定向地址')

    icon = Column(String(100), comment='图标名称')

    per_key = Column(String(200), comment='权限标识')

    is_show = Column(Enum('0', '1'), server_default='1', comment='是否显示(1是 0否)')

    is_sub = Column(Enum('0', '1'), server_default='0', comment='是否有子菜单(1是 0否)')

    is_cache = Column(Enum('0', '1'), server_default='0', comment='是否缓存(1是 0否)')

    is_delete = Column(Enum('0', '1'), server_default='0', comment='是否删除(1是 0否)')

    description = Column(String(500), server_default='空', comment='菜单描述')
