"""
用户相关
@Author:何同学
"""
from fastapi import APIRouter, Body

router = APIRouter()


@router.get('/getCurrent', summary='查询当前用户')
async def select_current_user():
    pass


@router.get('/getAll', summary='查询用户(All)')
async def select_all():
    pass


@router.get('/getPage', summary='查询用户(Page)')
async def select_page(data=Body(None)):
    pass


@router.get('/getOne/{id}', summary='查询用户(ById)')
async def select_one(id: int):
    pass


@router.post('/insert', summary='新增用户')
async def insert_one(data=Body(None)):
    pass


@router.delete('/delete/{id}', summary='删除用户')
async def delete_one(id: int):
    pass


@router.put('/update/{id}', summary='修改用户')
async def update_one(id: int):
    pass
