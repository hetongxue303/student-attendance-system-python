"""
初始化数据
@Author:何同学
"""
account_data = [
    {'username': 'admin', 'password': '$2b$12$I5lfn4eO8M0oH4yYQWjSQ.t4VJz9cGKXA.ht6syIG6tAXmbnQywqa'},
    {'username': 'teacher', 'password': '$2b$12$I5lfn4eO8M0oH4yYQWjSQ.t4VJz9cGKXA.ht6syIG6tAXmbnQywqa'},
    {'username': 'student', 'password': '$2b$12$I5lfn4eO8M0oH4yYQWjSQ.t4VJz9cGKXA.ht6syIG6tAXmbnQywqa'}
]

major_data = [
    {'name': '信息工程'},
    {'name': '物联网工程'},
    {'name': '电子信息工程'},
    {'name': '电子工程与管理'}
]

college_data = [
    {'name': '通信与信息工程学院'},
    {'name': '智能工程学院'},
    {'name': '大数据与计算机科学学院'},
    {'name': '艺术传媒学院'},
    {'name': '外国语学院'},
    {'name': '数字经济学院'},
    {'name': '信息管理学院'},
    {'name': '国际商务学院'}
]

role_data = [
    {'role_name': '超级管理员', 'role_key': 'admin'},
    {'role_name': '教师', 'role_key': 'teacher'},
    {'role_name': '学生', 'role_key': 'student'}
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
    }
]

account_role_data = [
    {'account_id': 1, 'role_id': 1},
    {'account_id': 2, 'role_id': 2},
    {'account_id': 3, 'role_id': 3}
]

account_user_data = [
    {'account_id': 1, 'user_id': 1},
    {'account_id': 2, 'user_id': 2},
    {'account_id': 3, 'user_id': 3}
]

user_data = [
    {
        'college_id': None,
        'major_id': 1,
        'role_id': 1,
        'user_no': 1,
        'nick_name': '何同学',
        'real_name': 'hy',
        'gender': '1',
        'email': 'yhe.cq@qq.com',
        'phone': '15658594785',
        'avatar': 'https://profile.csdnimg.cn/6/A/B/0_qq_14818715'
    },
    {
        'college_id': 1,
        'major_id': 1,
        'role_id': 2,
        'user_no': 10112,
        'nick_name': '周雄',
        'real_name': 'zx',
        'gender': '1',
        'email': 'zhongxiong.cq@qq.com',
        'phone': '15444585965',
        'avatar': ''
    },
    {
        'college_id': 3,
        'major_id': 1,
        'role_id': 3,
        'user_no': 2021230522,
        'nick_name': '王丽',
        'real_name': 'wl',
        'gender': '2',
        'email': '154865q.com',
        'phone': '1544585658',
        'avatar': ''
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
