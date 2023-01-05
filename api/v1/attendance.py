"""
考勤相关
@Author:何同学
"""
import typing

import jsonpickle
from aioredis import Redis
from fastapi import APIRouter, Security
from sqlalchemy.orm import Session

from core.security import check_permissions, get_user
from crud.attendance import insert_attendance, query_attendances_student_list_all, delete_attendance_by_id
from database.mysql import get_db
from database.redis import get_redis
from models import User, Attendance, Choice, Attendance_Record
from schemas.attendance import AttendanceDto
from schemas.attendance_record import StudentAttendanceDto
from schemas.common import Page
from schemas.result import Success
from schemas.user import StudentAttendanceRecordDto

router = APIRouter()
db: Session = next(get_db())


@router.post('/insert', response_model=Success[typing.Any], summary='新增考勤',
             dependencies=[Security(check_permissions)])
async def insert_one(data: AttendanceDto):
    await insert_attendance(data)
    return Success(message='新增成功')


@router.delete('/delete/{id}', response_model=Success[typing.Any], summary='删除考勤',
               dependencies=[Security(check_permissions)])
async def delete_one(id: int):
    delete_attendance_by_id(id)
    return Success(message='删除成功')


@router.put('/update', response_model=Success[typing.Any], summary='修改考勤',
            dependencies=[Security(check_permissions)])
async def update_one(data: AttendanceDto):
    item = db.query(Attendance).filter(Attendance.attendance_id == data.attendance_id).first()
    item.is_end = '1' if data.is_end else '0'
    db.commit()
    return Success(message='修改成功')


@router.get('/student/get/page', response_model=Success[Page[list[StudentAttendanceDto]]],
            summary='获取学生考勤列表',
            dependencies=[Security(check_permissions)])
async def select_student_page(currentPage: int, pageSize: int):
    attendances = await query_attendances_student_list_all(current_page=currentPage, page_size=pageSize)
    return Success(data=attendances, message='查询成功')


@router.get('/get/page', response_model=Success[Page[list[AttendanceDto]]], summary='分页获取签到信息',
            dependencies=[Security(check_permissions)])
async def select_attendance_page(currentPage: int, pageSize: int):
    redis: Redis = await get_redis()
    user: User = await get_user(jsonpickle.decode(await redis.get('current-user')).username)
    # 查询当前老师发布的签到信息
    total = db.query(Attendance).filter(Attendance.user_id == user.user_id).count()
    data = db.query(Attendance).filter(Attendance.user_id == user.user_id).limit(pageSize).offset(
        (currentPage - 1) * pageSize).all()
    return Success(data=Page(record=data, total=total), message='查询成功')


@router.get('/student/page/checked', response_model=Success[Page[list[StudentAttendanceRecordDto]]],
            summary='分页获取已签到学生',
            dependencies=[Security(check_permissions)])
async def select_user_checked_in(attendance_id: int, active: int, currentPage: int, pageSize: int):
    attendance = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()  # 查询签到信息
    attendance_records = db.query(Attendance_Record).filter(
        Attendance_Record.attendance_id == attendance.attendance_id).all()  # 查询签到记录
    choices = db.query(Choice).filter(Choice.course_id == attendance.course_count).all()  # 查询这门课有哪些学生选择
    checked_user_ids: list[int] = []  # 已签到学生信息
    no_checked_user_ids: list[int] = []  # 未签到学生信息
    user_ids: list[int] = []  # 选择该课程的所有学生
    if choices:
        for v in choices:
            user_ids.append(v.user_id)
    if attendance_records:
        for v in attendance_records:
            checked_user_ids.append(v.user_id)
    if user_ids:
        for user_id in user_ids:
            if user_id not in checked_user_ids:
                no_checked_user_ids.append(user_id)
    data: list[StudentAttendanceRecordDto] = []
    users: list = []
    total: int = 0
    # 已签到
    if active == 1:
        total: int = db.query(User).filter(User.user_id.in_(checked_user_ids)).count()
        users = db.query(User).filter(User.user_id.in_(checked_user_ids)).limit(pageSize).offset(
            (currentPage - 1) * pageSize).all()
    # 未签到
    else:
        total: int = db.query(User).filter(User.user_id.in_(no_checked_user_ids)).count()
        users: list = db.query(User).filter(User.user_id.in_(no_checked_user_ids)).limit(pageSize).offset(
            (currentPage - 1) * pageSize).all()

    for user in users:
        att = db.query(Attendance_Record).filter(Attendance_Record.attendance_id == attendance_id,
                                                 Attendance_Record.user_id == user.user_id).first()
        data.append(StudentAttendanceRecordDto(user_id=user.user_id, username=user.username, avatar=user.avatar,
                                               gender=user.gender, real_name=user.real_name, email=user.email,
                                               phone=user.phone,
                                               attendance_time=att.create_time if active == 1 else None,
                                               attendance_type=att.attendance_type if active == 1 else None))
    return Success(data=Page(total=total, record=data), message='查询成功')
