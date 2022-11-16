"""
中间件
@Author:何同学
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.logger import logger
from core.config import settings


# 跨域中间件
def cors_middleware(app: FastAPI):
    if settings.APP_CORS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_methods=['*'],
            allow_headers=['*'],
            allow_credentials=True
        )
        logger.success('跨域已开启！！！')
