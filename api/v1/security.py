"""
安全相关
@Author:何同学
"""
import typing
from datetime import timedelta

from aioredis import Redis
from fastapi import APIRouter, Form, Request

from core import Const
from core.config import settings
from core.security import authenticate, generate_token, captcha_check
from database.redis import get_redis
from schemas.result import Success
from schemas.token import Token
from utils.captcha import generate_captcha

router = APIRouter()


@router.post('/login', response_model=Token, summary='登录认证')
async def login(request: Request, username: str = Form(), password: str = Form(), code: str = Form()):
    """
    用户登录
    :param request: 请求
    :param username: 用户名
    :param password: 密码
    :param code: 验证码
    :return: token
    """
    if await captcha_check(request, code=code):
        user = authenticate(username=username, password=password)
        # TODO 查询权限代码
        scopes = []
        token = generate_token({'id': user.user_id, 'sub': user.username, 'scopes': scopes})
        redis: Redis = await get_redis(request)
        await redis.setex(name=Const.TOKEN, value=token, time=timedelta(milliseconds=settings.JWT_EXPIRE))
        return Token(code=200, message='登陆成功', access_token=token, expired_time=settings.JWT_EXPIRE,
                     user=user)


@router.get('/logout', response_model=Success, summary='用户注销')
async def logout(request: Request):
    redis: Redis = await get_redis(request)
    await redis.delete('token')
    return Success(message='注销成功')


@router.get('/captchaImage', response_model=Success[typing.Any], summary='获取验证码')
async def get_code(request: Request):
    """
    获取验证码
    :return:
    """
    data = await generate_captcha(request)
    return Success(message='获取验证码成功', data=data)

# @router.get('/user/me', response_model=User, summary='获取当前用户')
# async def get_current_user(current_user: User = Security(get_current_user)):
#     """
#     获取当前用户
#     :param current_user:
#     :return:
#     """
#     return current_user
