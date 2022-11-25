"""
事件监听
@Author:何同学
"""
from fastapi import FastAPI

from core.config import settings
from core.logger import logger
from core.middleware import cors_middleware
from database.mysql import drop_db, init_db, init_data
from api.bsae import router
from exception.globals import init_exception


def events_listen(app: FastAPI):
    """
    启动/关机 活动监听
    :param app: 主程序
    :return: none
    """

    @app.on_event('startup')
    async def startup():
        """
        应用程序启动之前执行
        :return: none
        """
        drop_db()  # 删除数据结果
        init_db()  # 初始化数据结构
        init_data()  # 初始化表数据
        cors_middleware(app)  # 开启跨域
        init_exception(app)  # 开启全局异常捕获
        # 注册路由
        app.include_router(router, prefix=settings.APP_API_PREFIX)
        logger.success('启动成功！！！')
        logger.success('访问文档: http://127.0.0.1:8000/docs')

    @app.on_event('shutdown')
    async def shutdown():
        """
        应用程序关闭之前执行
        :return:
        """
        logger.success('停止...')
