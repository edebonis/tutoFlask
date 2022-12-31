from dominate.util import lazy
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(250), nullable=False)
    cellphone = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"User {self.username}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Idea(db.Model):
    __tablename__ = 'ideas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category', backref=db.backref('ideas', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

