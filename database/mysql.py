"""
mysql配置
@Author:何同学
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.logger import logger
from database.data import user_data, college_data, major_data, role_data, user_role_data, course_data, menu_data, \
    role_menu_data
from models import User, Base, College, Major, Role, User_Role, Menu, Role_Menu
from models.course import Course

# 创建引擎
engine = create_engine(
    url='mysql+pymysql://root:123456@127.0.0.1:3306/student_attendance_system?charset=utf8',
    # 是否打印数据库日志
    echo=False,
    pool_pre_ping=True,
    pool_recycle=3600,
    # 设置隔离级别：READ COMMITTED | READ UNCOMMITTED | REPEATABLE READ | SERIALIZABLE | AUTOCOMMIT
    isolation_level='READ UNCOMMITTED')

# 操作数据库会话
localSession = sessionmaker(
    bind=engine,
    autoflush=True,
    autocommit=False,
    # 防止提交后属性过期
    expire_on_commit=False
)


def get_db():
    """ 获取数据库 """
    try:
        db = localSession()
        yield db
    except Exception as e:
        logger.error(f'获取数据库失败 -- 失败信息如下:\n{e}')
    finally:
        db.close()


def create_db():
    """ 创建表结构 """
    try:
        Base.metadata.create_all(engine)
        logger.success('表结构创建成功!!!')
    except Exception as e:
        logger.error(f'表结构创建失败 -- 错误信息如下:\n{e}')
    finally:
        engine.dispose()


def drop_db():
    """ 删除表结构 """
    try:
        Base.metadata.drop_all(engine)
        logger.success('表结构删除成功!!!')
    except Exception as e:
        logger.error(f'表结构删除失败 -- 错误信息如下:\n{e}')
    finally:
        engine.dispose()


def init_data():
    """ 初始化表数据 """
    try:
        engine.execute(User.__table__.insert(), [user for user in user_data])
        engine.execute(Role.__table__.insert(), [role for role in role_data])
        engine.execute(User_Role.__table__.insert(), [user_role for user_role in user_role_data])
        engine.execute(Menu.__table__.insert(), [menu for menu in menu_data])
        engine.execute(Role_Menu.__table__.insert(), [role_menu for role_menu in role_menu_data])
        engine.execute(College.__table__.insert(), [college for college in college_data])
        engine.execute(Major.__table__.insert(), [major for major in major_data])
        engine.execute(Course.__table__.insert(), [course for course in course_data])
        logger.success('初始化表数据成功!!!')
    except Exception as e:
        logger.error(f'初始化表数据失败 -- 错误信息如下:\n{e}')
    finally:
        engine.dispose()


def init_db():
    # 删除表和数据
    drop_db()
    # 创建表结构
    create_db()
    # 初始化表数据
    init_data()
