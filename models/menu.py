"""
菜单表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum, Integer

from models.base import Base


class Menu(Base):
    """ 菜单表 """
    __table_args__ = ({"comment": "菜单表"})

    menu_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='菜单ID')

    menu_name = Column(String(50), comment='菜单名称')

    menu_title = Column(String(50), comment='菜单标题')

    menu_type = Column(Enum('0', '1', '2'), comment='菜单类型(0:目录 1:菜单 2:按钮)')

    parent_id = Column(BigInteger, comment='父菜单ID')

    path = Column(String(200), comment='路由地址')

    component = Column(String(255), comment='组件地址')

    sort = Column(Integer, comment='排序')

    icon = Column(String(100), comment='图标')
    
    visible = Column(Enum('1', '0'), server_default='1', comment='是否显示(1:是 0:否)')

    is_frame = Column(Enum('1', '0'), server_default='0', comment='是否外链(1:是 0:否)')

    is_cache = Column(Enum('1', '0'), server_default='0', comment='是否外链(1:是 0:否)')

    per_key = Column(String(100), comment='权限标识')

    del_flag = Column(Enum('0', '1'), nullable=False, server_default='1', comment='是否删除(1是 0否)')

    remark = Column(String(500), comment='备注')
