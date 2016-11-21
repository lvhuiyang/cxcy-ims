from app.main import main
from app.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user


@main.route('/')
@main.route('/index')
def index():
    if current_user.is_authenticated and \
            (current_user.power == 3 or current_user.power == 2):
        return redirect(url_for('main.manger_index'))
    elif current_user.is_authenticated and current_user.power == 1:
        return redirect(url_for('main.user_index'))
    else:
        return redirect(url_for('main.login'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        print('username' + username + '\n' + 'password' + password)
        user = User.query.filter_by(username=username).first()
        if user.verify_password(password):
            return redirect(url_for('main.index'))
        return redirect(url_for('main.manager'))
        # if user.verify_password(password=password):
        #     return redirect(url_for('main.manager'))
        # else:
        #     flash("test")
        #     return redirect(url_for('main.login'))


@main.route('/manager')
def manager():
    return render_template('management.html')
