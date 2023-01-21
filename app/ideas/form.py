from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, HiddenField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length


class DeleteCategoryForm(FlaskForm):
    """Form para eliminar categorías"""
    submit = SubmitField("Eliminar")


class RegisterCategoryForm(FlaskForm):
    """Form para registrar categorías"""
    name = StringField("Categoría", validators=[DataRequired(), Length(min=2, max=15)])

    submit = SubmitField("Registrar")


class IdeaForm(FlaskForm):
    """Form de ideas"""
    id = HiddenField()
    title = StringField("Título", validators=[DataRequired(), Length(min=5, max=50)])
    description = StringField("Descripción", validators=[DataRequired(), Length(min=10, max=250)])
    is_public = BooleanField("Ideas públicas")
    category_id = SelectField("Ideas públicas", validators=[DataRequired()])

    submit = SubmitField("Enviar")


class DeleteIdeaForm(FlaskForm):
    """Form para eliminar el idea"""
    submit = SubmitField("")


class PublicarIdeaForm(FlaskForm):
    """Form para cambiar el estado de una idea"""
    submit = SubmitField("")
