"""
角色相关
@Author:何同学
"""
from fastapi import APIRouter, Body

router = APIRouter()


@router.get('/getAll', summary='查询角色(All)')
async def select_all():
    pass


@router.get('/getPage', summary='查询角色(Page)')
async def select_page(data=Body(None)):
    pass


@router.get('/getOne/{id}', summary='查询角色(ById)')
async def select_one(id: int):
    pass


@router.post('/insert', summary='新增角色')
async def insert_one(data=Body(None)):
    pass


@router.delete('/delete/{id}', summary='删除角色')
async def delete_one(id: int):
    pass


@router.put('/update/{id}', summary='修改角色')
async def update_one(id: int):
    pass
