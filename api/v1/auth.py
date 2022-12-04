"""
安全相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Security, Form, Request

from core.config import settings
from core.security import authenticate, generate_token, get_current_user, captcha_check
from schemas import success
from schemas.account import Account
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
        token = generate_token({'id': user.account_id, 'sub': user.username, 'scopes': scopes}, settings.JWT_EXPIRE)
        return Token(access_token=token, expired_time=settings.JWT_EXPIRE, code=200)


@router.get('/captchaImage', response_model=success[typing.Any], summary='获取验证码')
async def get_code(request: Request):
    """
    获取验证码
    :return:
    """
    data = await generate_captcha(request)
    return success(message='获取验证码成功', data=data)


@router.get('/user/me', response_model=Account, summary='获取当前用户')
async def get_current_user(current_user: Account = Security(get_current_user)):
    """
    获取当前用户
    :param current_user:
    :return:
    """
    return current_user
