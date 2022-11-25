"""
统一返回
@Author:何同学
"""
import typing

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic.generics import GenericModel
from starlette import status

T = typing.TypeVar("T")


class result(GenericModel, typing.Generic[T]):
    code: typing.Optional[int] | None = None
    message: str | None = None
    data: typing.Optional[T] | None = None

    def success(self, code: typing.Optional[int] = status.HTTP_200_OK,
                message: str = '请求成功',
                data: typing.Optional[T] | None = None):
        self.code = code
        self.message = message
        self.data = data

    def error(self, code: typing.Optional[int] = status.HTTP_400_BAD_REQUEST,
              message: str = '请求错误',
              data: typing.Optional[T] | None = None):
        self.code = code
        self.message = message
        self.data = data


def success(
        *,
        code: int = status.HTTP_200_OK,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        message: str = '请求成功',
        data: typing.Any | None = None
):
    return JSONResponse(status_code=code, headers=headers,
                        content={'code': code, 'message': message, 'data': jsonable_encoder(data)})


def error(*,
          code: int = status.HTTP_400_BAD_REQUEST,
          headers: typing.Optional[typing.Dict[str, str]] = None,
          message: str = '请求错误',
          data: typing.Any | None = None
          ):
    return JSONResponse(status_code=code, headers=headers,
                        content={'code': code, 'message': message, 'data': jsonable_encoder(data)})
