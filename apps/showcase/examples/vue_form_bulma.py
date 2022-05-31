from py4web import action

from .vue_form import myform


@action("vue_form_bulma", method=["GET"])
@action.uses("vueform_bulma.html", myform)
def vue_form_bulma():
    return dict(form=myform())
