"""
课程业务
@Author:何同学
"""
from typing import List

from sqlalchemy.orm import Session

from database.mysql import get_db
from models.course import Course
from schemas.common import Page
from schemas.course import CourseDto

db: Session = next(get_db())


def query_course_list_all() -> Page[List[CourseDto]]:
    """
    查询所有课程
    :return:
    """
    return Page(total=db.query(Course).filter(Course.is_delete == '0').count(),
                record=db.query(Course).filter(Course.is_delete == '0').all())


def query_course_list_page(current_page: int, page_size: int, course_name: str) -> Page[List[CourseDto]]:
    """
    分页查询课程列表
    :param current_page: 当前页
    :param page_size: 页面大小
    :param course_name: 课程名字
    :return: 学院列表
    """
    if course_name:
        return Page(total=db.query(Course).filter(Course.is_delete == '0',
                                                  Course.course_name.like('%{0}%'.format(course_name))).count(),
                    record=db.query(Course).filter(Course.is_delete == '0',
                                                   Course.course_name.like('%{0}%'.format(course_name))).limit(
                        page_size).offset((current_page - 1) * page_size).all())
    return Page(total=db.query(Course).filter(Course.is_delete == '0').count(),
                record=db.query(Course).filter(Course.is_delete == '0').limit(page_size).offset(
                    (current_page - 1) * page_size).all())


def insert_course(course: CourseDto):
    """
    新增课程
    :param course: 课程信息
    """
    db.add(Course(course_name=course.course_name,
                  teacher_id=course.teacher_id,
                  count=course.count,
                  description=course.description))
    db.commit()


def delete_course_by_id(id: int):
    """
    通过课程ID逻辑删除课程信息
    :param id: 课程ID
    :return:
    """
    item: Course = db.query(Course).filter(Course.course_id == id).first()
    item.is_delete = '1'
    db.commit()


def update_course_by_id(data: CourseDto):
    """
    通过课程ID修改信息
    :param data: 课程信息
    :return:
    """
    item: Course = db.query(Course).filter(Course.course_id == data.course_id).first()
    item.course_name = data.course_name
    item.count = data.count
    item.choice = data.choice
    item.description = data.description
    db.commit()
