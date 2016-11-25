from app import db


class Company(db.Model):
    """
    公司注册情况统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    academy = db.Column(db.String(64))  # 学院
    company_name = db.Column(db.String(64))  # 公司名字
    company_category = db.Column(db.String(64))  # 公司类型
    legal_person_name = db.Column(db.String(64))  # 法人代表学生姓名
    legal_person_number = db.Column(db.String(64))  # 学号
    legal_person_phone_number = db.Column(db.String(64))  # 学生手机
    legal_person_qq = db.Column(db.String(64))  # qq
    legal_person_class = db.Column(db.String(64))  # 专业班级
    register_addr = db.Column(db.String(64))  # 公司注册地址
    register_capital = db.Column(db.String(64))  # 公司注册资本
    register_date = db.Column(db.String(64))  # 公司注册时间
    scope = db.Column(db.String(64))  # 公司经营范围
    credit_code = db.Column(db.String(64))  # 公司经营范围
    comment = db.Column(db.String(64))  # 备注

    def __repr__(self):
        return "<Company '{}' >".format(self.company_name)
