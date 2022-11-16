"""
自定义异常
@Author:何同学
"""


# ip错误异常
class IpErrorException(Exception):
    def __init__(self, message: str = 'IP错误'):
        self.message = message


# redis存储错误
class RedisSaveException(Exception):
    def __init__(self, message: str = 'redis缓存失败'):
        self.message = message


# id不存在
class IdNotFoundException(Exception):
    def __init__(self, message: str = "查询id不存在"):
        self.message = message


# 用户不存在
class UserNotFoundException(Exception):
    def __init__(self, message: str = "用户不存在"):
        self.message = message


# 访问令牌失败
class AccessTokenFailException(Exception):
    def __init__(self, message: str = "访问令牌失败"):
        self.message = message


# 用户名或密码错误
class UserInfoException(Exception):
    def __init__(self, message: str = "用户名或密码错误"):
        self.message = message


# 权限不足,拒绝访问
class PermissionNotEnoughException(Exception):
    def __init__(self, message: str = "权限不足,拒绝访问"):
        self.message = message
