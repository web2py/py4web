"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

import datetime
import uuid

from py4web import action, request, abort, redirect, URL, HTTP
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.url_signer import URLSigner
from pydal.validators import *

from yatl.helpers import A, I, SPAN, DIV
from .common import db, session, T, cache, auth
from .components.grid import Grid
from .components.vueform import VueForm
from .components.fileupload import FileUpload
from .components.starrater import StarRater

url_signer = URLSigner(session, lifespan=3600)


# -----------------------------
# Sample grid.

vue_grid = Grid("grid_api", session)

@action('vuegrid_bulma', method=["GET"])
@action.uses('vuegrid_bulma.html', vue_grid)
def vuegrid_bulma():
    """This page generates a sample grid."""
    # We need to instantiate our grid component.
    return dict(grid=vue_grid())

# -----------------------------
# File uploader.

file_uploader = FileUpload("upload_api", session)


@action("file_uploader", method=["GET"])
@action.uses("file_uploader.html", file_uploader)
def fileuploader():
    return dict(uploader=file_uploader(id=1))


# -----------------------------
# Custom vue form.


def get_time():
    return datetime.datetime.utcnow()


class ViewForm(VueForm):

    def __init__(self):
        super().__init__(db.vue_form_table, session, 'view-form-vue',
                         use_id=True, readonly=True, db=db, auth=auth)

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
        raise HTTP(403) # Should not occur.


class InsertForm(VueForm):

    def __init__(self):
        super().__init__(db.vue_form_table, session, 'insert-form-vue',
                         signer=url_signer, db=db, auth=auth)

    def read_values(self, record_id):
        values = {}
        for f in self.fields.values():
            ff = f["field"]
            values[ff.name] = ff.formatter(None)
        return values

    def process_post(self, record_id, values):
        new_id = self.db.vue_form_table.insert(**values)
        return dict(redirect_url=URL('vue_grid_and_forms'))


class EditForm(VueForm):

    def __init__(self):
        super().__init__(db.vue_form_table, session, 'edit-form-vue',
                         use_id=True, signer=url_signer, db=db, auth=auth)

    def read_values(self, record_id):
        values = {}
        assert record_id is not None
        row = self.db(self.db.assignment.id == record_id).select().first()
        if row is not None:
            for f in self.fields.values():
                ff = f["field"]
                values[ff.name] = ff.formatter(row.get(ff.name))
        return values

    def process_post(self, record_id, values):
        self.db(self.db.vue_form_table.id == record_id).update(**values)
        return dict(redirect_url=URL('vue_grid_and_forms'))


class GridForVueForm(Grid):

    def __init__(self):
        super().__init__('grid_for_vue_forms', session, use_id=False, db=db)

    def api(self, id=None):
        """Returns data according to the API request."""
        # Builds the header.
        header = dict(
            is_header=True,
            cells=[
                dict(text="First Name", sortable=True),
                dict(text="Last Name", sortable=True),
                dict(text="Arrival Time", sortable=True,)
            ]
        )
        # Gets the request parameters, and copies the sort order in the header.
        req = self._get_request_params(header)
        timezone = request.query.get("timezone")
        q = request.query.get("q", "")  # Query string
        # Forms the query.
        if q:
            query = db(db.vue_form_table.first_name.contains(q)
                       | db.vue_form_table.last_name.contains(q))
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
            cells.append(dict(
                raw_html=SPAN(
                    A(I(_class="fa fa-eye"),
                      _href=URL('view-form-vue', r.id, signer=url_signer), _class="button"),
                    A(I(_class="fa fa-pencil"),
                      _href=URL('edit_form_vue', r.id, signer=url_signer), _class="button")
                ).xml()
            ))
            result_rows.append(dict(cells=cells, has_delete=True))
        has_more, result_rows = self._has_more(result_rows)
        return dict(
            page=req.page,
            has_search=True,
            search_placeholder="",
            has_more=has_more,
            rows=[header] + result_rows
        )


## Now for the controllers.

vue_grid_for_forms = GridForVueForm()

@action("vue_grid_and_forms")
@action.uses("vue_grid_and_forms.html", db, session, vue_grid_for_forms)
def vue_grid_and_forms():
    return dict(grid=vue_grid_for_forms())

insert_form = InsertForm()

@action('insert_form_vue')
@action.uses('insert_form.html', db, session, insert_form)
def insert_form_vue():
    return dict(form=insert_form(cancel_url=URL('vue_grid_and_forms')))

edit_form = EditForm()

@action('edit_form_vue/<row_id:int>')
@action.uses('edit_form.html', db, session, edit_form, url_signer.verify())
def edit_form_vue(row_id=None):
    assert row_id is not None
    return dict(form=edit_form(id=row_id, cancel_url=URL('vue_grid_and_forms')))

view_form = ViewForm()

@action('view_form_vue/<row_id:int>')
@action.uses('view_form.html', db, session, view_form, url_signer.verify())
def view_form_vue(row_id=None):
    assert row_id is not None
    return dict(form=view_form(id=row_id, cancel_url=URL('vue_grid_and_forms')))


# -----------------------------
# Star rater.

star_rater = StarRater("star_rater", session)


@action("star_rater", method=["GET"])
@action.uses("starrating.html", star_rater)
def starrater():
    # This performs a star rating of item 1.
    return dict(stars=star_rater(id=1))


# ------------------------------
# Star rater, instantiated from Vue.


@action("star_rater_vue", method=["GET"])
@action.uses("star_rater_vue.html", star_rater)
def star_rater_vue():
    return dict(get_posts_url=URL("star_rater_get_posts"))


@action('star_rater_vue_bulma', method=["GET"])
@action.uses('star_rater_vue_bulma.html', star_rater)
def star_rater_vue_bulma():
    return dict(get_posts_url=URL('star_rater_get_posts'))

@action("star_rater_get_posts", method=["GET"])
def star_rater_get_posts():
    posts = [
        {"id": 1, "content": "Hello there"},
        {"id": 2, "content": "I love you"},
        {"id": 3, "content": "Do you love me too?"},
    ]
    for p in posts:
        # Creates the callback URL for each rater.
        p["url"] = star_rater.url(p["id"])
    return dict(posts=posts)
