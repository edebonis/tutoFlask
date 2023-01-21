
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
