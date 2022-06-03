from py4web import action

from .vue_insert_form import myform, not_too_expensive


@action("vue_insert_form_bulma", method=["GET"])
@action.uses("vueform.html", myform)
def vue_insert_form_bulma():
    return dict(form=myform())
