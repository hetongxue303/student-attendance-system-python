"""
登录相关
@Author:何同学
"""
from fastapi import APIRouter

router = APIRouter()


@router.post('/login', summary='登录认证')
async def login():
    pass
