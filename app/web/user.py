from app.web import web
from flask import request, session
from models.user import User
from models.user import db


@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        print('get')
    else:
        print(request.data)
        data = eval(request.data.decode())
        name = data['name']
        password = data['password']
        tele = data['tele']
        # 手机号验证，如果被注册，就不能再注册
        user = User.query.filter(User.tele == tele).first()
        # 账户名验证，如果被注册，就不能再注册
        userName = User.query.filter(User.name == name).first()
        if user:
            return u'tele error'
        elif userName:
            return u'name error'
        else:
            user = User(name=name, password=password, tele=tele)
            db.session.add(user)
            db.session.commit()
            return 'post ok'


# @web.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         print('get')
#     else:
#         print(request.data)
#         data = eval(request.data.decode())
#         name = data['name']
#         password = data['password']
#         user = User.query.filter(User.name == name, User.password == password).first()
#         if user:
#             session['user_id'] = user.id
#             session['user_name'] = user.name
#             session.permanet = True  # 保存登录状态
#         else:
#             return u'账户或密码错误'
#         user_id = session['user_id']
#         return str(user_id)
