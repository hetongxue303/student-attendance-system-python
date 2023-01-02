"""
考勤模型
@Author:何同学
"""
from datetime import datetime

from pydantic import BaseModel

from schemas.attendance import AttendanceDto
from schemas.user import UserDtoOut


class AttendanceRecordDto(BaseModel):
    attendance_record_id: int = None
    user_id: int = None
    user: UserDtoOut = None
    attendance_id: int = None
    attendance: AttendanceDto = None
    attendance_type: int = None
    description: str = None
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class StudentAttendanceDto(BaseModel):
    attendance: AttendanceDto = None
    attendance_record: AttendanceRecordDto = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
