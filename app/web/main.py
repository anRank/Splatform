from app.web import web
from flask import render_template, request


@web.route('/')
def hello_world():
    return render_template('base.html')