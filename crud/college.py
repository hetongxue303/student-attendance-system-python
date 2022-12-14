"""
学院业务
@Author:何同学
"""
from sqlalchemy.orm import Session

from database.mysql import get_db
from models import College
from schemas.college import CollegeDto
from schemas.common import Page

db: Session = next(get_db())


def query_college_list_all() -> Page[list[CollegeDto]]:
    """
    查询所有学院
    :return:
    """
    return Page(total=db.query(College).filter(College.is_delete == '0').count(),
                record=db.query(College).filter(College.is_delete == '0').all())


def query_college_list_page(current_page: int, page_size: int, college_name: str) -> Page[list[CollegeDto]]:
    """
    分页查询学院列表
    :param current_page: 当前页
    :param page_size: 页面大小
    :param college_name: 学院名字
    :return: 学院列表
    """
    if college_name:
        return Page(total=db.query(College).filter(College.is_delete == '0',
                                                   College.college_name.like('%{0}%'.format(college_name))).count(),
                    record=db.query(College).filter(College.is_delete == '0',
                                                    College.college_name.like('%{0}%'.format(college_name))).limit(
                        page_size).offset((current_page - 1) * page_size).all())
    return Page(total=db.query(College).filter(College.is_delete == '0').count(),
                record=db.query(College).filter(College.is_delete == '0').limit(page_size).offset(
                    (current_page - 1) * page_size).all())


def insert_college(data: CollegeDto):
    """
    新增学院
    :param data: 学院信息
    """
    db.add(College(college_name=data.college_name, description=data.description))
    db.commit()


def delete_college_by_id(id: int):
    """
    通过学院ID逻辑删除学院信息
    :param id: 学院ID
    :return:
    """
    item: College = db.query(College).filter(College.college_id == id).first()
    item.is_delete = '1'
    db.commit()


def update_college_by_id(data: CollegeDto):
    """
    通过学院ID修改信息
    :param data: 学院信息
    :return:
    """
    item: College = db.query(College).filter(College.college_id == data.college_id).first()
    item.college_name = data.college_name
    item.description = data.description
    db.commit()
