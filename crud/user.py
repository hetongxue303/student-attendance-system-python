"""
用户业务
@Author:何同学
"""
from sqlalchemy.orm import Session

from database.mysql import get_db
from models import User


def query_by_username(username: str, db: Session = next(get_db())):
    return db.query(User).filter(User.username == username).first()
