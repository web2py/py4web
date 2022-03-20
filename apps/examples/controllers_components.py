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

from py4web import action, request, abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.url_signer import URLSigner
from pydal.validators import *

from yatl.helpers import A
from .common import db, session, T, cache, auth
from .components.grid import Grid
from .components.vueform import VueForm, InsertForm, TableForm
from .components.fileupload import FileUpload
from .components.starrater import StarRater

signed_url = URLSigner(session, lifespan=3600)


# -----------------------------
# Sample grid.

vue_grid = Grid("grid_api", session)

@action("vuegrid", method=["GET"])
@action.uses("vuegrid.html", vue_grid)
def vuegrid():
    """This page generates a sample grid."""
    # We need to instantiate our grid component.
    return dict(grid=vue_grid())

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


vue_form = VueForm(
    "test_form",
    session,
    [
        Field("name", default="Luca"),
        Field("last_name", default="Smith", writable=False),
        Field("read", "boolean", default=True),
        Field(
            "animal",
            requires=IS_IN_SET(["cat", "dog", "bird"]),
            default="dog",
            writable=False,
        ),
        Field(
            "choice",
            requires=IS_IN_SET({"c": "cat", "d": "dog", "b": "bird"}),
            default="d",
        ),
        Field("arrival_time", "datetime", default=get_time),
        Field("date_of_birth", "date"),
        Field("narrative", "text"),
    ],
    readonly=False,
    redirect_url="index",
)


@action("vue_form", method=["GET"])
@action.uses("vueform.html", vue_form)
def vueform():
    return dict(form=vue_form())

@action('vue_form_bulma', method=["GET"])
@action.uses("vueform_bulma.html", vue_form)
def vueform_bulma():
    return dict(form=vue_form())

# -----------------------------
# Insertion form.


def not_too_expensive(fields):
    """Validation function that checks that the total price is low enough."""
    if (
        fields["product_quantity"]["validated_value"]
        * fields["product_cost"]["validated_value"]
    ) > 1000000:
        err = "Please insert only products with total value of less than a million."
        fields["product_quantity"]["error"] = err
        fields["product_cost"]["error"] = err


insert_form = InsertForm(
    "insert_product",
    session,
    db.product,
    validate=not_too_expensive,
    redirect_url="index",
)


@action("insert_form", method=["GET"])
@action.uses("vueform.html", insert_form)
def insertform():
    return dict(form=insert_form())

@action('insert_form_bulma', method=["GET"])
@action.uses('vueform_bulma.html', insert_form)
def insertform_bulma():
    return dict(form=insert_form())

# -----------------------------
# Update form.
update_form = TableForm(
    "update_product",
    session,
    db.product,
    validate=not_too_expensive,
    redirect_url="index",
)


@action("update_form", method=["GET"])
@action.uses("vueform.html", update_form)
def updateform():
    # For simplicity, we update the record 1.
    return dict(form=update_form(id=1))

@action('update_form_bulma', method=["GET"])
@action.uses('vueform_bulma.html', update_form)
def updateform_bulma():
    # For simplicity, we update the record 1.
    return dict(form=update_form(id=1))

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
