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

import uuid

from py4web import action, request, abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.url_signer import URLSigner

from yatl.helpers import A
from .common import db, session, T, cache, auth
from .components.grid import Grid
from .components.vueform import VueForm, InsertForm, TableForm
from .components.fileupload import FileUpload
from .components.starrater import StarRater

signed_url = URLSigner(session)


# -----------------------------
# Sample grid.

vue_grid = Grid('grid_api', session)

@action('vuegrid', method=['GET'])
@action.uses(vue_grid, 'vuegrid.html')
def vuegrid():
    """This page generates a sample grid."""
    # We need to instantiate our grid component.
    return dict(grid=vue_grid())

# -----------------------------
# File uploader.

file_uploader = FileUpload('upload_api', session)

@action('file_uploader', method=['GET'])
@action.uses(file_uploader, 'file_uploader.html')
def fileuploader():
    return dict(uploader=file_uploader(id=1))

# -----------------------------
# Custom vue form.

vue_form = VueForm('custom_form', session,
                   [Field('name'), Field('read', 'boolean')])

@action('vue_form', method=['GET'])
@action.uses(vue_form, "vueform.html")
def vueform():
    return dict(form=vue_form(redirect_url=URL('index')))

# -----------------------------
# Insertion form.

insert_form = InsertForm('insert_product', session, db.product)

@action('insert_form', method=['GET'])
@action.uses(insert_form, 'vueform.html')
def insertform():
    return dict(form=insert_form(redirect_url=URL('index')))

# -----------------------------
# Update form.
update_form = TableForm('update_product', session, db.product)

@action('update_form', method=['GET'])
@action.uses(update_form, 'vueform.html')
def updateform():
    # For simplicity, we update the record 1.
    return dict(form=update_form(id=1, redirect_url=URL('index')))

# -----------------------------
# Star rater.

star_rater = StarRater('star_rater', session)

@action('star_rater', method=['GET'])
@action.uses(star_rater, 'starrating.html')
def starrater():
    # This performs a star rating of item 1.
    return dict(stars=star_rater(id=1))


