from py4web import action

from .vue_update_form import not_too_expensive, update_form


@action("vue_update_form_bulma", method=["GET"])
@action.uses("vueform_bulma.html", update_form)
def vue_update_form_bulma():
    # For simplicity, we update the record 1.
    return dict(form=update_form(id=1))
