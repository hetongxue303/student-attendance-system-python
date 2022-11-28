"""
菜单相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Body

from schemas import success

router = APIRouter()


@router.get('/getAll', response_model=success[typing.Any], summary='查询菜单(All)')
async def select_all():
    return success(data={'content': 'test'})


@router.get('/getPage', summary='查询菜单(Page)')
async def select_page(data=Body(None)):
    pass


@router.get('/getOne/{id}', summary='查询菜单(ById)')
async def select_one(id: int):
    pass


@router.post('/insert', summary='新增菜单')
async def insert_one(data=Body(None)):
    pass


@router.delete('/delete/{id}', summary='删除菜单')
async def delete_one(id: int):
    pass


@router.put('/update/{id}', summary='修改菜单')
async def update_one(id: int):
    pass
