"""
课程模型
@Author:何同学
"""
from datetime import datetime

from pydantic import BaseModel

from schemas.user import UserDtoOut


class CourseDto(BaseModel):
    course_id: int = None
    teacher_id: int = None
    teacher: UserDtoOut = None
    course_name: str = None
    count: int = None
    choice: int = None
    class_time: int = None
    is_delete: bool = None
    description: str = None
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class CourseDtoExt(BaseModel):
    course: CourseDto = None
    is_choice: bool = False

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
