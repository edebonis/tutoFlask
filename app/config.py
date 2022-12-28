class Config:
    """Clase de configuración de flask."""
    SECRET_KEY = "ideas secretas"
    SQLALCHEMY_DATABASE_URI = "sqlite:///../ideas.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
