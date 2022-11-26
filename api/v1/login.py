"""
登录相关
@Author:何同学
"""
import json

from fastapi import APIRouter, Security, Form
from sqlalchemy.orm import Session

from core.config import settings
from core.security import authenticate, generate_token, get_current_user
from database.mysql import get_db
from schemas.account import Account
from schemas.token import Token

router = APIRouter()


@router.post('/login', response_model=Token, summary='登录认证')
async def login(username: str = Form(), password: str = Form()):
    """
    用户登录
    :param username: 用户名
    :param password: 密码
    :return: token
    """
    user = authenticate(username=username, password=password)
    # TODO 查询权限代码
    token = generate_token({'id': user.account_id, 'sub': user.username, 'scopes': []}, settings.JWT_EXPIRE)
    return Token(access_token=token, expired_time=settings.JWT_EXPIRE)


@router.get('/user/me', response_model=Account, summary='获取当前用户')
async def get_current_user(current_user: Account = Security(get_current_user)):
    """
    获取当前用户
    :param current_user:
    :return:
    """
    return current_user
