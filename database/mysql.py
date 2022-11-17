"""
mysql配置
@Author:何同学
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.data import accountData
from models import Base, Account
from core.logger import logger
from core.config import settings

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
    db = localSession()
    try:
        yield db
    except Exception as e:
        logger.error(f'获取数据库失败 -- 失败信息如下:\n{e}')
    finally:
        db.close()


def get_session():
    """ 获取session会话 """
    return localSession()


def init_db():
    """ 初始化表结构 """
    try:
        Base.metadata.create_all(engine)
        logger.success('表结构创建成功!!!')
    except Exception as e:
        logger.error(f'表结构创建失败 -- 错误信息如下:\n{e}')
    finally:
        engine.dispose()


def drop_db():
    """ 删除所有表 """
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
        engine.execute(Account.__table__.insert(), [account for account in accountData])
        logger.success('初始化表数据成功!!!')
    except Exception as e:
        logger.error(f'初始化表数据失败 -- 错误信息如下:\n{e}')
    finally:
        engine.dispose()
