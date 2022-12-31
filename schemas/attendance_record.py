"""
考勤模型
@Author:何同学
"""
from schemas.attendance import AttendanceDto
from schemas.common import Common
from schemas.user import UserDtoOut


class AttendanceRecordDto(Common):
    attendance_record_id: int = None
    user_id: int = None
    user: UserDtoOut = None
    attendance_id: int = None
    attendance: AttendanceDto = None
    attendance_type: int = None
    description: str = None
