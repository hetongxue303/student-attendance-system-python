"""
路由配置
@Author:何同学
"""
from fastapi import APIRouter, FastAPI
from api.v1 import security, college, major, role, menu, user, test, course, choice
from core.config import settings

router = APIRouter(prefix='/v1')

router.include_router(test.router, tags=['测试模块'])
router.include_router(security.router, tags=['安全模块'])
router.include_router(role.router, tags=['角色模块'], prefix='/role')
router.include_router(choice.router, tags=['选课模块'], prefix='/choice')
router.include_router(course.router, tags=['课程模块'], prefix='/course')
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
