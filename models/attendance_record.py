"""
考勤记录表
@Author:何同学
"""
from sqlalchemy import Column, BigInteger, ForeignKey, String, Enum
from sqlalchemy.orm import relationship

from models.base import Base


class Attendance_Record(Base):
    """ 考勤记录表 """
    __table_args__ = ({"comment": "考勤记录表"})

    attendance_record_id = Column(BigInteger, primary_key=True, autoincrement=True, comment='考勤记录ID')

    user_id = Column(BigInteger, ForeignKey('user.user_id'), nullable=False, comment='学生ID')
    user = relationship('User', backref='attendance_record')

    attendance_id = Column(BigInteger, ForeignKey('attendance.attendance_id'), nullable=False, comment='签到ID')
    attendance = relationship('Attendance', backref='attendance_record')

    attendance_type = Column(Enum('0', '1', '2', '3'), server_default='1', nullable=False,
                             comment='菜单类型(0:未签到 1:已签到 2:请假 3:缺勤)')

    description = Column(String(500), server_default='已签到', comment='签到说明')
