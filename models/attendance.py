"""
考勤表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship

from models.base import Base


class Attendance(Base):
    """ 考勤表 """
    __table_args__ = ({"comment": "考勤表"})

    attendance_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='考勤ID')

    user_id = Column(BigInteger, ForeignKey('user.user_id'), nullable=False, comment='发布人ID')
    user = relationship('User', backref='attendance')

    course_id = Column(BigInteger, ForeignKey('course.course_id'), nullable=False, comment='课程ID')
    course = relationship('Course', backref='attendance')

    release_time = Column(DateTime(timezone=True), nullable=False, comment='发布时间')

    end_time = Column(DateTime(timezone=True), nullable=False, comment='结束时间')

    course_count = Column(Integer, nullable=False, server_default='0', comment='课程人数')

    attendance_count = Column(Integer, nullable=False, server_default='0', comment='签到人数')
