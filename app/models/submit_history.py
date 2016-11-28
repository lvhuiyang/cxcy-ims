from app import db


class SubmitHistory(db.Model):
    """
    提交历史情况统计:
    id, 提交人id, 提交人用户名, 提交的内容,附件名
    """
    id = db.Column(db.Integer, primary_key=True)  # id 作为主键
    user_id = db.Column(db.String(64))  # 提交人id
    username = db.Column(db.String(64))  # 提交人用户名
    submit_content = db.Column(db.String(64))  # 提交的内容
    filename = db.Column(db.String(64))  # 附件名
