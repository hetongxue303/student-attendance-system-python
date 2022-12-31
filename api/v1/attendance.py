"""
考勤相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Security

from core.security import check_permissions
from crud.attendance import insert_attendance, query_attendances_student_list_all, delete_attendance_by_id, \
    update_attendance_by_id
from schemas.attendance import AttendanceDto
from schemas.common import Page
from schemas.result import Success

router = APIRouter()


@router.post('/insert', response_model=Success[typing.Any], summary='新增考勤',
             dependencies=[Security(check_permissions)])
async def insert_one(data: AttendanceDto):
    await insert_attendance(data)
    return Success(message='新增成功')


@router.delete('/delete/{id}', response_model=Success[typing.Any], summary='删除考勤')
async def delete_one(id: int):
    delete_attendance_by_id(id)
    return Success(message='删除成功')


@router.put('/update', response_model=Success[typing.Any], summary='修改考勤')
async def update_one(data: AttendanceDto):
    update_attendance_by_id(data)
    return Success(message='修改成功')


@router.get('/student/get/page', response_model=Success[Page[list[AttendanceDto]]], summary='获取学生考勤列表',
            dependencies=[Security(check_permissions)])
async def select_student_page(currentPage: int, pageSize: int):
    attendances = await query_attendances_student_list_all(current_page=currentPage, page_size=pageSize)
    return Success(data=attendances, message='查询成功')
