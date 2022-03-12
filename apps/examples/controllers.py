import os
from py4web import action, request, abort, redirect, URL, Field, HTTP
from yatl.helpers import A, I
from py4web.utils.form import Form, FormStyleDefault
from py4web.utils.factories import ActionFactory, Inject
from py4web.utils.grid import Grid, GridClassStyle, Column
from py4web.utils.param import Param
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A, DIV, XML
from py4web.utils.param import Param
from .settings import SESSION_SECRET_KEY, HCAPTCHA_SITE_KEY

from .common import db, session, T, flash, cache, authenticated, unauthenticated, auth, hCaptcha

# import websocket examples
from .ws import *
from .socketio import *

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
def page_with_error():
    1 / 0


@action("page_with_raise")
def page_with_raise():
    raise HTTP(400, "oops")


@action("page_with_redirect")
def page_with_redirect():
    redirect(URL("target"))


@action("target")
def target():
    return "target"


@action("page_with_parameters/<x>/<y>/<z>")
def page_with_parameters(x, y, z):
    return repr({"x": x, "y": y, "z": z})


@action("page_with_query")
def page_with_query():
    return repr(dict(request.query))


@action("page_with_postback", method=["GET", "POST"])
def page_with_postback():
    return (
        "<html><body><pre>%s</pre>"
        + '<form method="POST" action="%s" enctype="multipart/form-data">'
        + '<input type="hidden" name="data" value="dummy"/>'
        + "<button>Click</button></form></body></html"
    ) % (dict(request.forms), URL("page_with_postback"))


@action("session/counter")
@action.uses("session_counter.html", session)
def session_counter():
    session["counter"] = session.get("counter", 0) + 1
    return {"counter": session.get("counter")}


@action("session/clear")
@action.uses(session)
def session_clear():
    session.clear()
    redirect(URL("session/counter"))


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
@action.uses("flash_example_next.html", flash)
def flash_example_next():
    return dict()


# exposed as /examples/create_form or /examples/update_form/<id>
@action("create_form", method=["GET", "POST"])
@action("update_form/<id>", method=["GET", "POST"])
@action.uses("form.html", db, session, T)
def example_form(id=None):
    form = Form(db.person, id, deletable=False, formstyle=FormStyleDefault)
    rows = db(db.person).select()
    return dict(form=form, rows=rows)


# exposed as /examples/custom_form
@action("custom_form", method=["GET", "POST"])
@action.uses("custom_form.html", db, session, T)
def custom_form(id=None):
    form = Form(db.person, id, deletable=False, formstyle=FormStyleDefault)
    rows = db(db.person).select()
    return dict(form=form, rows=rows)


@action("tagsinput_form", method=["GET", "POST"])
@action.uses("tagsinput_form.html", session)
def tagsinput_form():
    form = Form([Field("colors", "list:string")], keep_values=True)
    return dict(form=form)


# exposed as /examples/html_grid
@action("html_grid")
@action("html_grid/<path:path>", method=["POST", "GET"])
@action.uses("html_grid.html", session, db, auth, T)
def example_html_grid(path=None):
    #  controllers and used for all grids in the app
    grid_param = dict(
        rows_per_page=5,
        include_action_button_text=True,
        search_button_text="Filter",
        formstyle=FormStyleDefault,
        grid_class_style=GridClassStyle,
    )

    search_queries = [
        ["By Name", lambda value: db.thing.name.contains(value)],
        ["By Color", lambda value: db.thing.color == value],
        [
            "By Name or Color",
            lambda value: db.thing.name.contains(value) | (db.thing.color == value),
        ],
    ]

    query = db.thing.id > 0
    orderby = [db.thing.name]
    columns = [field for field in db.thing if field.readable]
    columns.insert(0, Column("Custom", lambda row: A("click me")))
    grid = Grid(
        path,
        query,
        columns=columns,
        search_queries=search_queries,
        orderby=orderby,
        show_id=False,
        T=T,
        **grid_param
    )

    grid.formatters["thing.color"] = lambda color: I(
        _class="fa fa-circle", _style="color:" + color
    )

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
            formstyle=FormStyleDefault,
        ),
        Form(
            [Field("name", requires=IS_NOT_EMPTY())],
            form_name="2",
            keep_values=True,
            formstyle=FormStyleDefault,
        ),
        Form(
            [Field("name", requires=IS_NOT_EMPTY()), Field("age", "integer")],
            form_name="3",
            formstyle=FormStyleDefault,
        ),
        Form(
            [Field("name", requires=IS_NOT_EMPTY()), Field("insane", "boolean")],
            form_name="4",
            formstyle=FormStyleDefault,
        ),
        Form(
            [
                Field("name", requires=IS_NOT_EMPTY()),
                Field("color", requires=IS_IN_SET(["red", "blue", "green"])),
            ],
            form_name="5",
            formstyle=FormStyleDefault,
        ),
        Form(
            [
                Field("name", requires=IS_NOT_EMPTY()),
                Field(
                    "favorite_hero", requires=IS_IN_DB(db, "person.id", "person.name")
                ),
            ],
            form_name="6",
            formstyle=FormStyleDefault,
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


expose = ActionFactory(auth, T, Inject(message="Hello World"))


@expose.get("test_expose1", template="generic.html")
def test_expose1():
    return dict()


@expose.get("test_expose2")
def test_expose2():
    return dict()


@expose("test_expose3")
def test_expose3():
    return dict()


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
    # this is experimntal, we must disable forms that require a logged in user
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
    flash.set("Welcome")
    form = Form([Field("your_name")])
    return DIV("Hello " + request.forms["your_name"] if form.accepted else form).xml()


# a py4web component loader is a page that loads page parts via ajax
@action("component_loader")
@action.uses("component_loader.html", flash)
def component_loader():
    return dict()

@unauthenticated("hcaptcha_form", "hcaptcha_form.html")
def hcaptcha_form():

    form = Form([
        Field('dummy_form', 'string',)
    ])

    form.structure.append(XML('<div class="h-captcha" data-sitekey="{}"></div>'.format(HCAPTCHA_SITE_KEY)))
    if form.accepted:
        r = hCaptcha(request.forms.get('g-recaptcha-response'))
        if r == True:
            #do something with form data
            form.structure.append(XML('<div style="color:green">Captcha was solved succesfully!</font></div>'))
        else:
            form.structure.append(XML('<div class="py4web-validation-error">invalid captcha</div>'))


    return dict(form=form)


# JSONRPC example

# define a function
def add(x, y):
    return x + y


# register your functions
jsonrpc_methods = {}
jsonrpc_methods["add"] = add

# this is a standard handler that implements the protocol
@action("rpc", method="POST")
def rpc():
    """
    this function implements the jsonrpc server protocol, do not edit
    client example:
    import jsonrpc.proxy
    p = jsonrpc.proxy.JSONRPCProxy("http://127.0.0.1:8000", "/examples/rpc")
    assert p.add(1,2) == 3
    assert p.add(x=1, y=2) == 3
    """
    if not request.json or request.json.get("jsonrpc") != "2.0":
        return {
            "id": None,
            "jsonrpc": "2.0",
            "error": {"code": -32600, "message": "Invalid Request"},
        }
    rid = request.json.get("id")
    method = request.json.get("method")
    params = request.json.get("params")
    if None in (rid, method) or not isinstance(params, (list, dict)):
        return {
            "id": None,
            "jsonrpc": "2.0",
            "error": {"code": -32600, "message": "Invalid Request"},
        }
    func = jsonrpc_methods.get(method)
    if not func:
        return {
            "rid": None,
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Method not found"},
        }
    try:
        result = func(*params) if isinstance(params, list) else func(**params)
        return {"result": result, "id": rid, "jsonrpc": "2.0"}
    except Exception as e:
        error = e
        return {
            "rid": None,
            "jsonrpc": "2.0",
            "error": {"code": -32603, "message": "Internal error", "data": e},
        }
