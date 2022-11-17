"""
统一返回类
@Author:何同学
"""
import typing
from starlette import status
from pydantic import BaseModel, Field


class success(BaseModel):
    code: int = Field(status.HTTP_200_OK, description='状态码')
    message: str = Field('请求成功', description='响应消息')
    data: typing.Any = Field(None, description='响应数据')


class fail(success):
    code: int = Field(status.HTTP_400_BAD_REQUEST, description='状态码')
    message: str = Field('请求失败', description='响应消息')


class error(success):
    code: int = Field(status.HTTP_500_INTERNAL_SERVER_ERROR, description='状态码')
    message: str = Field('服务器错误', description='响应消息')


class unauthorized(success):
    code: int = Field(status.HTTP_401_UNAUTHORIZED, description='状态码')
    message: str = Field('您还未登录，请先登录！', description='响应消息')
