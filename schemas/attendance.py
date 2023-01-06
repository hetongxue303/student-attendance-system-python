"""
考勤模型
@Author:何同学
"""
from datetime import datetime

from pydantic import BaseModel

from schemas.course import CourseDto
from schemas.user import UserDtoOut


class AttendanceDto(BaseModel):
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
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class updateAttendanceStatusVo(BaseModel):
    user_id: int = None
    attendance_id: int = None
    attendance_type: int = None
    description: str = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
