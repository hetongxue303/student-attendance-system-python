"""
统一返回类
@Author:何同学
"""
import json
import typing
from starlette import status
from starlette.background import BackgroundTask
from starlette.responses import Response
from fastapi.responses import JSONResponse


def success(code: int = status.HTTP_200_OK,
            message: str = '请求成功',
            data: typing.Any = None,
            headers: typing.Optional[typing.Dict[str, str]] = None,
            media_type: typing.Optional[str] = None,
            background: typing.Optional[BackgroundTask] = None) -> Response:
    return JSONResponse(
        status_code=code,
        media_type=media_type,
        background=background,
        headers=headers,
        content={
            'code': code,
            'message': message,
            'data': json.loads(data)
        }
    )


def fail(code: int = status.HTTP_400_BAD_REQUEST,
         message: str = '请求错误',
         data: typing.Any = None,
         headers: typing.Optional[typing.Dict[str, str]] = None,
         media_type: typing.Optional[str] = None,
         background: typing.Optional[BackgroundTask] = None) -> Response:
    return JSONResponse(
        status_code=code,
        media_type=media_type,
        background=background,
        headers=headers,
        content={
            'code': code,
            'message': message,
            'data': json.loads(data)
        }
    )
