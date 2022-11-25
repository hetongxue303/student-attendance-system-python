"""
登录相关
@Author:何同学
"""
import json

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from core.config import settings
from core.security import authenticate, generate_token, get_current_user
from schemas import success
from schemas.account import Account
from schemas.token import Token

router = APIRouter()


@router.post('/login', response_model=Token, summary='登录认证')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    """
    用户登录
    :param data:
    :return:
    """
    user = authenticate(username=data.username, password=data.password)
    print(data.scopes)
    token = generate_token({'id': user.account_id, 'sub': user.username, 'scopes': data.scopes}, settings.JWT_EXPIRE)
    return success(data=Token(token=token, expired_time=settings.JWT_EXPIRE))


@router.get('/user/me', summary='获取当前用户')
async def get_current_user(current_user: Account = Depends(get_current_user)):
    return current_user
