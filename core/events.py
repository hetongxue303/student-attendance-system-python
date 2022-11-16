"""
事件监听
@Author:何同学
"""
from fastapi import FastAPI

from core.logger import logger


# 事件监听
def events_listen(app: FastAPI):
    @app.on_event('startup')
    async def startup():
        logger.success('启动成功 ---> 点击访问: http://127.0.0.1:8000/docs')

    @app.on_event('shutdown')
    async def shutdown():
        logger.error('项目停止')
