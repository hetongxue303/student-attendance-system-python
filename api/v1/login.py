"""
登录相关
@Author:何同学
"""
import json

from fastapi import APIRouter, Form
from core.security import authenticate
from exception.custom import UnauthorizedException
from schemas import success
from schemas.token import Token

router = APIRouter()


@router.post('/login', response_model=Token, summary='登录认证')
async def login(username: str = Form(None), password: str = Form(None)):
    """
    用户登录
    :param username: 用户名
    :param password: 用户密码
    :return: token信息
    """
    return success(data=authenticate(username=username, password=password))
