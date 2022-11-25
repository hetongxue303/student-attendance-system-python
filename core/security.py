"""
安全性
@Author:何同学
"""
from datetime import timedelta, datetime

from fastapi import Depends, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt, ExpiredSignatureError, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from core.config import settings
from database.mysql import get_db
from exception.custom import UserNotFoundException, UserPasswordException, SecurityScopeException, JwtVerifyException
from models.account import Account
from schemas.token import TokenData

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oAuth2 = OAuth2PasswordBearer(tokenUrl='/api/v1/login',
                              scopes={'admin': '管理员', 'teacher': '教师', 'student': '学生'})


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


def get_user(username: str, db: Session = next(get_db())):
    """
    查询用户
    :param username: 用户名
    :param db: 数据库
    :return: 账户信息
    """
    return db.query(Account).filter(Account.username == username).first()


def authenticate(username: str, password: str):
    """
    登录认证
    :param username: 用户名
    :param password: 密码
    :return: 账户信息
    """
    user = get_user(username)
    if not user:
        raise UserNotFoundException()
    if not verify_password(password, user.password):
        raise UserPasswordException()
    if user.status is '0':
        raise SecurityScopeException(code=403, message='当前用户未激活')
    return user


def generate_token(data: dict, expires_time: int | None = None):
    """
    生成Token
    :param data:
    :param expires_time:
    :return: token
    """
    if not expires_time:
        expire = datetime.now() + timedelta(milliseconds=15 * 60 * 1000)
    else:
        expire = datetime.now() + timedelta(milliseconds=expires_time)
    data.update({'exp': expire})
    return jwt.encode(claims=data,
                      key=settings.JWT_SECRET_KEY,
                      algorithm=settings.JWT_ALGORITHM)


def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oAuth2)):
    try:
        # if not security_scopes.scopes:
        #     raise SecurityScopeException(message='请选择作用域！', headers={"WWW-Authenticate": 'Bearer '})
        payload = jwt.decode(token=token, key=settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        id = payload.get('id', None)
        username = payload.get('sub', None)
        scopes = payload.get('scopes', None)
        if not payload or id is None or username is None or scopes is None:
            raise JwtVerifyException(message='无效凭证')
        token_data = TokenData(username=username, scopes=scopes)
        user = get_user(token_data.username)
        for scope in security_scopes.scopes:
            if scope not in security_scopes.scopes:
                raise SecurityScopeException(code=403, message='没有访问权限', headers={"WWW-Authenticate": 'Bearer '})
        return user
    except ExpiredSignatureError:
        raise JwtVerifyException('凭证过期')
    except JWTError:
        raise JwtVerifyException('凭证解析失败')
