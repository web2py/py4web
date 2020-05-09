import os
from py4web import action, request, abort, redirect, URL, Field
from yatl.helpers import A
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A

from .common import db, session, T, cache, authenticated, unauthenticated

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)


@action("index")
@action.uses("index.html")
def index():
    return {}


@action("simple_page")
def simple_page():
    return "ok"


@action("error")
def error():
    1 / 0

@action("session/counter")
@action.uses(session)
def session_counter():
    session['counter'] = session.get('counter', 0) + 1
    return str(session.get('counter'))

@action("session/clear")
@action.uses(session)
def session_clear():
    session.clear()
    return 'done'


# exposed as /examples/create_form or /examples/update_form/<id>
@action("create_form", method=["GET", "POST"])
@action("update_form/<id>", method=["GET", "POST"])
@action.uses("form.html", db, session, T)
def example_form(id=None):
    form = Form(db.person, id, deletable=False, formstyle=FormStyleBulma)
    rows = db(db.person).select()
    return dict(form=form, rows=rows)


# exposed as /examples/custom_form
@action("custom_form", method=["GET", "POST"])
@action.uses("custom_form.html", db, session, T)
def custom_form(id=None):
    form = Form(db.person, id, deletable=False, formstyle=FormStyleBulma)
    rows = db(db.person).select()
    return dict(form=form, rows=rows)


# exposed as /examples/grid
@action("grid")
@action.uses("grid.html")
def example_grid():
    return dict(grid=publisher.grid(db.person))


@action("hello")
@action.uses(T)
def hello():
    return str(T("Hello World"))


@action("count")
@action("count/<number:int>")
@action.uses(T)
def count(number=1):
    message = T("Cat").format(n=number)
    link = A(T("more"), _href=URL("count/%s" % (number + 1)))
    return HTML(BODY(H1(message, " ", link))).xml()


@action("forms", method=["GET", "POST"])
@action.uses("forms.html", session, db, T)
def example_multiple_forms():
    name = Field("name", requires=IS_NOT_EMPTY())
    forms = [
        Form(
            [Field("name", requires=IS_NOT_EMPTY())],
            form_name="1",
            formstyle=FormStyleBulma,
        ),
        Form(
            [Field("name", requires=IS_NOT_EMPTY())],
            form_name="2",
            keep_values=True,
            formstyle=FormStyleBulma,
        ),
        Form(
            [Field("name", requires=IS_NOT_EMPTY()), Field("age", "integer")],
            form_name="3",
            formstyle=FormStyleBulma,
        ),
        Form(
            [Field("name", requires=IS_NOT_EMPTY()), Field("insane", "boolean")],
            form_name="4",
            formstyle=FormStyleBulma,
        ),
        Form(
            [
                Field("name", requires=IS_NOT_EMPTY()),
                Field("color", requires=IS_IN_SET(["red", "blue", "green"])),
            ],
            form_name="5",
            formstyle=FormStyleBulma,
        ),
        Form(
            [
                Field("name", requires=IS_NOT_EMPTY()),
                Field(
                    "favorite_hero", requires=IS_IN_DB(db, "person.id", "person.name")
                ),
            ],
            form_name="6",
            formstyle=FormStyleBulma,
        ),
    ]
    messages = []
    for form in forms:
        if form.accepted:
            messages.append("form %s accepted with: %s " % (form.form_name, form.vars))
        elif form.errors:
            messages.append("form %s has errors: %s " % (form.form_name, form.errors))
    return dict(forms=forms, messages=messages)


# exposed as /examples/showme
@action("helpers")
@action.uses("generic.html")
def example_helpers():
    return dict(a=H1("I am a title"), b=2, c=dict(d=3, e=4, x=INPUT(_name="test")))


# automatic actions


@unauthenticated.get()  # exposed as /hello_world
def hello_world():
    return dict()


@unauthenticated.get()  # exposed as /hello_world/<msg>
def hello_world(msg):
    return dict(msg=msg)


@unauthenticated.callback("click me")
def a_callback(msg):
    import logging

    logging.info(msg)


@unauthenticated.get()
def show_a_button():
    return dict(mybutton=a_callback.button("clickme")(msg="hello world"))
