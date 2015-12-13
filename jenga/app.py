from flask import Flask


def create_app(config=None, app_name=None, blueprints=None):
    """Create Flask app."""

    app = Flask(__name__)

    return app
