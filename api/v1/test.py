from fastapi import APIRouter

router = APIRouter()


@router.post('/test', summary='测试')
async def test():
    pass
