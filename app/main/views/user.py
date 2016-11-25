import os
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename
from app import db
from app.main import main
from app.decorators import user_required
from app.create_random_str import get_random_str
from app.models import Project, Competition, User

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
SAVE_PATH = 'app/picture'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@main.route('/user')
@login_required
@user_required
def user_index():
    """
    普通用户登录后的首页
    :return:
    """
    return render_template('user.html')


@main.route('/user/profile')
@login_required
@user_required
def user_profile():
    """
    用户状态查看与密码修改
    :return:
    """
    return render_template("user/user_account.html")


@main.route('/user/change_password', methods=['GET', 'POST'])
@login_required
@user_required
def user_change_password():
    """
    用户密码修改的请求
    :return:
    """
    if request.method == 'GET':
        return redirect(url_for('main.user_profile'))
    else:
        username = request.form['username']
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        new_password_confirm = request.form['new_password_confirm']
        print(username + '   ' + old_password + '  ' + new_password_confirm)
        try:
            this_user = User.query.filter_by(username=username).first()
            if (this_user.verify_password(old_password)):
                # 原密码正确
                if new_password == new_password_confirm:
                    this_user.password = new_password
                    flash("密码修改成功")
                    return redirect(url_for('main.user_profile'))
                else:
                    flash("发生了未知错误已经将页面跳转")
                    return redirect(url_for('main.user_profile'))
            else:
                # 原密码不正确
                flash("原密码不正确请您重新操作")
                return redirect(url_for('main.user_profile'))
        except Exception as e:
            print(e)
            db.session.rollback()
            flash("未知错误")
        return redirect(url_for('main.user_profile'))


@main.route('/user/submit_history')
def user_submit_history():
    return render_template("user/submit_history.html")


@main.route('/user/competition', methods=['GET', 'POST'])
def user_competition():
    """
    进行比赛项目的提交
    :return:
    """
    if request.method == 'GET':
        project = request.args.get('project_id')
        if project is not None:
            # get请求有参状态
            this_project = Project.query.filter_by(id=int(project)).first()
            return render_template("user/competition2.html", this_project=this_project)
        else:
            # get请求无参数状态
            projects = Project.query.all()
            return render_template("user/competition.html", projects=projects)
    else:
        # post请求接收表单
        try:
            # 尝试获取文件
            file = request.files['picture']
        except Exception as e:
            print(e)
            return '未知错误'
        if not allowed_file(file.filename):
            flash('不符合文件类型')
            # 返回提交前的url
            return redirect(request.referrer)

        try:
            # 获取文件扩展名并重命名，最后保存文件
            print('file.filename   ', file.filename)
            filename_extension = secure_filename(file.filename).rsplit('.', 1)[0]
            print(filename_extension)
            filename = '%s.%s' % (get_random_str(), filename_extension)
            file.save(
                os.path.join(SAVE_PATH, filename)
            )
            # 创建某个数据库模型的实例
            competition = Competition(
                project_id=request.form['project_id'],
                achievement_name=request.form['achievement_name'],
                prize_category=request.form['prize_category'],
                prize_level=request.form['prize_level'],
                stu_name=request.form['stu_name'],
                stu_phone_number=request.form['stu_phone_number'],
                stu_number=request.form['stu_number'],
                stu_qq=request.form['stu_qq'],
                stu_class=request.form['stu_class'],
                teacher_name=request.form['teacher_name'],
                teacher_title=request.form['teacher_title'],
                prize_date=request.form['prize_date'],
                award_department=request.form['award_department'],
                sponsor=request.form['sponsor'],
                comment=filename
            )
            # 打印数据用以测试
            '''print(
                project_id,
                achievement_name,
                prize_category,
                prize_level,
                stu_name,
                stu_phone_number,
                stu_number,
                stu_qq,
                stu_class,
                teacher_name,
                teacher_title,
                prize_date,
                award_department,
                sponsor
            )'''
            # competition = Competition()
            db.session.add(competition)
            db.session.commit()
            flash('竞赛获奖提交成功')
            return redirect(url_for('main.user_submit_history'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("发生了未知错误已经将页面跳转")
            return redirect(request.referrer)


@main.route('/user/thesis')
def user_thesis():
    return render_template("user/thesis.html")


@main.route('/user/create_project')
def user_create_project():
    return render_template("user/create_project.html")


@main.route('/user/company')
def user_company():
    return render_template("user/company.html")


@main.route('/user/other')
def user_other():
    return render_template("user/other.html")
