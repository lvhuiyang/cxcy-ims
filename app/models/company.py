from app import db
class Company(db.Model):
    """
    公司注册情况统计
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
