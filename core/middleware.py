"""
中间件
@Author:何同学
"""
import time

from fastapi import FastAPI
from jose import jwt, ExpiredSignatureError, JWTError
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from core.logger import logger
from core.config import settings
from exception.custom import JwtVerifyException, CaptchaException
from schemas.result import success_json, error_json


def cors_middleware(app: FastAPI):
    """
    跨域中间件
    :param app: 主程序
    :return: none
    """
    if settings.APP_CORS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_methods=['*'],
            allow_headers=['*'],
            allow_credentials=True
        )
        logger.success('跨域已开启！！！')


WHITE_LIST = {'/v1/login', '/v1/logout', '/v1/captchaImage'}


def http_middleware(app: FastAPI):
    """
    请求/响应拦截器
    :param app:
    :return:
    """

    @app.middleware("http")
    async def http_middleware_init(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        if request.url.path not in WHITE_LIST:
            try:
                token = request.headers.get('access_token')
                payload = jwt.decode(token=token, key=settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
                id = payload.get('id', None)
                username = payload.get('sub', None)
                scopes = payload.get('scopes', None)
                if not payload or id is None or username is None or scopes is None:
                    return error_json(message='无效凭证', code=401)
            except ExpiredSignatureError:
                return error_json(message='凭证过期', code=401)
            except JWTError:
                return error_json(message='凭证异常', code=401)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(round(process_time, 2))
        logger.debug('方法:{}  地址:{}  耗时:{} ms', request.method, request.url, str(round(process_time, 2)))
        return response
