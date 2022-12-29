"""
专业业务
@Author:何同学
"""
from typing import List

from sqlalchemy.orm import Session

from database.mysql import get_db
from models import Major
from schemas.common import Page
from schemas.major import MajorDto

db: Session = next(get_db())


def query_major_list_all():
    """
    查询所有专业
    :return:
    """
    return Page(total=db.query(Major).filter(Major.is_delete == '0').count(),
                record=db.query(Major).filter(Major.is_delete == '0').all())


def query_major_list_page(current_page: int, page_size: int, major_name: str):
    """
    分页查询专业列表
    :param current_page: 当前页
    :param page_size: 页面大小
    :param major_name: 专业名字
    :return: 专业列表
    """
    if major_name:
        return Page(total=db.query(Major).filter(Major.is_delete == '0',
                                                 Major.major_name.like('%{0}%'.format(major_name))).count(),
                    record=db.query(Major).filter(Major.is_delete == '0',
                                                  Major.major_name.like('%{0}%'.format(major_name))).limit(
                        page_size).offset((current_page - 1) * page_size).all())
    return Page(total=db.query(Major).filter(Major.is_delete == '0').count(),
                record=db.query(Major).filter(Major.is_delete == '0').limit(page_size).offset(
                    (current_page - 1) * page_size).all())


def insert_major(data: MajorDto):
    """
    新增专业
    :param data: 专业信息
    """
    db.add(Major(major_name=data.major_name, description=data.description))
    db.commit()


def delete_major_by_id(id: int):
    """
    通过专业ID逻辑删除专业信息
    :param id: 专业ID
    :return:
    """
    item: Major = db.query(Major).filter(Major.major_id == id).first()
    item.is_delete = '1'
    db.commit()


def update_major_by_id(data: MajorDto):
    """
    通过专业ID修改信息
    :param data: 专业信息
    :return:
    """
    item: Major = db.query(Major).filter(Major.major_id == data.major_id).first()
    item.major_name = data.major_name
    item.description = data.description
    db.commit()
