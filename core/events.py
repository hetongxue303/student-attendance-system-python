"""
事件监听
@Author:何同学
"""
from fastapi import FastAPI

from core.logger import logger
from core.middleware import cors_middleware
from database.mysql import drop_db, init_db
from exception.globals import init_exception


# 事件监听
def events_listen(app: FastAPI):
    @app.on_event('startup')
    async def startup():
        """ 程序启动前执行 """
        # 删除数据结果
        drop_db()
        # # 初始化数据结构
        init_db()
        # 开启跨域
        cors_middleware(app)
        # 开启全局异常捕获
        init_exception(app)
        logger.success('启动成功 ---> 点击访问: http://127.0.0.1:8000/docs')

    @app.on_event('shutdown')
    async def shutdown():
        """ 程序停止时执行 """
        logger.success('项目停止')
