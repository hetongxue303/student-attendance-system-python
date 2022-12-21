from datetime import timedelta

from aioredis import Redis
from fastapi import APIRouter, Request

from database.redis import get_redis
from utils.captcha import generate_captcha

router = APIRouter()


@router.post('/test', summary='测试')
async def test(request: Request):
    print(generate_captcha())
    redis: Redis = await get_redis(request)
    await redis.setex(name='11', value='123456', time=timedelta(seconds=15))
