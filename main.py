"""
程序入口
@Author:何同学
"""
from fastapi import FastAPI

from core.config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESC,
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG,
    openapi_url=f'{settings.APP_API_PREFIX}/openapi.json'
)


@app.get('/test', summary='测试接口')
async def test():
    return '测试成功'
