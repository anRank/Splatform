from app import login_manager
from models.base import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    tele = db.Column(db.String(11), nullable=False)


# 需要提供一个user_loader回调。此回调用于从会话中存储的用户ID重新加载用户对象。它应该unicode带有用户的ID，并返回相应的用户对象:
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))