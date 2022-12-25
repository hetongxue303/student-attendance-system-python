"""
初始化数据
@Author:何同学
"""
college_data = [
    {'college_name': '通信与信息工程学院'},
    {'college_name': '智能工程学院'},
    {'college_name': '大数据与计算机科学学院'},
    {'college_name': '艺术传媒学院'},
    {'college_name': '外国语学院'},
    {'college_name': '数字经济学院'},
    {'college_name': '信息管理学院'},
    {'college_name': '国际商务学院'}
]

major_data = [
    {'major_name': '信息工程'},
    {'major_name': '物联网工程'},
    {'major_name': '电子信息工程'},
    {'major_name': '电子工程与管理'}
]

user_data = [
    {
        'username': 'admin',
        'password': '$2b$12$q0OSa5wwpo1xkUfRCx2DZuPqWt04CQ.CNR.lV6oGqnpVmww2055Py',
        'real_name': '管理员',
        'gender': '1',
        'email': 'yhe.cq@qq.com',
        'phone': '15658594785',
        'avatar': 'https://profile.csdnimg.cn/6/A/B/0_qq_14818715',
        'role': '1',
        'is_admin': '1',
        'is_enable': '1'
    },
    {
        'username': 'teacher',
        'password': '$2b$12$q0OSa5wwpo1xkUfRCx2DZuPqWt04CQ.CNR.lV6oGqnpVmww2055Py',
        'real_name': '教师',
        'gender': '1',
        'email': 'yhe.cq@qq.com',
        'phone': '15658594785',
        'avatar': 'https://profile.csdnimg.cn/6/A/B/0_qq_14818715',
        'role': '2',
        'is_admin': '0',
        'is_enable': '1'
    },
    {
        'username': 'student',
        'password': '$2b$12$q0OSa5wwpo1xkUfRCx2DZuPqWt04CQ.CNR.lV6oGqnpVmww2055Py',
        'real_name': '学生',
        'gender': '1',
        'email': 'yhe.cq@qq.com',
        'phone': '15658594785',
        'avatar': 'https://profile.csdnimg.cn/6/A/B/0_qq_14818715',
        'role': '3',
        'is_admin': '0',
        'is_enable': '1'
    }
]

role_data = [
    {'role_name': '超级管理员', 'role_key': 'admin', 'is_enable': '1'},
    {'role_name': '教师', 'role_key': 'teacher', 'is_enable': '1'},
    {'role_name': '学生', 'role_key': 'student', 'is_enable': '1'}
]

user_role_data = [
    {'user_id': 1, 'role_id': 1},
    {'user_id': 2, 'role_id': 2},
    {'user_id': 3, 'role_id': 3}
]

course_data = [
    {'teacher_id': 2, 'course_name': '物联网工程', 'count': 45, 'choice': 0},
    {'teacher_id': 2, 'course_name': 'JAVA实践', 'count': 55, 'choice': 0},
    {'teacher_id': 2, 'course_name': '算法结构', 'count': 30, 'choice': 0},
    {'teacher_id': 2, 'course_name': '数据库设计', 'count': 40, 'choice': 0}
]

menu_data = [
    {
        'menu_name': 'user',
        'menu_title': '用户管理',
        'menu_type': '0',
        'parent_id': 0,
        'path': '/user',
        'component': 'Layout',
        'sort': 1,
        'icon': 'user',
        'per_key': None
    },
    {
        'menu_name': 'admin',
        'menu_title': '管理员',
        'menu_type': '1',
        'parent_id': 1,
        'path': '/user/admin',
        'component': '/user/admin/Index.vue',
        'sort': 2,
        'icon': 'admin',
        'per_key': 'user:admin:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增管理员',
        'menu_type': '1',
        'parent_id': 2,
        'path': None,
        'component': None,
        'sort': 3,
        'icon': None,
        'per_key': 'user:admin:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除管理员',
        'menu_type': '1',
        'parent_id': 2,
        'path': None,
        'component': None,
        'sort': 4,
        'icon': None,
        'per_key': 'user:admin:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新管理员',
        'menu_type': '1',
        'parent_id': 2,
        'path': None,
        'component': None,
        'sort': 5,
        'icon': None,
        'per_key': 'user:admin:update'
    },
    {
        'menu_name': 'teacher',
        'menu_title': '教师管理',
        'menu_type': '1',
        'parent_id': 1,
        'path': '/user/teacher',
        'component': '/user/teacher/Index.vue',
        'sort': 6,
        'icon': 'teacher',
        'per_key': 'user:teacher:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增教师',
        'menu_type': '2',
        'parent_id': 6,
        'path': None,
        'component': None,
        'sort': 7,
        'icon': None,
        'per_key': 'user:teacher:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除教师',
        'menu_type': '2',
        'parent_id': 6,
        'path': None,
        'component': None,
        'sort': 8,
        'icon': None,
        'per_key': 'user:teacher:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新教师',
        'menu_type': '2',
        'parent_id': 6,
        'path': None,
        'component': None,
        'sort': 9,
        'icon': None,
        'per_key': 'user:teacher:update'
    },
    {
        'menu_name': 'student',
        'menu_title': '学生管理',
        'menu_type': '1',
        'parent_id': 1,
        'path': '/user/teacher',
        'component': '/user/student/Index.vue',
        'sort': 10,
        'icon': 'student',
        'per_key': 'user:student:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增学生',
        'menu_type': '2',
        'parent_id': 6,
        'path': None,
        'component': None,
        'sort': 11,
        'icon': None,
        'per_key': 'user:student:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除学生',
        'menu_type': '2',
        'parent_id': 6,
        'path': None,
        'component': None,
        'sort': 12,
        'icon': None,
        'per_key': 'user:student:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新学生',
        'menu_type': '2',
        'parent_id': 6,
        'path': None,
        'component': None,
        'sort': 13,
        'icon': None,
        'per_key': 'user:student:update'
    },
    {
        'menu_name': 'school',
        'menu_title': '学校管理',
        'menu_type': '0',
        'parent_id': 0,
        'path': '/school',
        'component': 'Layout',
        'sort': 14,
        'icon': 'school',
        'per_key': None
    },
    {
        'menu_name': 'college',
        'menu_title': '学院管理',
        'menu_type': '1',
        'parent_id': 14,
        'path': '/school/college',
        'component': '/school/college/Index.vue',
        'sort': 15,
        'icon': 'college',
        'per_key': 'school:college:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增学院',
        'menu_type': '2',
        'parent_id': 15,
        'path': None,
        'component': None,
        'sort': 16,
        'icon': None,
        'per_key': 'school:college:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除学院',
        'menu_type': '2',
        'parent_id': 15,
        'path': None,
        'component': None,
        'sort': 17,
        'icon': None,
        'per_key': 'school:college:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新学院',
        'menu_type': '2',
        'parent_id': 15,
        'path': None,
        'component': None,
        'sort': 18,
        'icon': None,
        'per_key': 'school:college:update'
    },
    {
        'menu_name': 'major',
        'menu_title': '专业管理',
        'menu_type': '1',
        'parent_id': 14,
        'path': '/school/major',
        'component': '/school/major/Index.vue',
        'sort': 19,
        'icon': 'major',
        'per_key': 'user:major:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增专业',
        'menu_type': '2',
        'parent_id': 19,
        'path': None,
        'component': None,
        'sort': 20,
        'icon': None,
        'per_key': 'user:major:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除专业',
        'menu_type': '2',
        'parent_id': 19,
        'path': None,
        'component': None,
        'sort': 21,
        'icon': None,
        'per_key': 'user:major:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新专业',
        'menu_type': '2',
        'parent_id': 19,
        'path': None,
        'component': None,
        'sort': 22,
        'icon': None,
        'per_key': 'user:major:update'
    },
    {
        'menu_name': 'course',
        'menu_title': '课程管理',
        'menu_type': '1',
        'parent_id': 14,
        'path': '/school/course',
        'component': '/school/course/Index.vue',
        'sort': 23,
        'icon': 'course',
        'per_key': 'school:course:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增学生',
        'menu_type': '2',
        'parent_id': 23,
        'path': None,
        'component': None,
        'sort': 24,
        'icon': None,
        'per_key': 'school:course:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除学生',
        'menu_type': '2',
        'parent_id': 23,
        'path': None,
        'component': None,
        'sort': 25,
        'icon': None,
        'per_key': 'school:course:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新学生',
        'menu_type': '2',
        'parent_id': 23,
        'path': None,
        'component': None,
        'sort': 26,
        'icon': None,
        'per_key': 'school:course:update'
    },
    {
        'menu_name': 'selection',
        'menu_title': '选课管理',
        'menu_type': '1',
        'parent_id': 14,
        'path': '/school/selection',
        'component': '/school/selection/Index.vue',
        'sort': 27,
        'icon': 'selection',
        'per_key': 'school:selection:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增选课',
        'menu_type': '2',
        'parent_id': 27,
        'path': None,
        'component': None,
        'sort': 28,
        'icon': None,
        'per_key': 'school:selection:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除选课',
        'menu_type': '2',
        'parent_id': 27,
        'path': None,
        'component': None,
        'sort': 29,
        'icon': None,
        'per_key': 'school:selection:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新选课',
        'menu_type': '2',
        'parent_id': 27,
        'path': None,
        'component': None,
        'sort': 30,
        'icon': None,
        'per_key': 'school:selection:update'
    },
    {
        'menu_name': 'system',
        'menu_title': '系统管理',
        'menu_type': '0',
        'parent_id': 0,
        'path': '/system',
        'component': 'Layout',
        'sort': 31,
        'icon': 'system',
        'per_key': None
    },
    {
        'menu_name': 'account',
        'menu_title': '账户管理',
        'menu_type': '1',
        'parent_id': 31,
        'path': '/system/account',
        'component': '/system/account/Index.vue',
        'sort': 32,
        'icon': 'account',
        'per_key': 'system:account:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增账户',
        'menu_type': '2',
        'parent_id': 32,
        'path': None,
        'component': None,
        'sort': 33,
        'icon': None,
        'per_key': 'system:account:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除账户',
        'menu_type': '2',
        'parent_id': 32,
        'path': None,
        'component': None,
        'sort': 34,
        'icon': None,
        'per_key': 'system:account:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新账户',
        'menu_type': '2',
        'parent_id': 32,
        'path': None,
        'component': None,
        'sort': 35,
        'icon': None,
        'per_key': 'system:account:update'
    },
    {
        'menu_name': 'role',
        'menu_title': '角色管理',
        'menu_type': '1',
        'parent_id': 31,
        'path': '/system/role',
        'component': '/system/role/Index.vue',
        'sort': 36,
        'icon': 'role',
        'per_key': 'system:role:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增角色',
        'menu_type': '2',
        'parent_id': 36,
        'path': None,
        'component': None,
        'sort': 37,
        'icon': None,
        'per_key': 'system:role:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除角色',
        'menu_type': '2',
        'parent_id': 36,
        'path': None,
        'component': None,
        'sort': 38,
        'icon': None,
        'per_key': 'system:role:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新角色',
        'menu_type': '2',
        'parent_id': 36,
        'path': None,
        'component': None,
        'sort': 39,
        'icon': None,
        'per_key': 'system:role:update'
    },
    {
        'menu_name': 'menu',
        'menu_title': '菜单管理',
        'menu_type': '1',
        'parent_id': 31,
        'path': '/system/menu',
        'component': '/system/menu/Index.vue',
        'sort': 40,
        'icon': 'menu',
        'per_key': 'system:menu:list'
    },
    {
        'menu_name': None,
        'menu_title': '新增菜单',
        'menu_type': '2',
        'parent_id': 40,
        'path': None,
        'component': None,
        'sort': 41,
        'icon': None,
        'per_key': 'system:menu:add'
    },
    {
        'menu_name': None,
        'menu_title': '删除菜单',
        'menu_type': '2',
        'parent_id': 40,
        'path': None,
        'component': None,
        'sort': 42,
        'icon': None,
        'per_key': 'system:menu:del'
    },
    {
        'menu_name': None,
        'menu_title': '更新菜单',
        'menu_type': '2',
        'parent_id': 40,
        'path': None,
        'component': None,
        'sort': 43,
        'icon': None,
        'per_key': 'system:menu:update'
    },
    {
        'menu_name': None,
        'menu_title': None,
        'menu_type': '0',
        'parent_id': 0,
        'path': '/',
        'component': 'Layout',
        'sort': 44,
        'icon': None,
        'per_key': None
    },
    {
        'menu_name': 'about',
        'menu_title': '关于系统',
        'menu_type': '2',
        'parent_id': 44,
        'path': '/about',
        'component': None,
        'sort': 45,
        'icon': 'about',
        'per_key': None
    }
]

role_menu_data = [
    {'role_id': 1, 'menu_id': 1},
    {'role_id': 1, 'menu_id': 2},
    {'role_id': 1, 'menu_id': 3},
    {'role_id': 1, 'menu_id': 4},
    {'role_id': 1, 'menu_id': 5},
    {'role_id': 1, 'menu_id': 6},
    {'role_id': 1, 'menu_id': 7},
    {'role_id': 1, 'menu_id': 8},
    {'role_id': 1, 'menu_id': 9},
    {'role_id': 1, 'menu_id': 10},
    {'role_id': 1, 'menu_id': 11},
    {'role_id': 1, 'menu_id': 12},
    {'role_id': 1, 'menu_id': 13}
]
