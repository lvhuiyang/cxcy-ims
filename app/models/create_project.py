from app import db


class CreateProject(db.Model):
    """
    项目立项情况统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
