"""
选课模型
@Author:何同学
"""
import decimal
from datetime import datetime

from pydantic import BaseModel

from schemas.course import CourseDto
from schemas.user import UserDtoOut


class ChoiceDto(BaseModel):
    choice_id: int = None
    user_id: int = None
    user: UserDtoOut = None
    course_id: int = None
    course: CourseDto = None
    score: float | decimal.Decimal = None
    is_quit: bool = None
    is_delete: bool = None
    status: int = None
    description: str = None
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UpdateBatchChoiceDto(BaseModel):
    operate: bool = None
    choice_ids: list[int] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
