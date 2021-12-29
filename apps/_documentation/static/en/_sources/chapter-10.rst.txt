============
YATL helpers
============

Helpers overview
----------------

Consider the following code in a template:

::

   [[=DIV('this', 'is', 'a', 'test', _id='123', _class='myclass')]]

it is rendered as:

.. code:: html

   <div id="123" class="myclass">thisisatest</div>

You can easily test the rendering of these commands by copying the _scaffold app (see
:ref:`copying-the-scaffold-app`) and then editing the file
``new_app/template/index.html``. 

``DIV`` is a **helper class**, i.e., something that can be used to build
HTML programmatically. It corresponds to the HTML ``<div>`` tag.

Helpers can have:

- **positional arguments** interpreted as objects contained between the
  open and close tags, like ``thisisatest`` in the previous example
- **named arguments** (start with an underscore) 
  interpreted as HTML tag attributes (without the underscore), like ``_class``
  and ``_id`` in the previous example
- **named arguments** (start without an underscore), in this case these
  arguments are tag-specific


Instead of a set of unnamed arguments, a helper can also take a single
list or tuple as its set of components using the ``*`` notation and it
can take a single dictionary as its set of attributes using the ``**``,
for example:

::

   [[
   contents = ['this', 'is', 'a', 'test']
   attributes = {'_id':'123', '_class':'myclass'}
   =DIV(*contents, **attributes)
   ]]

(produces the same output as before).

The following are the current set of helpers available within the YATL
module:

``A``, ``BEAUTIFY``, ``BODY``, ``CAT``, ``CODE``, ``DIV``, ``EM``,
``FORM``, ``H1``, ``H2``, ``H3``, ``H4``, ``H5``, ``H6``, ``HEAD``,
``HTML``, ``IMG``, ``INPUT``, ``LABEL``, ``LI``, ``METATAG``,
``OL``, ``OPTION``, ``P``, ``PRE``, ``SELECT``, ``SPAN``, ``STRONG``,
``TABLE``, ``TAG``, ``TAGGER``, ``THEAD``, ``TBODY``, ``TD``,
``TEXTAREA``, ``TH``, ``TT``, ``TR``, ``UL``, ``XML``, ``xmlescape``,
``I``, ``META``, ``LINK``, ``TITLE``, ``STYLE``, ``SCRIPT``

Helpers can be used to build complex expressions, that can then be serialized to
XML. For example:

::

   [[=DIV(STRONG(I("hello ", "<world>")), _class="myclass")]]

is rendered:

.. code:: html

   <div class="myclass"><strong><i>hello &lt;world&gt;</i></strong></div>

Helpers can also be serialized into strings, equivalently, with the
``__str__`` and the ``xml`` methods. This can be manually tested directly
with a Python shell or by using the :ref:`shell command option` of py4web
and then:

.. code:: python

   >>> from yatl.helpers import *
   >>> 
   >>> str(DIV("hello world"))
   '<div>hello world</div>'
   >>> DIV("hello world").xml()
   '<div>hello world</div>'


The helpers mechanism in py4web is more than a system to generate HTML
without concatenating strings. It provides a server-side representation
of the document object model (DOM).

Components of helpers can be referenced via their position, and helpers
act as lists with respect to their components:

.. code:: python

   >>> a = DIV(SPAN('a', 'b'), 'c')
   >>> print(a)
   <div><span>ab</span>c</div>
   >>> del a[1]
   >>> a.append(STRONG('x'))
   >>> a[0][0] = 'y'
   >>> print(a)
   <div><span>yb</span><strong>x</strong></div>

Attributes of helpers can be referenced by name, and helpers act as
dictionaries with respect to their attributes:

.. code:: python

   >>> a = DIV(SPAN('a', 'b'), 'c')
   >>> a['_class'] = 's'
   >>> a[0]['_class'] = 't'
   >>> print(a)
   <div class="s"><span class="t">ab</span>c</div>

Note, the complete set of components can be accessed via a list called
``a.children``, and the complete set of attributes can be accessed via
a dictionary called ``a.attributes``. So, ``a[i]`` is equivalent to
``a.children[i]`` when ``i`` is an integer, and ``a[s]`` is equivalent
to ``a.attributes[s]`` when ``s`` is a string.

Notice that helper attributes are passed as keyword arguments to the
helper. In some cases, however, attribute names include special
characters that are not allowed in Python identifiers (e.g., hyphens)
and therefore cannot be used as keyword argument names. For example:

.. code:: python

   DIV('text', _data-role='collapsible')

will not work because “_data-role” includes a hyphen, which will produce
a Python syntax error.

In such cases you can pass the attributes as a dictionary and make use
of Python’s ``**`` function arguments notation, which maps a dictionary
of (key:value) pairs into a set of keyword arguments:

.. code:: python

   >>> print(DIV('text', **{'_data-role': 'collapsible'}))
   <div data-role="collapsible">text</div>

You can also dynamically create special TAGs:

.. code:: python

   >>> print(TAG['soap:Body']('whatever', **{'_xmlns:m':'http://www.example.org'}))
   <soap:Body xmlns:m="http://www.example.org">whatever</soap:Body>


Built-in helpers
----------------

.. _XML:

``XML``
~~~~~~~

``XML`` is an helper object used to encapsulate text that should **not** be
escaped. The text may or may not contain valid XML; for example it
could contain JavaScript.

The text in this example is escaped:

.. code:: python

   >>> print(DIV("<strong>hello</strong>"))
   <div>&lt;strong&gt;hello&lt;/strong&gt;</div>

by using ``XML`` you can prevent escaping:

.. code:: python

   >>> print(DIV(XML("<strong>hello</strong>")))
   <div><strong>hello</strong></div>

Sometimes you want to render HTML stored in a variable, but the HTML may
contain unsafe tags such as scripts:

.. code:: python

   >>> print(XML('<script>alert("unsafe!")</script>'))
   <script>alert("unsafe!")</script>

Un-escaped executable input such as this (for example, entered in the
body of a comment in a blog) is unsafe, because it can be used to
generate cross site scripting (XSS) attacks against other visitors to
the page.
In this case the py4web ``XML`` helper can sanitize our text to prevent injections
and escape all tags except those that you explicitly allow. Here is an
example:

.. code:: python

   >>> print(XML('<script>alert("unsafe!")</script>', sanitize=True))
   &lt;script&gt;alert(&quot;unsafe!&quot;)&lt;/script&gt;

The ``XML`` constructors, by default, consider the content of some tags
and some of their attributes safe. You can override the defaults using
the optional ``permitted_tags`` and ``allowed_attributes`` arguments.
Here are the default values of the optional arguments of the ``XML``
helper.

.. code:: python

   XML(text, sanitize=False,
       permitted_tags=['a', 'b', 'blockquote', 'br/', 'i', 'li',
           'ol', 'ul', 'p', 'cite', 'code', 'pre', 'img/',
           'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'tr', 'td',
           'div', 'strong', 'span'],
       allowed_attributes={'a': ['href', 'title', 'target'],
           'img': ['src', 'alt'], 'blockquote': ['type'], 'td': ['colspan']})


``A``
~~~~~

This helper is used to build links.

.. code:: python

   >>> print(A('<click>', XML('<strong>me</strong>'),
               _href='http://www.py4web.com'))
   <a href="http://www.py4web.com">&lt;click&gt;<strong>me</strong></a>

``BODY``
~~~~~~~~

This helper makes the body of a page.

.. code:: python

   >>> print(BODY('<hello>', XML('<strong>world</strong>'), _bgcolor='red'))
   <body bgcolor="red">&lt;hello&gt;<strong>world</strong></body>

``CAT``
~~~~~~~

This helper concatenates other helpers.

.. code:: python

   >>> print(CAT('Here is a ', A('link', _href='target'), ', and here is some ', STRONG('bold text'), '.'))
   Here is a <a href="target">link</a>, and here is some <strong>bold text</strong>.

``DIV``
~~~~~~~

This is the content division element.

.. code:: python

   >>> print(DIV('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <div id="0" class="test">&lt;hello&gt;<strong>world</strong></div>

``EM``
~~~~~~

Emphasizes its content.

.. code:: python

   >>> print(EM('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <em id="0" class="test">&lt;hello&gt;<strong>world</strong></em>

``FORM``
~~~~~~~~

Use this helper to make a FORM for user input. Forms will be later discussed
in detail in the dedicated :ref:`Forms` chapter.

.. code:: python

   >>> print(FORM(INPUT(_type='submit'), _action='', _method='post'))
   <form action="" method="post"><input type="submit"/></form>

``H1``, ``H2``, ``H3``, ``H4``, ``H5``, ``H6``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These helpers are for paragraph headings and subheadings.

.. code:: python

   >>> print(H1('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <h1 id="0" class="test">&lt;hello&gt;<strong>world</strong></h1>

``HEAD``
~~~~~~~~

For tagging the HEAD of an HTML page.

.. code:: python

   >>> print(HEAD(TITLE('<hello>', XML('<strong>world</strong>'))))
   <head><title>&lt;hello&gt;<strong>world</strong></title></head>

``HTML``
~~~~~~~~

For tagging an HTML page.

.. code:: python

   >>> print(HTML(BODY('<hello>', XML('<strong>world</strong>'))))
   <html><body>&lt;hello&gt;<strong>world</strong></body></html>

``I``
~~~~~

This helper makes its contents italic.

.. code:: python

   >>> print(I('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <i id="0" class="test">&lt;hello&gt;<strong>world</strong></i>

``IMG``
~~~~~~~

It can be used to embed images into HTML.

.. code:: python

   >>> print(IMG(_src='http://example.com/image.png', _alt='test'))
   <img alt="test" src="http://example.com/image.png"/>

Here is a combination of A, IMG, and URL helpers for including a static
image with a link:

.. code:: python

   >>> print(A(IMG(_src=URL('static', 'logo.png'), _alt="My Logo"),
   ... _href=URL('default', 'index')))
   <a href="/default/index"><img alt="My Logo" src="/static/logo.png"/></a>

``INPUT``
~~~~~~~~~

Creates an ``<input.../>`` tag. An input tag may not contain other tags,
and is closed by ``/>`` instead of ``>``. The input tag has an optional
attribute ``_type`` that can be set to “text” (the default), “submit”,
“checkbox”, or “radio”.

.. code:: python

   >>> print(INPUT(_name='test', _value='a'))
   <input name="test" value="a"/>

For radio buttons use the ``_checked`` attribute:

.. code:: python

   >>> for v in ['a', 'b', 'c']:
   ...     print(INPUT(_type='radio', _name='test', _value=v, _checked=v=='b'), v)
   ... 
   <input name="test" type="radio" value="a"/> a
   <input checked="checked" name="test" type="radio" value="b"/> b
   <input name="test" type="radio" value="c"/> c

and similarly for checkboxes:

.. code:: python

   >>> print(INPUT(_type='checkbox', _name='test', _value='a', _checked=True))
   <input checked="checked" name="test" type="checkbox" value="a"/>
   >>> print(INPUT(_type='checkbox', _name='test', _value='a', _checked=False))
   <input name="test" type="checkbox" value="a"/>

``LABEL``
~~~~~~~~~

It is used to create a LABEL tag for an INPUT field.

.. code:: python

   >>> print(LABEL('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <label id="0" class="test">&lt;hello&gt;<strong>world</strong></label>

``LI``
~~~~~~

It makes a list item and should be contained in a ``UL`` or ``OL`` tag.

.. code:: python

   >>> print(LI('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <li id="0" class="test">&lt;hello&gt;<strong>world</strong></li>

``OL``
~~~~~~

It stands for ordered list. The list should contain LI tags.

.. code:: python

   >>> print(OL(LI('<hello>'), LI(XML('<strong>world</strong>')), _class='test', _id=0))
   <ol class="test" id="0"><li>&lt;hello&gt;</li><li><strong>world</strong></li></ol>

``OPTION``
~~~~~~~~~~

This should only be used as argument of a ``SELECT``.

.. code:: python

   >>> print(OPTION('<hello>', XML('<strong>world</strong>'), _value='a'))
   <option value="a">&lt;hello&gt;<strong>world</strong></option>

For selected options use the ``_selected`` attribute:

.. code:: python

   >>> print(OPTION('Thank You', _value='ok', _selected=True))
   <option selected="selected" value="ok">Thank You</option>

``P``
~~~~~

This is for tagging a paragraph.

.. code:: python

   >>> print(P('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <p id="0" class="test">&lt;hello&gt;<strong>world</strong></p>

``PRE``
~~~~~~~

Generates a ``<pre>...</pre>`` tag for displaying pre-formatted text.
The ``CODE`` helper is generally preferable for code listings.

.. code:: python

   >>> print(SELECT(OPTION('first', _value='1'), OPTION('second', _value='2'), _class='test', _id=0))
   <pre id="0" class="test">&lt;hello&gt;<strong>world</strong></pre>

``SCRIPT``
~~~~~~~~~~

This is for include or link a script, such as JavaScript.

.. code:: python

   >>> print(SCRIPT('console.log("hello world");', _type='text/javascript'))
   <script type="text/javascript">console.log("hello world");</script>

``SELECT``
~~~~~~~~~~

Makes a ``<select>...</select>`` tag. This is used with the ``OPTION``
helper.

.. code:: python

   >>> print(SELECT(OPTION('first', _value='1'), OPTION('second', _value='2'),
   ... _class='test', _id=0))
   <select class="test" id="0"><option value="1">first</option><option value="2">second</option></select>

``SPAN``
~~~~~~~~

Similar to ``DIV`` but used to tag inline (rather than block) content.

.. code:: python

   >>> print(SPAN('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <span id="0" class="test">&lt;hello&gt;<strong>world</strong></span>

``STYLE``
~~~~~~~~~

Similar to script, but used to either include or link CSS code. Here the
CSS is included:

.. code:: python

   >>> print(STYLE(XML('body {color: white}')))
   <style>body {color: white}</style>

and here it is linked:

.. code:: python

   >>> print(STYLE(_src='style.css'))
   <style src="style.css"></style>

``TABLE``, ``TR``, ``TD``
~~~~~~~~~~~~~~~~~~~~~~~~~

These tags (along with the optional ``THEAD`` and ``TBODY`` helpers) are
used to build HTML tables.

.. code:: python

   >>> print(TABLE(TR(TD('a'), TD('b')), TR(TD('c'), TD('d'))))
   <table><tr><td>a</td><td>b</td></tr><tr><td>c</td><td>d</td></tr></table>

``TR`` expects ``TD`` content.

It is easy to convert a Python array into an HTML table using Python’s
``*`` function arguments notation, which maps list elements to
positional function arguments.

Here, we will do it line by line:

.. code:: python

   >>> table = [['a', 'b'], ['c', 'd']]
   >>> print(TABLE(TR(*map(TD, table[0])), TR(*map(TD, table[1]))))
   <table><tr><td>a</td><td>b</td></tr><tr><td>c</td><td>d</td></tr></table>

Here we do all lines at once:

.. code:: python

   >>> table = [['a', 'b'], ['c', 'd']]
   >>> print(TABLE(*[TR(*map(TD, rows)) for rows in table]))
   <table><tr><td>a</td><td>b</td></tr><tr><td>c</td><td>d</td></tr></table>

``TBODY``
~~~~~~~~~

This is used to tag rows contained in the table body, as opposed to
header or footer rows. It is optional.

.. code:: python

   >>> print(TBODY(TR(TD('<hello>')), _class='test', _id=0))
   <tbody id="0" class="test"><tr><td>&lt;hello&gt;</td></tr></tbody>

``TEXTAREA``
~~~~~~~~~~~~

This helper makes a ``<textarea>...</textarea>`` tag.

.. code:: python

   >>> print(TEXTAREA('<hello>', XML('<strong>world</strong>'), _class='test',
   ... _cols="40", _rows="10"))
   <textarea class="test" cols="40" rows="10">&lt;hello&gt;<strong>world</strong></textarea>

``TH``
~~~~~~

This is used instead of ``TD`` in table headers.

.. code:: python

   >>> print(TH('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <th id="0" class="test">&lt;hello&gt;<strong>world</strong></th>

``THEAD``
~~~~~~~~~

This is used to tag table header rows.

.. code:: python

   >>> print(THEAD(TR(TH('<hello>')), _class='test', _id=0))
   <thead id="0" class="test"><tr><th>&lt;hello&gt;</th></tr></thead>

``TITLE``
~~~~~~~~~

This is used to tag the title of a page in an HTML header.

.. code:: python

   >>> print(TITLE('<hello>', XML('<strong>world</strong>')))
   <title>&lt;hello&gt;<strong>world</strong></title>

``TT``
~~~~~~

Tags text as typewriter (monospaced) text.

.. code:: python

   >>> print(TT('<hello>', XML('<strong>world</strong>'), _class='test', _id=0))
   <tt id="0" class="test">&lt;hello&gt;<strong>world</strong></tt>

``UL``
~~~~~~

It stands for unordered list. The list should contain LI tags.

.. code:: python

   >>> print(UL(LI('<hello>'), LI(XML('<strong>world</strong>')), _class='test', _id=0))
   <ul class="test" id="0"><li>&lt;hello&gt;</li><li><strong>world</strong></li></ul>

``URL``
~~~~~~~

.. FIXME: maybe this section should go in another chapter

The URL helper is not part of yatl package, instead it is provided by py4web.

Custom helpers
--------------

.. _TAG:

``TAG``
~~~~~~~

Sometimes you need to generate **custom XML tags***. For this purpose py4web
provides ``TAG``, a universal tag generator.

::

   [[=TAG.name('a', 'b', _c='d')]]

generates the following XML:

.. code:: xml

   <name c="d">ab</name>

Arguments “a”, “b”, and “d” are automatically escaped; use the ``XML``
helper to suppress this behavior. Using ``TAG`` you can generate
HTML/XML tags not already provided by the API. TAGs can be nested, and
are serialized with ``str().`` An equivalent syntax is:

::

   [[=TAG['name']('a', 'b', _c='d')]]

Self-closing tags can be generated with the TAG helper. The tag name
must end with a “/”.

::

   [[=TAG['link/'](_href='http://py4web.com')]]

generates the following XML:

.. code:: xml

   <link ref="http://py4web.com"/>

Notice that ``TAG`` is an object, and ``TAG.name`` or ``TAG['name']`` is
a function that returns an helper instance.

``BEAUTIFY``
~~~~~~~~~~~~

``BEAUTIFY`` is used to build HTML representations of compound objects,
including lists, tuples and dictionaries:

::

   [[=BEAUTIFY({"a": ["hello", STRONG("world")], "b": (1, 2)})]]

``BEAUTIFY`` returns an XML-like object serializable to XML, with a nice
looking representation of its constructor argument. In this case, the
XML representation of:

.. code:: python

   {"a": ["hello", STRONG("world")], "b": (1, 2)}

will render as:

.. code:: html

   <table><tbody>
   <tr><th>a</th><td><ul><li>hello</li><li><strong>world</strong></li></ul></td></tr>
   <tr><th>b</th><td>(1, 2)</td></tr>
   </tbody></table>

Server-side *DOM*
-----------------

As we've already seen the helpers mechanism in py4web also provides a server-side representation of the document object model (DOM).

``children``
~~~~~~~~~~~~

Each helper object keep the list of its components into the ``children``
attribute.

.. code:: python

   >>> CAT('hello', STRONG('world')).children
   ['hello', <yatl.helpers.TAGGER object at 0x7fa533ff7640>]

``find``
~~~~~~~~

To help searching into the DOM, all helpers have a ``find`` method with
the following signature:

.. code:: python

   def find(self, query=None, **kargs)

that returns all the components matching supplied arguments.

A very simple ``query`` can be a tag name:

.. code:: python

   >>> a = DIV(DIV(SPAN('x'), 3, DIV(SPAN('y'))))
   >>> for c in a.find('span', first_only=True): c[0]='z'
   >>> print(a)  # We should .xml() here instead of print
   <div><div><span>z</span>3<div><span>y</span></div></div></div>
   >>> for c in a.find('span'): c[0]='z'
   >>> print(a)
   <div><div><span>z</span>3<div><span>z</span></div></div></div>

It also supports a syntax compatible with `jQuery <https://api.jquery.com/>`__,
accepting the following expressions:

- `jQuery Multiple Selector <https://api.jquery.com/multiple-selector/>`__,
  e.g. “selector1, selector2, selectorN”,
- `jQuery Descendant Selector <https://api.jquery.com/descendant-selector/>`__,
  e.g. “ancestor descendant”,
- `jQuery ID Selector <https://api.jquery.com/id-selector/>`__, e.g. “#id”,
- `jQuery Class Selector <https://api.jquery.com/class-selector/>`__,
  e.g. “.class”, and
- `jQuery Attribute Equals Selector <https://api.jquery.com/attribute-equals-selector/>`__,
  e.g. “[name=value]”, notice that here the value must be unquoted.

Here are some examples:

.. code:: python

   >>> a = DIV(SPAN(A('hello', **{'_id': '1-1', '_u:v': '$'})), P('world', _class='this is a test'))
   >>> for e in a.find('div a#1-1, p.is'): print(e)
   <a id="1-1" u:v="$">hello</a>
   <p class="this is a test">world</p>
   >>> for e in a.find('#1-1'): print(e)
   <a id="1-1" u:v="$">hello</a>
   >>> a.find('a[u:v=$]')[0].xml()
   '<a id="1-1" u:v="$">hello</a>'
   >>> a = FORM(INPUT(_type='text'), SELECT(OPTION(0)), TEXTAREA())
   >>> for c in a.find('input, select, textarea'): c['_disabled'] = True
   >>> a.xml()
   '<form><input disabled="disabled" type="text"/><select disabled="disabled"><option>0</option></select><textarea disabled="disabled"></textarea></form>'
   >>> for c in a.find('input, select, textarea'): c['_disabled'] = False
   >>> a.xml()
   '<form><input type="text"/><select><option>0</option></select><textarea></textarea></form>'

Elements that are matched can also be replaced or removed by specifying
a ``replace`` argument (note, a list of the original matching elements
is still returned as usual).

.. code:: python

   >>> a = DIV(DIV(SPAN('x', _class='abc'), DIV(SPAN('y', _class='abc'), SPAN('z', _class='abc'))))
   >>> b = a.find('span.abc', replace=P('x', _class='xyz'))
   >>> print(a)
   <div><div><p class="xyz">x</p><div><p class="xyz">x</p><p class="xyz">x</p></div></div></div>

``replace`` can be a callable, which will be passed the original element and
should return a new element to replace it.

.. code:: python

   >>> a = DIV(DIV(SPAN('x', _class='abc'), DIV(SPAN('y', _class='abc'), SPAN('z', _class='abc'))))
   >>> b = a.find('span.abc', replace=lambda el: P(el[0], _class='xyz'))
   >>> print(a)
   <div><div><p class="xyz">x</p><div><p class="xyz">y</p><p class="xyz">z</p></div></div></div>

If ``replace=None``, matching elements will be removed completely.

.. code:: python

   >>> a = DIV(DIV(SPAN('x', _class='abc'), DIV(SPAN('y', _class='abc'), SPAN('z', _class='abc'))))
   >>> b = a.find('span', text='y', replace=None)
   >>> print(a)
   <div><div><span class="abc">x</span><div><span class="abc"></span><span class="abc">z</span></div></div></div>

If a ``text`` argument is specified, elements will be searched for text
components that match text, and any matching text components will be
replaced (``text`` is ignored if ``replace`` is not also specified, use
a ``find`` argument when you only need searching for textual elements).

Like the ``find`` argument, ``text`` can be a string or a compiled regex.

.. code:: python

   >>> a = DIV(DIV(SPAN('x', _class='abc'), DIV(SPAN('y', _class='abc'), SPAN('z', _class='abc'))))
   >>> b = a.find(text=re.compile('x|y|z'), replace='hello')
   >>> print(a)
   <div><div><span class="abc">hello</span><div><span class="abc">hello</span><span class="abc">hello</span></div></div></div>

If other attributes are specified along with ``text``, then only components
that match the specified attributes will be searched for text.

.. code:: python

   >>> a = DIV(DIV(SPAN('x', _class='abc'), DIV(SPAN('y', _class='efg'), SPAN('z', _class='abc'))))
   >>> b = a.find('span.efg', text=re.compile('x|y|z'), replace='hello')
   >>> print(a)
   <div><div><span class="abc">x</span><div><span class="efg">hello</span><span class="abc">z</span></div></div></div>

Using Inject
------------

Normally all the code should be called from the controller program, and only the
necessary data is passed to the template in order to be displayed.
But sometimes it's useful to pass variables or even use a python function as a helper called from a template.

In this case you can use the fixture ``Inject`` from py4web.utils.factories.

This is a simple example for injecting a variable:

.. code:: python

   from py4web.utils.factories import Inject

   my_var = "Example variable to be passed to a Template"

   ...

   @unauthenticated("index", "index.html")
   @action.uses(Inject(my_var=my_var))
   def index():

      ...


Then in ``index.html`` you can use the injected variable:

.. code:: html

   [[=my_var]]


You can also use ``Inject`` to add variables to the auth.enable line;
in this way auth forms would have access to that variable.

.. code:: python

   auth.enable(uses=(session, T, db, Inject(TIMEOFFSET=settings.TIMEOFFSET)))

A more complex usage of Inject is for passing python functions to templates.
For example if your helper function is called *sidebar_menu*
and it's inside the libs/helpers.py module of your app, you could use this in **controllers.py**:

.. code:: python

   from py4web.utils.factories import Inject
   from .libs.helpers import sidebar_menu

   @action(...)
   @action.uses(Inject(sidebar_menu=sidebar_menu), "index.html")
   def index(): ....

OR

.. code:: python

   from py4web.utils.factories import Inject
   from .libs import helpers

   @action(...)
   @action.uses(Inject(**vars(helpers)), "index.html")
   def index(): ....


Then you can import the needed code in the index.html template in a clean way:

.. code:: html

   [[=sidebar_menu]]

