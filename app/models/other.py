from app import db


class Other(db.Model):
    """
    其他成果统计:
    序号	,学院,获奖名称,【获奖类型】,奖励级别
    获奖个人/集体,主要负责人学号,主要负责人电话,主要负责人QQ
    专业班级,奖励时间,颁奖单位,备注
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    stu_academy = db.Column(db.String(64))  # 学院
    prize_name = db.Column(db.String(64))  # 获奖名称
    prize_category = db.Column(db.String(64))  # 奖励类型
    prize_level = db.Column(db.String(64))  # 奖励级别
    prize_personage_collective = db.Column(db.String(64))  # 获奖个人/集体
    head_number = db.Column(db.String(64))  # 主要负责人学号
    head_phone = db.Column(db.String(64))  # 主要负责人电话
    head_qq = db.Column(db.String(64))  # 主要负责人QQ
    head_class = db.Column(db.String(64))  # 专业班级
    prize_date = db.Column(db.String(64))  # 获奖时间
    award_department = db.Column(db.String(64))  # 颁奖单位
    filename = db.Column(db.String(64))  # 附件名称