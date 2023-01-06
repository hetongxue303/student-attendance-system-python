"""
考勤业务
@Author:何同学
"""
from datetime import datetime, timedelta

import jsonpickle
from aioredis import Redis
from sqlalchemy import desc
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
    db.add(Attendance(user_id=user.user_id, course_id=data.course_id,
                      release_time=data.release_time + timedelta(hours=8), end_time=data.end_time + timedelta(hours=8),
                      course_count=db.query(Choice).filter(Choice.course_id == data.course_id).count()))
    db.commit()


async def query_attendances_student_list_all(current_page: int, page_size: int, course_name: str,
                                             real_name: str, status: int) -> Page[
    list[StudentAttendanceDto]]:
    """
    获取学生考勤列表
    :param current_page: 当前页
    :param page_size: 页面大小
    :param course_name: 课程名称
    :param real_name: 教师名称
    :param status: 状态
    """
    redis: Redis = await get_redis()
    user: User = await get_user(jsonpickle.decode(await redis.get('current-user')).username)
    course_ids: list[int] = []
    choices = db.query(Choice).filter(Choice.user_id == user.user_id).all()
    for item in choices:
        course_ids.append(item.course_id)
    # 判断是否结束
    attendances = db.query(Attendance).filter(Attendance.course_id.in_(course_ids)).all()
    for item in attendances:
        if datetime.now().timestamp() >= item.end_time.timestamp():
            record = db.query(Attendance).filter(Attendance.attendance_id == item.attendance_id).first()
            record.is_end = '1'
            db.add(Attendance_Record(user_id=user.user_id, attendance_id=record.attendance_id,
                                     attendance_type='3', description='用户未签到，默认缺勤！'))
            db.commit()

    # 教师 + 状态 + 课程
    if status is not None and real_name and course_name:
        temp_course_ids: list[int] = []
        course = db.query(Course).filter(
            Course.course_name.like('%{0}%'.format(course_name)), Course.course_id.in_(course_ids)).all()
        for item in course:
            temp_course_ids.append(item.course_id)
        user_ids: list[int] = []
        users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name), User.role == 2)).all()
        for item in users:
            user_ids.append(item.user_id)
        total = db.query(Attendance).filter(Attendance.course_id.in_(temp_course_ids),
                                            Attendance.user_id.in_(user_ids),
                                            Attendance.is_end == status.__str__()).count()
        attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(temp_course_ids),
                                                      Attendance.user_id.in_(user_ids),
                                                      Attendance.is_end == status.__str__()).order_by(
            Attendance.end_time.desc(), Attendance.is_end).limit(page_size).offset(
            (current_page - 1) * page_size).all()
        data: list[StudentAttendanceDto] = []
        for item in attendance_page:
            record = db.query(Attendance_Record).filter(
                Attendance_Record.attendance_id == item.attendance_id).first()
            data.append(StudentAttendanceDto(attendance=item, attendance_record=record))
        return Page(total=total, record=data)

    # 状态 + 教师
    if status is not None and real_name:
        user_ids: list[int] = []
        users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name), User.role == 2)).all()
        for item in users:
            user_ids.append(item.user_id)
        total = db.query(Attendance).filter(Attendance.course_id.in_(course_ids),
                                            Attendance.user_id.in_(user_ids),
                                            Attendance.is_end == status.__str__()).count()
        attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(course_ids),
                                                      Attendance.user_id.in_(user_ids),
                                                      Attendance.is_end == status.__str__()).order_by(
            Attendance.end_time.desc(), Attendance.is_end).limit(page_size).offset((current_page - 1) * page_size).all()
        data: list[StudentAttendanceDto] = []
        for item in attendance_page:
            record = db.query(Attendance_Record).filter(Attendance_Record.attendance_id == item.attendance_id).first()
            data.append(StudentAttendanceDto(attendance=item, attendance_record=record))
        return Page(total=total, record=data)

    # 状态 + 课程
    if status is not None and course_name:
        temp_course_ids: list[int] = []
        course = db.query(Course).filter(
            Course.course_name.like('%{0}%'.format(course_name)), Course.course_id.in_(course_ids)).all()
        for item in course:
            temp_course_ids.append(item.course_id)
        total = db.query(Attendance).filter(Attendance.course_id.in_(temp_course_ids),
                                            Attendance.is_end == status.__str__()).count()
        attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(temp_course_ids),
                                                      Attendance.is_end == status.__str__()).order_by(
            Attendance.end_time.desc(), Attendance.is_end).limit(page_size).offset((current_page - 1) * page_size).all()
        data: list[StudentAttendanceDto] = []
        for item in attendance_page:
            record = db.query(Attendance_Record).filter(Attendance_Record.attendance_id == item.attendance_id).first()
            data.append(StudentAttendanceDto(attendance=item, attendance_record=record))
        return Page(total=total, record=data)

    # 教师 + 课程
    if course_name and real_name:
        temp_course_ids: list[int] = []
        course = db.query(Course).filter(
            Course.course_name.like('%{0}%'.format(course_name)), Course.course_id.in_(course_ids)).all()
        for item in course:
            temp_course_ids.append(item.course_id)
        user_ids: list[int] = []
        users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name), User.role == 2)).all()
        for item in users:
            user_ids.append(item.user_id)
        total = db.query(Attendance).filter(Attendance.course_id.in_(temp_course_ids),
                                            Attendance.user_id.in_(user_ids)).count()
        attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(temp_course_ids),
                                                      Attendance.user_id.in_(user_ids)).order_by(
            Attendance.end_time.desc(), Attendance.is_end).limit(page_size).offset(
            (current_page - 1) * page_size).all()
        data: list[StudentAttendanceDto] = []
        for item in attendance_page:
            record = db.query(Attendance_Record).filter(
                Attendance_Record.attendance_id == item.attendance_id).first()
            data.append(StudentAttendanceDto(attendance=item, attendance_record=record))
        return Page(total=total, record=data)

    # 状态
    if status is not None:
        total = db.query(Attendance).filter(Attendance.course_id.in_(course_ids),
                                            Attendance.is_end == status.__str__()).count()
        attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(course_ids),
                                                      Attendance.is_end == status.__str__()).order_by(
            Attendance.end_time.desc(), Attendance.is_end).limit(page_size).offset((current_page - 1) * page_size).all()
        data: list[StudentAttendanceDto] = []
        for item in attendance_page:
            record = db.query(Attendance_Record).filter(Attendance_Record.attendance_id == item.attendance_id).first()
            data.append(StudentAttendanceDto(attendance=item, attendance_record=record))
        return Page(total=total, record=data)

    # 教师姓名
    if real_name:
        user_ids: list[int] = []
        users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name), User.role == 2)).all()
        for item in users:
            user_ids.append(item.user_id)
        total = db.query(Attendance).filter(Attendance.course_id.in_(course_ids),
                                            Attendance.user_id.in_(user_ids)).count()
        attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(course_ids),
                                                      Attendance.user_id.in_(user_ids)).order_by(
            Attendance.end_time.desc(), Attendance.is_end).limit(page_size).offset((current_page - 1) * page_size).all()
        data: list[StudentAttendanceDto] = []
        for item in attendance_page:
            record = db.query(Attendance_Record).filter(Attendance_Record.attendance_id == item.attendance_id).first()
            data.append(StudentAttendanceDto(attendance=item, attendance_record=record))
        return Page(total=total, record=data)

    # 课程名称
    if course_name:
        temp_course_ids: list[int] = []
        course = db.query(Course).filter(
            Course.course_name.like('%{0}%'.format(course_name)), Course.course_id.in_(course_ids)).all()
        for item in course:
            temp_course_ids.append(item.course_id)
        total = db.query(Attendance).filter(Attendance.course_id.in_(temp_course_ids)).count()
        attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(temp_course_ids)).order_by(
            Attendance.end_time.desc(), Attendance.is_end).limit(page_size).offset((current_page - 1) * page_size).all()
        data: list[StudentAttendanceDto] = []
        for item in attendance_page:
            record = db.query(Attendance_Record).filter(Attendance_Record.attendance_id == item.attendance_id).first()
            data.append(StudentAttendanceDto(attendance=item, attendance_record=record))
        return Page(total=total, record=data)

    # 默认查询
    total = db.query(Attendance).filter(Attendance.course_id.in_(course_ids)).count()
    attendance_page = db.query(Attendance).filter(Attendance.course_id.in_(course_ids)).order_by(
        Attendance.end_time.desc(), Attendance.is_end).limit(page_size).offset((current_page - 1) * page_size).all()
    data: list[StudentAttendanceDto] = []
    for item in attendance_page:
        record = db.query(Attendance_Record).filter(Attendance_Record.attendance_id == item.attendance_id).first()
        data.append(StudentAttendanceDto(attendance=item, attendance_record=record))
    return Page(total=total, record=data)


def delete_attendance_by_id(id: int):
    """
    根据考勤ID删除
    :param id:
    :return:
    """
    pass
