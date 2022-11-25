"""
账户实体
@Author:何同学
"""
from pydantic import BaseModel


class Account(BaseModel):
    account_id: int = None
    username: str = None
    status: bool = None
    del_flag: bool = None

    class Config:
        orm_mode = True


class AccountInDB(Account):
    password: str = None
