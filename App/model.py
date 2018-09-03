
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_sql(app):
    db.init_app(app=app)

