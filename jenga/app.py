from flask import Flask

from .config import DefaultConfig
from .views import www
from .extensions import db, mail, login_manager, cache

DEFAULT_BLUEPRINTS = (
    www,
)


def register_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)

    # flask-mail
    mail.init_app(app)

    # flask-cache
    cache.init_app(app)

    # flask-login
    login_manager.init_app(app)


def create_app(config=None, app_name=None, blueprints=None):
    """Create Flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, instance_relative_config=True)

    register_blueprints(app, blueprints)
    configure_extensions(app)

    return app
