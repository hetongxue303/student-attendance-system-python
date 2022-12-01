from fastapi import APIRouter

from utils.captcha import generate_captcha

router = APIRouter()


@router.post('/test', summary='测试')
async def test():
    print(generate_captcha())
