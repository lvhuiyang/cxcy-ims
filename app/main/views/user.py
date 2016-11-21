import os
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from app.main import main
from app.create_random_str import get_random_str
from app.models import Project, Competition

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@main.route('/user')
def user_index():
    return render_template('user.html')


@main.route('/user/profile')
def user_profile():
    return render_template("user/user_account.html")


@main.route('/user/submit_history')
def user_submit_history():
    return render_template("user/submit_history.html")


@main.route('/user/competition', methods=['GET', 'POST'])
def user_competition():
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
            file = request.files['picture']
        except Exception as e:
            print(e)
            return '未知错误'
        if not allowed_file(file.filename):
            print('不符合文件类型')
            redirect(url_for('mian.index'))
        # 获取文件扩展名并重命名，最后保存文件
        filename_extension = secure_filename(file.filename).rsplit('.', 1)[1]
        filename = '%s.%s' % (get_random_str(), filename_extension)
        file.save(
            os.path.join('data', filename)
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
        return '上传文件成功'


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
