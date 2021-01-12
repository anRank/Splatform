from flask_login import login_user
from sqlalchemy import desc

from app.web import web
from flask import render_template, request
from models.forum import Post, Reply
from models.user import User


@web.route('/')
def hello_world():
    user = User.query.first()
    login_user(user, remember=True)
    context = {
        'posts': Post.query.order_by(desc('create_time')).all()  # desc逆序排序
    }
    return render_template('square.html', **context)


@web.route('/test')
def test():
    return render_template('test.html')