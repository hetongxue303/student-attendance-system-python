"""
统一返回模型
@Author:何同学
"""
import typing
from starlette import status
from pydantic import BaseModel, Field


class Success(BaseModel):
    code: int = Field(status.HTTP_200_OK, description='状态码')
    message: str = Field('请求成功', description='响应消息')
    data: typing.Any = Field(None, description='响应数据')


class Error(Success):
    code: int = Field(status.HTTP_400_BAD_REQUEST, description='状态码')
    message: str = Field('服务器错误', description='响应消息')
