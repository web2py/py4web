import os
from py4web import action, request, abort, redirect, URL, Field, HTTP
from yatl.helpers import A
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid, get_grid_key, get_storage_value, ActionButton, GridClassStyle, GridClassStyleBulma
from py4web.utils.param import Param
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A, DIV
from . settings import SESSION_SECRET_KEY

from .common import db, session, T, flash, cache, authenticated, unauthenticated, auth

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)


@action("index")
@action.uses("index.html")
def index():
    return {}


@action("page_without_template")
def page_without_template():
    return "ok"


@action("page_with_template")
@action.uses("page_with_template.html")
def page_with_template():
    return {"message": "Hello World"}


@action("page_with_error")
def page_with_errorr():
    1 / 0

@action("page_with_raise")
def page_with_raise():
    raise HTTP(400)


@action("page_with_redirect")
def page_with_redirect():
    redirect(URL('target'))


@action("target")
def target():
    return "tagret"


@action("page_with_parameters/<x>/<y>/<z>")
def page_with_parameters(x,y,z):
    return repr({"x": x, "y": y, "z": z})


@action("page_with_query")
def page_with_query():
    return repr(dict(request.query))

@action("page_with_postback", method=['GET', 'POST'])
def page_with_postback():
    return ('<html><body><pre>%s</pre>' +
            '<form method="POST" action="%s" enctype="multipart/form-data">' +
            '<input type="hidden" name="data" value="dummy"/>' +
            '<button>Click</button></form></body></html') % (
            dict(request.forms), URL('page_with_postback'))

@action("session/counter")
@action.uses(session, 'session_counter.html')
def session_counter():
    session["counter"] = session.get("counter", 0) + 1
    return {"counter": session.get("counter")}


@action("session/clear")
@action.uses(session)
def session_clear():
    session.clear()
    redirect(URL('session/counter'))


@action("flash_example")
@action.uses("flash_example.html")
def flash_example_naive():
    return dict(flash={"message": "hello", "class": "error"})


@action("flash_example_fixture")
@action.uses(flash)
def flash_example_fixture():
    flash.set("you have been redirected <test!>", sanitize=True)
    redirect("flash_next")


@action("flash_next")
@action.uses(flash, "flash_example_next.html")
def flash_example_next():
    return dict()


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


@action("tagsinput_form", method=["GET", "POST"])
@action.uses("tagsinput_form.html", session)
def tagsinput_form():
    form = Form([Field('colors', 'list:string')], keep_values=True)
    return dict(form=form)


# exposed as /examples/htmlgrid
@action('html_grid', method=['POST', 'GET'])
@action('html_grid/<action>/<tablename>/<record_id>', method=['POST', 'GET'])
@action.uses(session, db, auth, 'html_grid.html')
def example_html_grid(action=None, tablename=None, record_id=None):
    #  GRID_COMMON would normally be defined in common.py, imported into
    #  controllers and used for all grids in the app
    GRID_COMMON = Param(db=db,
                        secret=SESSION_SECRET_KEY,
                        rows_per_page=5,
                        grid_key_max_age=3600,
                        search_button_text='Filter',
                        include_action_button_text=True,
                        formstyle=FormStyleBulma,
                        grid_class_style=GridClassStyle)
    #  check session to see if we've saved a default value
    grid_key = get_grid_key()
    search_filter = get_storage_value(grid_key, 'search_filter', common_settings=GRID_COMMON)

    search_form = Form([Field('search_filter',
                              length=50,
                              default=search_filter,
                              _placeholder='...search text...',
                              _title='Enter search text and click on Filter')],
                       keep_values=True, formstyle=FormStyleBulma, )

    if search_form.accepted:
        search_filter = search_form.vars['search_filter']

    queries = [(db.superhero.id > 0)]
    if search_filter:
        queries.append(db.superhero.name.contains(search_filter))

    orderby = [db.superhero.name]

    grid = Grid(GRID_COMMON,
                queries,
                search_form=search_form,
                storage_values=dict(search_filter=search_filter),
                orderby=orderby,
                create=True,
                details=True,
                editable=True,
                deletable=True,
                grid_key=grid_key)

    return dict(grid=grid)


# exposed as /examples/ajaxgrid
@action("ajax_grid")
@action.uses("ajax_grid.html")
def example_ajax_grid():
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


@action("auth_forms", method=["GET", "POST"])
@action.uses("auth_forms.html", db, session, T, auth)
def auth_forms():
    disabled = False
    # this is experimntal, we must disabld forms that rquired a logged in user
    if not auth.is_logged_in:
        disabled = "disabled"
    return dict(
        register_form=auth.form("register"),
        login_form=auth.form("login"),
        reset_password_form=auth.form("reset_password"),
        change_password_form=disabled or auth.form("change_password"),
        profile_form=disabled or auth.form("profile"),
    )


@action("auth_form/<name>", method=["GET", "POST"])
@action.uses("auth_form.html", db, session, T, auth)
def auth_form(name):
    form = auth.form(name)
    if form.submitted:
        pass
    elif form.accepted:
        pass
    elif form.errors:
        pass
    return dict(form=auth.form(name))


# a py4web component is a action that returns a part of a page, not a full page
# it can use templates but they should not extend a layout
@action("mycomponent.load", method=["GET", "POST"])
@action.uses(flash)
def mycomponent():
    flash.set('Welcome')
    form = Form([Field("your_name")])
    return DIV("Hello " + request.forms["your_name"] if form.accepted else form).xml()


# a py4web component loader is a page that loads page parts via ajax
@action("component_loader")
@action.uses(flash, "component_loader.html")
def component_loader():
    return dict()
