# -*- coding: utf-8 -*-
import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DATABASE_HOST = os.getenv('database_host') or 'localhost'
    DATABASE_PORT = os.getenv('database_port') or '3306'
    DATABASE_USER = os.getenv('database_user') or 'root'
    DATABASE_PASSWORD = os.getenv('database_password') or ''
    DATABASE_INSTANCE = os.getenv('database_instance') or 'default'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DATABASE_USER + ':' + DATABASE_PASSWORD + \
                              '@' + DATABASE_HOST + ':' + DATABASE_PORT + '/' + DATABASE_INSTANCE
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


config = {'default': Config}
