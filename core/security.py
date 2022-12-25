"""
安全性
@Author:何同学
"""
from datetime import timedelta, datetime

from aioredis import Redis
from fastapi import Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from core import Const
from core.config import settings
from database.redis import get_redis
from database.mysql import get_db
from exception.custom import *
from models import User

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oAuth2 = OAuth2PasswordBearer('/api/v1/login')


def verify_password(plain_password: str, hashed_password: str):
    """
    密码校验
    :param plain_password: 原密码
    :param hashed_password: 加密后的密码
    :return: 对比结果(Bool)
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    密码加密
    :param password: 原密码
    :return: 加密后的密码
    """
    return pwd_context.hash(password)


def get_user(username: str, db: Session = next(get_db())):
    """
    查询用户
    :param username: 用户名
    :param db: 数据库
    :return: 账户信息
    """
    return db.query(User).filter(User.username == username).first()


def authenticate(username: str, password: str):
    """
    登录认证
    :param username: 用户名
    :param password: 密码
    :return: 账户信息
    """
    user = get_user(username)
    if not user:
        raise UserNotFoundException()
    if not verify_password(password, user.password):
        raise UserPasswordException()
    if not bool(int(user.is_enable)):
        raise SecurityScopeException(code=403, message='当前用户未激活')
    return user


def generate_token(data: dict, expires_time: int | None = None):
    """
    生成Token
    :param data:
    :param expires_time:
    :return: token
    """
    if not expires_time:
        expire = datetime.now() + timedelta(milliseconds=15 * 60 * 1000)
    else:
        expire = datetime.now() + timedelta(milliseconds=expires_time)
    data.update({'exp': expire})
    return jwt.encode(claims=data,
                      key=settings.JWT_SECRET_KEY,
                      algorithm=settings.JWT_ALGORITHM)


# async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oAuth2)):
#     """
#     获取当前用户
#     :param security_scopes:
#     :param token:
#     :return: 账户信息
#     """
#     try:
#         payload = jwt.decode(token=token, key=settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
#         id = payload.get('id', None)
#         username = payload.get('sub', None)
#         scopes = payload.get('scopes', None)
#         if not payload or id is None or username is None or scopes is None:
#             raise JwtVerifyException(message='无效凭证')
#         token_data = TokenData(username=username, scopes=scopes)
#         user = get_user(token_data.username)
#         for scope in security_scopes.scopes:
#             if scope not in token_data.scopes:
#                 raise SecurityScopeException(code=403, message='没有访问权限', headers={"WWW-Authenticate": 'Bearer '})
#         return user
#     except ExpiredSignatureError:
#         raise JwtVerifyException('凭证过期')
#     except JWTError:
#         raise JwtVerifyException('凭证解析失败')


async def captcha_check(request: Request, code: str):
    """
    校验验证码
    :param request:
    :param code: 用户输入的验证码
    :return:
    """
    redis: Redis = await get_redis(request)
    save_code: str = await redis.get(name=Const.CAPTCHA)
    if not save_code:
        raise CaptchaException(message='验证码过期')
    if save_code.lower() != code.lower():
        await redis.delete(Const.CAPTCHA)
        raise CaptchaException(message='验证码错误')
    await redis.delete(Const.CAPTCHA)
    return True
