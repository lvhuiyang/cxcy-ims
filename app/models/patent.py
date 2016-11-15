from app import db


class Patent(db.Model):
    """
    获取专利情况统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
