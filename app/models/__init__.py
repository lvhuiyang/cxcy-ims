from flask_login import UserMixin
from app import db


class Accounts(db.Model):
    """
    用户账号信息
    """
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(32), index=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    created_date = db.Column(db.DateTime())
    created_people = db.Column(db.String(32))


class Project(db.Model):
    """
    项目信息情况，总共100+项目
    """
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.String(32)
    created_date = db.Column(db.DateTime())
    created_people = db.Column(db.String(32))
    competitions = db.relationship(
        'Competition',
        backref='projects',
        lazy='dynamic'
    )


class Competition(db.Model):
    """
    竞赛信息表
    """
    __tablename__ = 'competitions'  # 表名
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id'))  # 项目名，外键连接到项目名id
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
    prize_date = db.Column(db.Date())  # 获奖日期
    award_department = db.Column(db.String(64))  # 颁奖单位
    sponsor = db.Column(db.String(64))  # 主办方
    comment = db.Column(db.String(64))  # 备注


class Theses(db.Model):
    """
    论文发表管理
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键


class Patent(db.Model):
    """
    获取专利情况统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键


class CreateProject(db.Model):
    """
    项目立项情况统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键


class Company(db.Model):
    """
    公司注册情况统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键


class Other(db.Model):
    """
    其他成果统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
