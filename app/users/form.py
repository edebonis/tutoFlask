from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired


class UpdateImageProfileForm(FlaskForm):
    """Form para actualizar la foto de perfil de usuario"""
    upload = FileField("Imágen de perfil", validators=[
        FileRequired(),
        FileAllowed(['jpeg', 'jpg', 'png'], 'Solo imágenes ("jpeg", "jpg", "png")'),
    ])
