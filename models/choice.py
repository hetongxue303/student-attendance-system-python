"""
选课表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, String, Enum, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from models.base import Base


class Choice(Base):
    """ 学院表 """
    __table_args__ = ({"comment": "选课表"})

    choice_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='选课ID')

    user_id = Column(BigInteger, ForeignKey('user.user_id'), comment='用户ID')
    user = relationship('User', backref='choice')

    course_id = Column(BigInteger, ForeignKey('course.course_id'), comment='课程ID')
    course = relationship('Course', backref='choice2')

    score = Column(DECIMAL(3, 2), server_default='0', comment='课程成绩')

    is_quit = Column(Enum('0', '1'), server_default='0', comment='是否退选(1是 0否)')

    is_delete = Column(Enum('0', '1'), server_default='0', comment='是否删除(1是 0否)')

    status = Column(Enum('0', '1', '2'), server_default='0', comment='状态(0未处理 1同意 2拒绝)')

    description = Column(String(500), server_default='空', comment='学院描述')
