from py4web import URL, action

from .common import auth, db, session
from .components.vueform import VueForm


class InsertForm(VueForm):
    def __init__(self):
        super().__init__(
            db.vue_form_table, session, "insert-form-vue", db=db, auth=auth
        )

    def read_values(self, record_id):
        values = {}
        for f in self.fields.values():
            ff = f["field"]
            values[ff.name] = ff.formatter(None)
        return values

    def process_post(self, record_id, values):
        new_id = self.db.vue_form_table.insert(**values)
        return dict(redirect_url=URL("vue_grid_and_forms"))


insert_form = InsertForm()


@action("vue_insert_form")
@action.uses("vue/insert_form.html", db, session, insert_form)
def vue_insert_form():
    return dict(form=insert_form(cancel_url=URL("vue_grid_and_forms")))
