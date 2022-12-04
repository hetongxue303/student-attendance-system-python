"""
redis配置
@Author:何同学
"""
import aioredis

from aioredis import Redis
from fastapi import FastAPI, Request


async def get_async_redis_pool() -> Redis:
    """
    获取异步redis连接池
    :return: Redis
    """
    async_connection_pool = aioredis.ConnectionPool.from_url(url='redis://127.0.0.1', port=6379, db=1, encoding="utf-8",
                                                             decode_responses=True)
    return Redis(connection_pool=async_connection_pool)


async def init_redis_pool(app: FastAPI):
    """
    注入缓存到app state
    :param app:
    :return:
    """
    app.state.redis = await get_async_redis_pool()


async def get_redis(request: Request) -> Redis:
    return request.app.state.redis
