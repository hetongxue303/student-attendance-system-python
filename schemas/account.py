"""
账户模型
@Author:何同学
"""
from pydantic import BaseModel


class Account(BaseModel):
    account_id: int = None
    username: str = None
    password: str = None
    status: str = None
    del_flag: str = None
