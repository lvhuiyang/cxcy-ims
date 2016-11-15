from app import db


class Other(db.Model):
    """
    其他成果统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
