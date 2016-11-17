from app.main import main
from app.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user


@main.route('/')
def index():
    if current_user.is_authenticated:
        print("用户是登录状态")
    else:
        print("没有用户登录")
        # return redirect(url_for('main.login'))
    return render_template("base.html")


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        print('username' + username + '\n' + 'password' + password)
        user = User.query.filter_by(username=username).first()
        return redirect(url_for('main.manager'))
        # if user.verify_password(password=password):
        #     return redirect(url_for('main.manager'))
        # else:
        #     flash("test")
        #     return redirect(url_for('main.login'))


@main.route('/manager')
def manager():
    return render_template('management.html')
