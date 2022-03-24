============================
Advanced topics and examples
============================



py4web and asyncio
------------------

Asyncio is not strictly needed, at least for most of the normal use
cases where it will add problems more than value because of its concurrency model.
On the other hand, we think py4web needs a built-in websocket async based solution.

If you plan to play with asyncio be careful that you should also deal with all
the framework's components: in particular pydal is not asyncio compliant because
not all the adapters work with async.

htmx
----

There are many javascript front-end frameworks available today that allow you great flexibility
over how you design your web client. Vue, React and Angular are just a few.  However, the
complexity in building one of these systems prevents many developers from reaping those benefits. 
Add to that the rapid state of change in the ecosystem and you soon have an application that is
difficult to maintain just a year or two down the road.

As a consequence, there is a growing need to use simple html elements to add reactivity to your web
pages. htmx is one of the tools emerging as a leader in page reactivity without the complexities of javascript.
Technically, htmx allows you to access AJAX, CSS Transitions, Web Sockets and Server Sent Events directly
in HTML, using attributes, so you can build modern user interfaces with the simplicity and power of hypertext.
[CIT1601]_

Read all about htmx and its capabilities on the official site at https://htmx.org . If you prefer,
there is also a video tutorial: `Simple, Fast Frontends With htmx <https://www.youtube.com/watch?v=cBfz4W_KvEI>`__ .


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
    @action.uses("htmx_list.html", db)
    def htmx_list():
        superheros = db(db.superhero.id > 0).select()
        return dict(superheros=superheros)


    @action("htmx_form/<record_id>", method=["GET", "POST"])
    @action.uses("htmx_form.html", db)
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
    @action.uses("htmx_form.html", db)
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
    @action.uses( "htmx_grid.html", session, db)
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
        "htmx/autocomplete.html",
        session,
        db,
        auth.user,
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

utils.js
--------

Multiple times in this documentation we have mentioned utils.js which comes with the scaffolding application,
yet we never clearly listed what is in there. So here it is.

string.format
~~~~~~~~~~~~~

It extends the String object prototype to allow expressions like this:

.. code:: javascript

    var a = "hello {name}".format(name="Max");

The Q object
~~~~~~~~~~~~

The Q object can be used like a selector supporting jQuery like syntax:

.. code:: javascript

   var element = Q("#element-id")[0];
   var selected_elements = Q(".element-class");

It supports the same syntax as JS ``querySelectorAll``
and always returns an array of selected elements (can be empty).

The Q objects is also a container for functions that can be useful when programming in Javascript.
It is stateless.

For example:

**Q.clone**

A function to clone any object:

.. code:: javascript

   var b = {any: "object"}
   var a = Q.clone(b);

**Q.eval**

It evaluates JS expressions in a string. It is not a sandbox.

.. code:: javascript

   var a = Q.eval("2+3+Math.random()");

**Q.ajax**

A wrapper for the JS fetch method which provides a nicer syntax:

.. code:: javascript

    var data = {};
    var headers = {'custom-header-name': 'value'}
    var success = response => { console.log("recereived", response); } 
    var failure = response => { console.log("recereived", response); }
    Q.ajax("POST", url, data, headers).then(success, failure);

**Q.get_cookie**

Extracts a cookie by name from the header of cookies in the current page:
returns null if the cookie does not exist. Can be used within the JS of a page to retrieve a session cookie
in case it is needed to call an API.

.. code:: javascript

   var a = Q.get_cookie("session");

**Q.register_vue_component**

This is specific for Vue 2 and may be deprecated in the future but it allows
to define a vue component where the template is stored in a separate HTML file
and the template will be loaded lazily only when/if the component is used.

For example instead of doing:

.. code:: javascript

    Vue.component('button-counter', {
    data: function () {
        return {
            count: 0
        }
    },
    template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
    });

You would put the template in a button-counter.html and do

.. code:: javascript

    Q.register_vue_component("button-counter", "button-counter.html", function(res) {
        return {
            data: function () {
                return {
                    count: 0
                };
            };
    });


**Q.upload_helper**

It allows to bind an input tag of type file to a callback so that when a file is selected
the content of the selected file is loaded, base64 encoded, and passed to the callback.

This is useful to create form which include an input field selector - but you want to
place the content of the selected file into a variable, for example to do an ajax post of that content.

For example:

.. code:: html

   <input type="file" id="my-id" />

and 

.. code:: javascript

   var file_name = ""
   var file_content = "";
   Q.upload_helper("my_id", function(name, content) {
      file_name = name;
      file_content = content; // base 64 encoded;
   }


The T object
~~~~~~~~~~~~

This is a Javascript reimplementation of the Python pluralize library in Python
which is used by the Python T object in py4web. So basically a client-side T.

.. code:: javascript

   T.translations = {'dog': {0: 'no cane', 1: 'un case', 2: '{n} cani', 10: 'tanti cani'}};
   var message = T('dog').format({n: 5}); // "5 cani"

The intended usage is to create a server endopoint that can provide translations
for the client accepted-language, obtain T.translations via ajax get, and then use 
T to translate and pluralize all messages clientside rather than serverside.

**Q.debounce**

Prevents a function from stepping on itself.

.. code:: javascript

   setInterval(500, Q.debounce(function(){console.log("hello!)}, 200);

and the function will be called every 500ms
but will skip if the previous call did not terminate.
Unlike other debounce implementations out there, it makes sure
the last call is always executed by delaying it (in the example 200ms);

**Q.debounce**

Prevents a function from being called too often;

.. code:: javascript

   Q("#element").onclick = Q.debounce(function(){console.log("clicked!)}, 1000);

If the element is clicked more often than once every 1000ms, the other clicks will be ignored.

**Q.tags_inputs**

It turns a regular text input containing a string of comma separated tags into a tag widgets.
For example:

.. code:: html

    <input name="browsers"/>

and in JSL

.. code:: javascript

   Q.tags_input('[name=zip_codes]')

You can restrict the set of options with:

.. code:: javascript

   Q.tags_input('[name=zip_codes]', {
      freetext: false,
      tags: ['Chrome', 'Firefox', 'Safari', 'Edge']
   });

It works with the datalist element to provide autocomplete. Simply prepend `-list` to the datalist id:

.. code:: html

    <input name="browsers"/>
    <datalist id="browses-list">
       <option>Chrome</option>
       <option>Firfox</option>
       <option>Safari</option>
       <option>Edge</option>
    </datalist>

and in JS:

.. code:: javascript

   Q.tags_input('[name=zip_codes]', {freetext: false});

It provides more undocumented options.
You need to style the tags. For example:

.. code:: css

    ul.tags-list {
      padding-left: 0;
    }
    ul.tags-list li {
      display: inline-block;
      border-radius: 100px;
      background-color: #111111;
      color: white;
      padding: 0.3em 0.8em 0.2em 0.8em;
      line-height: 1.2em;
      margin: 2px;
      cursor: pointer;
      opacity: 0.2;
      text-transform: capitalize;
    }
    ul.tags-list li[data-selected=true] {
      opacity: 1.0;
    }

Notice that if an input element has class `.type-list-string` or `.type-list-integer`, utils.js applies the
`tag_input` function automatically.

*Q.score_input**

..code:: javascript

    Q.score_input(Q('input[type=password]')[0]);

This will turn the password input into a widget that scores the password complexity.
It is applied automatically to inputs with name "password" or "new_password".

**Components**

This is a poor man version of HTMX. It allows to insert in the page ajax-component tags that
are loaded via ajax and any form in those components will be trapped 
(i.e. the result of form submission will also be displayed inside the same component)

For example imagine an index.html that contains

.. code:: html

    <ajax-component id="component_1" url="[[=URL('mycomponent')]]">
        <blink>Loading...</blink>
    </ajax-component>

And a different action serving the component:

.. code:: python

    @action("mycomponent", method=["GET", "POST"])
    @action.uses(flash)
    def mycomponent():
        flash.set("Welcome")
        form = Form([Field("your_name")])
        return DIV(
            "Hello " + request.forms["your_name"]
            if form.accepted else form).xml()

A component action is a regular action except that it should generate html without the
`<html><body>...</body></html>` envelop and it can make use of templates and flash for example.

Notice that if the main page supports flash messages, any flash message in the component will be displayed
by the parent page.

Moreover if the component returns a `redirect("other_page")` not just the content of the component,
but the entire page will be redirected.

The contents of the component html can contain `<script>...</script>` and they can modify global page variables
as well as modify other components.
