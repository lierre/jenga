from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

db = SQLAlchemy()
cache = Cache()
login_manager = LoginManager()
mail = Mail()
