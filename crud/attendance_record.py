"""
考勤记录业务
@Author:何同学
"""
import jsonpickle
from aioredis import Redis
from sqlalchemy.orm import Session

from core.security import get_user
from database.mysql import get_db
from database.redis import get_redis
from models import User, Attendance_Record
from schemas.attendance_record import AttendanceRecordDto
from schemas.common import Page

db: Session = next(get_db())


async def insert_attendance_record(data: AttendanceRecordDto):
    """
    新增考勤记录
    :param data:
    :return:
    """
    redis: Redis = await get_redis()
    user: User = await get_user(jsonpickle.decode(await redis.get('current-user')).username)
    db.add(Attendance_Record(user_id=user.user_id,
                             attendance_id=data.attendance_id,
                             attendance_type=data.attendance_type.__str__(),
                             description=None if data.description is None else data.description))
    db.commit()
    db.close()


def query_attendance_record_list_all(current_page: int, page_size: int) -> Page[list[AttendanceRecordDto]]:
    """
    获取学生考勤列表
    :param current_page:
    :param page_size:
    :return:
    """
    pass


def delete_attendance_record_by_id(id: int):
    """
    根据考勤记录ID删除
    :param id:
    :return:
    """
    pass


def update_attendance_record_by_id(data: AttendanceRecordDto):
    """
    根据考勤记录ID修改
    :param data:
    :return:
    """
    pass
