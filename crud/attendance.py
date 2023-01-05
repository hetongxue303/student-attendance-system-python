"""
考勤业务
@Author:何同学
"""
from datetime import datetime, timedelta

import jsonpickle
from aioredis import Redis
from sqlalchemy.orm import Session

from core.security import get_user
from database.mysql import get_db
from database.redis import get_redis
from models import Attendance, User, Choice, Attendance_Record, Course
from schemas.attendance import AttendanceDto
from schemas.attendance_record import StudentAttendanceDto
from schemas.common import Page

db: Session = next(get_db())


async def insert_attendance(data: AttendanceDto):
    """
    新增考勤
    :param data:
    :return:
    """
    redis: Redis = await get_redis()
    user: User = await get_user(jsonpickle.decode(await redis.get('current-user')).username)
    db.query(Attendance).filter(Attendance.end_time)
    db.add(Attendance(user_id=user.user_id, course_id=data.course_id,
                      release_time=data.release_time + timedelta(hours=8), end_time=data.end_time + timedelta(hours=8),
                      course_count=db.query(Choice).filter(Choice.course_id == data.course_id).count()))
    db.commit()


async def query_attendances_student_list_all(current_page: int, page_size: int) -> Page[
    list[StudentAttendanceDto]]:
    """
    获取学生考勤列表
    :param current_page:
    :param page_size:
    :return:
    """
    redis: Redis = await get_redis()
    user: User = await get_user(jsonpickle.decode(await redis.get('current-user')).username)
    # 存当前学生的课程ID
    course_ids: list[int] = []
    # 获取该学生自己的选课信息
    choices = db.query(Choice).filter(Choice.user_id == user.user_id).all()
    if choices:
        for item in choices:
            course_ids.append(item.course_id)
    # 判断是否结束
    attendances = db.query(Attendance).filter(Attendance.course_id.in_(course_ids), Attendance.is_end == '0').all()
    for item in attendances:
        # 如果结束时间大于或等于当前时间 则更改状态 并且新增考勤记录
        if datetime.now().timestamp() >= item.end_time.timestamp():
            record = db.query(Attendance).filter(Attendance.attendance_id == item.attendance_id).first()
            record.is_end = '1'
            db.add(Attendance_Record(user_id=user.user_id, attendance_id=record.attendance_id,
                                     attendance_type='3', description='用户未签到，默认缺勤！'))
            db.commit()
    attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(course_ids)).limit(page_size).offset(
        (current_page - 1) * page_size).all()
    data: list[StudentAttendanceDto] = []
    for item in attendance_page:
        i = db.query(Attendance_Record).filter(Attendance_Record.attendance_id == item.attendance_id).first()
        data.append(StudentAttendanceDto(attendance=item, attendance_record=i))
    return Page(total=db.query(Attendance).filter(Attendance.course_id.in_(course_ids)).count(),
                record=data)


def delete_attendance_by_id(id: int):
    """
    根据考勤ID删除
    :param id:
    :return:
    """
    pass
