"""
选课业务
@Author:何同学
"""
import jsonpickle
from aioredis import Redis
from sqlalchemy.orm import Session

from core.security import get_user
from database.mysql import get_db
from database.redis import get_redis
from exception.custom import UpdateException
from models import Choice, Course, User
from schemas.choice import ChoiceDto, UpdateBatchChoiceDto
from schemas.common import Page
from schemas.user import LoginDto

db: Session = next(get_db())


async def query_choice_student_list_all(current_page: int, page_size: int, course_name: str) -> Page[
    list[ChoiceDto]]:
    """
    获取学生选课记录
    :param current_page: 当前页
    :param page_size: 页面大小
    :param course_name: 课程名称
    :return:
    """
    redis: Redis = await get_redis()
    login_info: LoginDto = jsonpickle.decode(await redis.get('current-user'))
    user: User = await get_user(login_info.username)
    if course_name:
        course_ids: list[int] = []
        courses = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
        for item in courses:
            course_ids.append(item.course_id)
        return Page(total=db.query(Choice).filter(Choice.user_id == user.user_id, Choice.status == '1',
                                                  Choice.is_quit == '0', Choice.course_id.in_(course_ids)).count(),
                    record=db.query(Choice).filter(Choice.user_id == user.user_id, Choice.status == '1',
                                                   Choice.is_quit == '0', Choice.course_id.in_(course_ids)).limit(
                        page_size).offset((current_page - 1) * page_size).all())

    return Page(total=db.query(Choice).filter(Choice.user_id == user.user_id, Choice.status == '1',
                                              Choice.is_quit == '0').count(),
                record=db.query(Choice).filter(Choice.user_id == user.user_id, Choice.status == '1',
                                               Choice.is_quit == '0').limit(page_size).offset(
                    (current_page - 1) * page_size).all())


def query_choice_list_all() -> Page[list[ChoiceDto]]:
    """
    查询所有选课记录
    :return:
    """
    return Page(total=db.query(Choice).filter(Choice.is_delete == '0').count(),
                record=db.query(Choice).filter(Choice.is_delete == '0').all())


async def query_choice_list_page(current_page: int, page_size: int, status: int = None,
                                 real_name: str = None, course_name: str = None) -> Page[list[ChoiceDto]]:
    """
    分页查询学院列表
    :param current_page: 当前页
    :param page_size: 页面大小
    :param status: 状态
    :param real_name: 学生姓名
    :param course_name: 课程名称
    :return: 选课列表
    """
    redis: Redis = await get_redis()
    role_keys: list[str] = jsonpickle.decode(await redis.get('current-role-keys'))
    # 管理员：查询所有
    if 'admin' in role_keys:

        if status is not None and real_name and course_name:
            user_ids: list[int] = []
            course_ids: list[int] = []
            course = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
            users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name))).all()
            for item in users:
                user_ids.append(item.user_id)
            for item in course:
                course_ids.append(item.course_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                              Choice.user_id.in_(user_ids), Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                               Choice.user_id.in_(user_ids), Choice.course_id.in_(course_ids)).limit(
                    page_size).offset((current_page - 1) * page_size).all())

        if status is not None and real_name:
            user_ids: list[int] = []
            users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name))).all()
            for item in users:
                user_ids.append(item.user_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                              Choice.user_id.in_(user_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                               Choice.user_id.in_(user_ids)).limit(page_size).offset(
                    (current_page - 1) * page_size).all())

        if status is not None and course_name:
            course_ids: list[int] = []
            course = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
            for item in course:
                course_ids.append(item.course_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                              Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                               Choice.course_id.in_(course_ids)).limit(page_size).offset(
                    (current_page - 1) * page_size).all())

        if real_name and course_name:
            user_ids: list[int] = []
            course_ids: list[int] = []
            course = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
            users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name))).all()
            for item in users:
                user_ids.append(item.user_id)
            for item in course:
                course_ids.append(item.course_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.user_id.in_(user_ids),
                                              Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.user_id.in_(user_ids),
                                               Choice.course_id.in_(course_ids)).limit(page_size).offset(
                    (current_page - 1) * page_size).all())

        if status is not None:
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(), ).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__()).limit(
                    page_size).offset((current_page - 1) * page_size).all())

        if real_name:
            user_ids: list[int] = []
            users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name))).all()
            for item in users:
                user_ids.append(item.user_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.user_id.in_(user_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.user_id.in_(user_ids)).limit(
                    page_size).offset((current_page - 1) * page_size).all())

        if course_name:
            course_ids: list[int] = []
            course = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
            for item in course:
                course_ids.append(item.course_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.course_id.in_(course_ids)).limit(
                    page_size).offset((current_page - 1) * page_size).all())
        # 默认查询
        return Page(total=db.query(Choice).filter(Choice.is_delete == '0').count(),
                    record=db.query(Choice).filter(Choice.is_delete == '0').limit(page_size).offset(
                        (current_page - 1) * page_size).all())

    # 教师：只能查询自己的课程
    if 'teacher' in role_keys:
        user: User = await get_user(jsonpickle.decode(await redis.get('current-user')).username)
        courses = db.query(Course).filter(Course.teacher_id == user.user_id).all()
        course_ids: list[int] = []
        for v in courses:
            course_ids.append(v.course_id)

        if status is not None and real_name and course_name:
            user_ids: list[int] = []
            course_ids: list[int] = []
            course = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
            users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name))).all()
            for item in users:
                user_ids.append(item.user_id)
            for item in course:
                course_ids.append(item.course_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                              Choice.user_id.in_(user_ids), Choice.course_id.in_(course_ids),
                                              Choice.is_quit == '0', Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                               Choice.user_id.in_(user_ids), Choice.course_id.in_(course_ids),
                                               Choice.is_quit == '0', Choice.course_id.in_(course_ids)).limit(
                    page_size).offset((current_page - 1) * page_size).all())

        if status is not None and real_name:
            user_ids: list[int] = []
            users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name))).all()
            for item in users:
                user_ids.append(item.user_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                              Choice.user_id.in_(user_ids), Choice.is_quit == '0',
                                              Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                               Choice.user_id.in_(user_ids), Choice.is_quit == '0',
                                               Choice.course_id.in_(course_ids)).limit(page_size).offset(
                    (current_page - 1) * page_size).all())

        if status is not None and course_name:
            course_ids: list[int] = []
            course = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
            for item in course:
                course_ids.append(item.course_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                              Choice.course_id.in_(course_ids), Choice.is_quit == '0',
                                              Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                               Choice.course_id.in_(course_ids), Choice.is_quit == '0',
                                               Choice.course_id.in_(course_ids)).limit(page_size).offset(
                    (current_page - 1) * page_size).all())

        if real_name and course_name:
            user_ids: list[int] = []
            course_ids: list[int] = []
            course = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
            users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name))).all()
            for item in users:
                user_ids.append(item.user_id)
            for item in course:
                course_ids.append(item.course_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.user_id.in_(user_ids),
                                              Choice.status == '0', Choice.course_id.in_(course_ids),
                                              Choice.is_quit == '0', Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.user_id.in_(user_ids),
                                               Choice.status == '0', Choice.course_id.in_(course_ids),
                                               Choice.is_quit == '0', Choice.course_id.in_(course_ids)).limit(
                    page_size).offset((current_page - 1) * page_size).all())

        if status is not None:
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                              Choice.is_quit == '0',
                                              Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.status == status.__str__(),
                                               Choice.is_quit == '0',
                                               Choice.course_id.in_(course_ids)).limit(
                    page_size).offset((current_page - 1) * page_size).all())

        if real_name:
            user_ids: list[int] = []
            users = db.query(User).filter(User.real_name.like('%{0}%'.format(real_name))).all()
            for item in users:
                user_ids.append(item.user_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.user_id.in_(user_ids),
                                              Choice.is_quit == '0', Choice.status == '0',
                                              Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.user_id.in_(user_ids),
                                               Choice.is_quit == '0', Choice.status == '0',
                                               Choice.course_id.in_(course_ids)).limit(
                    page_size).offset((current_page - 1) * page_size).all())

        if course_name:
            course_ids: list[int] = []
            course = db.query(Course).filter(Course.course_name.like('%{0}%'.format(course_name))).all()
            for item in course:
                course_ids.append(item.course_id)
            return Page(
                total=db.query(Choice).filter(Choice.is_delete == '0', Choice.course_id.in_(course_ids),
                                              Choice.is_quit == '0', Choice.status == '0',
                                              Choice.course_id.in_(course_ids)).count(),
                record=db.query(Choice).filter(Choice.is_delete == '0', Choice.course_id.in_(course_ids),
                                               Choice.is_quit == '0', Choice.status == '0',
                                               Choice.course_id.in_(course_ids)).limit(
                    page_size).offset((current_page - 1) * page_size).all())
        # 默认查询
        return Page(total=db.query(Choice).filter(Choice.is_delete == '0', Choice.is_quit == '0', Choice.status == '0',
                                                  Choice.course_id.in_(course_ids)).count(),
                    record=db.query(Choice).filter(Choice.is_delete == '0', Choice.is_quit == '0', Choice.status == '0',
                                                   Choice.course_id.in_(course_ids)).limit(page_size).offset(
                        (current_page - 1) * page_size).all())


def insert_choice(data: ChoiceDto):
    """
    新增学院
    :param data: 选课信息
    """
    db.add(Choice(user_id=data.user_id, course_id=data.course_id))
    db.commit()


def delete_choice_by_id(id: int):
    """
    通过学院ID逻辑删除选课信息
    :param id: 选课ID
    :return:
    """
    item: Choice = db.query(Choice).filter(Choice.choice_id == id).first()
    item.is_delete = '1'
    db.commit()


def update_choice_by_id(data: ChoiceDto):
    """
    通过选课ID修改信息
    :param data: 选课信息
    :return:
    """
    item: Choice = db.query(Choice).filter(Choice.choice_id == data.choice_id).first()
    item.status = data.status.__str__()
    item.score = data.score
    item.description = data.description
    item.is_quit = '1' if data.is_quit else '0'
    item.is_delete = '1' if data.is_delete else '0'
    db.commit()


def update_choice_quit(user_id: int, course_id: int):
    """
    学生退选
    :param user_id: 用户ID
    :param course_id: 选课ID
    """
    choice: Choice = db.query(Choice).filter(Choice.course_id == course_id, Choice.user_id == user_id).first()
    if choice:
        choice.is_quit = '1'
        db.commit()
    else:
        raise UpdateException(message='记录不存在', code=400)


def update_choice_batch_by_id(data: UpdateBatchChoiceDto):
    """
    批量同意/拒绝
    :param data: 数据
    """
    for id in data.choice_ids:
        item: Choice = db.query(Choice).filter(Choice.choice_id == id).first()
        if item:
            item.status = '1' if data.operate else '2'
            db.commit()
        else:
            raise UpdateException(message='记录不存在', code=400)
