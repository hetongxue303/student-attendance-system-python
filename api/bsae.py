"""
路由配置
@Author:何同学
"""
from fastapi import APIRouter, Security, FastAPI
from api.v1 import auth, college, major, role, menu, user, account, test
from core.config import settings
from core.security import get_current_user

router = APIRouter(prefix='/v1')

router.include_router(test.router, tags=['测试模块'])
router.include_router(auth.router, tags=['安全模块'])
router.include_router(account.router, tags=['账户模块'], prefix='/account', dependencies=[Security(get_current_user)])
router.include_router(role.router, tags=['角色模块'], prefix='/role', dependencies=[Security(get_current_user)])
router.include_router(menu.router, tags=['菜单模块'], prefix='/menu', dependencies=[Security(get_current_user)])
router.include_router(user.router, tags=['用户模块'], prefix='/user', dependencies=[Security(get_current_user)])
router.include_router(college.router, tags=['学院模块'], prefix='/college', dependencies=[Security(get_current_user)])
router.include_router(major.router, tags=['专业模块'], prefix='/major', dependencies=[Security(get_current_user)])


def init_router(app: FastAPI):
    """
    注册路由
    :param app:
    :return:
    """
    app.include_router(router, prefix=settings.APP_API_PREFIX)
