from app.web import web
from flask import request
from models.content import Article, Comment
from models.user import User
from models.base import db
from flask_login import login_required


@web.route('/publish', methods=['GET', 'POST'])
@login_required
def publish():
    if request.method == 'GET':
        print('get')
    else:
        # print(request.data)
        data = eval(request.data.decode())
        author_id = data[0]
        content = data[1]
        user = User.query.filter(User.id == author_id).first()
        print(author_id, content)
        article = Article(content=content, author_id=author_id, author=user)
        db.session.add(article)
        db.session.commit()
        return 'publish ok'


@web.route('/article_list', methods=['GET', 'POST'])
def show_post():
    articles = Article.query.all()
    result = {}
    i = 0
    for article in articles:
        post = [article.author_id, article.content, article.id]
        result[i] = post
        i = i + 1
    return result


@web.route('/article_detail', methods=['GET', 'POST'])
def article_get():
    if request.method == 'GET':
        return 'only get'
    else:
        data = eval(request.data.decode())
        print(data)
        article_id = data[0]
        article = Article.query.filter(Article.id == article_id).first()
        print(article.content)
        return article.content


@web.route('/comment_post', methods=['GET', 'POST'])
def comment_post():
    if request.method == 'GET':
        return 'only post'
    else:
        data = eval(request.data.decode())
        print(data)
        user_id = data[0]
        user = User.query.filter(User.id == user_id).first()
        article_id = data[1]
        article = Article.query.filter(Article.id == article_id).first()
        comment_content = data[2]
        comment = Comment(content=comment_content, author_id=user_id, author=user, article_id=article_id,
                          article=article)
        db.session.add(comment)
        db.session.commit()
        return 'post ok'


@web.route('/get_comments', methods=['GET', 'POST'])
def get_comment():
    if request.method == 'GET':
        return 'only post'
    else:
        data = eval(request.data.decode())
        article_id = data[0]
        comment_list = Comment.query.filter(Comment.article_id == article_id).all()
        print(comment_list)
        result = {}
        i = 0
        for comment in comment_list:
            result[i] = [comment.author_id, comment.content]
            i += 1
        return result


@web.route('/my_article', methods=['GET', 'POST'])
def my_article():
    if request.method == 'GET':
        return 'only post'
    else:
        data = eval(request.data.decode())
        # print(data)
        user_id = data[0]
        articles = Article.query.filter(Article.author_id == user_id)
        result = {}
        i = 0
        for article in articles:
            post = [article.author_id, article.content, article.id]
            result[i] = post
            i = i + 1
        return result
