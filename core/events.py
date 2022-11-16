"""
事件监听
@Author:何同学
"""
from fastapi import FastAPI

from core.config import settings
from core.logger import logger
from core.middleware import cors_middleware
from database.mysql import drop_db, init_db, init_data
from exception.globals import init_exception
from api.bsae import router


# 事件监听
def events_listen(app: FastAPI):
    @app.on_event('startup')
    async def startup():
        """ 程序启动前执行 """
        # 删除数据结果
        drop_db()
        # # 初始化数据结构
        init_db()
        # 初始化表数据
        init_data()
        # 开启跨域
        cors_middleware(app)
        # 开启全局异常捕获
        init_exception(app)
        # 注册路由
        app.include_router(router, prefix=settings.APP_API_PREFIX)
        logger.success('启动成功！！！')
        logger.success('访问文档: http://127.0.0.1:8000/docs')

    @app.on_event('shutdown')
    async def shutdown():
        """ 程序停止时执行 """
        logger.success('项目停止')
