"""
全局异常捕获
@Author:何同学
"""
import traceback
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.orm.exc import UnmappedInstanceError
from starlette import status
from starlette.requests import Request
from core.logger import logger
from exception.custom import IpErrorException, UserInfoException, UserNotFoundException, IdNotFoundException, \
    RedisSaveException, PermissionNotEnoughException, AccessTokenFailException
from schemas import fail, error, unauthorized


def init_exception(app: FastAPI):
    logger.success('全局异常捕获已开启！！！')

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, e: Exception):
        text: str = '全局异常'
        logger.error(f'{text}\n{request.method}URL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}')
        return error(message="服务器内部错误")

    @app.exception_handler(
        IpErrorException or UserInfoException or UserNotFoundException or IdNotFoundException or RedisSaveException)
    async def ip_error_handler(request: Request, e: IpErrorException):
        logger.warning(f'{e.message}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}')
        return fail(message=e.message)

    @app.exception_handler(AccessTokenFailException)
    async def access_token_fail_handler(request: Request, e: AccessTokenFailException):
        logger.warning(f'{e.message}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}')
        return unauthorized(message=e.message)

    @app.exception_handler(PermissionNotEnoughException)
    async def permission_not_enough_handler(request: Request, e: PermissionNotEnoughException):
        logger.warning(f'{e.message}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}')
        return fail(code=status.HTTP_403_FORBIDDEN, message=e.message)

    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(request: Request, e: IntegrityError):
        text: str = f'添加/更新的数据与数据库中数据冲突!'
        logger.warning(f'{text}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{e.orig}')
        return error(message=text)

    @app.exception_handler(ProgrammingError)
    async def programming_error_handle(request: Request, e: ProgrammingError):
        text: str = '请求参数丢失'
        logger.error(f'{text}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{e}')
        return fail(message=text)

    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, e: RequestValidationError):
        text: str = '请求参数格式错误'
        logger.error(f'{text}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{e.errors()}')
        return fail(code=status.HTTP_422_UNPROCESSABLE_ENTITY, message=text)

    @app.exception_handler(ValidationError)
    async def inner_validation_exception_handler(request: Request, e: ValidationError):
        text: str = '内部参数验证错误'
        logger.error(f'{text}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{e.errors()}')
        return error(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=text)

    @app.exception_handler(UnmappedInstanceError)
    async def un_mapped_instance_error_handler(request: Request, e: UnmappedInstanceError):
        text = f'不存在编号为 {id} 的数据, 删除失败!'
        logger.warning(f'{text}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}')
        return fail(message=text)
