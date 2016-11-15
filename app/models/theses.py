from app import db


class Theses(db.Model):
    """
    论文发表管理
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
