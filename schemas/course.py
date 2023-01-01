"""
课程模型
@Author:何同学
"""

from schemas.common import Common
from schemas.user import UserDtoOut


class CourseDto(Common):
    course_id: int = None
    teacher_id: int = None
    teacher: UserDtoOut = None
    course_name: str = None
    count: int = None
    choice: int = None
    class_time: int = None
    is_delete: bool = None
    description: str = None
