============
YATL helpers
============

Consider the following code in a view:

.. code:: html

   [[=DIV('this', 'is', 'a', 'test', _id='123', _class='myclass')]]

it is rendered as:

.. code:: html

   <div id="123" class="myclass">thisisatest</div>

``DIV`` is a helper class, i.e., something that can be used to build
HTML programmatically. It corresponds to the HTML ``<div>`` tag.

Positional arguments are interpreted as objects contained between the
open and close tags. Named arguments that start with an underscore are
interpreted as HTML tag attributes (without the underscore). Some
helpers also have named arguments that do not start with underscore;
these arguments are tag-specific.

Instead of a set of unnamed arguments, a helper can also take a single
list or tuple as its set of components using the ``*`` notation and it
can take a single dictionary as its set of attributes using the ``**``,
for example:

.. code:: html

   [[
   contents = ['this', 'is', 'a', 'test']
   attributes = {'_id':'123', '_class':'myclass'}
   =DIV(*contents, **attributes)
   ]]

(produces the same output as before).

The following set of helpers:

``A``, ``BEAUTIFY``, ``BODY``, ``CAT``, ``CODE``, ``DIV``, ``EM``,
``FORM``, ``H1``, ``H2``, ``H3``, ``H4``, ``H5``, ``H6``, ``HEAD``,
``HTML``, ``IMG``, ``INPUT``, ``LABEL``, ``LI``, ``METATAG``,
``OL``, ``OPTION``, ``P``, ``PRE``, ``SELECT``, ``SPAN``, ``STRONG``,
``TABLE``, ``TAG``, ``TAGGER``, ``THEAD``, ``TBODY``, ``TD``,
``TEXTAREA``, ``TH``, ``TT``, ``TR``, ``UL``, ``XML``, ``xmlescape``,
``I``, ``META``, ``LINK``, ``TITLE``, ``STYLE``, ``SCRIPT``

can be used to build complex expressions that can then be serialized to
XML. For example:

.. code:: html

   [[=DIV(STRONG(I("hello ", "<world>")), _class="myclass")]]

is rendered:

.. code:: html

   <div class="myclass"><strong><i>hello &lt;world&gt;</i></strong></div>

Helpers can also be serialized into strings, equivalently, with the
``__str__`` and the ``xml`` methods:

.. code:: python

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
``a.components``, and the complete set of attributes can be accessed via
a dictionary called ``a.attributes``. So, ``a[i]`` is equivalent to
``a.components[i]`` when ``i`` is an integer, and ``a[s]`` is equivalent
to ``a.attributes[s]`` when ``s`` is a string.

Notice that helper attributes are passed as keyword arguments to the
helper. In some cases, however, attribute names include special
characters that are not allowed in Python identifiers (e.g., hyphens)
and therefore cannot be used as keyword argument names. For example:

.. code:: python

   DIV('text', _data-role='collapsible')

will not work because "_data-role" includes a hyphen, which will produce
a Python syntax error.

In such cases you have a couple of options. You can use the ``data``
argument (this time without a leading underscore) to pass a dictionary
of related attributes without their leading hyphen, and the output will
have the desired combinations e.g.

.. code:: python

   >>> print(DIV('text', data={'role': 'collapsible'}))
   <div data-role="collapsible">text</div>

or you can instead pass the attributes as a dictionary and make use of
Python’s ``**`` function arguments notation, which maps a dictionary of
(key:value) pairs into a set of keyword arguments:

.. code:: python

   >>> print(DIV('text', **{'_data-role': 'collapsible'}))
   <div data-role="collapsible">text</div>

Note that more elaborate entries will introduce HTML character entities,
but they will work nonetheless e.g.

.. code:: python

   >>> print(DIV('text', data={'options':'{"mode":"calbox", "useNewStyle":true}'}))
   <div data-options="{&quot;mode&quot;:&quot;calbox&quot;, &quot;useNewStyle&quot;:true}">text</div>

You can also dynamically create special TAGs:

.. code:: python

   >>> print(TAG['soap:Body']('whatever', **{'_xmlns:m':'http://www.example.org'}))
   <soap:Body xmlns:m="http://www.example.org">whatever</soap:Body>


``XML``
-------

``XML`` is an object used to encapsulate text that should not be
escaped. The text may or may not contain valid XML. For example, it
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

The py4web ``XML`` helper can sanitize our text to prevent injections
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


Built-in helpers
----------------

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

This helper concatenates other helpers, same as TAG[''].

.. code:: python

   >>> print(CAT('Here is a ', A('link', _href='target'), ', and here is some ', STRONG('bold text'), '.'))
   Here is a <a href="target">link</a>, and here is some <strong>bold text</strong>.

``DIV``
~~~~~~~

All helpers apart from ``XML`` are derived from ``DIV`` and inherit its
basic methods.

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

This is one of the most important helpers. In its simple form, it just
makes a ``<form>...</form>`` tag, but because helpers are objects and
have knowledge of what they contain, they can process submitted forms
(for example, perform validation of the fields). This will be discussed
in detail in `Chapter 12 <#chapter-12>`__.

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

.. FIXME: URL('static', ...) is broken on py4web shell

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

This is include or link a script, such as JavaScript.

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

Sometimes you need to generate custom XML tags. py4web provides ``TAG``,
a universal tag generator.

.. code:: html

   [[=TAG.name('a', 'b', _c='d')]]

generates the following XML

.. code:: xml

   <name c="d">ab</name>

Arguments “a”, “b”, and “d” are automatically escaped; use the ``XML``
helper to suppress this behavior. Using ``TAG`` you can generate
HTML/XML tags not already provided by the API. TAGs can be nested, and
are serialized with ``str().`` An equivalent syntax is:

.. code:: html

   [[=TAG['name']('a', 'b', _c='d')]]

If the TAG object is created with an empty name, it can be used to
concatenate multiple strings and HTML helpers together without inserting
them into a surrounding tag, but this use is deprecated. Use the ``CAT``
helper instead.

Self-closing tags can be generated with the TAG helper. The tag name
must end with a “/”.

.. code:: html

   [[=TAG['link/'](_href='http://py4web.com')]]

generates the following XML:

.. code:: xml

   <link ref="http://py4web.com"/>

Notice that ``TAG`` is an object, and ``TAG.name`` or ``TAG['name']`` is
a function that returns a temporary helper class.

``BEAUTIFY``
------------

``BEAUTIFY`` is used to build HTML representations of compound objects,
including lists, tuples and dictionaries:

.. code:: html

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

Server-side *DOM* and parsing
-----------------------------

.. FIXME: review needed

``elements``
~~~~~~~~~~~~

The DIV helper and all derived helpers provide the search methods
``element`` and ``elements``.

``element`` returns the first child element matching a specified
condition (or None if no match).

``elements`` returns a list of all matching children.

**element** and **elements** use the same syntax to specify the matching
condition, which allows for three possibilities that can be mixed and
matched: jQuery-like expressions, match by exact attribute value, match
using regular expressions.

Here is a simple example:

.. code:: python

   >>> a = DIV(DIV(DIV('a', _id='target', _class='abc')))
   >>> d = a.elements('div#target')
   >>> d[0][0] = 'changed'
   >>> print a
   <div><div><div id="target" class="abc">changed</div></div></div>

The un-named argument of ``elements`` is a string, which may contain:
the name of a tag, the id of a tag preceded by a pound symbol, the class
preceded by a dot, the explicit value of an attribute in square
brackets.

Here are 4 equivalent ways to search the previous tag by id:

.. code:: python

   d = a.elements('#target')
   d = a.elements('div#target')
   d = a.elements('div[id=target]')
   d = a.elements('div', _id='target')

Here are 4 equivalent ways to search the previous tag by class:

.. code:: python

   d = a.elements('.abc')
   d = a.elements('div.abc')
   d = a.elements('div[class=abc]')
   d = a.elements('div', _class='abc')

Any attribute can be used to locate an element (not just ``id`` and
``class``), including multiple attributes (the function element can take
multiple named arguments), but only the first matching element will be
returned.

Using the jQuery syntax “div#target” it is possible to specify multiple
search criteria separated by a comma:

.. code:: python

   a = DIV(SPAN('a', _id='t1'), DIV('b', _class='c2'))
   d = a.elements('span#t1, div.c2')

or equivalently

.. code:: python

   a = DIV(SPAN('a', _id='t1'), DIV('b', _class='c2'))
   d = a.elements('span#t1', 'div.c2')

If the value of an attribute is specified using a name argument, it can
be a string or a regular expression:

.. code:: python

   a = DIV(SPAN('a', _id='test123'), DIV('b', _class='c2'))
   d = a.elements('span', _id=re.compile('test\d{3}')

A special named argument of the DIV (and derived) helpers is ``find``.
It can be used to specify a search value or a search regular expression
in the text content of the tag. For example:

.. code:: python

   >>> a = DIV(SPAN('abcde'), DIV('fghij'))
   >>> d = a.elements(find='bcd')
   >>> print d[0]
   <span>abcde</span>

or

.. code:: python

   >>> a = DIV(SPAN('abcde'), DIV('fghij'))
   >>> d = a.elements(find=re.compile('fg\w{3}'))
   >>> print d[0]
   <div>fghij</div>

``components``
~~~~~~~~~~~~~~

Here’s an example of listing all elements in an html string:

.. code:: python

   >>> html = TAG('<a>xxx</a><b>yyy</b>')
   >>> for item in html.components:
   ...     print item
   ... 
   <a>xxx</a>
   <b>yyy</b>

``parent`` and ``siblings``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``parent`` returns the parent of the current element.

.. code:: python

   >>> a = DIV(SPAN('a'), DIV('b'))
   >>> s = a.element('span')
   >>> d = s.parent
   >>> d['_class']='abc'
   >>> print a
   <div class="abc"><span>a</span><div>b</div></div>
   >>> for e in s.siblings(): print e
   <div>b</div>

Replacing elements
~~~~~~~~~~~~~~~~~~

Elements that are matched can also be replaced or removed by specifying
the ``replace`` argument. Notice that a list of the original matching
elements is still returned as usual.

.. code:: python

   >>> a = DIV(SPAN('x'), DIV(SPAN('y'))
   >>> b = a.elements('span', replace=P('z')
   >>> print a
   <div><p>z</p><div><p>z</p></div>

``replace`` can be a callable. In this case it will be passed the
original element and it is expected to return the replacement element:

.. code:: python

   >>> a = DIV(SPAN('x'), DIV(SPAN('y'))
   >>> b = a.elements('span', replace=lambda t: P(t[0])
   >>> print a
   <div><p>x</p><div><p>y</p></div>

If ``replace=None``, matching elements will be removed completely.

.. code:: python

   >>> a = DIV(SPAN('x'), DIV(SPAN('y'))
   >>> b = a.elements('span', replace=None)
   >>> print a
   <div></div>

``flatten``
~~~~~~~~~~~

The flatten method recursively serializes the content of the children of
a given element into regular text (without tags):

.. code:: python

   >>> a = DIV(SPAN('this', DIV('is', STRONG('a'))), SPAN('test'))
   >>> print a.flatten()
   thisisatest

Flatten can be passed an optional argument, ``render``, i.e. a function
that renders/flattens the content using a different protocol. Here is an
example to serialize some tags into Markmin wiki syntax:

.. code:: python

   >>> a = DIV(H1('title'), P('example of a ', A('link', _href='#test')))
   >>> from gluon.html import markmin_serializer
   >>> print a.flatten(render=markmin_serializer)
   # titles

   example of *a link * 

At the time of writing we provide ``markmin_serializer`` and
``markdown_serializer``.

Parsing
~~~~~~~

The TAG object is also an XML/HTML parser. It can read text and convert
into a tree structure of helpers. This allows manipulation using the API
above:

.. code:: python

   >>> html = '<h1>Title</h1><p>this is a <span>test</span></p>'
   >>> parsed_html = TAG(html)
   >>> parsed_html.element('span')[0]='TEST'
   >>> print parsed_html
   <h1>Title</h1><p>this is a <span>TEST</span></p>

Page layout
-----------

Views can extend and include other views in a tree-like structure.

For example, we can think of a view “index.html” that extends
“layout.html” and includes “body.html”. At the same time, “layout.html”
may include “header.html” and “footer.html”.

The root of the tree is what we call a layout view. Just like any other
HTML template file, you can edit it using the py4web administrative
interface. The file name “layout.html” is just a convention.

Here is a minimalist page that extends the “layout.html” view and
includes the “page.html” view:

.. code:: python

   [[extend 'layout.html']]
   <h1>Hello World</h1>
   [[include 'page.html']]

The extended layout file must contain an ``[[include]]`` directive,
something like:

.. code:: python

   <html>
     <head>
       <title>Page Title</title>
     </head>
     <body>
       [[include]]
     </body>
   </html>

When the view is called, the extended (layout) view is loaded, and the
calling view replaces the ``[[include]]`` directive inside the layout.
Processing continues recursively until all ``extend`` and ``include``
directives have been processed. The resulting template is then
translated into Python code. Note, when an application is bytecode
compiled, it is this Python code that is compiled, not the original view
files themselves. So, the bytecode compiled version of a given view is a
single .pyc file that includes the Python code not just for the original
view file, but for its entire tree of extended and included views.

   ``extend``, ``include``, ``block`` and ``super`` are special template
   directives, not Python commands.

Any content or code that precedes the ``[[extend ...]]`` directive will
be inserted (and therefore executed) before the beginning of the
extended view’s content/code. Although this is not typically used to
insert actual HTML content before the extended view’s content, it can be
useful as a means to define variables or functions that you want to make
available to the extended view. For example, consider a view
“index.html”:

.. code:: python

   [[sidebar_enabled=True]]
   [[extend 'layout.html']]
   <h1>Home Page</h1>

and an excerpt from “layout.html”:

.. code:: python

   [[if sidebar_enabled:]]
       <div id="sidebar">
           Sidebar Content
       </div>
   [[pass]]

Because the ``sidebar_enabled`` assignment in “index.html” comes before
the ``extend``, that line gets inserted before the beginning of
“layout.html”, making ``sidebar_enabled`` available anywhere within the
“layout.html” code (a somewhat more sophisticated version of this is
used in the **welcome** app).

It is also worth pointing out that the variables returned by the
controller function are available not only in the function’s main view,
but in all of its extended and included views as well.

The argument of an ``extend`` or ``include`` (i.e., the extended or
included view name) can be a Python variable (though not a Python
expression). However, this imposes a limitation – views that use
variables in ``extend`` or ``include`` statements cannot be bytecode
compiled. As noted above, bytecode-compiled views include the entire
tree of extended and included views, so the specific extended and
included views must be known at compile time, which is not possible if
the view names are variables (whose values are not determined until run
time). Because bytecode compiling views can provide a significant speed
boost, using variables in ``extend`` and ``include`` should generally be
avoided if possible.

In some cases, an alternative to using a variable in an ``include`` is
simply to place regular ``[[include ...]]`` directives inside an
``if...else`` block.

.. code:: html

   [[if some_condition:]]
   [[include 'this_view.html']]
   [[else:]]
   [[include 'that_view.html']]
   [[pass]]

The above code does not present any problem for bytecode compilation
because no variables are involved. Note, however, that the bytecode
compiled view will actually include the Python code for both
“this_view.html” and “that_view.html”, though only the code for one of
those views will be executed, depending on the value of
``some_condition``.

Keep in mind, this only works for ``include`` – you cannot place
``[[extend ...]]`` directives inside ``if...else`` blocks.

Layouts are used to encapsulate page commonality (headers, footers,
menus), and though they are not mandatory, they will make your
application easier to write and maintain. In particular, we suggest
writing layouts that take advantage of the following variables that can
be set in the controller. Using these well known variables will help
make your layouts interchangeable:

::

   response.title
   response.subtitle
   response.meta.author
   response.meta.keywords
   response.meta.description
   response.flash
   response.menu
   response.files

Except for ``menu`` and ``files``, these are all strings and their
meaning should be obvious.

``response.menu`` menu is a list of 3-tuples or 4-tuples. The three
elements are: the link name, a boolean representing whether the link is
active (is the current link), and the URL of the linked page. For
example:

.. code:: python

   response.menu = [('Google', False, 'http://www.google.com', []),
                    ('Index',  True,  URL('index'), [])]

The fourth tuple element is an optional sub-menu.

``response.files`` is a list of CSS and JS files that are needed by your
page.

We also recommend that you use:

.. code:: html

   [[include 'py4web_ajax.html']]

in the HTML head, since this will include the jQuery libraries and
define some backward-compatible JavaScript functions for special effects
and Ajax. “py4web_ajax.html” includes the ``response.meta`` tags in the
view, jQuery base, the calendar datepicker, and all required CSS and JS
``response.files``.

Default page layout
~~~~~~~~~~~~~~~~~~~

The “views/layout.html” that ships with the py4web scaffolding
application **welcome** (stripped down of some optional parts) is quite
complex but it has the following structure:

.. code:: html

   <!DOCTYPE html>
   <head>
     <meta charset="utf-8" />
     <title>[[=response.title or request.application]]</title>
     ...
     <script src="[[=URL('static', 'js/modernizr.custom.js')]]"></script>

     [[
     response.files.append(URL('static', 'css/py4web.css'))
     response.files.append(URL('static', 'css/bootstrap.min.css'))
     response.files.append(URL('static', 'css/bootstrap-responsive.min.css'))
     response.files.append(URL('static', 'css/py4web_bootstrap.css'))
     ]]

     [[include 'py4web_ajax.html']]

     [[
     # using sidebars need to know what sidebar you want to use
     left_sidebar_enabled = globals().get('left_sidebar_enabled', False)
     right_sidebar_enabled = globals().get('right_sidebar_enabled', False)
     middle_columns = {0:'span12', 1:'span9', 2:'span6'}[
       (left_sidebar_enabled and 1 or 0)+(right_sidebar_enabled and 1 or 0)]
     ]]

     [[block head]][[end]]
   </head>

   <body>
     <!-- Navbar ================================================== -->
     <div class="navbar navbar-inverse navbar-fixed-top">
       <div class="flash">[[=response.flash or '']]</div>
       <div class="navbar-inner">
         <div class="container">
           [[=response.logo or '']]
           <ul id="navbar" class="nav pull-right">
             [[='auth' in globals() and auth.navbar(mode="dropdown") or '']]
           </ul>
           <div class="nav-collapse">
             [[if response.menu:]]
             [[=MENU(response.menu)]]
             [[pass]]
           </div><!--/.nav-collapse -->
         </div>
       </div>
     </div><!--/top navbar -->

     <div class="container">
       <!-- Masthead ================================================== -->
       <header class="mastheader row" id="header">
           <div class="span12">
               <div class="page-header">
                   <h1>
                       [[=response.title or request.application]]
                       <small>[[=response.subtitle or '']]</small>
                   </h1>
               </div>
           </div>
       </header>

       <section id="main" class="main row">
           [[if left_sidebar_enabled:]]
           <div class="span3 left-sidebar">
               [[block left_sidebar]]
               <h3>Left Sidebar</h3>
               <p></p>
               [[end]]
           </div>
           [[pass]]

           <div class="[[=middle_columns]]">
               [[block center]]
               [[include]]
               [[end]]
           </div>

           [[if right_sidebar_enabled:]]
           <div class="span3">
               [[block right_sidebar]]
               <h3>Right Sidebar</h3>
               <p></p>
               [[end]]
           </div>
           [[pass]]
       </section><!--/main-->

       <!-- Footer ================================================== -->
       <div class="row">
           <footer class="footer span12" id="footer">
               <div class="footer-content">
                   [[block footer]] <!-- this is default footer -->
                   ...
                   [[end]]
               </div>
           </footer>
       </div>

     </div> <!-- /container -->

     <!-- The javascript =============================================
          (Placed at the end of the document so the pages load faster) -->
     <script src="[[=URL('static', 'js/bootstrap.min.js')]]"></script>
     <script src="[[=URL('static', 'js/py4web_bootstrap.js')]]"></script>
     [[if response.google_analytics_id:]]
       <script src="[[=URL('static', 'js/analytics.js')]]"></script>
       <script type="text/javascript">
       analytics.initialize({
         'Google Analytics':{trackingId:'[[=response.google_analytics_id]]'}
       });</script>
     [[pass]]
   </body>
   </html>

There are a few features of this default layout that make it very easy
to use and customize:

-  It is written in HTML5 and uses the “modernizr” library for backward
   compatibility. The actual layout includes some extra conditional
   statements required by IE and they are omitted for brevity.
-  It displays both ``response.title`` and ``response.subtitle`` which
   can be set in a model or a controller. If they are not set, it adopts
   the application name as title.
-  It includes the ``py4web_ajax.html`` file in the header which
   generated all the link and script import statements.
-  It uses a modified version of Twitter Bootstrap for flexible layouts
   which works on mobile devices and re-arranges columns to fit small
   screens.
-  It uses “analytics.js” to connect to Google Analytics.
-  The ``[[=auth.navbar(...)]]`` displays a welcome to the current user
   and links to the auth functions like login, logout, register, change
   password, etc. depending on context. ``auth.navbar`` is a helper
   factory and its output can be manipulated as any other helper. It is
   placed in an expression to check for auth definition, the expression
   evaluates to ’’ in case auth is undefined.
-  The ``[[=MENU(response.menu)]]`` displays the menu structure as
   ``<ul>...</ul>``.
-  ``[[include]]`` is replaced by the content of the extending view when
   the page is rendered.
-  By default it uses a conditional three column (the left and right
   sidebars can be turned off by the extending views)
-  It uses the following classes: page-header, main, footer.
-  It contains the following blocks: head, left_sidebar, center,
   right_sidebar, footer.

In views, you can turn on and customize sidebars as follows:

.. code:: html

   [[left_sidebar_enabled=True]]
   [[extend 'layout.html']]

   This text goes in center

   [[block left_sidebar]]
   This text goes in sidebar
   [[end]]

Customizing the default layout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Customizing the default layout without editing is easy because the
welcome application is based on Twitter Bootstrap which is well
documented and supports themes. In py4web four static files which are
relevant to style:

-  “css/py4web.css” contains py4web specific styles
-  “css/bootstrap.min.css” contains the Twitter Bootstrap CSS style
-  “css/py4web_bootstrap.css” which overrides some Bootstrap styles to
   conform to py4web needs.
-  “js/bootstrap.min.js” which includes the libraries for menu effects,
   modals, panels.

To change colors and background images, try append the following code to
layout.html header:

.. code:: css

   <style>
   body { background: url('images/background.png') repeat-x #3A3A3A; }
   a { color: #349C01; }
   .page-header h1 { color: #349C01; }
   .page-header h2 { color: white; font-style: italic; font-size: 14px;}
   .statusbar { background: #333333; border-bottom: 5px #349C01 solid; }
   .statusbar a { color: white; }
   .footer { border-top: 5px #349C01 solid; }
   </style>

Of course you can also completely replace the “layout.html” and
“py4web.css” files with your own.

Mobile development
~~~~~~~~~~~~~~~~~~

Although the default layout.html is designed to be mobile-friendly, one
may sometimes need to use different views when a page is visited by a
mobile device.

To make developing for desktop and mobile devices easier, py4web
includes the ``@mobilize`` decorator. This decorator is applied to
actions that should have a normal view and a mobile view. This is
demonstrated here:

.. code:: python

   from gluon.contrib.user_agent_parser import mobilize
   @mobilize
   def index():
       return dict()

Notice that the decorator must be imported before using it in a
controller. When the “index” function is called from a regular browser
(desktop computer), py4web will render the returned dictionary using the
view “[controller]/index.html”. However, when it is called by a mobile
device, the dictionary will be rendered by
“[controller]/index.mobile.html”. Notice that mobile views have the
“mobile.html” extension.

Alternatively you can apply the following logic to make all views mobile
friendly:

.. code:: python

   if request.user_agent().is_mobile:
       response.view.replace('.html', '.mobile.html')

The task of creating the "\*.mobile.html" views is left to the developer
but we strongly suggest using the “jQuery Mobile” plugin which makes the
task very easy.

Functions in views
------------------

Consider this “layout.html”:

.. code:: python

   <html>
     <body>
       [[include]]
       <div class="sidebar">
         [[if 'mysidebar' in globals():]][[mysidebar()]][[else:]]
           my default sidebar
         [[pass]]
       </div>
     </body>
   </html>

and this extending view

.. code:: html

   [[def mysidebar():]]
   my new sidebar!!!
   [[return]]
   [[extend 'layout.html']]
   Hello World!!!

Notice the function is defined before the ``[[extend...]]`` statement –
this results in the function being created before the “layout.html” code
is executed, so the function can be called anywhere within
“layout.html”, even before the ``[[include]]``. Also notice the function
is included in the extended view without the ``=`` prefix.

The code generates the following output:

.. code:: html

   <html>
     <body>
       Hello World!!!
       <div class="sidebar">
         my new sidebar!!!
       </div>
     </body>
   </html>

Notice that the function is defined in HTML (although it could also
contain Python code) so that ``response.write`` is used to write its
content (the function does not return the content). This is why the
layout calls the view function using ``[[mysidebar()]]`` rather than
``[[=mysidebar()]]``. Functions defined in this way can take arguments.

Blocks in views
---------------

The main way to make a view more modular is by using
``[[block ...]]``\ s and this mechanism is an alternative to the
mechanism discussed in the previous section.

To understand how this works, consider apps based on the scaffolding app
welcome, which has a view layout.html. This view is extended by the view
``default/index.html`` via ``[[extend 'layout.html']]``. The contents of
layout.html predefine certain blocks with certain default content, and
these are therefore included into default/index.html.

You can override these default content blocks by enclosing your new
content inside the same block name. The location of the block in the
layout.html is not changed, but the contents is.

Here is a simplifed version. Imagine this is “layout.html”:

.. code:: python

   <html>
     <body>
       [[include]]
       <div class="sidebar">
         [[block mysidebar]]
           my default sidebar (this content to be replaced)
         [[end]]
       </div>
     </body>
   </html>

and this is a simple extending view ``default/index.html``:

.. code:: html

   [[extend 'layout.html']]
   Hello World!!!
   [[block mysidebar]]
   my new sidebar!!!
   [[end]]

It generates the following output, where the content is provided by the
over-riding block in the extending view, yet the enclosing DIV and class
comes from layout.html. This allows consistency across views:

.. code:: html

   <html>
     <body>
       Hello World!!!
       <div class="sidebar">
           my new sidebar!!!
       </div>
     </body>
   </html>

The real layout.html defines a number of useful blocks, and you can
easily add more to match the layout your desire.

You can have many blocks, and if a block is present in the extended view
but not in the extending view, the content of the extended view is used.
Also, notice that unlike with functions, it is not necessary to define
blocks before the ``[[extend ...]]`` – even if defined after the
``extend``, they can be used to make substitutions anywhere in the
extended view.

Inside a block, you can use the expression ``[[super]]`` to include the
content of the parent. For example, if we replace the above extending
view with:

.. code:: html

   [[extend 'layout.html']]
   Hello World!!!
   [[block mysidebar]]
   [[super]]
   my new sidebar!!!
   [[end]]

we get:

.. code:: html

   <html>
     <body>
       Hello World!!!
       <div class="sidebar">
           my default sidebar
           my new sidebar!
       </div>
     </body>
   </html>
