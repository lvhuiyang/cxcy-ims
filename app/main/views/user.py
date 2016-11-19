from flask import render_template, request
from app.main import main
from app.models import Project


@main.route('/user/profile')
def user_profile():
    return render_template("user/user_account.html")


@main.route('/user/submit_history')
def user_submit_history():
    return render_template("user/submit_history.html")


@main.route('/user/competition')
def user_competition():
    project = request.args.get('project_id')
    if project is not None:
        this_project = Project.query.filter_by(id=int(project)).first()
        # print(this_project)
        return render_template("user/competition2.html", this_project=this_project)
    else:
        projects = Project.query.all()
        return render_template("user/competition.html", projects=projects)


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
