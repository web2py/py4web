from yatl.helpers import SPAN, A, I

from py4web import URL, action, request

from .common import db, session
from .components.grid import Grid


class GridForVueForm(Grid):
    def __init__(self):
        super().__init__(
            "grid_for_vue_forms",
            session,
            use_id=False,
            db=db,
            sort_fields=[
                db.vue_form_table.first_name,
                db.vue_form_table.last_name,
                db.vue_form_table.arrival_time,
            ],
            default_sort=[0, 0, 1],
        )

    def api(self, id=None):
        """Returns data according to the API request."""
        # Builds the header.
        header = dict(
            is_header=True,
            cells=[
                dict(text="First Name", sortable=True),
                dict(text="Last Name", sortable=True),
                dict(text="Arrival Time", sortable=True),
                dict(text="", sortable=False),  # Icons
            ],
        )
        # Gets the request parameters, and copies the sort order in the header.
        req = self._get_request_params(header)
        timezone = request.query.get("timezone")
        q = request.query.get("q", "")  # Query string
        # Forms the query.
        if q:
            query = db(
                db.vue_form_table.first_name.contains(q)
                | db.vue_form_table.last_name.contains(q)
            )
        else:
            query = db.vue_form_table
        # Forms the select.
        rows = db(query).select(**req.search_args)
        # Builds the result rows.
        result_rows = []
        for r in rows:
            cells = []
            cells.append(dict(text=r.first_name))
            cells.append(dict(text=r.last_name))
            cells.append(dict(text=r.arrival_time.isoformat(), type="date"))
            cells.append(
                dict(
                    raw_html=SPAN(
                        A(
                            I(_class="fa fa-eye"),
                            _href=URL("vue_view_form", r.id, signer=self.signer),
                        ),
                        " ",
                        A(
                            I(_class="fa fa-pen"),
                            _href=URL("vue_edit_form", r.id, signer=self.signer),
                        ),
                    ).xml()
                )
            )
            result_rows.append(
                dict(cells=cells, delete=URL("delete_row", r.id, signer=self.signer))
            )
        has_more, result_rows = self._has_more(result_rows)
        return dict(
            page=req.page,
            has_search=True,
            has_delete=True,
            search_placeholder="",
            has_more=has_more,
            rows=[header] + result_rows,
        )


## Now for the controllers.

vue_grid_for_forms = GridForVueForm()


@action("vue_grid_and_forms")
@action.uses("vue/vue_grid_and_forms.html", db, session, vue_grid_for_forms)
def vue_grid_and_forms():
    return dict(grid=vue_grid_for_forms())
