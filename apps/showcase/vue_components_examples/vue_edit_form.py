from py4web import URL, action

from .common import auth, db, session
from .components.vueform import VueForm


class EditForm(VueForm):
    def __init__(self):
        super().__init__(
            db.vue_form_table, session, "edit-form-vue", use_id=True, db=db, auth=auth
        )

    def read_values(self, record_id):
        values = {}
        assert record_id is not None
        row = self.db(self.db.vue_form_table.id == record_id).select().first()
        if row is not None:
            for f in self.fields.values():
                ff = f["field"]
                values[ff.name] = ff.formatter(row.get(ff.name))
        return values

    def process_post(self, record_id, values):
        self.db(self.db.vue_form_table.id == record_id).update(**values)
        return dict(redirect_url=URL("vue_grid_and_forms"))


edit_form = EditForm()


@action("vue_edit_form/<row_id:int>")
@action.uses("vue/edit_form.html", db, session, edit_form, edit_form.signer.verify())
def vue_edit_form(row_id=None):
    assert row_id is not None
    return dict(form=edit_form(id=row_id, cancel_url=URL("vue_grid_and_forms")))
