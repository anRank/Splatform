from sqlalchemy import desc

from app.web import web
from flask import request, session, render_template, redirect, url_for

from models.forum import Post, Reply
from models.user import User
from models.user import db
from flask_login import login_user, logout_user, current_user, login_required


@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        form = request.form
        username = form.get('username')
        password = form.get('password')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return render_template('auth/login.html')


@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user, remember=True)
            return redirect(url_for('web.hello_world'))
    else:
        return render_template('auth/login.html')


@web.route('/personal_zone')
@login_required
def personal_zone():
    author_id = current_user.id
    context = {
        'posts': Post.query.filter_by(author_id=author_id).order_by(desc('create_time')).all(),  # desc逆序排序
        'replies': Reply.query.filter_by(author_id=author_id).order_by(desc('create_time')).all()
    }
    return render_template('auth/personal_zone.html', **context)
