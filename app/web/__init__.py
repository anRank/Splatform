from flask import Blueprint

web = Blueprint('web', __name__, url_prefix='/')

from app.web import user
from app.web import forum
