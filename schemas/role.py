"""
角色模型
@Author:何同学
"""
from schemas.common import Common


class RoleDto(Common):
    role_id: int = None
    role_name: str = None
    role_key: str = None
    is_enable: bool = None
    is_delete: bool = None
    description: str = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
