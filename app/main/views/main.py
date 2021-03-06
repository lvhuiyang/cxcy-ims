from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user, login_user, logout_user
from app.main import main
from app.models import User, Competition


@main.route('/test')
def test():
    return render_template('base.html')


@main.route('/')
@main.route('/index')
def index():
    if current_user.is_authenticated and \
            (current_user.power == 3 or current_user.power == 2):
        return redirect(url_for('main.manager_index'))
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
        # print('username' + username + '\n' + 'password' + password)
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash("账号或者密码错误")
            return redirect(url_for('main.login'))


@login_required
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/picture_data')
@login_required
def picture_data():
    picture_id = request.args.get('picture_id')
    picture_id = '14800601146905'
    # pic_obj = Competition.query.filter_by(comment=picture_id).first()
    if picture_id:
        return 1
    else:
        abort(404)
