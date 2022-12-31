import bdb
from .serializer import *
from .database import *


def get_user_by_username(username):
    """devuelve user by username"""
    return User.query.filter_by(username=username).first()


def register_user(user_data):
    """Método para registrar un nuevo usuario en base de datos"""
    user = User(
        name=user_data['name'],
        lastname=user_data['name'],
        email=user_data['email'],
        username=user_data['username'],
        password=user_data['password'],
        cellphone=user_data['cellphone']
    )
    user.set_password(user_data['password'])

    db.session.add(user)
    db.session.commit()


def delete_category(category_id):
    category = get_category_by_id(category_id)
    db.session.delete(category)
    db.session.commit()


def get_category_by_id(category_id):
    """Método para buscar categoria por id"""
    return Category.query.get(category_id)


def create_category(name):
    """Método para crear categoria"""
    category = Category(name=name)

    db.session.add(category)
    db.session.commit()


def list_categories():
    """Método para obtener el listado de categorias"""
    schema = CategorySchema()
    data = Category.query.all()
    categories = [schema.dump(c) for c in data]

    return categories