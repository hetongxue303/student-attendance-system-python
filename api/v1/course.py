"""
课程相关
@Author:何同学
"""
import typing
from typing import List

from fastapi import APIRouter, Security

from core.security import check_permissions
from crud.course import query_course_list_all, query_course_list_page, insert_course, delete_course_by_id, \
    update_course_by_id
from schemas.common import Page
from schemas.course import CourseDto
from schemas.result import Success

router = APIRouter()


@router.get('/getAll', response_model=Success[Page[List[CourseDto]]], summary='查询课程(All)')
async def select_all():
    courses = query_course_list_all()
    return Success(data=courses, message='查询成功')


@router.get('/getPage', response_model=Success[Page[List[CourseDto]]], summary='查询课程(Page)',
            dependencies=[Security(check_permissions, scopes=['course:list'])])
async def select_page(currentPage: int, pageSize: int, course_name: str = None):
    courses = await query_course_list_page(current_page=currentPage, page_size=pageSize, course_name=course_name)
    return Success(data=courses, message='查询成功')


@router.post('/insert', response_model=Success[typing.Any], summary='新增课程')
async def insert_one(data: CourseDto):
    insert_course(data)
    return Success(message='增加成功')


@router.delete('/delete/{id}', response_model=Success[typing.Any], summary='删除课程')
async def delete_one(id: int):
    delete_course_by_id(id)
    return Success(message='删除成功')


@router.delete('/delete/batch', response_model=Success[typing.Any], summary='批量删除课程')
async def delete_batch(data: List[int]):
    pass


@router.put('/update', response_model=Success[typing.Any], summary='修改课程')
async def update_one(data: CourseDto):
    update_course_by_id(data)
    return Success(message='修改成功')
