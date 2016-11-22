from functools import wraps
from flask import flash, redirect, url_for, render_template
from flask_login import current_user


def root_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.power == 3:
            return func(*args, **kwargs)
        else:
            flash("请请求的页面与您当前用户身份不符")
            return redirect(url_for('main.index'))

    return wrapper


def manager_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.power == 3:
            return func(*args, **kwargs)
        else:
            flash("请请求的页面与您当前用户身份不符")
            return redirect(url_for('main.index'))

    return wrapper


def user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.power == 1:
            return func(*args, **kwargs)
        else:
            flash("请请求的页面与您当前用户身份不符")
            return redirect(url_for('main.index'))

    return wrapper
