from flask import render_template
from flask_login import login_required
from app.main import main


@login_required
@main.route('/manager')
def manager_index():
    return render_template('management.html')
