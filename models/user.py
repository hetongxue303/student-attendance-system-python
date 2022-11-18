"""
用户表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum, DateTime, func, ForeignKey
from models.base import Base


class User(Base):
    """ 用户表 """
    __table_args__ = ({"comment": "用户表"})

    user_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='用户ID')

    college_id = Column(BigInteger, ForeignKey('college.college_id'), comment='学院ID')

    major_id = Column(BigInteger, ForeignKey('major.major_id'), comment='专业ID')

    role_id = Column(BigInteger, ForeignKey('role.role_id'), comment='角色ID')

    user_no = Column(BigInteger, comment='学号/工号')

    nick_name = Column(String(30), comment='用户昵称')

    real_name = Column(String(30), comment='真实姓名')

    gender = Column(Enum('1', '2', '3'), comment='性别(1:男 2:女 3:保密)')

    email = Column(String(50), comment='邮箱')

    phone = Column(String(11), comment='电话')

    avatar = Column(String(255), comment='头像地址')

    status = Column(Enum('0', '1'), nullable=False, server_default='1', comment='是否启用(1是 0否)')

    del_flag = Column(Enum('0', '1'), nullable=False, server_default='1', comment='是否删除(1是 0否)')

    remark = Column(String(500), comment='备注')

    last_login_ip = Column(String(100), comment='最后登录IP')

    last_login_time = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(),
                             comment='最后登录时间')
