from flask import render_template as render, flash, redirect, url_for
from flask_login import login_required
from . import ideas
from app.services import get_category_by_id, delete_category, create_category, list_categories
from .form import DeleteCategoryForm, RegisterCategoryForm


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


@ideas.route('/home')
@login_required
def home():
    """Método para retornar el home de la aplicación"""
    return render('ideas/home.html')

