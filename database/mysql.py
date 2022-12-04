"""
mysql配置
@Author:何同学
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.data import account_data, major_data, college_data, role_data, menu_data, account_role_data, \
    account_user_data, user_data, role_menu_data
from core.logger import logger
from core.config import settings
from models import Account, Major, College, Role, Menu, Account_Role, Base, Account_User, User, Role_Menu

# 创建引擎
engine = create_engine(
    url=settings.DATABASE_URI,  # MySQL URI
    echo=settings.DATABASE_ECHO,  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)
    pool_pre_ping=True,
    pool_recycle=3600
)

# 操作数据库会话
localSession = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False  # 防止提交后属性过期
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
        engine.execute(Account.__table__.insert(), [account for account in account_data])
        engine.execute(Major.__table__.insert(), [major for major in major_data])
        engine.execute(College.__table__.insert(), [college for college in college_data])
        engine.execute(Role.__table__.insert(), [role for role in role_data])
        engine.execute(Menu.__table__.insert(), [menu for menu in menu_data])
        engine.execute(User.__table__.insert(), [user for user in user_data])
        engine.execute(Account_Role.__table__.insert(), [account_role for account_role in account_role_data])
        engine.execute(Account_User.__table__.insert(), [account_user for account_user in account_user_data])
        engine.execute(Role_Menu.__table__.insert(), [role_menu for role_menu in role_menu_data])
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
