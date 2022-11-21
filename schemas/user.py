"""
用户实体
@Author:何同学
"""
from pydantic import BaseModel


class User(BaseModel):
    user_id: int = None
    college_id: int = None
    major_id: int = None
    role_id: int = None
    user_no: str = None
    nick_name: str = None
    real_name: str = None
    gender: str = None
    email: str = None
    phone: str = None
    avatar: str = None
    status: str = None
    del_flag: str = None
    remark: str = None
    last_login_ip: str = None
    last_login_time: str = None
