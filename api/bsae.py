"""
路由配置
@Author:何同学
"""
from fastapi import APIRouter, Security, FastAPI
from api.v1 import auth, college, major, role, menu, user, test
from core.config import settings

router = APIRouter(prefix='/v1')

router.include_router(test.router, tags=['测试模块'])
router.include_router(auth.router, tags=['安全模块'])
# router.include_router(role.router, tags=['角色模块'], prefix='/role', dependencies=[Security(get_current_user)])
router.include_router(role.router, tags=['角色模块'], prefix='/role')
router.include_router(menu.router, tags=['菜单模块'], prefix='/menu')
router.include_router(user.router, tags=['用户模块'], prefix='/user')
router.include_router(college.router, tags=['学院模块'], prefix='/college')
router.include_router(major.router, tags=['专业模块'], prefix='/major')


def init_router(app: FastAPI):
    """
    注册路由
    :param app:
    :return:
    """
    app.include_router(router, prefix=settings.APP_API_PREFIX)
