============================
Advanced topics and examples
============================



py4web and asyncio
------------------

py4web (as bottle) is thread-based, with high speed and efficient memory usage.
Asyncio is not strictly needed, at least for most of the normal use
cases where it will add problems more than value because of its concurrency model.
On the other hand, we think py4web needs a built-in websocket async based solution.

If you plan to play with asyncio be careful that you should also deal with all
the framework's components: in particular pydal is not asyncio compliant because
not all the adapters work with async.

htmx
----
htmx allows you to access AJAX, CSS Transitions, WebSockets and Server Sent Events directly in HTML,
using attributes, so you can build modern user interfaces with the simplicity and power of hypertext.
[CIT1601]_

htmx is a powerful tool that allows you to build interactivity into your web page with little to no javascript.

Read all about htmx and its capabilities on the htmx site at https://htmx.org

py4web enables htmx integration in a couple of ways.

#. Allow you to add htmx attributes to your forms and buttons
#. Includes an htmx attributes plugin for the py4web grid

htmx usage in Form
~~~~~~~~~~~~~~~~~~

The py4web Form class allows you to pass \**kwargs to it that will be passed along as attributes to the html
form. For example, to add the hx-post and hx-target to the <form> element you would use:

.. code:: python

    attrs = {
        "_hx-post": URL("url_to_post_to/%s" % record_id),
        "_hx-target": "#detail-target",
    }
    form = Form(
        db.tablename,
        record=record_id,
        **attrs,
    )

Now when your form is submitted it will call the URL in the hx-post attribute and whatever is returned
to the browser will replace the html inside of the element with id="detail-target".

Let's continue with a full example (started from scaffold).

**controllers.py**

.. code:: python

    import datetime

    @action("htmx_form_demo", method=["GET", "POST"])
    @action.uses("htmx_form_demo.html")
    def htmx_form_demo():
        return dict(timestamp=datetime.datetime.now())


    @action("htmx_list", method=["GET", "POST"])
    @action.uses(db, "htmx_list.html")
    def htmx_list():
        superheros = db(db.superhero.id > 0).select()
        return dict(superheros=superheros)


    @action("htmx_form/<record_id>", method=["GET", "POST"])
    @action.uses(db, "htmx_form.html")
    def htmx_form(record_id=None):
        attrs = {
            "_hx-post": URL("htmx_form/%s" % record_id),
            "_hx-target": "#htmx-form-demo",
        }
        form = Form(db.superhero, record=db.superhero(record_id), **attrs)
        if form.accepted:
            redirect(URL("htmx_list"))

        cancel_attrs = {
            "_hx-get": URL("htmx_list"),
            "_hx-target": "#htmx-form-demo",
        }
        form.param.sidecar.append(A("Cancel", **cancel_attrs))

        return dict(form=form)

**templates/htmx_form_demo.html**

.. code:: html

    [[extend 'layout.html']]

    [[=timestamp]]
    <div id="htmx-form-demo">
        <div hx-get="[[=URL('htmx_list')]]" hx-trigger="load" hx-target="#htmx-form-demo"></div>
    </div>

    <script src="https://unpkg.com/htmx.org@1.3.2"></script>

**templates/htmx_list.html**

.. code:: html

    <ul>
    [[for sh in superheros:]]
        <li><a hx-get="[[=URL('htmx_form/%s' % sh.id)]]" hx-target="#htmx-form-demo">[[=sh.name]]</a></li>
    [[pass]]
    </ul>

**templates/htmx_form.html**

.. code:: html

    [[=form]]


We now have a functional maintenance app to update our superheros.  In your browser navigate to the htmx_form_demo page
in your new application.  The hx-trigger="load" attribute on the inner div of the htmx_form_demo.html page
loads the htmx_list.html page inside the htmx-form-demo DIV once the htmx_form_demo page is loaded.

Notice the timestamp added outside of the htmx-form-demo DIV does not change when transitions occur.  This is
because the outer page is never reloaded, only the content inside the htmx-form-demo DIV.

The htmx attributes hx-get and hx-target are then used on the anchor tags to call the htmx_form page to
load the form inside the htmx-form-demo DIV.

So far we've just seen standard htmx processing. Nothing fancy here, and nothing specific to py4web. However,
in the htmx_form method we see how you can pass any attribute to a py4web form that will be rendered on the
<form> element as we add the hx-post and hx-target. This tells the form to allow htmx to override the default
form behavior and to render the resulting output in the target specified.

The default py4web form does not include a Cancel button in case you want to cancel out of the edit form. But
you can add 'sidecar' elements to your forms. You can see in htmx_form that we add a cancel option and add the
required htmx attributes to make sure the htmx_list page is rendered inside the htmx-form-demo DIV.


htmx usage in Grid
~~~~~~~~~~~~~~~~~~

The py4web grid provides an attributes plugin system that allows you to build plugins to provide custom attributes
for form elements, anchor elements or confirmation messages. py4web also provide an attributes plugin specifically for
htmx.

Here is an example building off the previous htmx forms example.

**controller.py**

.. code:: python

    @action("htmx_form/<record_id>", method=["GET", "POST"])
    @action.uses(db, "htmx_form.html")
    def htmx_form(record_id=None):
        attrs = {
            "_hx-post": URL("htmx_form/%s" % record_id),
            "_hx-target": "#htmx-form-demo",
        }
        form = Form(db.superhero, record=db.superhero(record_id), **attrs)
        if form.accepted:
            redirect(URL("htmx_list"))

        cancel_attrs = {
            "_hx-get": URL("htmx_list"),
            "_hx-target": "#htmx-form-demo",
        }
        form.param.sidecar.append(A("Cancel", **cancel_attrs))

        return dict(form=form)

    @action("htmx_grid", method=["GET", "POST"])
    @action("htmx_grid/<path:path>", method=["GET", "POST"])
    @action.uses(session, db, "htmx_grid.html")
    def htmx_grid(path=None):
        grid = Grid(path, db.superhero, auto_process=False)

        grid.attributes_plugin = AttributesPluginHtmx("#htmx-grid-demo")
        attrs = {
            "_hx-get": URL(
                "htmx_grid",
            ),
            "_hx-target": "#htmx-grid-demo",
        }
        grid.param.new_sidecar = A("Cancel", **attrs)
        grid.param.edit_sidecar = A("Cancel", **attrs)

        grid.process()

        return dict(grid=grid)

**templates/htmx_form_demo.html**

.. code:: html

    [[extend 'layout.html']]

    [[=timestamp]]
    <div id="htmx-form-demo">
        <div hx-get="[[=URL('htmx_list')]]" hx-trigger="load" hx-target="#htmx-form-demo"></div>
    </div>

    <div id="htmx-grid-demo">
        <div hx-get="[[=URL('htmx_grid')]]" hx-trigger="load" hx-target="#htmx-grid-demo"></div>
    </div>

    <script src="https://unpkg.com/htmx.org@1.3.2"></script>

Notice that we added the #htmx-grid-demo DIV which calls the htmx_grid route.

**templates/htmx_grid.html**

.. code:: html

    [[=grid.render()]]

In htmx_grid we take advantage of deferred processing on the grid. We setup a standard CRUD grid, defer
processing and then tell the grid we're going to use an alternate attributes plugin to build our navigation.
Now the forms, links and delete confirmations are all handled by htmx.

Autocomplete Widget using htmx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmx can be used for much more than just form/grid processing. In this example we'll take advantage of htmx and the
py4web form widgets to build an autocomplete widget that can be used in your forms. *NOTE: this is just an example, none
of this code comes with py4web*

Again we'll use the superheros database as defined in the examples app.

Add the following to your controllers.py.  This code will build your autocomplete dropdowns as well as
handle the database calls to get your data.

.. code:: python

    import json
    from functools import reduce

    from yatl import DIV, INPUT, SCRIPT

    from py4web import action, request, URL
    from ..common import session, db, auth


    @action(
        "htmx/autocomplete",
        method=["GET", "POST"],
    )
    @action.uses(
        session,
        db,
        auth.user,
        "htmx/autocomplete.html",
    )
    def autocomplete():
        tablename = request.params.tablename
        fieldname = request.params.fieldname
        autocomplete_query = request.params.query

        field = db[tablename][fieldname]
        data = []

        fk_table = None

        if field and field.requires:
            fk_table = field.requires.ktable
            fk_field = field.requires.kfield

            queries = []
            if "_autocomplete_search_fields" in dir(field):
                for sf in field._autocomplete_search_fields:
                    queries.append(
                        db[fk_table][sf].contains(
                            request.params[f"{tablename}_{fieldname}_search"]
                        )
                    )
                query = reduce(lambda a, b: (a | b), queries)
            else:
                for f in db[fk_table]:
                    if f.type in ["string", "text"]:
                        queries.append(
                            db[fk_table][f.name].contains(
                                request.params[f"{tablename}_{fieldname}_search"]
                            )
                        )

                query = reduce(lambda a, b: (a | b), queries)

            if len(queries) == 0:
                queries = [db[fk_table].id > 0]
                query = reduce(lambda a, b: (a & b), queries)

            if autocomplete_query:
                query = reduce(lambda a, b: (a & b), [autocomplete_query, query])
            data = db(query).select(orderby=field.requires.orderby)

        return dict(
            data=data,
            tablename=tablename,
            fieldname=fieldname,
            fk_table=fk_table,
            data_label=field.requires.label,
        )

    class HtmxAutocompleteWidget:
        def __init__(self, simple_query=None, url=None, **attrs):
            self.query = simple_query
            self.url = url if url else URL("htmx/autocomplete")
            self.attrs = attrs

            self.attrs.pop("simple_query", None)
            self.attrs.pop("url", None)

        def make(self, field, value, error, title, placeholder="", readonly=False):
            #  TODO: handle readonly parameter
            control = DIV()
            if "_table" in dir(field):
                tablename = field._table
            else:
                tablename = "no_table"

            #  build the div-hidden input field to hold the value
            hidden_input = INPUT(
                _type="text",
                _id="%s_%s" % (tablename, field.name),
                _name=field.name,
                _value=value,
            )
            hidden_div = DIV(hidden_input, _style="display: none;")
            control.append(hidden_div)

            #  build the input field to accept the text

            #  set the htmx attributes

            values = {
                "tablename": str(tablename),
                "fieldname": field.name,
                "query": str(self.query) if self.query else "",
                **self.attrs,
            }
            attrs = {
                "_hx-post": self.url,
                "_hx-trigger": "keyup changed delay:500ms",
                "_hx-target": "#%s_%s_autocomplete_results" % (tablename, field.name),
                "_hx-indicator": ".htmx-indicator",
                "_hx-vals": json.dumps(values),
            }
            search_value = None
            if value and field.requires:
                row = (
                    db(db[field.requires.ktable][field.requires.kfield] == value)
                    .select()
                    .first()
                )
                if row:
                    search_value = field.requires.label % row

            control.append(
                INPUT(
                    _type="text",
                    _id="%s_%s_search" % (tablename, field.name),
                    _name="%s_%s_search" % (tablename, field.name),
                    _value=search_value,
                    _class="input",
                    _placeholder=placeholder if placeholder and placeholder != "" else "..",
                    _title=title,
                    _autocomplete="off",
                    **attrs,
                )
            )

            control.append(DIV(_id="%s_%s_autocomplete_results" % (tablename, field.name)))

            control.append(
                SCRIPT(
                    """
            htmx.onLoad(function(elt) {
                document.querySelector('#%(table)s_%(field)s_search').onkeydown = check_%(table)s_%(field)s_down_key;
                \n
                function check_%(table)s_%(field)s_down_key(e) {
                    if (e.keyCode == '40') {
                        document.querySelector('#%(table)s_%(field)s_autocomplete').focus();
                        document.querySelector('#%(table)s_%(field)s_autocomplete').selectedIndex = 0;
                    }
                }
            })
                """
                    % {
                        "table": tablename,
                        "field": field.name,
                    }
                )
            )

            return control

Usage - in your controller code, this example uses bulma as the base css formatter.

.. code:: python

    formstyle = FormStyleFactory()
    formstyle.classes = FormStyleBulma.classes
    formstyle.class_inner_exceptions = FormStyleBulma.class_inner_exceptions
    formstyle.widgets["vendor"] = HtmxAutocompleteWidget(
        simple_query=(db.vendor.vendor_type == "S")
    )

    form = Form(
        db.product,
        record=product_record,  # defined earlier in controller
        formstyle=formstyle,
    )

First, get an instance of FormStyleFactory.  Then get the base css classes from whichever css framework you wish. Add
the class inner exceptions from your css framework. Once this is set up you can override the default widget for a
field based on its name.  In this case we're overriding the widget for the 'vendor' field. Instead of including all
vendors in the select dropdown, we're limiting only to those with a vendor type equal to 'S'.

When this is rendered in your page, the default widget for the vendor field is replaced with the widget generated by
the HtmxAutocompleteWidget. When you pass a simple query to the HtmxAutocompleteWidget the widget will use the default
route to fill the dropdown with data.

If using the simple query and default build url, you are limited to a simple DAL query. You cannot use DAL subqueries
within this simple query.  If the data for the dropdown requires a more complex DAL query you can override the default
data builder URL to provide your own controller function to retrieve the data.


.. [CIT1601] from the https://htmx.org website

