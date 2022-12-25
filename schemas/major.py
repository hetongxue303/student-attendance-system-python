"""
专业模型
@Author:何同学
"""
from schemas.common import Common


class MajorDto(Common):
    major_id: int = None
    major_name: str = None
    is_delete: bool = None
    description: str = None
