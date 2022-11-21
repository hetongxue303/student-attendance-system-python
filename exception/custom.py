"""
自定义异常
@Author:何同学
"""


class UserNotFoundException(Exception):
    def __init__(self, message: str = '用户名或密码错误'):
        self.message = message


class UserPasswordException(Exception):
    def __init__(self, message: str = '密码错误'):
        self.message = message


class UnauthorizedException(Exception):
    def __init__(self, message: str = '您还未登录,请先登录!'):
        self.message = message


class JwtVerifyException(Exception):
    def __init__(self, message: str = 'JWT解析失败'):
        self.message = message
