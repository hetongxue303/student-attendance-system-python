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

    college_id = Column(BigInteger, ForeignKey('college.college_id'), comment='学院ID')
    college = relationship("College", back_populates='user')

    major_id = Column(BigInteger, ForeignKey('major.major_id'), comment='专业ID')
    major = relationship("Major", back_populates='user')

    role_id = Column(BigInteger, ForeignKey('role.role_id'), comment='角色ID')
    role = relationship("Role", back_populates='user')

    user_no = Column(BigInteger, nullable=False, comment='学号/工号')

    nick_name = Column(String(30), nullable=False, comment='用户昵称')

    real_name = Column(String(30), comment='真实姓名')

    gender = Column(Enum('1', '2', '3'), server_default='3', comment='性别(1:男 2:女 3:保密)')

    email = Column(String(50), comment='邮箱')

    phone = Column(String(11), comment='电话')

    avatar = Column(String(255), comment='头像地址')

    status = Column(Enum('0', '1'), nullable=False, server_default='1', comment='是否启用(1是 0否)')

    del_flag = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否删除(1是 0否)')

    remark = Column(String(500), comment='备注')

    # 多对多
    account = relationship('Account', secondary='account_user', back_populates='user')
