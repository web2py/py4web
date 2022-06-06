from py4web import HTTP, URL, action

from .common import auth, session
from .components.vueform import VueForm
from .models import db


class ViewForm(VueForm):
    def __init__(self):
        super().__init__(
            db.vue_form_table,
            session,
            "view-form-vue",
            use_id=True,
            readonly=True,
            db=db,
            auth=auth,
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
        raise HTTP(403)  # Should not occur.


view_form = ViewForm()


@action("vue_view_form/<row_id:int>")
@action.uses("vue/view_form.html", db, session, view_form, view_form.signer.verify())
def vue_view_form(row_id=None):
    assert row_id is not None
    return dict(form=view_form(id=row_id, cancel_url=URL("vue_grid_and_forms")))
