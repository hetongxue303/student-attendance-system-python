"""
统一返回实体
@Author:何同学
"""
import json
import typing

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette import status


def success(
        *,
        code: int = status.HTTP_200_OK,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        message: str = 'success',
        data: typing.Any | None = None
):
    return JSONResponse(status_code=code, headers=headers,
                        content={'code': code, 'message': message, 'data': jsonable_encoder(data)})


def error(*,
          code: int = status.HTTP_400_BAD_REQUEST,
          headers: typing.Optional[typing.Dict[str, str]] = None,
          message: str = 'error',
          data: typing.Any | None = None
          ):
    return JSONResponse(status_code=code, headers=headers,
                        content={'code': code, 'message': message, 'data': jsonable_encoder(data)})
