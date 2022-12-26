"""
课程表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class Course(Base):
    """ 课程表 """
    __table_args__ = ({"comment": "课程表"})

    course_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='课程ID')

    teacher_id = Column(BigInteger, ForeignKey('user.user_id'), comment='发布课程教师ID')
    teacher = relationship('User', backref='course')

    course_name = Column(String(100), nullable=False, comment='课程名称')

    count = Column(Integer, nullable=False, server_default='0', comment='课程总人数')

    choice = Column(Integer, nullable=False, server_default='0', comment='课程已选人数')

    time = Column(Integer, nullable=False, server_default='0', comment='课时')

    is_delete = Column(Enum('0', '1'), nullable=False, server_default='0', comment='是否删除(1是 0否)')

    description = Column(String(500), server_default='空', comment='学院描述')
