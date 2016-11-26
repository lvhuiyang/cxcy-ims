from app import db


class Patent(db.Model):
    """
    获取专利情况统计:
    序号,学院,专利名称,专利类别,专利权人,发明人,
    位次	,发明人电话,发明人学号,发明人QQ,
    专业班级,专利号,证书号,专利申请日,授权公告日,备注
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    stu_academy = db.Column(db.String(64)) #学生所在学院
    patent_name = db.Column(db.String(64))
    patent_categorg = db.Column(db.String(64))
    patentee = db.Column(db.String(64))
    inventor = db.Column(db.String(64))
    weici = db.Column(db.String(64))
    inventor_phone = db.Column(db.String(64))
    inventor_number = db.Column(db.String(64))
    inventor_qq = db.Column(db.String(64))
    inventor_class = db.Column(db.String(64))
    patent_number = db.Column(db.String(64))
    certificate_number = db.Column(db.String(64))
    date1 = db.Column(db.String(64))
    date2 = db.Column(db.String(64))
    filename = db.Column(db.String(64))