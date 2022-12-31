from flask import render_template as render, flash, redirect, url_for
from flask_login import login_required, current_user
from . import ideas
from app.services import get_category_by_id, delete_category, create_category, list_categories, list_ideas_by_username
from .form import DeleteCategoryForm, RegisterCategoryForm, IdeaForm


def contextHome():
    username = current_user.id
    categories = [(c["id"], c["name"]) for c in list_categories()]
    idea_form = IdeaForm()
    idea_form.category_id.choices = [("", "--seleccione categoría--")] + categories
    context = {
        'username': username,
        'ideas': list_ideas_by_username(username),
        'idea_form': idea_form,
        'modal': {
            "insert": False,
            "update": False
        }
    }
    return context


@ideas.route('/categories', methods=['POST', 'GET'])
@login_required
def categories():
    categories = list_categories()
    register_form = RegisterCategoryForm()
    context = {
        'register_form': register_form,
        'delete_form': DeleteCategoryForm(),
        'categories': categories
    }

    if register_form.validate_on_submit():
        create_category(register_form.name.data)
        flash("Categoría registrada exitosamente", category="success")
        return redirect(url_for('ideas.categories'))
    return render('ideas/categories.html', **context)


@ideas.route('/category/delete/<category_id>', methods=['POST'])
@login_required
def delete_category_view(category_id):
    delete_category(category_id)
    flash("Categoría eliminada", category="success")

    return redirect(url_for('ideas.categories'))


@ideas.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    """Método para retornar el home de la aplicación"""
    context = contextHome()
    idea_form = context["idea_form"]
    if idea_form.validate_on_submit():
        pass
    return render('ideas/home.html', **context)


@ideas.route('/insert', methods=['POST', 'GET'])
@login_required
def insertideas_view():
    context = contextHome()
    context["modal"] = {
        "insert": True,
        "update": False
    }
    return render('ideas/home.html', **context)

