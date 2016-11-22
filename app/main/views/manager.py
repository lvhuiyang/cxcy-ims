from flask import render_template, request
from flask_login import login_required
from app.main import main


@login_required
@main.route('/manager')
def manager_index():
    return render_template('management.html')


@login_required
@main.route('/manager/add_user', methods=['GET','POST'])
def manager_add_user():
    if request.method == 'GET':
        return render_template('manager/add_user.html')
    else:
        return 0

