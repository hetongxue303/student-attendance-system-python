"""
学院相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Security

from core.security import check_permissions
from crud.college import query_college_list_all, query_college_list_page, insert_college, delete_college_by_id, \
    update_college_by_id
from schemas.college import CollegeDto
from schemas.common import Page, BatchDto
from schemas.result import Success

router = APIRouter()


@router.get('/get/all', response_model=Success[Page[list[CollegeDto]]], summary='查询学院(All)',
            dependencies=[Security(check_permissions)])
async def select_all():
    colleges = query_college_list_all()
    return Success(data=colleges, message='查询成功')


@router.get('/get/page', response_model=Success[Page[list[CollegeDto]]], summary='查询学院(Page)',
            dependencies=[Security(check_permissions)])
async def select_page(currentPage: int, pageSize: int, college_name: str = None):
    colleges = query_college_list_page(current_page=currentPage, page_size=pageSize, college_name=college_name)
    return Success(data=colleges, message='查询成功')


@router.post('/insert', response_model=Success[typing.Any], summary='新增学院',
             dependencies=[Security(check_permissions, scopes=['college:insert'])])
async def insert_one(data: CollegeDto):
    insert_college(data)
    return Success(message='增加成功')


@router.delete('/delete/{id}', response_model=Success[typing.Any], summary='删除学院',
               dependencies=[Security(check_permissions)])
async def delete_one(id: int):
    delete_college_by_id(id)
    return Success(message='删除成功')


@router.delete('/delete/batch', response_model=Success[typing.Any], summary='批量删除学院',
               dependencies=[Security(check_permissions)])
async def delete_batch(data: BatchDto):
    pass


@router.put('/update', response_model=Success[typing.Any], summary='修改学院',
            dependencies=[Security(check_permissions)])
async def update_one(data: CollegeDto):
    update_college_by_id(data)
    return Success(message='修改成功')
