from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    """Formulario de registration de usuarios"""
    name = StringField("Nombre", validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField("Apellido", validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField("Correo", validators=[DataRequired(), Email(), Length(min=5, max=30)])
    username = StringField("Nombre", validators=[DataRequired(), Length(min=5, max=10)])
    password = PasswordField("Nueva Contraseña", validators=[
        DataRequired(),
        Length(min=3, max=10),
        EqualTo('password_confirm')
    ])
    cellphone = StringField("Celular", validators=[DataRequired(), Length(min=7, max=20)])
    password_confirm = PasswordField("Confirmar Contraseña", validators=[DataRequired(), Length(min=3, max=20)])

    submit = SubmitField("Registrame")


class LoginForm(FlaskForm):
    """Formulario de Login"""
    username = StringField("Nombre", validators=[DataRequired(), Length(min=5, max=10)])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=3, max=10),])

    submit = SubmitField("Login")
