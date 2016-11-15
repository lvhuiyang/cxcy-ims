from app.main import main
from flask import render_template
from flask_login import current_user


@main.route('/')
def index():
    if current_user.is_authenticated:
        print("用户是登录状态", current_user.is_authenticated.__doc__)
    else:
        print("没有用户登录", current_user.is_authenticated.__doc__)
    return render_template("base.html")


@main.route('/login')
def login():
    return render_template("login.html")
