from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager, db


class User(UserMixin, db.Model):
    """
    用户账号信息
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True, nullable=True)
    real_name = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128), nullable=True)
    power = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime())
    created_people = db.Column(db.String(32))

    @property
    def password(self):
        raise AttributeError('用户名或者密码错误')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def reset_password(self):
        """
        密码重设，初始密码为123456
        :return: None
        """
        self.password_hash = '123456'

    def verify_password(self, password):
        """
        将密码和密码哈希值比较，相同返回True,不同False
        :param password:传入的密码
        :return: True or False
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}' >".format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
