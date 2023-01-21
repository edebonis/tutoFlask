from flask import render_template as render, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.testing.config import ident

from . import ideas
from app.services import get_category_by_id, delete_category, create_category, list_categories, list_ideas_by_username,\
    create_idea, delete_idea, update_idea, update_state_idea
from .form import DeleteCategoryForm, RegisterCategoryForm, IdeaForm, DeleteIdeaForm, PublicarIdeaForm
from app.utils import get_dict_from_wftform


def context_home():
    username = current_user.id
    context_categories = [(c["id"], c["name"]) for c in list_categories()]
    idea_form = IdeaForm()
    idea_form.category_id.choices = [("", "--seleccione categoría--")] + context_categories
    context = {
        'username': username,
        'ideas': list_ideas_by_username(username),
        'idea_form': idea_form,
        'delete_form': DeleteIdeaForm(),
        'public_idea_form': PublicarIdeaForm(),
        'modal': {
            "insert": False,
            "update": False
        }
    }
    return context


@ideas.route('/categories', methods=['POST', 'GET'])
@login_required
def categories():
    category_list = list_categories()
    register_form = RegisterCategoryForm()
    context = {
        'register_form': register_form,
        'delete_form': DeleteCategoryForm(),
        'categories': category_list
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
    context = context_home()
    idea_form = context["idea_form"]
    if idea_form.validate_on_submit():
        form_dict = get_dict_from_wftform(idea_form)
        form_dict['username'] = context['username']
        if idea_form.id.data == "":
            create_idea(form_dict)
            flash("Idea creada correctamente", category="success")
            return redirect(url_for('ideas.home'))
        else:
            pass
    return render('ideas/home.html', **context)


@ideas.route('/insert', methods=['POST', 'GET'])
@login_required
def insertideas_view():
    context = context_home()
    context["modal"] = dict(insert=True, update=False)
    return render('ideas/home.html', **context)


@ideas.route('/delete_idea/<idea_id>', methods=['POST', 'GET'])
@login_required
def delete_idea_db(idea_id):
    print(idea_id)
    delete_idea(idea_id)
    flash('Idea eliminada exitosamente', category="success")
    return redirect(url_for('ideas.home'))


@ideas.route('/public_idea/<idea_id>/<int:is_public>', methods=['POST', 'GET'])
@login_required
def public_idea(idea_id, is_public):
    update_state_idea(idea_id, is_public)
    flash('Idea actualizada exitosamente', category="success")
    return redirect(url_for('ideas.home'))
