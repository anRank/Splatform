from models.base import db
from app import create_app
__author__ = 'anRan'


app = create_app()


if __name__ == '__main__':
    # db.create_all(app=app)
    app.run(debug=app.config['DEBUG'], threaded=True)
