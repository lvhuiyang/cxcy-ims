from functools import wraps
from flask import abort
from flask_login import current_user


def root_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.power == 3:
            func(*args, **kwargs)
        else:
            abort(404)

    return wrapper


def manager_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.power == 2:
            func(*args, **kwargs)
        else:
            abort(404)

    return wrapper


def user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.power == 1:
            func(*args, **kwargs)
        else:
            abort(404)

    return wrapper
