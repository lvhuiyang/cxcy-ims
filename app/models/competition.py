from app import db


class Project(db.Model):
    """
    项目信息情况，总共100+项目
    """
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    created_date = db.Column(db.DateTime())
    created_people = db.Column(db.String(32))
    # competitions = db.relationship(
    #     'Competition',
    #     backref='projects',
    #     lazy='dynamic'
    # )


class Competition(db.Model):
    """
    竞赛信息表
    """
    __tablename__ = 'competitions'  # 表名
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    project_id = db.Column(db.Integer())  # 项目名，外键连接到项目名id
    # project_id = db.Column(db.Integer(), db.ForeignKey('projects.id'))  # 项目名，外键连接到项目名id
    achievement_name = db.Column(db.String(64))  # 成果名称
    prize_category = db.Column(db.String(64))  # 获奖类型：国际级别，国家级别...
    prize_level = db.Column(db.String(64))  # 获奖等级 一二三等奖
    stu_name = db.Column(db.String(64))  # 学生姓名
    stu_phone_number = db.Column(db.String(64))  # 学生手机
    stu_number = db.Column(db.String(64))  # 学号
    stu_qq = db.Column(db.String(64))  # qq
    stu_class = db.Column(db.String(64))  # 专业班级
    teacher_name = db.Column(db.String(64))  # 教师姓名
    teacher_title = db.Column(db.String(64))  # 教师职称
    prize_date = db.Column(db.String(64))  # 获奖日期
    award_department = db.Column(db.String(64))  # 颁奖单位
    sponsor = db.Column(db.String(64))  # 主办方
    filename = db.Column(db.String(64))  # 备注--> 11.20 --> 附件名
