from flask import Flask
from .config import Config
from .database import db
from flask_bootstrap import Bootstrap


def create_app():
    """método de creación de la app de flask"""
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    db.init_app(app)
    return app

