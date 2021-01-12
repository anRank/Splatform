from sqlalchemy import desc

from app.web import web
from flask import render_template, request
from models.forum import Post, Reply


@web.route('/')
def hello_world():
    context = {
        'posts': Post.query.order_by(desc('create_time')).all()  # desc逆序排序
    }
    return render_template('square.html', **context)