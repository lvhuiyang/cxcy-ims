from app import db


class CreateProject(db.Model):
    """
    项目立项情况统计:
    序号,学院,项目编号,项目名称,项目类型,项目级别
    立项年份,项目负责人姓名,项目负责人学号,项目负责人电话,项目负责人QQ,专业班级
    参与学生人数	,项目其他成员姓名、电话、学号,指导教师姓名,指导教师职称,项目所属一级学科,项目简介
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    stu_academy = db.Column(db.String(64))  # 学生所在学院
    c_project_number = db.Column(db.String(64))  # 项目编号
    c_project_name = db.Column(db.String(64))  # 项目名称
    c_project_category = db.Column(db.String(64))  # 项目类型
    c_project_level = db.Column(db.String(64))  # 项目级别
    c_year = db.Column(db.String(64))  # 立项年份
    c_stu_name = db.Column(db.String(64))  # 项目负责人姓名
    c_stu_number = db.Column(db.String(64))  # 负责人学号
    c_stu_phone = db.Column(db.String(64))  # 负责人电话
    c_stu_qq = db.Column(db.String(64))  # 负责人QQ
    c_stu_class = db.Column(db.String(64))  # 专业班级
    c_stu_count = db.Column(db.String(64))  # 参与学生人数
    c_other_stu = db.Column(db.String(64))  # 项目其他成员姓名电话学号
    c_teacher_name = db.Column(db.String(64))  # 指导老师姓名
    c_teacher_title = db.Column(db.String(64))  # 指导老师职称
    c_of_class = db.Column(db.String(64))  # 项目所属一级学科
    c_abstract = db.Column(db.Text)  # 项目简介
    filename = db.Column(db.String(64))
