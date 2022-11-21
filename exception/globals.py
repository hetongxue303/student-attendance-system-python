"""
全局异常捕获
@Author:何同学
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from jose import ExpiredSignatureError
from starlette import status
from starlette.requests import Request
from core.logger import logger
from exception.custom import UnauthorizedException, UserPasswordException, UserNotFoundException
from schemas.result import error, success


def init_exception(app: FastAPI):
    logger.success('全局异常捕获已开启！！！')

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, e: Exception):
        return error(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="服务器内部错误")

    @app.exception_handler(UserNotFoundException)
    async def http_exception(request: Request, e: UserNotFoundException):
        logger.warning(e.message)
        return error(code=status.HTTP_202_ACCEPTED, message=e.message)

    @app.exception_handler(UserPasswordException)
    async def http_exception(request: Request, e: UserPasswordException):
        logger.warning(e.message)
        return error(code=status.HTTP_202_ACCEPTED, message=e.message)

    @app.exception_handler(UnauthorizedException)
    async def http_exception(request: Request, e: UnauthorizedException):
        logger.warning(e.message)
        return error(code=status.HTTP_401_UNAUTHORIZED, message=e.message)
