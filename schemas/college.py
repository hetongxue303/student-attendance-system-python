"""
学院模型
@Author:何同学
"""
from schemas.common import Common


class CollegeDto(Common):
    college_id: int = None
    college_name: str = None
    is_delete: bool = None
    description: str = None