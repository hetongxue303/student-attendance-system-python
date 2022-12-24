from datetime import datetime

from pydantic import BaseModel


class Common(BaseModel):
    create_time: datetime = None
    update_time: datetime = None

    class Config:
        orm_mode = True
