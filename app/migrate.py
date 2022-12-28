from .database import db, User


def create_db():
    """Método de creación de la base de datos."""
    db.drop_all()
    db.create_all()


def init_db():
    create_db()
    # user admin app
    admin = User(
        name="Admin",
        lastname="Administ",
        email="admin@example.com",
        username="admin",
        is_admin=True,
        cellphone="1122334455",
    )
    admin.set_password("admin")
    db.session.add(admin)
    db.session.commit()
