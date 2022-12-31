from flask import Flask
from flask_login import LoginManager
from .config import Config
from .database import db
from flask_bootstrap import Bootstrap
from .auth import auth
from .ideas import ideas
from .models import UserModel
from flask_fontawesome import FontAwesome

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(username):
    return UserModel.get(username)


def create_app():
    """método de creación de la app de flask"""
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    fa = FontAwesome(app)
    app.config.from_object(Config)
    app.register_blueprint(ideas)
    app.register_blueprint(auth)

    login_manager.init_app(app)

    db.init_app(app)
    return app

