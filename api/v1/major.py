"""
专业相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Security

from core.security import check_permissions
from crud.major import query_major_list_all, query_major_list_page, insert_major, delete_major_by_id, update_major_by_id
from schemas.common import Page, BatchDto
from schemas.major import MajorDto
from schemas.result import Success

router = APIRouter()


@router.get('/get/all', response_model=Success[Page[list[MajorDto]]], summary='查询专业(All)',
            dependencies=[Security(check_permissions)])
async def select_all():
    majors = query_major_list_all()
    return Success(data=majors, message='查询成功')


@router.get('/get/page', response_model=Success[Page[list[MajorDto]]], summary='查询专业(Page)',
            dependencies=[Security(check_permissions)])
async def select_page(currentPage: int, pageSize: int, major_name: str = None):
    majors = query_major_list_page(current_page=currentPage, page_size=pageSize, major_name=major_name)
    return Success(data=majors, message='查询成功')


@router.post('/insert', response_model=Success[typing.Any], summary='新增专业',
             dependencies=[Security(check_permissions)])
async def insert_one(data: MajorDto):
    insert_major(data)
    return Success(message='增加成功')


@router.delete('/delete/{id}', response_model=Success[typing.Any], summary='删除专业',
               dependencies=[Security(check_permissions)])
async def delete_one(id: int):
    delete_major_by_id(id)
    return Success(message='删除成功')


@router.delete('/delete/batch', response_model=Success[typing.Any], summary='批量删除专业',
               dependencies=[Security(check_permissions)])
async def delete_batch(data: BatchDto):
    pass


@router.put('/update', response_model=Success[typing.Any], summary='修改专业',
            dependencies=[Security(check_permissions)])
async def update_one(data: MajorDto):
    update_major_by_id(data)
    return Success(message='修改成功')
