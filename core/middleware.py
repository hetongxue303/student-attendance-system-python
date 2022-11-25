"""
中间件
@Author:何同学
"""
import time

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from core.logger import logger
from core.config import settings


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

        @app.middleware("http")
        async def http_middleware(request: Request, call_next):
            """
            请求/响应拦截器
            :param request: 请求
            :param call_next: 下一步
            :return: 响应体
            """
            start_time = time.time()
            response = await call_next(request)
            process_time = time.time() - start_time
            response.headers["X-Process-Time"] = str(round(process_time, 2))
            logger.debug('方法:{}  地址:{}  耗时:{} ms', request.method, request.url, str(round(process_time, 2)))
            return response
