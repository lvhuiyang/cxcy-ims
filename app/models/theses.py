from app import db


class Theses(db.Model):
    """
    论文发表管理
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    stu_academy = db.Column(db.String(64))  # 学生所在学院
    stu_name = db.Column(db.String(64))  # 学生姓名
    stu_phone_number = db.Column(db.String(64))  # 学生手机
    stu_number = db.Column(db.String(64))  # 学号
    stu_qq = db.Column(db.String(64))  # qq
    stu_class = db.Column(db.String(64))  # 专业班级
    publication_name = db.Column(db.String(64))  # 刊物名称
    thesis_name = db.Column(db.String(64))  # 论文名称
    dangci = db.Column(db.String(64))  # 档次
    weici = db.Column(db.String(64))  # 位次
    publication_number = db.Column(db.String(64))  # 刊号
    publication_date = db.Column(db.String(64))  # 发表日期
    filename = db.Column(db.String(64))  # 附件名
