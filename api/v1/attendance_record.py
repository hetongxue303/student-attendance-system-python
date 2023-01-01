"""
考勤记录相关
@Author:何同学
"""
import typing

from fastapi import APIRouter, Security

from core.security import check_permissions
from crud.attendance_record import insert_attendance_record, update_attendance_record_by_id, \
    query_attendance_record_list_all, delete_attendance_record_by_id
from schemas.attendance_record import AttendanceRecordDto
from schemas.common import Page
from schemas.result import Success

router = APIRouter()


@router.post('/insert', response_model=Success[typing.Any], summary='新增考勤记录',
             dependencies=[Security(check_permissions)])
async def insert_one(data: AttendanceRecordDto):
    await insert_attendance_record(data)
    return Success(message='新增成功')


@router.post('/student/attendance', response_model=Success[typing.Any], summary='学生签到',
             dependencies=[Security(check_permissions)])
async def insert_one(data: AttendanceRecordDto):
    await insert_attendance_record(data)
    return Success(message='新增成功')


@router.delete('/delete/{id}', response_model=Success[typing.Any], summary='删除考勤记录')
async def delete_one(id: int):
    delete_attendance_record_by_id(id)
    return Success(message='删除成功')


@router.put('/update', response_model=Success[typing.Any], summary='修改考勤记录')
async def update_one(data: AttendanceRecordDto):
    update_attendance_record_by_id(data)
    return Success(message='修改成功')


@router.get('/get/page', response_model=Success[Page[list[AttendanceRecordDto]]], summary='获取考勤记录列表',
            dependencies=[Security(check_permissions)])
async def select_student_page(currentPage: int, pageSize: int):
    attendance_records = query_attendance_record_list_all(current_page=currentPage, page_size=pageSize)
    return Success(data=attendance_records, message='查询成功')
