from fastapi import APIRouter, Request

from core.redis import get_redis
from utils.captcha import generate_captcha

router = APIRouter()


@router.post('/test', summary='测试')
async def test(request: Request):
    print(generate_captcha())
    await request.app.state.redis.set(name='test', value='123')
