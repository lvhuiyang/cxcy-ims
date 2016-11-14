from app.main import main
from flask import jsonify, render_template


@main.route('/')
def index():
    return render_template("base.html")


@main.route('/login', methods=['POST'])
def login():
    return jsonify({'Hello': 'World'})
