"""
安全性
@Author:何同学
"""
from datetime import timedelta, datetime
from fastapi import Request
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from schemas.token import Token
from core.config import settings
from database.mysql import get_db
from models import Account

ALGORITHM = settings.JWT_ALGORITHM
SECRET = settings.JWT_SECRET_KEY
ACCESS_EXPIRE_TIME = settings.JWT_EXPIRE

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    """
    密码校验
    :param plain_password: 原密码
    :param hashed_password: 加密后的密码
    :return: 对比结果(Bool)
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    密码加密
    :param password: 原密码
    :return: 加密后的密码
    """
    return pwd_context.hash(password)


def get_account(username: str, db: Session = next(get_db())):
    """
    查询账户
    :param username: 用户名
    :param db: 数据库
    :return: 账户信息
    """
    return db.query(Account).filter(Account.username == username).first()


def authenticate(username: str, password: str):
    """
    登录认证
    :param username: 用户名
    :param password: 用户密码
    :return: Token信息
    """
    account = get_account(username)
    if not account:
        return False
    if not verify_password(password, account.password):
        return False
    print(ACCESS_EXPIRE_TIME)
    return Token(token=generate_token(account, ACCESS_EXPIRE_TIME), expired_time=ACCESS_EXPIRE_TIME)


def generate_token(data: Account, expires_time: timedelta):
    """
    生成Token
    :param data: 账户信息
    :param expires_time: 过期时间
    :return: Token信息
    """
    return jwt.encode({'id': data.account_id, 'sub': data.username, 'exp': datetime.now() + expires_time}, SECRET,
                      algorithm=ALGORITHM)


def verify_token(request: Request):
    """
    校验Token
    :param request: 请求体
    :return: 校验结果(Bool)
    """
    payload = jwt.decode(request.headers.get(settings.JWT_SAVE_KEY), SECRET, algorithms=[ALGORITHM])
    if not payload:
        return False
    return payload


def get_current_user(request: Request):
    """
    获取当前用户
    :param request: 请求体
    :return: 当前登录用户
    """
    try:
        payload = verify_token(request)
        if not payload:
            return False
        username = payload.get('sub')
        if not username:
            return False
        return get_account(username)
    except ExpiredSignatureError:
        print('token过期...')
        return False
    except JWTError:
        print('验证失败...')
        return False
