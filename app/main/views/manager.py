from datetime import datetime
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.main import main
from app.models import User, Competition, Project, Theses, Patent, \
    CreateProject, Company, Other, SubmitHistory
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
        # print(username)
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


# 重置密码操作
@main.route('/manager/reset_password', methods=['POST'])
@login_required
@manager_required
def manager_reset_password():
    this_user = User.query.filter_by(id=request.form['user_id']).first()
    try:
        this_user.password = '123456'
        db.session.add(this_user)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 'ERROR'
    return 'OK'


# 竞赛管理列表
@main.route('/manager/competition')
@login_required
@manager_required
def manager_competition():
    competitions = Competition.query.all()
    return render_template('manager/competition.html', competitions=competitions)


# 竞赛管理列表-详细列表
@main.route('/manager/competition')
@login_required
@manager_required
def manager_comperirion_details():
    competitions = Competition.query.all()
    return render_template('manager/competition_details.html', competitions=competitions)


# 发表论文列表管理
@main.route('/manager/theses')
@login_required
@manager_required
def manager_theses():
    theses = Theses.query.all()
    return render_template('manager/thesis_list.html', theses=theses)


# 发表论文列表管理-详细列表
@main.route('/manager/theses_details')
@login_required
@manager_required
def manager_theses_details():
    theses = Theses.query.all()
    return render_template('manager/thesis_list_details.html', theses=theses)


# 获批专利列表管理
@main.route('/manager/patent')
@login_required
@manager_required
def manager_patent():
    patents = Patent.query.all()
    return render_template('manager/patent.html', patents=patents)


# 获批专利列表管理-详细列表
@main.route('/manager/patent_details')
@login_required
@manager_required
def manager_patent_details():
    patents = Patent.query.all()
    return render_template('manager/patent_details.html', patents=patents)


# 项目立项列表管理
@main.route('/manager/create_project')
@login_required
@manager_required
def manager_create_project():
    create_projects = CreateProject.query.all()
    return render_template('manager/create_project_list.html', create_projects=create_projects)


# 项目立项列表管理-详细列表
@main.route('/manager/create_project_details')
@login_required
@manager_required
def manager_create_project_details():
    create_projects = CreateProject.query.all()
    return render_template('manager/create_project_list2.html', create_projects=create_projects)


# 公司注册列表管理
@main.route('/manager/company')
@login_required
@manager_required
def manager_company():
    companys = Company.query.all()
    return render_template('manager/company_list.html', companys=companys)


# 公司注册列表管理-详细列表
@main.route('/manager/company_details')
@login_required
@manager_required
def manager_company_details():
    companys = Company.query.all()
    return render_template('manager/company_list2.html', companys=companys)


# 其他项目列表管理
@main.route('/manager/other')
@login_required
@manager_required
def manager_other():
    others = Other.query.all()
    return render_template('manager/other_list.html', others=others)


# 其他项目列表管理-详细列表管理
@main.route('/manager/other_details')
@login_required
@manager_required
def manager_other_details():
    others = Other.query.all()
    return render_template('manager/other_list2.html', others=others)


# 用户提交历史查看
@main.route('/manager/submit_history')
@login_required
@manager_required
def manager_submit_history():
    histories = SubmitHistory.query.order_by(SubmitHistory.id.desc()).all()
    return render_template("manager/submit_history.html", histories=histories)
