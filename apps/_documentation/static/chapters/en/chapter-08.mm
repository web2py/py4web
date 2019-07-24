### YATL helpers
``helpers``:inxx

Consider the following code in a view:
``
[[=DIV('this', 'is', 'a', 'test', _id='123', _class='myclass')]]
``:html

it is rendered as:
``
<div id="123" class="myclass">thisisatest</div>
``:html
``DIV`` is a helper class, i.e., something that can be used to build HTML programmatically. It corresponds to the HTML ``<div>`` tag.

Positional arguments are interpreted as objects contained between the open and close tags. Named arguments that start with an underscore are interpreted as HTML tag attributes (without the underscore). Some helpers also have named arguments that do not start with underscore; these arguments are tag-specific.

Instead of a set of unnamed arguments, a helper can also take a single list or tuple as its set of components using the ``*`` notation and it can take a single dictionary as its set of attributes using the ``**``, for example:
``
[[
contents = ['this', 'is', 'a', 'test']
attributes = {'_id':'123', '_class':'myclass'}
=DIV(*contents, **attributes)
]]
``:html
(produces the same output as before).

The following set of helpers:

``A``, ``BEAUTIFY``, ``BODY``, ``CAT``, ``CODE``, ``DIV``, ``EM``, ``FORM``, ``H1``, ``H2``, ``H3``, ``H4``, ``H5``, ``H6``, ``HEAD``, ``HTML``, ``I``, ``IMG``, ``INPUT``, ``LABEL``, ``LI``, ``LINK``, ``META``, ``METATAG``, ``OL``, ``OPTION``, ``PRE``, ``SELECT``, ``SPAN``, ``STRONG``, ``TABLE``, ``TAG``, ``TBODY``, ``TD``, ``TEXTAREA``, ``TH``, ``THAED``, ``TR``, ``UL``, ``XML``, ``sanitize``, ``xmlescape``

can be used to build complex expressions that can then be serialized to XML``xml-w``:cite ``xml-o``:cite. For example:
``
[[=DIV(B(I("hello ", "<world>")), _class="myclass")]]
``:html

is rendered:
``
<div class="myclass"><b><i>hello &lt;world&gt;</i></b></div>
``:html

Helpers can also be serialized into strings, equivalently, with the ``__str__`` and the ``xml`` methods:

``
>>> print str(DIV("hello world"))
<div>hello world</div>
>>> print DIV("hello world").xml()
<div>hello world</div>
``:python

``Document Object Model (DOM)``:inxx
The helpers mechanism in py4web is more than a system to generate HTML without concatenating strings. It provides a server-side representation of the Document Object Model (DOM).

Components of helpers can be referenced via their position, and helpers act as lists with respect to their components:
``
>>> a = DIV(SPAN('a', 'b'), 'c')
>>> print a
<div><span>ab</span>c</div>
>>> del a[1]
>>> a.append(B('x'))
>>> a[0][0] = 'y'
>>> print a
<div><span>yb</span><b>x</b></div>
``:python

Attributes of helpers can be referenced by name, and helpers act as dictionaries with respect to their attributes:
``
>>> a = DIV(SPAN('a', 'b'), 'c')
>>> a['_class'] = 's'
>>> a[0]['_class'] = 't'
>>> print a
<div class="s"><span class="t">ab</span>c</div>
``:python

Note, the complete set of components can be accessed via a list called ``a.components``, and the complete set of attributes can be accessed via a dictionary called ``a.attributes``. So, ``a[i]`` is equivalent to ``a.components[i]`` when ``i`` is an integer, and ``a[s]`` is equivalent to ``a.attributes[s]`` when ``s`` is a string.

Notice that helper attributes are passed as keyword arguments to the helper. In some cases, however, attribute names include special characters that are not allowed in Python identifiers (e.g., hyphens) and therefore cannot be used as keyword argument names. For example:

``
DIV('text', _data-role='collapsible')
``:python

will not work because "_data-role" includes a hyphen, which will produce a Python syntax error.

In such cases you have a couple of options.
You can use the ``data`` argument (this time without a leading underscore) to pass a dictionary of related attributes without their leading hyphen, and the output will have the desired combinations e.g.

``
>>> print DIV('text', data={'role': 'collapsible'})
<div data-role="collapsible">text</div>
``:python

or you can instead pass the attributes as a dictionary and make use of Python's ``**`` function arguments notation, which maps a dictionary of (key:value) pairs into a set of keyword arguments:

``
>>> print DIV('text', **{'_data-role': 'collapsible'})
<div data-role="collapsible">text</div>
``:python

Note that more elaborate entries will introduce HTML character entities, but they will work nonetheless e.g.

``
>>> print DIV('text', data={'options':'{"mode":"calbox", "useNewStyle":true}'})
<div data-options="{&quot;mode&quot;:&quot;calbox&quot;, &quot;useNewStyle&quot;:true}">text</div>
``:python

You can also dynamically create special TAGs:

``
>>> print TAG['soap:Body']('whatever', **{'_xmlns:m':'http://www.example.org'})
<soap:Body xmlns:m="http://www.example.org">whatever</soap:Body>
``:python

#### ``XML``
``XML``:inxx
``XML`` is an object used to encapsulate text that should not be escaped. The text may or may not contain valid XML. For example, it could contain JavaScript.

The text in this example is escaped:
``
>>> print DIV("<b>hello</b>")
<div>&lt;b&gt;hello&lt;/b&gt;</div>
``:python

by using ``XML`` you can prevent escaping:
``
>>> print DIV(XML("<b>hello</b>"))
<div><b>hello</b></div>
``:python

Sometimes you want to render HTML stored in a variable, but the HTML may contain unsafe tags such as scripts:
``
>>> print XML('<script>alert("unsafe!")</script>')
<script>alert("unsafe!")</script>
``:python

Un-escaped executable input such as this (for example, entered in the body of a comment in a blog) is unsafe, because it can be used to generate Cross Site Scripting (XSS) attacks against other visitors to the page.

``sanitize``:inxx
The py4web ``XML`` helper can sanitize our text to prevent injections and escape all tags except those that you explicitly allow. Here is an example:
``
>>> print XML('<script>alert("unsafe!")</script>', sanitize=True)
&lt;script&gt;alert(&quot;unsafe!&quot;)&lt;/script&gt;
``:python

The ``XML`` constructors, by default, consider the content of some tags and some of their attributes safe. You can override the defaults using the optional ``permitted_tags`` and ``allowed_attributes`` arguments. Here are the default values of the optional arguments of the ``XML`` helper.
``
XML(text, sanitize=False,
    permitted_tags=['a', 'b', 'blockquote', 'br/', 'i', 'li',
       'ol', 'ul', 'p', 'cite', 'code', 'pre', 'img/'],
    allowed_attributes={'a':['href', 'title'],
       'img':['src', 'alt'], 'blockquote':['type']})
``:python

### Built-in helpers

#### ``A``
``A``:inxx

This helper is used to build links.

``
>>> print A('<click>', XML('<b>me</b>'),
            _href='http://www.py4web.com')
<a href='http://www.py4web.com'>&lt;click&gt;<b>me</b></a>
``:python

#### ``BODY``
``BODY``:inxx
This helper makes the body of a page.
``
>>> print BODY('<hello>', XML('<b>world</b>'), _bgcolor='red')
<body bgcolor="red">&lt;hello&gt;<b>world</b></body>
``:python

#### ``CAT``
``CAT``:inxx

This helper concatenates other helpers, same as TAG[\'\'].

``
>>> print CAT('Here is a ', A('link', _href=URL()), ', and here is some ', B('bold text'), '.')
Here is a <a href="/app/default/index">link</a>, and here is some <b>bold text</b>.
``:python

#### ``CODE``
``CODE``:inxx

This helper performs syntax highlighting for Python, C, C++, HTML and py4web code, and is preferable to ``PRE`` for code listings. ``CODE`` also has the ability to create links to the py4web API documentation.

Here is an example of highlighting sections of Python code.
``
>>> print CODE('print "hello"', language='python').xml()
``:python
``
<table><tr style="vertical-align:top;">
  <td style="min-width:40px; text-align: right;"><pre style="
        font-size: 11px;
        font-family: Bitstream Vera Sans Mono,monospace;
        background-color: transparent;
        margin: 0;
        padding: 5px;
        border: none;
        color: #A0A0A0;
    ">1.</pre></td><td><pre style="
        font-size: 11px;
        font-family: Bitstream Vera Sans Mono,monospace;
        background-color: transparent;
        margin: 0;
        padding: 5px;
        border: none;
        overflow: auto;
        white-space: pre !important;
"><span style="color:#185369; font-weight: bold">print </span>
  <span style="color: #FF9966">"hello"</span></pre></td></tr></table>
``:html

Here is a similar example for HTML
``
>>> print CODE('<html><body>[[=request.env.remote_add]]</body></html>',
...     language='html')
``:python
``
<table>...<code>...
<html><body>[[=request.env.remote_add]]</body></html>
...</code>...</table>
``:python

These are the default arguments for the ``CODE`` helper:
``
CODE("print 'hello world'", language='python', link=None, counter=1, styles={})
``:python

Supported values for the ``language`` argument are "python", "html_plain", "c", "cpp", "py4web", and "html". The "html" language interprets [[ and ]] tags as "py4web" code, while "html_plain" doesn't.

If a ``link`` value is specified, for example "/examples/global/vars/", py4web API references in the code are linked to documentation at the link URL. For example "request" would be linked to "/examples/global/vars/request". In the above example, the link URL is handled by the "vars" action in the "global.py" controller that is distributed as part of the py4web "examples" application.

The ``counter`` argument is used for line numbering. It can be set to any of three different values. It can be ``None`` for no line numbers, a numerical value specifying the start number, or a string. If the counter is set to a string, it is interpreted as a prompt, and there are no line numbers.

The ``styles`` argument is a bit tricky. If you look at the generated HTML above, it contains a table with two columns, and each column has its own style declared inline using CSS. The ``styles`` attributes allows you to override those two CSS styles. For example:

``
CODE(..., styles={'CODE':'margin: 0;padding: 5px;border: none;'})
``:python

The ``styles`` attribute must be a dictionary, and it allows two possible keys: ``CODE`` for the style of the actual code, and ``LINENUMBERS`` for the style of the left column, which contains the line numbers. Mind that these styles completely replace the default styles and are not simply added to them.

#### ``COL``
``COL``:inxx

``
>>> print COL('a', 'b')
<col>ab</col>
``:python

#### ``DIV``
``DIV``:inxx

All helpers apart from ``XML`` are derived from ``DIV`` and inherit its basic methods.

``
>>> print DIV('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<div id="0" class="test">&lt;hello&gt;<b>world</b></div>
``:python

#### ``EM``
``EM``:inxx

Emphasizes its content.

``
>>> print EM('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<em id="0" class="test">&lt;hello&gt;<b>world</b></em>
``:python

#### ``FIELDSET``
``FIELDSET``:inxx

This is used to create an input field together with its label.
``
>>> print FIELDSET('Height:', INPUT(_name='height'), _class='test')
<fieldset class="test">Height:<input name="height" /></fieldset>
``:python

#### ``FORM``
``FORM``:inxx

This is one of the most important helpers. In its simple form, it just makes a ``<form>...</form>`` tag, but because helpers are objects and have knowledge of what they contain, they can process submitted forms (for example, perform validation of the fields). This will be discussed in detail in Chapter 7.
``
>>> print FORM(INPUT(_type='submit'), _action='', _method='post')
<form enctype="multipart/form-data" action="" method="post">
<input type="submit" /></form>
``:python

The "enctype" is "multipart/form-data" by default.

``hidden``:inxx
The constructor of a ``FORM``, and of ``SQLFORM``, can also take a special argument called ``hidden``. When a dictionary is passed as ``hidden``, its items are translated into "hidden" INPUT fields. For example:
``
>>> print FORM(hidden=dict(a='b'))
<form enctype="multipart/form-data" action="" method="post">
<input value="b" type="hidden" name="a" /></form>
``:python

#### ``H1``, ``H2``, ``H3``, ``H4``, ``H5``, ``H6``
``H1``:inxx

These helpers are for paragraph headings and subheadings:
``
>>> print H1('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<h1 id="0" class="test">&lt;hello&gt;<b>world</b></h1>
``:python

#### ``HEAD``
``HEAD``:inxx

For tagging the HEAD of an HTML page.

``
>>> print HEAD(TITLE('<hello>', XML('<b>world</b>')))
<head><title>&lt;hello&gt;<b>world</b></title></head>
``:python

#### ``HTML``
``HTML``:inxx ``XHTML``:inxx

This helper is a little different. In addition to making the ``<html>`` tags,
it prepends the tag with a doctype string``xhtml-w,xhtml-o,xhtml-school``:cite .
``
>>> print HTML(BODY('<hello>', XML('<b>world</b>')))
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html><body>&lt;hello&gt;<b>world</b></body></html>
``:python

The HTML helper also takes some additional optional arguments that have the following default:
``
HTML(..., lang='en', doctype='transitional')
``:python

where doctype can be 'strict', 'transitional', 'frameset', 'html5', or a full doctype string.

#### ``I``
``I``:inxx

This helper makes its contents italic.
``
>>> print I('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<i id="0" class="test">&lt;hello&gt;<b>world</b></i>
``:python

#### ``IMG``
``IMG``:inxx

It can be used to embed images into HTML:

``
>>> print IMG(_src='http://example.com/image.png', _alt='test')
<img src="http://example.com/image.ong" alt="rest" />
``:python

Here is a combination of A, IMG, and URL helpers for including a static image with a link:

``
>>> print A(IMG(_src=URL('static', 'logo.png'), _alt="My Logo"),
...   _href=URL('default', 'index'))
... 
<a href="/myapp/default/index">
  <img src="/myapp/static/logo.png" alt="My Logo" />
</a>
``:python

#### ``INPUT``
``INPUT``:inxx

Creates an ``<input.../>`` tag. An input tag may not contain other tags, and is closed by ``/>`` instead of ``>``. The input tag has an optional attribute ``_type`` that can be set to "text" (the default), "submit", "checkbox", or "radio".
``
>>> print INPUT(_name='test', _value='a')
<input value="a" name="test" />
``:python

It also takes an optional special argument called "value", distinct from "_value". The latter sets the default value for the input field; the former sets its current value. For an input of type "text", the former overrides the latter:
``
>>> print INPUT(_name='test', _value='a', value='b')
<input value="b" name="test" />
``:python

For radio buttons, ``INPUT`` selectively sets the "checked" attribute:

``radio``:inxx
``
>>> for v in ['a', 'b', 'c']:
...     print INPUT(_type='radio', _name='test', _value=v, value='b'), v
... 
<input value="a" type="radio" name="test" /> a
<input value="b" type="radio" checked="checked" name="test" /> b
<input value="c" type="radio" name="test" /> c
``:python

and similarly for checkboxes:

``checkbox``:inxx
``
>>> print INPUT(_type='checkbox', _name='test', _value='a', value=True)
<input value="a" type="checkbox" checked="checked" name="test" />
>>> print INPUT(_type='checkbox', _name='test', _value='a', value=False)
<input value="a" type="checkbox" name="test" />
``:python

#### ``LABEL``
``LABEL``:inxx

It is used to create a LABEL tag for an INPUT field.

``
>>> print LABEL('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<label id="0" class="test">&lt;hello&gt;<b>world</b></label>
``:python

#### ``LEGEND``
``LEGEND``:inxx

It is used to create a legend tag for a field in a form.

``
>>> print LEGEND('Name', _for='myfield')
<legend for="myfield">Name</legend>
``:python

#### ``LI``
``LI``:inxx

It makes a list item and should be contained in a ``UL`` or ``OL`` tag.

``
>>> print LI('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<li id="0" class="test">&lt;hello&gt;<b>world</b></li>
``:python

#### ``OL``
``OL``:inxx

It stands for Ordered List. The list should contain LI tags. ``OL`` arguments that are not ``LI`` objects are automatically enclosed in ``<li>...</li>`` tags.

``
>>> print OL('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<ol id="0" class="test"><li>&lt;hello&gt;</li><li><b>world</b></li></ol>
``:python


#### ``OPTION``
``OPTION``:inxx

This should only be used as part of a ``SELECT``/``OPTION`` combination.

``
>>> print OPTION('<hello>', XML('<b>world</b>'), _value='a')
<option value="a">&lt;hello&gt;<b>world</b></option>
``:python

As in the case of ``INPUT``, py4web make a distinction between "_value" (the value of the OPTION), and "value" (the current value of the enclosing select). If they are equal, the option is "selected".

``selected``:inxx
``
>>> print SELECT('a', 'b', value='b'):
<select>
<option value="a">a</option>
<option value="b" selected="selected">b</option>
</select>
``:python

#### ``P``
``P``:inxx

This is for tagging a paragraph.
``
>>> print P('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<p id="0" class="test">&lt;hello&gt;<b>world</b></p>
``:python

#### ``PRE``
``PRE``:inxx

Generates a ``<pre>...</pre>`` tag for displaying pre-formatted text. The ``CODE`` helper is generally preferable for code listings.
``
>>> print PRE('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<pre id="0" class="test">&lt;hello&gt;<b>world</b></pre>
``:python

#### ``SCRIPT``
``SCRIPT``:inxx

This is include or link a script, such as JavaScript. The content between the tags is rendered as an HTML comment, for the benefit of really old browsers.
``
>>> print SCRIPT('alert("hello world");', _type='text/javascript')
<script type="text/javascript"><!--
alert("hello world");
//--></script>
``:python

#### ``SELECT``
``SELECT``:inxx

Makes a ``<select>...</select>`` tag. This is used with the ``OPTION`` helper. Those ``SELECT`` arguments that are not ``OPTION`` objects are automatically converted to options.
``
>>> print SELECT('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<select id="0" class="test">
<option value="&lt;hello&gt;">&lt;hello&gt;</option>
<option value="&lt;b&gt;world&lt;/b&gt;"><b>world</b></option>
</select>
``:python

#### ``SPAN``
``SPAN``:inxx

Similar to ``DIV`` but used to tag inline (rather than block) content.
``
>>> print SPAN('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<span id="0" class="test">&lt;hello&gt;<b>world</b></span>
``:python

#### ``STYLE``
``STYLE``:inxx

Similar to script, but used to either include or link CSS code.
Here the CSS is included:
``
>>> print STYLE(XML('body {color: white}'))
<style><!--
body { color: white }
//--></style>
``:python

and here it is linked:
``
>>> print STYLE(_src='style.css')
<style src="style.css"><!--
//--></style>
``:python

#### ``TABLE``, ``TR``, ``TD``
``TABLE``:inxx ``TR``:inxx ``TD``:inxx

These tags (along with the optional ``THEAD`` and ``TBODY`` helpers) are used to build HTML tables.
``
>>> print TABLE(TR(TD('a'), TD('b')), TR(TD('c'), TD('d')))
<table><tr><td>a</td><td>b</td></tr><tr><td>c</td><td>d</td></tr></table>
``:python
``TR`` expects ``TD`` content; arguments that are not ``TD`` objects are converted automatically.
``
>>> print TABLE(TR('a', 'b'), TR('c', 'd'))
<table><tr><td>a</td><td>b</td></tr><tr><td>c</td><td>d</td></tr></table>
``:python

It is easy to convert a Python array into an HTML table using Python's ``*`` function arguments notation, which maps list elements to positional function arguments.

Here, we will do it line by line:
``
>>> table = [['a', 'b'], ['c', 'd']]
>>> print TABLE(TR(*table[0]), TR(*table[1]))
<table><tr><td>a</td><td>b</td></tr><tr><td>c</td><td>d</td></tr></table>
``:python

Here we do all lines at once:
``
>>> table = [['a', 'b'], ['c', 'd']]
>>> print TABLE(*[TR(*rows) for rows in table])
<table><tr><td>a</td><td>b</td></tr><tr><td>c</td><td>d</td></tr></table>
``:python

#### ``TBODY``
``TBODY``:inxx

This is used to tag rows contained in the table body, as opposed to header or footer rows. It is optional.
``
>>> print TBODY(TR('<hello>'), _class='test', _id=0)
<tbody id="0" class="test"><tr><td>&lt;hello&gt;</td></tr></tbody>
``:python

#### ``TEXTAREA``
``TEXTAREA``:inxx

This helper makes a ``<textarea>...</textarea>`` tag.
``
>>> print TEXTAREA('<hello>', XML('<b>world</b>'), _class='test')
<textarea class="test" cols="40" rows="10">&lt;hello&gt;<b>world</b></textarea>
``:python

The only caveat is that its optional "value" overrides its content (inner HTML)
``
>>> print TEXTAREA(value="<hello world>", _class="test")
<textarea class="test" cols="40" rows="10">&lt;hello world&gt;</textarea>
``:python

#### ``TH``
``TH``:inxx

This is used instead of ``TD`` in table headers.
``
>>> print TH('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<th id="0" class="test">&lt;hello&gt;<b>world</b></th>
``:python

#### ``THEAD``
``THEAD``:inxx

This is used to tag table header rows.
``
>>> print THEAD(TR(TH('<hello>')), _class='test', _id=0)
<thead id="0" class="test"><tr><th>&lt;hello&gt;</th></tr></thead>
``:python

#### ``TITLE``
``TITLE``:inxx

This is used to tag the title of a page in an HTML header.
``
>>> print TITLE('<hello>', XML('<b>world</b>'))
<title>&lt;hello&gt;<b>world</b></title>
``:python

#### ``TR``
``TR``:inxx

Tags a table row. It should be rendered inside a table and contain ``<td>...</td>`` tags. ``TR`` arguments that are not ``TD`` objects will be automatically converted.
``
>>> print TR('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<tr id="0" class="test"><td>&lt;hello&gt;</td><td><b>world</b></td></tr>
``:python

#### ``TT``
``TT``:inxx

Tags text as typewriter (monospaced) text.
``
>>> print TT('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<tt id="0" class="test">&lt;hello&gt;<b>world</b></tt>
``:python

#### ``UL``
``UL``:inxx

Signifies an Unordered List and should contain ``LI`` items. If its content is not tagged as ``LI``, ``UL`` does it automatically.
``
>>> print UL('<hello>', XML('<b>world</b>'), _class='test', _id=0)
<ul id="0" class="test"><li>&lt;hello&gt;</li><li><b>world</b></li></ul>
``:python

#### ``URL``

The URL helper is documented in [[Chapter 4 URL ../04#URL]]

### Custom helpers

#### ``TAG``
``TAG``:inxx

Sometimes you need to generate custom XML tags. py4web provides ``TAG``, a universal tag generator.
``
[[=TAG.name('a', 'b', _c='d')]]
``:html

generates the following XML
``
<name c="d">ab</name>
``:python[lexer='xml']

Arguments "a", "b", and "d" are automatically escaped; use the ``XML`` helper to suppress this behavior. Using ``TAG`` you can generate HTML/XML tags not already provided by the API. TAGs can be nested, and are serialized with ``str().``
An equivalent syntax is:
``
[[=TAG['name']('a', 'b', c='d')]]
``:html

If the TAG object is created with an empty name, it can be used to concatenate multiple strings and HTML helpers together without inserting them into a surrounding tag, but this use is deprecated. Use the ``CAT`` helper instead.

Self-closing tags can be generated with the TAG helper. The tag name must end with a "/".
``
[[=TAG['link/'](_href='http://py4web.com')]]
``:html
generates the following XML:
``
<link ref="http://py4web.com"/>
``:python[lexer='xml']
Notice that ``TAG`` is an object, and ``TAG.name`` or ``TAG['name']`` is a function that returns a temporary helper class.

#### ``MENU``
``MENU``:inxx

The MENU helper takes a list of lists or of tuples of the form of ``response.menu`` (as described in Chapter 4) and generates a tree-like structure using unordered lists representing the menu. For example:
``
>>> print MENU([['One', False, 'link1'], ['Two', False, 'link2']])
<ul class="py4web-menu py4web-menu-vertical">
<li><a href="link1">One</a></li>
<li><a href="link2">Two</a></li>
</ul>
``:python

------
The first item in each list/tuple is the text to be displayed for the given menu item.

The second item in each list/tuple is a boolean indicating whether that particular menu item is active
(i.e., the currently selected item). When set to True, the ``MENU`` helper will add a "py4web-menu-active"
class to the ``<li>`` for that item (you can change the name of that class via the "li_active" argument to ``MENU``).
Another way to specify the active url is by directly passing it to ``MENU`` via its "active_url" argument.

The third item in each list/tuple can be an HTML helper (which could include nested helpers), and the ``MENU`` helper will simply render that helper rather than creating its own ``<a>`` tag.
------

Each menu item can have a fourth argument that is a nested submenu (and so on recursively):
``
>>> print MENU([['One', False, 'link1', [['Two', False, 'link2']]]])
<ul class="py4web-menu py4web-menu-vertical">
<li class="py4web-menu-expand">
<a href="link1">One</a>
<ul class="py4web-menu-vertical">
<li><a href="link2">Two</a></li>
</ul>
</li>
</ul>
``:python

A menu item can also have an optional 5th element, which is a boolean. When false, the menu item is ignored by the MENU helper.

The ``MENU`` helper takes the following optional arguments:
- ``_class``: defaults to "py4web-menu py4web-menu-vertical" and sets the class of the outer UL elements.
- ``ul_class``: defaults to "py4web-menu-vertical" and sets the class of the inner UL elements.
- ``li_class``: defaults to "py4web-menu-expand" and sets the class of the inner LI elements.
- ``li_first``: allows to add a class to the first list element.
- ``li_last``: allows to add a class to the last list element.

``mobile``:inxx

``MENU`` takes an optional argument ``mobile``. When set to ``True`` instead of building a recursive ``UL`` menu structure it returns a ``SELECT`` dropdown with all the menu options and a ``onchange`` attribute that redirects to the page corresponding to the selected option. This is designed an an alternative menu representation that increases usability on small mobile devices such as phones.

Normally the menu is used in a layout with the following syntax:

``
[[=MENU(response.menu, mobile=request.user_agent().is_mobile)]]
``:html

In this way a mobile device is automatically detected and the menu is rendered accordingly.

### ``BEAUTIFY``
``BEAUTIFY``:inxx

``BEAUTIFY`` is used to build HTML representations of compound objects, including lists, tuples and dictionaries:
``
[[=BEAUTIFY({"a": ["hello", XML("world")], "b": (1, 2)})]]
``:html
``BEAUTIFY`` returns an XML-like object serializable to XML, with a nice looking representation of its constructor argument. In this case, the XML representation of:
``
{"a": ["hello", XML("world")], "b": (1, 2)}
``:python

will render as:
``
<table>
<tr><td>a</td><td>:</td><td>hello<br />world</td></tr>
<tr><td>b</td><td>:</td><td>1<br />2</td></tr>
</table>
``:html

### Server-side ''DOM'' and parsing

#### ``elements``
``element``:inxx ``elements``:inxx

The DIV helper and all derived helpers provide the search methods ``element`` and ``elements``.

``element`` returns the first child element matching a specified condition (or None if no match).

``elements`` returns a list of all matching children.

**element** and **elements** use the same syntax to specify the matching condition, which allows for three possibilities that can be mixed and matched: jQuery-like expressions, match by exact attribute value, match using regular expressions.

Here is a simple example:
``
>>> a = DIV(DIV(DIV('a', _id='target', _class='abc')))
>>> d = a.elements('div#target')
>>> d[0][0] = 'changed'
>>> print a
<div><div><div id="target" class="abc">changed</div></div></div>
``:python

The un-named argument of ``elements`` is a string, which may contain: the name of a tag, the id of a tag preceded by a pound symbol, the class preceded by a dot, the explicit value of an attribute in square brackets.

Here are 4 equivalent ways to search the previous tag by id:
``
d = a.elements('#target')
d = a.elements('div#target')
d = a.elements('div[id=target]')
d = a.elements('div', _id='target')
``:python

Here are 4 equivalent ways to search the previous tag by class:
``
d = a.elements('.abc')
d = a.elements('div.abc')
d = a.elements('div[class=abc]')
d = a.elements('div', _class='abc')
``:python

Any attribute can be used to locate an element (not just ``id`` and ``class``), including multiple attributes (the function element can take multiple named arguments), but only the first matching element will be returned.

Using the jQuery syntax "div#target" it is possible to specify multiple search criteria separated by a comma:
``
a = DIV(SPAN('a', _id='t1'), DIV('b', _class='c2'))
d = a.elements('span#t1, div.c2')
``:python

or equivalently
``
a = DIV(SPAN('a', _id='t1'), DIV('b', _class='c2'))
d = a.elements('span#t1', 'div.c2')
``:python

If the value of an attribute is specified using a name argument, it can be a string or a regular expression:
``
a = DIV(SPAN('a', _id='test123'), DIV('b', _class='c2'))
d = a.elements('span', _id=re.compile('test\d{3}')
``:python

A special named argument of the DIV (and derived) helpers is ``find``. It can be used to specify a search value or a search regular expression in the text content of the tag. For example:
``
>>> a = DIV(SPAN('abcde'), DIV('fghij'))
>>> d = a.elements(find='bcd')
>>> print d[0]
<span>abcde</span>
``:python

or
``
>>> a = DIV(SPAN('abcde'), DIV('fghij'))
>>> d = a.elements(find=re.compile('fg\w{3}'))
>>> print d[0]
<div>fghij</div>
``:python

#### ``components`` 
``components``:inxx

Here's an example of listing all elements in an html string:
``
>>> html = TAG('<a>xxx</a><b>yyy</b>')
>>> for item in html.components:
...     print item
... 
<a>xxx</a>
<b>yyy</b>
``:python

#### ``parent`` and ``siblings``
``parent``:inxx ``sibling``:inxx

``parent`` returns the parent of the current element.
``
>>> a = DIV(SPAN('a'), DIV('b'))
>>> s = a.element('span')
>>> d = s.parent
>>> d['_class']='abc'
>>> print a
<div class="abc"><span>a</span><div>b</div></div>
>>> for e in s.siblings(): print e
<div>b</div>
``:python

#### Replacing elements

Elements that are matched can also be replaced or removed by specifying
the ``replace`` argument. Notice that a
list of the original matching elements is still returned as usual.

``
>>> a = DIV(SPAN('x'), DIV(SPAN('y'))
>>> b = a.elements('span', replace=P('z')
>>> print a
<div><p>z</p><div><p>z</p></div>
``:python

``replace`` can be a callable. In this case it will be passed
the original element and it is expected to return the replacement element:

``
>>> a = DIV(SPAN('x'), DIV(SPAN('y'))
>>> b = a.elements('span', replace=lambda t: P(t[0])
>>> print a
<div><p>x</p><div><p>y</p></div>
``:python

If ``replace=None``, matching elements will be removed completely.

``
>>> a = DIV(SPAN('x'), DIV(SPAN('y'))
>>> b = a.elements('span', replace=None)
>>> print a
<div></div>
``:python

#### ``flatten`` 
``flatten``:inxx

The flatten method recursively serializes the content of the children of a given element into regular text (without tags):
``
>>> a = DIV(SPAN('this', DIV('is', B('a'))), SPAN('test'))
>>> print a.flatten()
thisisatest
``:python

Flatten can be passed an optional argument, ``render``, i.e. a function that renders/flattens the content using a different protocol. Here is an example to serialize some tags into Markmin wiki syntax:
``
>>> a = DIV(H1('title'), P('example of a ', A('link', _href='#test')))
>>> from gluon.html import markmin_serializer
>>> print a.flatten(render=markmin_serializer)
# titles

example of [[a link #test]]

``:python

At the time of writing we provide ``markmin_serializer`` and ``markdown_serializer``.

#### Parsing

The TAG object is also an XML/HTML parser. It can read text and convert into a tree structure of helpers. This allows manipulation using the API above:
``
>>> html = '<h1>Title</h1><p>this is a <span>test</span></p>'
>>> parsed_html = TAG(html)
>>> parsed_html.element('span')[0]='TEST'
>>> print parsed_html
<h1>Title</h1><p>this is a <span>TEST</span></p>
``:python


### Page layout
``page layout``:inxx ``layout.html``:inxx ``extent``:inxx ``include``:inxx

Views can extend and include other views in a tree-like structure.

For example, we can think of a view "index.html" that extends "layout.html" and includes "body.html".
At the same time,  "layout.html" may include "header.html" and "footer.html".

The root of the tree is what we call a layout view.  Just like any other HTML template file, you can edit it using the py4web administrative interface. The file name "layout.html" is just a convention.

Here is a minimalist page that extends the "layout.html" view and includes the "page.html" view:

``
[[extend 'layout.html']]
<h1>Hello World</h1>
[[include 'page.html']]
``:python

The extended layout file must contain an ``[[include]]`` directive, something like:
``
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    [[include]]
  </body>
</html>
``:python

When the view is called, the extended (layout) view is loaded, and the calling view replaces the ``[[include]]`` directive inside the layout. Processing continues recursively until all ``extend`` and ``include`` directives have been processed. The resulting template is then translated into Python code. Note, when an application is bytecode compiled, it is this Python code that is compiled, not the original view files themselves. So, the bytecode compiled version of a given view is a single .pyc file that includes the Python code not just for the original view file, but for its entire tree of extended and included views.

-------
``extend``, ``include``, ``block`` and ``super`` are special template directives,
not Python commands.
-------

Any content or code that precedes the ``[[extend ...]]`` directive will be inserted (and therefore executed) before the beginning of the extended view's content/code. Although this is not typically used to insert actual HTML content before the extended view's content, it can be useful as a means to define variables or functions that you want to make available to the extended view. For example, consider a view "index.html":
``
[[sidebar_enabled=True]]
[[extend 'layout.html']]
<h1>Home Page</h1>
``:python

and an excerpt from "layout.html":
``
[[if sidebar_enabled:]]
    <div id="sidebar">
        Sidebar Content
    </div>
[[pass]]
``:python

Because the ``sidebar_enabled`` assignment in "index.html" comes before the ``extend``, that line gets inserted before the beginning of "layout.html", making ``sidebar_enabled`` available anywhere within the "layout.html" code (a somewhat more sophisticated version of this is used in the **welcome** app).

It is also worth pointing out that the variables returned by the controller function are available not only in the function's main view, but in all of its extended and included views as well.

The argument of an ``extend`` or ``include`` (i.e., the extended or included view name) can be a Python variable (though not a Python expression). However, this imposes a limitation -- views that use variables in ``extend`` or ``include`` statements cannot be bytecode compiled. As noted above, bytecode-compiled views include the entire tree of extended and included views, so the specific extended and included views must be known at compile time, which is not possible if the view names are variables (whose values are not determined until run time). Because bytecode compiling views can provide a significant speed boost, using variables in ``extend`` and ``include`` should generally be avoided if possible.

In some cases, an alternative to using a variable in an ``include`` is simply to place regular ``[[include ...]]`` directives inside an ``if...else`` block.

``
[[if some_condition:]]
[[include 'this_view.html']]
[[else:]]
[[include 'that_view.html']]
[[pass]]
``:html

The above code does not present any problem for bytecode compilation because no variables are involved. Note, however, that the bytecode compiled view will actually include the Python code for both "this_view.html" and "that_view.html", though only the code for one of those views will be executed, depending on the value of ``some_condition``.

Keep in mind, this only works for ``include`` -- you cannot place ``[[extend ...]]`` directives inside ``if...else`` blocks.

``response.menu``:inxx ``menu``:inxx ``response.meta``:inxx ``meta``:inxx

Layouts are used to encapsulate page commonality (headers, footers, menus), and though they are not mandatory, they will make your application easier to write and maintain.  In particular, we suggest writing layouts that take advantage of the following variables that can be set in the controller. Using these well known variables will help make your layouts interchangeable:
``
response.title
response.subtitle
response.meta.author
response.meta.keywords
response.meta.description
response.flash
response.menu
response.files
``:python[lexer=None]

Except for ``menu`` and ``files``, these are all strings and their meaning should be obvious.

``response.menu`` menu is a list of 3-tuples or 4-tuples. The three elements are: the link name, a boolean representing whether the link is active (is the current link), and the URL of the linked page. For example:
``
response.menu = [('Google', False, 'http://www.google.com', []),
                 ('Index',  True,  URL('index'), [])]
``:python

``sub-menu``:inxx
The fourth tuple element is an optional sub-menu.

``response.files`` is a list of CSS and JS files that are needed by your page.

We also recommend that you use:

``
[[include 'py4web_ajax.html']]
``:html

in the HTML head, since this will include the jQuery libraries and define some backward-compatible JavaScript functions for special effects and Ajax. "py4web_ajax.html" includes the ``response.meta`` tags in the view, jQuery base, the calendar datepicker, and all required CSS and JS ``response.files``.

#### Default page layout

``Twitter Bootstrap``:inxx

The "views/layout.html" that ships with the py4web scaffolding application **welcome** (stripped down of some optional parts) is quite complex but it has the following structure:

``
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
``:python

There are a few features of this default layout that make it very easy to use and customize:

- It is written in HTML5 and uses the "modernizr" ``modernizr``:cite library for backward compatibility. The actual layout includes some extra conditional statements required by IE and they are omitted for brevity.
- It displays both ``response.title`` and ``response.subtitle`` which can be set in a model or a controller. If they are not set, it adopts the application name as title.
- It includes the ``py4web_ajax.html`` file in the header which generated all the link and script import statements.
- It uses a modified version of Twitter Bootstrap for flexible layouts which works on mobile devices and re-arranges columns to fit small screens.
- It uses "analytics.js" to connect to Google Analytics.
- The ``[[=auth.navbar(...)]]`` displays a welcome to the current user and links to the auth functions like login, logout, register, change password, etc. depending on context. ``auth.navbar`` is a helper factory and its output can be manipulated as any other helper. It is placed in an expression to check for auth definition, the expression evaluates to '' in case auth is undefined.
- The ``[[=MENU(response.menu)]]`` displays the menu structure as ``<ul>...</ul>``.
- ``[[include]]`` is replaced by the content of the extending view when the page is rendered.
- By default it uses a conditional three column (the left and right sidebars can be turned off by the extending views)
- It uses the following classes: page-header, main, footer.
- It contains the following blocks: head, left_sidebar, center, right_sidebar, footer.

In views, you can turn on and customize sidebars as follows:

``
[[left_sidebar_enabled=True]]
[[extend 'layout.html']]

This text goes in center

[[block left_sidebar]]
This text goes in sidebar
[[end]]
``:html

#### Customizing the default layout
``CSS``:inxx

Customizing the default layout without editing is easy because the welcome application is based on Twitter Bootstrap which is well documented and supports themes. In py4web four static files which are relevant to style:

- "css/py4web.css" contains py4web specific styles
- "css/bootstrap.min.css" contains the Twitter Bootstrap CSS style ``bootstrap``:cite ``Bootstrap``:inxx
- "css/py4web_bootstrap.css" which overrides some Bootstrap styles to conform to py4web needs.
- "js/bootstrap.min.js" which includes the libraries for menu effects, modals, panels.

To change colors and background images,
try append the following code to layout.html header:

``
<style>
body { background: url('images/background.png') repeat-x #3A3A3A; }
a { color: #349C01; }
.page-header h1 { color: #349C01; }
.page-header h2 { color: white; font-style: italic; font-size: 14px;}
.statusbar { background: #333333; border-bottom: 5px #349C01 solid; }
.statusbar a { color: white; }
.footer { border-top: 5px #349C01 solid; }
</style>
``:python[lexer='css']

Of course you can also completely replace the "layout.html" and "py4web.css" files with your own.

#### Mobile development

Although the default layout.html is designed to be mobile-friendly, one may sometimes need to use different views when a page is visited by a mobile device.

To make developing for desktop and mobile devices easier, py4web includes the ``@mobilize`` decorator. This decorator is applied to actions that should have a normal view and a mobile view. This is demonstrated here:

``
from gluon.contrib.user_agent_parser import mobilize
@mobilize
def index():
    return dict()
``:python

Notice that the decorator must be imported before using it in a controller.
When the "index" function is called from a regular browser (desktop computer), py4web will render the returned dictionary using the view "[controller]/index.html". However, when it is called by a mobile device, the dictionary will be rendered by "[controller]/index.mobile.html". Notice that mobile views have the "mobile.html" extension.

Alternatively you can apply the following logic to make all views mobile friendly:

``
if request.user_agent().is_mobile:
    response.view.replace('.html', '.mobile.html')
``:python

The task of creating the "*.mobile.html" views is left to the developer but we strongly suggest using the "jQuery Mobile" plugin which makes the task very easy.

### Functions in views

Consider this "layout.html":

``
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
``:python

and this extending view

``
[[def mysidebar():]]
my new sidebar!!!
[[return]]
[[extend 'layout.html']]
Hello World!!!
``:html

Notice the function is defined before the ``[[extend...]]`` statement -- this results in the function being created before the "layout.html" code is executed, so the function can be called anywhere within "layout.html", even before the ``[[include]]``. Also notice the function is included in the extended view without the ``=`` prefix.

The code generates the following output:

``
<html>
  <body>
    Hello World!!!
    <div class="sidebar">
      my new sidebar!!!
    </div>
  </body>
</html>
``:html

Notice that the function is defined in HTML (although it could also contain Python code) so that ``response.write`` is used to write its content (the function does not return the content). This is why the layout calls the view function using ``[[mysidebar()]]`` rather than ``[[=mysidebar()]]``. Functions defined in this way can take arguments.

### Blocks in views
``block``:inxx

The main way to make a view more modular is by using ``[[block ...]]``s and this mechanism is an alternative to the mechanism discussed in the previous section.

To understand how this works, consider apps based on the scaffolding app welcome, which has a view layout.html. This view is extended by the view ``default/index.html`` via ``[[extend 'layout.html']]``. The contents of layout.html predefine certain blocks with certain default content, and these are therefore included into default/index.html.

You can override these default content blocks by enclosing your new content inside the same block name. The location of the block in the layout.html is not changed, but the contents is. 

Here is a simplifed version. Imagine this is  "layout.html":

``
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
``:python

and this is a simple extending view ``default/index.html``:

``
[[extend 'layout.html']]
Hello World!!!
[[block mysidebar]]
my new sidebar!!!
[[end]]
``:html

It generates the following output, where the content is provided by the over-riding block in the extending view, yet the enclosing DIV and class comes from layout.html. This allows consistency across views:

``
<html>
  <body>
    Hello World!!!
    <div class="sidebar">
        my new sidebar!!!
    </div>
  </body>
</html>
``:html

The real layout.html defines a number of useful blocks, and you can easily add more to match the layout your desire. 

You can have many blocks, and if a block is present in the extended view but not in the extending view, the content of the extended view is used. Also, notice that unlike with functions, it is not necessary to define blocks before the ``[[extend ...]]`` -- even if defined after the ``extend``, they can be used to make substitutions anywhere in the extended view.

``super``:inxx

Inside a block, you can use the expression ``[[super]]`` to include the content of the parent. For example, if we replace the above extending view with:

``
[[extend 'layout.html']]
Hello World!!!
[[block mysidebar]]
[[super]]
my new sidebar!!!
[[end]]
``:html

we get:

``
<html>
  <body>
    Hello World!!!
    <div class="sidebar">
        my default sidebar
        my new sidebar!
    </div>
  </body>
</html>
``:html


