from app import db


class Other(db.Model):
    """
    其他成果统计:
    序号	,学院,获奖名称,奖励级别
    获奖个人/集体,主要负责人学号,主要负责人电话,主要负责人QQ
    专业班级,奖励时间,颁奖单位,备注
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    academy = db.Column(db.String(64))  # 学院
    company_name = db.Column(db.String(64))  # 公司名称
    company_category = db.Column(db.String(64))  # 公司类型
    legal_person_name = db.Column(db.String(64))  # 法人代表学生姓名
    legal_person_number = db.Column(db.String(64))  # 学号
    legal_person_phone_number = db.Column(db.String(64))  # 学生电话
    legal_person_qq = db.Column(db.String(64))  # qq
    legal_person_class = db.Column(db.String(64))  # 专业班级
    register_addr = db.Column(db.String(64))  # 公司注册地址
    register_capital = db.Column(db.String(64))  # 公司注册资本
    register_date = db.Column(db.String(64))  # 公司注册时间
    scope = db.Column(db.String(64))  # 公司经营范围
    credit_code = db.Column(db.String(64))  # 统一社会信用代码
    filename = db.Column(db.String(64))  # 备注