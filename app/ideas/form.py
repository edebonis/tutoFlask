from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import DataRequired, Length


class DeleteCategoryForm(FlaskForm):
    """Form para eliminar categorías"""
    submit = SubmitField("Eliminar")


class RegisterCategoryForm(FlaskForm):
    """Form para registrar categorías"""
    name = StringField("Categoría", validators=[DataRequired(), Length(min=2, max=15)])

    submit = SubmitField("Registrar")
