from app.web import web
from flask import render_template


@web.route('/')
def hello_world():
    return render_template('base.html')


@web.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'