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
        'username': 'teacher1',
        'password': '$2b$12$q0OSa5wwpo1xkUfRCx2DZuPqWt04CQ.CNR.lV6oGqnpVmww2055Py',
        'real_name': '王大唛',
        'nick_name': '王老师',
        'gender': '2',
        'email': 'yhe.cq@qq.com',
        'phone': '15658594785',
        'avatar': 'https://profile.csdnimg.cn/6/A/B/0_qq_14818715',
        'role': '1',
        'is_admin': '0',
        'is_enable': '1'
    },
    {
        'username': 'student1',
        'password': '$2b$12$q0OSa5wwpo1xkUfRCx2DZuPqWt04CQ.CNR.lV6oGqnpVmww2055Py',
        'real_name': '周武瞬',
        'nick_name': '周学生',
        'gender': '1',
        'email': 'yhe.cq@qq.com',
        'phone': '15658594785',
        'avatar': 'https://profile.csdnimg.cn/6/A/B/0_qq_14818715',
        'role': '3',
        'is_admin': '0',
        'is_enable': '1'
    },
    {
        'username': 'teacher2',
        'password': '$2b$12$q0OSa5wwpo1xkUfRCx2DZuPqWt04CQ.CNR.lV6oGqnpVmww2055Py',
        'real_name': '臧瞬馨',
        'nick_name': '臧老师',
        'gender': '2',
        'email': 'yhe.cq@qq.com',
        'phone': '15658594785',
        'avatar': 'https://profile.csdnimg.cn/6/A/B/0_qq_14818715',
        'role': '2',
        'is_admin': '0',
        'is_enable': '1'
    },
    {
        'username': 'student2',
        'password': '$2b$12$q0OSa5wwpo1xkUfRCx2DZuPqWt04CQ.CNR.lV6oGqnpVmww2055Py',
        'real_name': '张鑫敏',
        'nick_name': '张学生',
        'gender': '2',
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
    {'user_id': 3, 'role_id': 3},
    {'user_id': 4, 'role_id': 2},
    {'user_id': 5, 'role_id': 3}
]

course_data = [
    {'teacher_id': 2, 'course_name': '物联网工程', 'count': 45, 'choice': 0, 'class_time': 4},
    {'teacher_id': 2, 'course_name': 'JAVA实践', 'count': 55, 'choice': 0, 'class_time': 16},
    {'teacher_id': 2, 'course_name': '算法结构', 'count': 30, 'choice': 0, 'class_time': 8},
    {'teacher_id': 2, 'course_name': '数据库设计', 'count': 40, 'choice': 0, 'class_time': 6},
    {'teacher_id': 4, 'course_name': '美术设计', 'count': 20, 'choice': 0, 'class_time': 12},
    {'teacher_id': 4, 'course_name': '美术基础', 'count': 50, 'choice': 0, 'class_time': 16},
    {'teacher_id': 4, 'course_name': '素描理论', 'count': 30, 'choice': 0, 'class_time': 4}
]

menu_data = [
    {
        'menu_name': 'dashboard',
        'path': '/dashboard',
        'component': 'dashboard/index.vue',
        'redirect': '',
        'icon': 'index',
        'is_sub': '0',
        'menu_title': '仪表盘',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 1,
        'per_key': '*',
        'is_show': '1'
    },
    {
        'menu_name': 'sign-in',
        'path': '/sign-in',
        'component': 'sign-in/index.vue',
        'redirect': '',
        'icon': 'user',
        'is_sub': '0',
        'menu_title': '学生签到',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 2,
        'per_key': 'student:sign-in',
        'is_show': '1'
    },
    {
        'menu_name': 'my-course',
        'path': '/my-course',
        'component': 'my-course/index.vue',
        'redirect': '',
        'icon': 'user',
        'is_sub': '0',
        'menu_title': '我的课程',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 3,
        'per_key': 'student:course',
        'is_show': '1'
    },
    {
        'menu_name': 'choice-list',
        'path': '/choice-list',
        'component': 'choice-list/index.vue',
        'redirect': '',
        'icon': 'user',
        'is_sub': '0',
        'menu_title': '选课列表',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 4,
        'per_key': 'student:course-list',
        'is_show': '1'
    },
    {
        'menu_name': 'create-attendance',
        'path': '/create-attendance',
        'component': 'create-attendance/index.vue',
        'redirect': '',
        'icon': 'course',
        'is_sub': '0',
        'menu_title': '发布签到',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 5,
        'per_key': 'teacher:create-attendance',
        'is_show': '1'
    },
    {
        'menu_name': 'application-list',
        'path': '/application-list',
        'component': 'application-list/index.vue',
        'redirect': '',
        'icon': 'user',
        'is_sub': '0',
        'menu_title': '申请列表',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 6,
        'per_key': 'teacher:application-list',
        'is_show': '1'
    },
    {
        'menu_name': 'course-list',
        'path': '/course-list',
        'component': 'course/index.vue',
        'redirect': '',
        'icon': 'course',
        'is_sub': '0',
        'menu_title': '课程列表',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 7,
        'per_key': 'teacher:course-list',
        'is_show': '1'
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
        'sort': 8,
        'per_key': '',
        'is_show': '1'
    },
    {
        'menu_name': 'college-list',
        'path': '/educational/college-list',
        'component': 'educational/college/index.vue',
        'redirect': '',
        'icon': 'college',
        'is_sub': '0',
        'menu_title': '学院列表',
        'menu_type': '2',
        'parent_id': 8,
        'sort': 9,
        'per_key': 'college:list',
        'is_show': '1'
    },
    {
        'menu_name': 'major-list',
        'path': '/educational/major-list',
        'component': 'educational/major/index.vue',
        'redirect': '',
        'icon': 'major',
        'is_sub': '0',
        'menu_title': '专业列表',
        'menu_type': '2',
        'parent_id': 8,
        'sort': 10,
        'per_key': 'major:list',
        'is_show': '1'
    },
    {
        'menu_name': 'system',
        'path': '/system',
        'component': 'Layout',
        'redirect': '',
        'icon': 'system',
        'is_sub': '1',
        'menu_title': '系统管理',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 11,
        'per_key': '',
        'is_show': '1'
    },
    {
        'menu_name': 'user',
        'path': '/system/user',
        'component': 'system/user/index.vue',
        'redirect': '',
        'icon': 'user',
        'is_sub': '0',
        'menu_title': '用户管理',
        'menu_type': '2',
        'parent_id': 11,
        'sort': 12,
        'per_key': 'system:user:list',
        'is_show': '1'
    },
    {
        'menu_name': 'role',
        'path': '/system/role',
        'component': 'system/role/index.vue',
        'redirect': '',
        'icon': 'role',
        'is_sub': '0',
        'menu_title': '角色管理',
        'menu_type': '2',
        'parent_id': 11,
        'sort': 13,
        'per_key': 'system:role:list',
        'is_show': '1'
    },
    {
        'menu_name': 'menu',
        'path': '/system/menu',
        'component': 'system/menu/index.vue',
        'redirect': '',
        'icon': 'menu',
        'is_sub': '0',
        'menu_title': '菜单管理',
        'menu_type': '2',
        'parent_id': 11,
        'sort': 14,
        'per_key': 'system:menu:list',
        'is_show': '1'
    },
    {
        'menu_name': 'about',
        'path': '/about',
        'component': 'about/index.vue',
        'redirect': '',
        'icon': 'about',
        'is_sub': '0',
        'menu_title': '关于系统',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 15,
        'per_key': '',
        'is_show': '1'
    },
    {
        'menu_name': 'center',
        'path': '/user/center',
        'component': 'center/index.vue',
        'redirect': '',
        'icon': 'center',
        'is_sub': '0',
        'menu_title': '个人中心',
        'menu_type': '1',
        'parent_id': 0,
        'sort': 16,
        'per_key': '',
        'is_show': '0'
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

    {'role_id': 2, 'menu_id': 1},
    {'role_id': 2, 'menu_id': 5},
    {'role_id': 2, 'menu_id': 6},
    {'role_id': 2, 'menu_id': 7},
    {'role_id': 2, 'menu_id': 8},
    {'role_id': 2, 'menu_id': 9},
    {'role_id': 2, 'menu_id': 10},
    {'role_id': 2, 'menu_id': 15},
    {'role_id': 2, 'menu_id': 16},

    {'role_id': 3, 'menu_id': 1},
    {'role_id': 3, 'menu_id': 2},
    {'role_id': 3, 'menu_id': 3},
    {'role_id': 3, 'menu_id': 4},
    {'role_id': 3, 'menu_id': 8},
    {'role_id': 3, 'menu_id': 9},
    {'role_id': 3, 'menu_id': 15},
    {'role_id': 3, 'menu_id': 16}
]
