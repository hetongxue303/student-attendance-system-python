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
        'nick_name': '管理员啦',
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
        'real_name': '王大唛',
        'nick_name': '教师啦',
        'gender': '2',
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
        'real_name': '周武瞬',
        'nick_name': '学生啦',
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
    {'teacher_id': 2, 'course_name': '物联网工程', 'count': 45, 'choice': 0, 'class_time': 4},
    {'teacher_id': 2, 'course_name': 'JAVA实践', 'count': 55, 'choice': 0, 'class_time': 16},
    {'teacher_id': 2, 'course_name': '算法结构', 'count': 30, 'choice': 0, 'class_time': 8},
    {'teacher_id': 2, 'course_name': '数据库设计', 'count': 40, 'choice': 0, 'class_time': 6}
]

menu_data = [
    {
        'menu_name': 'school',
        'path': '/school',
        'component': 'Layout',
        'redirect': '',
        'icon': 'school',
        'is_sub': '1',
        'menu_title': '学校管理',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 1,
        'per_key': ''
    },
    {
        'menu_name': 'college',
        'path': '/school/college',
        'component': '/school/college/index.vue',
        'redirect': '',
        'icon': 'college',
        'is_sub': '0',
        'menu_title': '学院管理',
        'menu_type': '2',
        'parent_id': 1,
        'sort': 2,
        'per_key': 'college:list'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '新增学院',
        'menu_type': '3',
        'parent_id': 2,
        'sort': 3,
        'per_key': 'college:insert',
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '删除学院',
        'menu_type': '3',
        'parent_id': 2,
        'sort': 4,
        'per_key': 'college:delete'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '更新学院',
        'menu_type': '3',
        'parent_id': 2,
        'sort': 5,
        'per_key': 'college:update'
    },
    {
        'menu_name': 'major',
        'path': '/school/major',
        'component': '/school/major/index.vue',
        'redirect': '',
        'icon': 'major',
        'is_sub': '0',
        'menu_title': '专业管理',
        'menu_type': '2',
        'parent_id': 1,
        'sort': 6,
        'per_key': 'major:list'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '新增专业',
        'menu_type': '3',
        'parent_id': 6,
        'sort': 7,
        'per_key': 'major:insert',
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '删除专业',
        'menu_type': '3',
        'parent_id': 6,
        'sort': 8,
        'per_key': 'major:delete'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '更新专业',
        'menu_type': '3',
        'parent_id': 6,
        'sort': 9,
        'per_key': 'major:update'
    },
    {
        'menu_name': 'educational',
        'path': '/educational',
        'component': 'Layout',
        'redirect': '',
        'icon': 'user',
        'is_sub': '1',
        'menu_title': '教务管理',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 10,
        'per_key': ''
    },
    {
        'menu_name': 'college',
        'path': '/educational/course',
        'component': '/educational/course/index.vue',
        'redirect': '',
        'icon': 'course',
        'is_sub': '0',
        'menu_title': '课程管理',
        'menu_type': '2',
        'parent_id': 10,
        'sort': 11,
        'per_key': 'course:list'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '新增课程',
        'menu_type': '3',
        'parent_id': 11,
        'sort': 12,
        'per_key': 'course:insert',
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '删除课程',
        'menu_type': '3',
        'parent_id': 11,
        'sort': 13,
        'per_key': 'course:delete'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '更新课程',
        'menu_type': '3',
        'parent_id': 11,
        'sort': 14,
        'per_key': 'course:update'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '选择课程',
        'menu_type': '3',
        'parent_id': 11,
        'sort': 15,
        'per_key': 'course:choice'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '退选课程',
        'menu_type': '3',
        'parent_id': 11,
        'sort': 16,
        'per_key': 'course:quit'
    },
    {
        'menu_name': 'choice',
        'path': '/educational/choice',
        'component': '/educational/choice/index.vue',
        'redirect': '',
        'icon': 'choice',
        'is_sub': '0',
        'menu_title': '选课记录',
        'menu_type': '2',
        'parent_id': 10,
        'sort': 17,
        'per_key': 'choice:list'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '查看记录',
        'menu_type': '3',
        'parent_id': 17,
        'sort': 18,
        'per_key': 'choice:look',
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '删除记录',
        'menu_type': '3',
        'parent_id': 17,
        'sort': 19,
        'per_key': 'choice:delete'
    },
    {
        'menu_name': '',
        'path': '',
        'component': '',
        'redirect': '',
        'icon': '',
        'is_sub': '0',
        'menu_title': '选课操作',
        'menu_type': '3',
        'parent_id': 17,
        'sort': 20,
        'per_key': 'course:operate'
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
    {'role_id': 1, 'menu_id': 13},
    {'role_id': 1, 'menu_id': 14},
    {'role_id': 1, 'menu_id': 15},
    {'role_id': 1, 'menu_id': 16},
    {'role_id': 1, 'menu_id': 17},
    {'role_id': 1, 'menu_id': 18},
    {'role_id': 1, 'menu_id': 19},
    {'role_id': 1, 'menu_id': 20},

    {'role_id': 2, 'menu_id': 1},
    {'role_id': 2, 'menu_id': 2},
    {'role_id': 2, 'menu_id': 6},
    {'role_id': 2, 'menu_id': 10},
    {'role_id': 2, 'menu_id': 11},
    {'role_id': 2, 'menu_id': 12},
    {'role_id': 2, 'menu_id': 13},

    {'role_id': 3, 'menu_id': 1},
    {'role_id': 3, 'menu_id': 2},
    {'role_id': 3, 'menu_id': 6},
    {'role_id': 3, 'menu_id': 10},
    {'role_id': 3, 'menu_id': 11},
    {'role_id': 3, 'menu_id': 15},
    {'role_id': 3, 'menu_id': 16}
]
