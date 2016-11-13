from app.main import main
from flask import jsonify


@main.route('/')
def index():
    return jsonify({'test_cookie': 'test_cookie_value'})


@main.route('/login', methods=['POST'])
def login():
    return jsonify({'Hello': 'World'})
