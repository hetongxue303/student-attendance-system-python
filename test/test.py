"""
测试
@Author:何同学
"""
from sqlalchemy.orm import Session

from database.mysql import get_db
from models import User, College, Menu, Role


def test(db: Session = next(get_db())):
    # 使用sql
    account = db.execute('select * from account')
    for a in account:
        print(a)
    print('############################################')
    # 一对一
    user = db.execute('select * from user').first()
    print(user)
    print('############################################')
    user2 = db.query(User).filter(User.user_id == 2).first()
    print(user2.nick_name)
    print(user2.role.role_name)
    print(user2.college.name)
    print(user2.major.name)
    print('############################################')
    college = db.query(College).first()
    print(college.name)
    print(college.user)
    print('############################################')
    menus = db.query(Menu).first()
    # menus = db.execute('select * from menu')
    for role in menus.role:
        print(role.role_name)
    print('############################################')
    menusa = db.query(Role).filter(Role.role_id == 1).all()
    for menu in menusa:
        for a in menu.menu:
            print(a.menu_id)
    print('############################################')
    aa = db.query(User, College).join(User, User.college_id == College.college_id).all()
    for a in aa:
        for i in a:
            print(i)


if __name__ == '__main__':
    test()
