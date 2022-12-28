"""
选课模型
@Author:何同学
"""
import decimal

from schemas.common import Common
from schemas.course import CourseDto
from schemas.user import UserDtoOut


class ChoiceDto(Common):
    choice_id: int = None
    user_id: int = None
    user: UserDtoOut = None
    course_id: int = None
    course: CourseDto = None
    score: decimal.Decimal = None
    is_quit: bool = None
    is_delete: bool = None
    status: int = None
    description: str = None
