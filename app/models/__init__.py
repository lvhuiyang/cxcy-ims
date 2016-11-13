from flask_login import UserMixin
from app import db


class Accounts(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(32), index=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    created_date = db.Column(db.DateTime())
    created_people = db.Column(db.String(32))


class CreateUser(db.Model):
    create_user_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), primary_key=True)
    created_user_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), primary_key=True)


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.String(32)
    created_date = db.Column(db.DateTime())
    created_people = db.Column(db.String(32))
