"""
登录相关
@Author:何同学
"""
from fastapi import APIRouter, HTTPException, Form
from starlette import status
from core.security import authenticate
from schemas import Success

router = APIRouter()


@router.post('/login', summary='登录认证')
async def login(username: str = Form(None), password: str = Form(None)):
    """
    用户登录
    :param username: 用户名
    :param password: 用户密码
    :return: token信息
    """
    result = authenticate(username=username, password=password)
    if not result:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='用户名或密码错误')
    return Success(data=result)
