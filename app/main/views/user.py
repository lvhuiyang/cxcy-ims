import os
from datetime import datetime
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.main import main
from app.decorators import user_required
from app.create_random_str import get_random_str
from app.models import Project, Competition, \
    User, Theses, Patent, Company, CreateProject, Other, SubmitHistory

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
SAVE_PATH = 'app/static/picture_data'


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
        # print(username + '   ' + old_password + '  ' + new_password_confirm)
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
@login_required
@user_required
def user_submit_history():
    histories = SubmitHistory.query.order_by(SubmitHistory.id.desc()) \
        .filter_by(user_id=current_user.id).all()
    return render_template("user/submit_history.html", histories=histories)


@main.route('/user/competition', methods=['GET', 'POST'])
@login_required
@user_required
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
            filename_extension = secure_filename(file.filename).split('.')[-1]
            print('上传文件后缀名 --:\n', filename_extension)
            filename = '%s.%s' % (get_random_str(), filename_extension)
            file.save(
                os.path.join(SAVE_PATH, filename)
            )
            # 创建某个数据库模型的实例
            competition = Competition(
                project_id=request.form['project_id'],
                project_name=request.form['project_name'],
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
                filename=filename
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
            history = SubmitHistory(
                user_id=current_user.id,
                username=current_user.username,
                submit_content='竞赛项目的提交',
                submit_date=datetime.now(),
                filename=filename
            )
            db.session.add(history)
            db.session.commit()
            flash('竞赛获奖提交成功')
            return redirect(url_for('main.user_submit_history'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("发生了未知错误已经将页面跳转")
            return redirect(request.referrer)


@main.route('/user/thesis', methods=['GET', 'POST'])
@login_required
@user_required
def user_thesis():
    """
       进行论文的提交
       :return:
       """
    if request.method == 'GET':
        return render_template("user/thesis.html")
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
            filename_extension = secure_filename(file.filename).split('.')[-1]
            filename = '%s.%s' % (get_random_str(), filename_extension)
            print('file.filename   ', filename)
            file.save(
                os.path.join(SAVE_PATH, filename)
            )

            # 创建某个数据库模型的实例
            theses = Theses(
                stu_academy=request.form['stu_academy'],
                stu_name=request.form['stu_name'],
                stu_phone_number=request.form['stu_phone_number'],
                stu_number=request.form['stu_number'],
                stu_qq=request.form['stu_qq'],
                stu_class=request.form['stu_class'],
                publication_name=request.form['publication_name'],
                thesis_name=request.form['thesis_name'],
                dangci=request.form['dangci'],
                weici=request.form['weici'],
                publication_number=request.form['publication_number'],
                publication_date=request.form['publication_date'],
                filename=filename
            )
            print('test')
            # competition = Competition()
            db.session.add(theses)
            history = SubmitHistory(
                user_id=current_user.id,
                username=current_user.username,
                submit_content='论文发表的提交',
                submit_date=datetime.now(),
                filename=filename
            )
            db.session.add(history)
            db.session.commit()
            flash('论文发表提交成功')
            return redirect(url_for('main.user_submit_history'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("发生了未知错误已经将页面跳转")
            return redirect(request.referrer)


@main.route('/user/patent', methods=['GET', 'POST'])
@login_required
@user_required
def user_patent():
    if request.method == 'GET':
        return render_template('user/patent.html')
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
            filename_extension = secure_filename(file.filename).split('.')[-1]
            filename = '%s.%s' % (get_random_str(), filename_extension)
            file.save(
                os.path.join(SAVE_PATH, filename)
            )
            # 创建某个数据库模型的实例
            patent = Patent(
                stu_academy=request.form['stu_academy'],
                patent_name=request.form['patent_name'],
                patent_categorg=request.form['patent_categorg'],
                patentee=request.form['patentee'],
                inventor=request.form['inventor'],
                weici=request.form['weici'],
                inventor_phone=request.form['inventor_phone'],
                inventor_number=request.form['inventor_number'],
                inventor_qq=request.form['inventor_qq'],
                inventor_class=request.form['inventor_class'],
                patent_number=request.form['patent_number'],
                certificate_number=request.form['certificate_number'],
                date1=request.form['date1'],
                date2=request.form['date2'],
                filename=filename
            )
            db.session.add(patent)
            history = SubmitHistory(
                user_id=current_user.id,
                username=current_user.username,
                submit_content='获批专利的提交',
                submit_date=datetime.now(),
                filename=filename
            )
            db.session.add(history)
            db.session.commit()
            flash('获批专利提交成功')
            return redirect(url_for('main.user_submit_history'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("发生了未知错误已经将页面跳转")
            return redirect(request.referrer)


@main.route('/user/create_project', methods=['GET', 'POST'])
@login_required
@user_required
def user_create_project():
    if request.method == 'GET':
        return render_template("user/create_project.html")
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
            filename_extension = secure_filename(file.filename).split('.')[-1]
            filename = '%s.%s' % (get_random_str(), filename_extension)
            file.save(
                os.path.join(SAVE_PATH, filename)
            )
            # 创建某个数据库模型的实例
            c_project = CreateProject(
                stu_academy=request.form['stu_academy'],
                c_project_number=request.form['c_project_number'],
                c_project_name=request.form['c_project_name'],
                c_project_category=request.form['c_project_category'],
                c_project_level=request.form['c_project_level'],
                c_year=request.form['c_year'],
                c_stu_name=request.form['c_stu_name'],
                c_stu_number=request.form['c_stu_number'],
                c_stu_phone=request.form['c_stu_phone'],
                c_stu_qq=request.form['c_stu_qq'],
                c_stu_class=request.form['c_stu_class'],
                c_stu_count=request.form['c_stu_count'],
                c_other_stu=request.form['c_other_stu'],
                c_teacher_name=request.form['c_teacher_name'],
                c_teacher_title=request.form['c_teacher_title'],
                c_of_class=request.form['c_of_class'],
                c_abstract=request.form['c_abstract'],
                filename=filename
            )
            db.session.add(c_project)
            history = SubmitHistory(
                user_id=current_user.id,
                username=current_user.username,
                submit_content='立项项目的提交',
                submit_date=datetime.now(),
                filename=filename
            )
            db.session.add(history)
            db.session.commit()
            flash('立项项目提交成功')
            return redirect(url_for('main.user_submit_history'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("发生了未知错误已经将页面跳转")
            return redirect(request.referrer)


@main.route('/user/company', methods=['GET', 'POST'])
@login_required
@user_required
def user_company():
    if request.method == 'GET':
        return render_template("user/company.html")
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
            filename_extension = secure_filename(file.filename).split('.')[-1]
            filename = '%s.%s' % (get_random_str(), filename_extension)
            file.save(
                os.path.join(SAVE_PATH, filename)
            )
            # 创建某个数据库模型的实例
            # 测试表单提交内容
            # print(1,request.form['academy'])
            # print(2,request.form['company_name'])
            # print(3,request.form['company_category'])
            # print(4,request.form['legal_person_name'])
            # print(5,request.form['legal_person_number'])
            # print(6,request.form['legal_person_phone_number'])
            # print(7,request.form['legal_person_qq'])
            # print(8,request.form['legal_person_class'])
            # print(9,request.form['register_addr'])
            # print(10,request.form['register_capital'])
            # print(11,request.form['register_date'])
            # print(12,request.form['scope'])
            # print(13,request.form['credit_code'])
            company = Company(
                academy=request.form['academy'],
                company_name=request.form['company_name'],
                company_category=request.form['company_category'],
                legal_person_name=request.form['legal_person_name'],
                legal_person_number=request.form['legal_person_number'],
                legal_person_phone_number=request.form['legal_person_phone_number'],
                legal_person_qq=request.form['legal_person_qq'],
                legal_person_class=request.form['legal_person_class'],
                register_addr=request.form['register_addr'],
                register_capital=request.form['register_capital'],
                register_date=request.form['register_date'],
                scope=request.form['scope'],
                credit_code=request.form['credit_code'],
                filename=filename
            )
            db.session.add(company)
            history = SubmitHistory(
                user_id=current_user.id,
                username=current_user.username,
                submit_content='公司注册的提交',
                submit_date=datetime.now(),
                filename=filename
            )
            db.session.add(history)
            db.session.commit()
            flash('公司注册提交成功')
            return redirect(url_for('main.user_submit_history'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("发生了未知错误已经将页面跳转")
            return redirect(request.referrer)


@main.route('/user/other', methods=['GET', 'POST'])
@login_required
@user_required
def user_other():
    if request.method == 'GET':
        return render_template("user/other.html")
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
            filename_extension = secure_filename(file.filename).split('.')[-1]
            filename = '%s.%s' % (get_random_str(), filename_extension)
            file.save(
                os.path.join(SAVE_PATH, filename)
            )
            # 创建某个数据库模型的实例
            other = Other(
                stu_academy=request.form['stu_academy'],
                prize_name=request.form['prize_name'],
                prize_category=request.form['prize_category'],
                prize_level=request.form['prize_level'],
                prize_personage_collective=request.form['prize_personage_collective'],
                head_number=request.form['head_number'],
                head_phone=request.form['head_phone'],
                head_qq=request.form['head_qq'],
                head_class=request.form['head_class'],
                prize_date=request.form['prize_date'],
                award_department=request.form['award_department'],
                filename=filename
            )
            db.session.add(other)
            history = SubmitHistory(
                user_id=current_user.id,
                username=current_user.username,
                submit_content='其他项目的提交',
                submit_date=datetime.now(),
                filename=filename
            )
            db.session.add(history)
            db.session.commit()
            flash('其他项目提交成功')
            return redirect(url_for('main.user_submit_history'))
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("发生了未知错误已经将页面跳转")
            return redirect(request.referrer)
