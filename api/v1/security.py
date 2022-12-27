"""
安全相关
@Author:何同学
"""
import typing
from typing import List
from datetime import timedelta

import jsonpickle
from aioredis import Redis
from fastapi import APIRouter, Form

from core import Const
from core.config import settings
from core.security import authenticate, generate_token, captcha_check, logout_redis, set_current_user_info, \
    generate_scope
from database.redis import get_redis
from schemas.menu import MenuDto
from schemas.result import Success
from schemas.role import RoleDto
from schemas.token import Token
from schemas.user import LoginDto
from utils.captcha import generate_captcha

router = APIRouter()


@router.post('/login', response_model=Token, summary='登录认证')
async def login(username: str = Form(), password: str = Form(), code: str = Form()):
    """
    用户登录
    :param username: 用户名
    :param password: 密码
    :param code: 验证码
    :return: token
    """
    redis: Redis = await get_redis()
    if await captcha_check(code=code):
        user = await authenticate(username=username, password=password)
        await set_current_user_info(user.user_id)
        scopes: List[str] = await generate_scope()
        roles: List[RoleDto] = jsonpickle.decode(await redis.get('current-role-data'))
        menus: List[MenuDto] = jsonpickle.decode(await redis.get('current-menu-data'))
        token: str = await generate_token({'id': user.user_id, 'sub': user.username, 'scopes': scopes})
        await redis.setex(name=Const.TOKEN, value=token, time=timedelta(milliseconds=settings.JWT_EXPIRE))
        return Token(code=200,
                     message='登陆成功',
                     access_token=token,
                     expired_time=settings.JWT_EXPIRE,
                     user=LoginDto(avatar=user.avatar, is_admin=user.is_admin,
                                   menus=menus,
                                   roles=roles,
                                   permissions=scopes))


@router.get('/logout', response_model=Success, summary='用户注销')
async def logout():
    await logout_redis()
    return Success(message='注销成功')


@router.get('/captchaImage', response_model=Success[typing.Any], summary='获取验证码')
async def get_code():
    """
    获取验证码
    """
    data = await generate_captcha()
    return Success(message='获取验证码成功', data=data)
