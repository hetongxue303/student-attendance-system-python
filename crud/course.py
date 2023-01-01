"""
课程业务
@Author:何同学
"""
from typing import List

import jsonpickle
from aioredis import Redis
from sqlalchemy.orm import Session

from core.security import get_user
from crud.choice import insert_choice, update_choice_quit
from database.mysql import get_db
from database.redis import get_redis
from exception.custom import UpdateException
from models import User, Choice
from models.course import Course
from schemas.choice import ChoiceDto
from schemas.common import Page
from schemas.course import CourseDto
from schemas.user import LoginDto

db: Session = next(get_db())


async def query_course_list_all() -> Page[List[CourseDto]]:
    """
    查询所有课程
    :return:
    """
    return Page(total=db.query(Course).filter(Course.is_delete == '0').count(),
                record=db.query(Course).filter(Course.is_delete == '0').all())


async def query_course_teacher_list_all() -> List[Course]:
    """
    查询教师的所有课程
    :return: List[CourseDto]
    """
    redis: Redis = await get_redis()
    role_keys: List[str] = jsonpickle.decode(await redis.get('current-role-keys'))
    login_info: LoginDto = jsonpickle.decode(await redis.get('current-user'))
    user: User = await get_user(login_info.username)
    if 'teacher' in role_keys:
        return db.query(Course).filter(Course.teacher_id == user.user_id).all()


async def query_course_list_page(current_page: int, page_size: int, course_name: str) -> Page[List[CourseDto]]:
    """
    分页查询课程列表
    :param current_page: 当前页
    :param page_size: 页面大小
    :param course_name: 课程名字
    :return: 学院列表
    """
    redis: Redis = await get_redis()
    role_keys: List[str] = jsonpickle.decode(await redis.get('current-role-keys'))
    # 管理员/学生：可查询所有课程
    if 'admin' in role_keys or 'student' in role_keys:
        if course_name:
            return Page(total=db.query(Course).filter(Course.is_delete == '0',
                                                      Course.course_name.like('%{0}%'.format(course_name))).count(),
                        record=db.query(Course).filter(Course.is_delete == '0',
                                                       Course.course_name.like('%{0}%'.format(course_name))).limit(
                            page_size).offset((current_page - 1) * page_size).all())
        return Page(total=db.query(Course).filter(Course.is_delete == '0').count(),
                    record=db.query(Course).filter(Course.is_delete == '0').limit(page_size).offset(
                        (current_page - 1) * page_size).all())
    # 教师：只能查询自己的课程
    login_info: LoginDto = jsonpickle.decode(await redis.get('current-user'))
    user: User = await get_user(login_info.username)
    if 'teacher' in role_keys:
        if course_name:
            return Page(total=db.query(Course).filter(Course.is_delete == '0', Course.teacher_id == user.user_id,
                                                      Course.course_name.like('%{0}%'.format(course_name))).count(),
                        record=db.query(Course).filter(Course.is_delete == '0', Course.teacher_id == user.user_id,
                                                       Course.course_name.like('%{0}%'.format(course_name))).limit(
                            page_size).offset((current_page - 1) * page_size).all())
        return Page(total=db.query(Course).filter(Course.is_delete == '0', Course.teacher_id == user.user_id).count(),
                    record=db.query(Course).filter(Course.is_delete == '0', Course.teacher_id == user.user_id).limit(
                        page_size).offset((current_page - 1) * page_size).all())


async def insert_course(course: CourseDto):
    """
    新增课程
    :param course: 课程信息
    """
    redis: Redis = await get_redis()
    role_keys: List[str] = jsonpickle.decode(await redis.get('current-role-keys'))
    # 管理员：指定教师添加课程
    if 'admin' in role_keys:
        db.add(Course(course_name=course.course_name, teacher_id=course.teacher_id,
                      count=course.count, class_time=course.class_time, description=course.description))
        db.commit()
        return

    # 教师：根据自己的ID新增课程
    login_info: LoginDto = jsonpickle.decode(await redis.get('current-user'))
    user: User = await get_user(login_info.username)
    if 'teacher' in role_keys:
        db.add(Course(course_name=course.course_name, teacher_id=user.user_id,
                      count=course.count, class_time=course.class_time, description=course.description))
        db.commit()
        return


async def delete_course_by_id(id: int):
    """
    通过课程ID逻辑删除课程信息
    :param id: 课程ID
    :return:
    """
    item: Course = db.query(Course).filter(Course.course_id == id).first()
    item.is_delete = '1'
    db.commit()


async def update_course_by_id(data: CourseDto):
    """
    通过课程ID修改信息
    :param data: 课程信息
    :return:
    """
    item: Course = db.query(Course).filter(Course.course_id == data.course_id).first()
    item.course_name = data.course_name
    item.count = data.count
    item.choice = data.choice
    item.class_time = data.class_time
    item.teacher_id = data.teacher_id
    item.description = data.description
    db.commit()


async def update_course_choice(course_id: int):
    """
    学生选课
    :param course_id: 课程ID
    """
    redis: Redis = await get_redis()
    role_keys: List[str] = jsonpickle.decode(await redis.get('current-role-keys'))
    item: Course = db.query(Course).filter(Course.course_id == course_id).first()
    if 'student' in role_keys and item and item.is_delete == '0' and item.count != item.choice:
        login_info: LoginDto = jsonpickle.decode(await redis.get('current-user'))
        user: User = await get_user(login_info.username)
        item.choice += 1
        insert_choice(ChoiceDto(user_id=user.user_id, course_id=item.course_id))
        db.commit()
    else:
        raise UpdateException(message='选课失败')


async def update_course_quit(course_id: int):
    """
    学生退选
    :param course_id: 课程ID
    """
    redis: Redis = await get_redis()
    role_keys: List[str] = jsonpickle.decode(await redis.get('current-role-keys'))
    item: Course = db.query(Course).filter(Course.course_id == course_id).first()
    if 'student' in role_keys and item and item.is_delete == '0' and item.choice != 0:
        login_info: LoginDto = jsonpickle.decode(await redis.get('current-user'))
        user: User = await get_user(login_info.username)
        update_choice_quit(user.user_id, item.course_id)
        item.choice -= 1
        db.commit()
    else:
        raise UpdateException(message='退选失败', code=400)
