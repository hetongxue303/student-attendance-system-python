"""
专业模型
@Author:何同学
"""
from datetime import datetime

from pydantic import BaseModel


class MajorDto(BaseModel):
    major_id: int = None
    major_name: str = None
    is_delete: bool = None
    description: str = None
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
