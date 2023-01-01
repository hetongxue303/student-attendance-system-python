"""
考勤模型
@Author:何同学
"""
from datetime import datetime

from schemas.common import Common
from schemas.course import CourseDto
from schemas.user import UserDtoOut


class AttendanceDto(Common):
    attendance_id: int = None
    user_id: int = None
    user: UserDtoOut = None
    course_id: int = None
    course: CourseDto = None
    release_time: datetime = None
    end_time: datetime = None
    course_count: int = None
    attendance_count: int = None
    is_end: bool = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
