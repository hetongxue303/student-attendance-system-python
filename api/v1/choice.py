"""
选课相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Security

from core.security import check_permissions
from crud.choice import insert_choice, delete_choice_by_id, update_choice_by_id, query_choice_list_all, \
    query_choice_list_page, update_choice_batch_by_id, query_choice_student_list_all
from schemas.choice import ChoiceDto, UpdateBatchChoiceDto
from schemas.common import Page
from schemas.result import Success

router = APIRouter()


@router.get('/student/get/page', response_model=Success[Page[list[ChoiceDto]]], summary='查询学生选课记录(Page)',
            dependencies=[Security(check_permissions)])
async def select_student_page(currentPage: int, pageSize: int, course_name: str = None):
    choices = await query_choice_student_list_all(current_page=currentPage, page_size=pageSize, course_name=course_name)
    return Success(data=choices, message='查询成功')


@router.get('/get/all', response_model=Success[Page[list[ChoiceDto]]], summary='查询选课记录(All)',
            dependencies=[Security(check_permissions)])
async def select_all():
    choices = query_choice_list_all()
    return Success(data=choices, message='查询成功')


@router.get('/get/page', response_model=Success[Page[list[ChoiceDto]]], summary='查询选课记录(Page)',
            dependencies=[Security(check_permissions)])
async def select_page(currentPage: int, pageSize: int, status: int = None,
                      real_name: str = None, course_name: str = None):
    choices = await query_choice_list_page(current_page=currentPage, page_size=pageSize, status=status,
                                           real_name=real_name, course_name=course_name)
    return Success(data=choices, message='查询成功')


@router.post('/insert', response_model=Success[typing.Any], summary='新增选课记录',
             dependencies=[Security(check_permissions)])
async def insert_one(data: ChoiceDto):
    insert_choice(data)
    return Success(message='增加成功')


@router.delete('/delete/{id}', response_model=Success[typing.Any], summary='删除选课记录',
               dependencies=[Security(check_permissions)])
async def delete_one(id: int):
    delete_choice_by_id(id)
    return Success(message='删除成功')


@router.put('/update/batch', response_model=Success[typing.Any], summary='批量更新选课记录',
            dependencies=[Security(check_permissions)])
async def update_batch(data: UpdateBatchChoiceDto = None):
    update_choice_batch_by_id(data)
    return Success(message='修改成功')


@router.put('/update', response_model=Success[typing.Any], summary='修改选课记录',
            dependencies=[Security(check_permissions)])
async def update_one(data: ChoiceDto):
    update_choice_by_id(data)
    return Success(message='修改成功')
