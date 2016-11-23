from datetime import datetime
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.main import main
from app.models import User, Project
from app.decorators import manager_required


@main.route('/manager')
@login_required
@manager_required
def manager_index():
    return render_template('management.html')


@main.route('/manager/add_user', methods=['GET', 'POST'])
@login_required
@manager_required
def manager_add_user():
    if request.method == 'GET':
        return render_template('manager/add_user.html')
    else:
        username = request.form['username']
        print(username)
        user = User.query.filter_by(username=username).first()
        if user is not None:
            flash("该用户名已经被注册过，请重新注册")
            return redirect(url_for("main.manager_add_user"))
        try:
            new_user = User(
                username=username,
                real_name=1,
                power=1,
                password='123456',
                created_date=datetime.today(),
                created_people=current_user.username,
                comment=request.form['comment']
            )
            db.session.add(new_user)
            db.session.commit()
            flash("新添加用户：" + new_user.username + "添加成功")
        except Exception as e:
            print(e)
            db.session.rollback()
            flash("未知错误")
        return redirect(url_for('main.manager_add_user'))


@main.route('/manager/user_list')
@login_required
@manager_required
def manager_user_list():
    users = User.query.all()
    return render_template('manager/user_list.html', users=users)


@main.route('/manager/add_new_project', methods=['GET', 'POST'])
@login_required
@manager_required
def manager_add_new_project():
    if request.method == 'GET':
        return render_template('manager/add_new_project.html')
    else:
        try:
            project_name = request.form['project_name']
            project_obj = Project(
                name=project_name,
                created_date=datetime.today(),
                created_people=current_user.username
            )
            db.session.add(project_obj)
            db.session.commit()
            flash("新添加项目：" + project_obj.name + "添加成功")
        except Exception as e:
            print(e)
            db.session.rollback()
            flash("未知错误")
        return redirect(url_for('main.manager_add_new_project'))


@main.route('/manager/project_list')
@login_required
@manager_required
def manager_project_list():
    projects = Project.query.all()
    return render_template('manager/project_list.html', projects=projects)
