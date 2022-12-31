"""
考勤业务
@Author:何同学
"""
import jsonpickle
from aioredis import Redis
from sqlalchemy.orm import Session

from core.security import get_user
from database.mysql import get_db
from database.redis import get_redis
from models import Attendance, User, Course, Choice
from schemas.attendance import AttendanceDto
from schemas.attendance_record import AttendanceRecordDto
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
                      release_time=data.release_time, end_time=data.end_time,
                      course_count=db.query(Choice).filter(Choice.course_id == data.course_id).count()))
    db.commit()


async def query_attendances_student_list_all(current_page: int, page_size: int) -> Page[list[AttendanceDto]]:
    """
    获取学生考勤列表
    :param current_page:
    :param page_size:
    :return:
    """
    redis: Redis = await get_redis()
    user: User = await get_user(jsonpickle.decode(await redis.get('current-user')).username)
    course_ids: list[int] = []
    choices = db.query(Choice).filter(Choice.user_id == user.user_id).all()
    if choices:
        for item in choices:
            course_ids.append(item.course_id)
    print(course_ids)
    return Page(total=db.query(Attendance).filter(Attendance.course_id.in_(course_ids)).count(),
                record=db.query(Attendance).filter(Attendance.course_id.in_(course_ids)).limit(page_size).offset(
                    (current_page - 1) * page_size).all())


def delete_attendance_by_id(id: int):
    """
    根据考勤ID删除
    :param id:
    :return:
    """
    pass


def update_attendance_by_id(data: AttendanceDto):
    """
    根据考勤ID修改
    :param data:
    :return:
    """
    pass
