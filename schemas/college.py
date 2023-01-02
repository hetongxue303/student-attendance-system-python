"""
学院模型
@Author:何同学
"""
from datetime import datetime

from pydantic import BaseModel


class CollegeDto(BaseModel):
    college_id: int = None
    college_name: str = None
    is_delete: bool = None
    description: str = None
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
