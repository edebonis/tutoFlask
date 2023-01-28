# -*- coding: utf-8 -*-
from os import path, remove
import datetime


def get_dict_from_wftform(form):
    """Método para obtener un diccionario a partir de un formulario de wtf forms."""
    dictionary = dict()
    try:
        for key in form.data.keys():
            if key in ['crsf_token', 'submit']:
                continue
            dictionary[str(key)] = form[key].data
    except AttributeError as error:
        dictionary = dict()
    finally:
        return dictionary


def path_url_exists(path_url):
    """Método para verificar existencia de path"""
    if path.exists(path_url):
        return True
    return False


def remove_picture_profile(profile_name):
    """Método para remover foto de perfil de un usuario"""
    path_url = 'app/uploads/picture_profile' + profile_name
    if path_url_exists(path_url):
        remove(path_url)


def random_name(name_base):
    """Método para crear un nombre aleatorio"""
    suffix = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "_".join([name_base, suffix])
    return filename
