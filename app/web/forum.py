from sqlalchemy import desc

from app.web import web
from flask import request, render_template, redirect, url_for
from models.forum import Post, Reply
from models.user import User
from models.base import db
from flask_login import login_required, current_user


@web.route('/publish')
@login_required
def publish():
    return render_template('publish.html')


@web.route('/publish_post', methods=['GET', 'POST'])
@login_required
def publish_post():
    if request.method == 'GET':
        return 'error'
    else:
        content = request.form.get('content')
    author_id = current_user.id
    post = Post(content=content, author_id=author_id)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('web.hello_world'))


@web.route('/post_detail/<post_id>/')
@login_required
def post_detail(post_id):
    context = {
        'post': Post.query.filter_by(id=post_id).order_by(desc('create_time')).first(),  # desc逆序排序
        'replies': Reply.query.filter_by(post_id=post_id).order_by(desc('create_time')).all()
    }
    return render_template('postdetail.html', **context)


@web.route('/reply_post/<post_id>/', methods=['GET', 'POST'])
@login_required
def reply_post(post_id):
    if request.method == 'GET':
        pass
    else:
        content = request.form.get('reply_content')
    post_id = post_id
    author_id = current_user.id
    reply = Reply(content=content, post_id=post_id, author_id=author_id)
    db.session.add(reply)
    db.session.commit()
    return redirect(url_for('web.post_detail', post_id=post_id))


@web.route('/search_post', methods=['GET', 'POST'])
def search_post():
    if request.method == 'GET':
        content = request.args.get('search')
    else:
            content = request.form.get('search')
    print(11)
    posts = Post.query.all()
    result = []
    for post in posts:
        if content in post.content:
            result.append(post)
    context = {
        'posts': result
    }
    return render_template('square.html', **context)