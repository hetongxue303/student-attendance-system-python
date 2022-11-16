"""
路由配置
@Author:何同学
"""
from fastapi import APIRouter
from api.v1 import login, college, major, role, menu, user, account

router = APIRouter(prefix='/v1')

router.include_router(login.router, tags=['登录模块'])
router.include_router(account.router, tags=['账户模块'], prefix='/account')
router.include_router(role.router, tags=['角色模块'], prefix='/role')
router.include_router(menu.router, tags=['菜单模块'], prefix='/menu')
router.include_router(user.router, tags=['用户模块'], prefix='/user')
router.include_router(college.router, tags=['学院模块'], prefix='/college')
router.include_router(major.router, tags=['专业模块'], prefix='/major')
