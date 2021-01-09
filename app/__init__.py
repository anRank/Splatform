from flask import Flask
from flask_cors import CORS
from app.models.user import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    # 设置允许跨域请求
    CORS(app, supports_credentials=True)

    from .web import web
    app.register_blueprint(web)

    db.init_app(app)
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()
    return app