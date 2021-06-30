======================
YATL Template Language
======================

py4web uses an external Python module called **YATL** (Yet Another Template
Language, see `here <https://github.com/web2py/yatl>`__) for rendering dynamic HTML
pages that contain Python code.

py4web uses double square brackets ``[[ ... ]]`` to escape Python code embedded in HTML. The
advantage of using square brackets instead of angle brackets is that
it’s transparent to all common HTML editors. This allows the developer
to use those editors to create py4web templates.

.. warning::
    Be careful not to mix Python code square brackets with other square brackets!
    For example, you'll soon see syntax like this:
    
      .. code:: html

         [[items = ['a', 'b', 'c']]] # this gives "Internal Server Error"
         [[items = ['a', 'b', 'c'] ]] # this works
    
    
    It's mandatory to add a space after the first closed bracket for
    separating the list from the Python code square brackets.
    
Since the developer is embedding Python code into HTML, the document
should be indented according to HTML rules, and not Python rules.
Therefore, we allow un-indented Python inside the ``[[ ... ]]`` tags.
But since Python normally uses indentation to delimit blocks of code, we
need a different way to delimit them; this is why the py4web template
language makes use of the Python keyword ``pass``.

A **code block** starts with a line ending with a colon and ends with a
line beginning with ``pass``. The keyword ``pass`` is not necessary
when the end of the block is obvious from the context.

Here is an example:

.. code:: html

   [[
   if i == 0:
   response.write('i is 0')
   else:
   response.write('i is not 0')
   pass
   ]]

Note that ``pass`` is a Python keyword, not a py4web keyword. Some
Python editors, such as Emacs, use the keyword ``pass`` to signify the
division of blocks and use it to re-indent code automatically.

The py4web template language does exactly the same. When it finds
something like:

.. code:: html

   <html><body>
   [[for x in range(10):]][[=x]] hello <br />[[pass]]
   </body></html>

it translates it into a program:

.. code:: html

   response.write("""<html><body>""", escape=False)
   for x in range(10):
       response.write(x)
       response.write(""" hello <br />""", escape=False)
   response.write("""</body></html>""", escape=False)

``response.write`` writes to the response body.

When there is an error in a py4web template, the error report shows the
generated template code, not the actual template as written by the developer.
This helps the developer debug the code by highlighting the actual code
that is executed (which is something that can be debugged with an HTML
editor or the DOM inspector of the browser).

Also note that:

.. code:: html

   [[=x]]

generates

.. code:: python

   response.write(x)

Variables injected into the HTML in this way are escaped by default. The
escaping is ignored if ``x`` is an ``XML`` object, even if escape is set
to ``True`` (see :ref:`XML` later for details).

Here is an example that introduces the ``H1`` helper:

.. code:: html

   [[=H1(i)]]

which is translated to:

.. code:: python

   response.write(H1(i))

upon evaluation, the ``H1`` object and its components are recursively
serialized, escaped and written to the response body. The tags generated
by ``H1`` and inner HTML are not escaped. This mechanism guarantees that
all text — and only text — displayed on the web page is always escaped,
thus preventing XSS vulnerabilities. At the same time, the code is
simple and easy to debug.

The method ``response.write(obj, escape=True)`` takes two arguments, the
object to be written and whether it has to be escaped (set to ``True``
by default). If ``obj`` has an ``.xml()`` method, it is called and the
result written to the response body (the ``escape`` argument is
ignored). Otherwise it uses the object’s ``__str__`` method to serialize
it and, if the escape argument is ``True``, escapes it. All built-in
helper objects (``H1`` in the example) are objects that know how to
serialize themselves via the ``.xml()`` method.

This is all done transparently.


.. Note::
   While the response object used inside the controllers is a
   full ``bottle.response`` object, inside the yatl templates it is 
   replaced by a dummy object (``yatl.template.DummyResponse``). 
   This object is quite different, and much simpler: it only has a write method!
   Also, you never need to (and never should) call the ``response.write``
   method explicitly.
   

Basic syntax
------------

The py4web template language supports all Python control structures.
Here we provide some examples of each of them. They can be nested
according to usual programming practice.
You can easily test them by copying the _scaffold app (see
:ref:`copying-the-scaffold-app`) and then editing the file
``new_app/template/index.html``.

``for...in``
~~~~~~~~~~~~

In templates you can loop over any iterable object:

.. code:: html

   [[items = ['a', 'b', 'c'] ]]
   <ul>
   [[for item in items:]]<li>[[=item]]</li>[[pass]]
   </ul>

which produces:

.. code:: html

   <ul>
   <li>a</li>
   <li>b</li>
   <li>c</li>
   </ul>

Here ``items`` is any iterable object such as a Python list, Python
tuple, or Rows object, or any object that is implemented as an iterator.
The elements displayed are first serialized and escaped.

``while``
~~~~~~~~~

You can create a loop using the while keyword:

.. code:: html

   [[k = 3]]
   <ul>
   [[while k > 0:]]<li>[[=k]][[k = k - 1]]</li>[[pass]]
   </ul>

which produces:

.. code:: html

   <ul>
   <li>3</li>
   <li>2</li>
   <li>1</li>
   </ul>

``if...elif...else``
~~~~~~~~~~~~~~~~~~~~

You can use conditional clauses:

.. code:: html

   [[
   import random
   k = random.randint(0, 100)
   ]]
   <h2>
   [[=k]]
   [[if k % 2:]]is odd[[else:]]is even[[pass]]
   </h2>

which produces:

.. code:: html

   <h2>
   45 is odd
   </h2>

Since it is obvious that ``else`` closes the first ``if`` block, there
is no need for a ``pass`` statement, and using one would be incorrect.
However, you must explicitly close the ``else`` block with a ``pass``.

Recall that in Python “else if” is written ``elif`` as in the following
example:

.. code:: html

   [[
   import random
   k = random.randint(0, 100)
   ]]
   <h2>
   [[=k]]
   [[if k % 4 == 0:]]is divisible by 4
   [[elif k % 2 == 0:]]is even
   [[else:]]is odd
   [[pass]]
   </h2>

It produces:

.. code:: html

   <h2>
   64 is divisible by 4
   </h2>

``try...except...else...finally``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is also possible to use ``try...except`` statements in templates with one
caveat. Consider the following example:

.. code:: html

   [[try:]]
   Hello [[= 1 / 0]]
   [[except:]]
   division by zero
   [[else:]]
   no division by zero
   [[finally:]]
   <br />
   [[pass]]

It will produce the following output:

.. code:: html

   Hello division by zero
   <br />

This example illustrates that all output generated before an exception
occurs is rendered (including output that preceded the exception) inside
the try block. “Hello” is written because it precedes the exception.

``def...return``
~~~~~~~~~~~~~~~~

The py4web template language allows the developer to define and
implement functions that can return any Python object or a text/html
string. Here we consider two examples:

.. code:: html

   [[def itemize1(link): return LI(A(link, _href="http://" + link))]]
   <ul>
   [[=itemize1('www.google.com')]]
   </ul>

produces the following output:

.. code:: html

   <ul>
   <li><a href="http://www.google.com">www.google.com</a></li>
   </ul>

The function ``itemize1`` returns a helper object that is inserted at
the location where the function is called.

Consider now the following code:

.. code:: html

   [[def itemize2(link):]]
   <li><a href="http://[[=link]]">[[=link]]</a></li>
   [[return]]
   <ul>
   [[itemize2('www.google.com')]]
   </ul>

It produces exactly the same output as above. In this case, the function
``itemize2`` represents a piece of HTML that is going to replace the
py4web tag where the function is called. Notice that there is no ‘=’ in
front of the call to ``itemize2``, since the function does not return
the text, but it writes it directly into the response.

There is one caveat: functions defined inside a template must terminate with
a ``return`` statement, or the automatic indentation will fail.

Information workflow
--------------------

For dynamically modifying the workflow of the information there are custom commands available: 
``extend``, ``include``, ``block`` and ``super``. Note that they are special template
directives, not Python commands.

In addition, you can use normal Python functions inside templates.


``extend`` and ``include``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Templates can extend and include other templates in a tree-like structure.

For example, we can think of a template “index.html” that extends
“layout.html” and includes “body.html”. At the same time, “layout.html”
may include “header.html” and “footer.html”.

The root of the tree is what we call a **layout template**. Just like any other
HTML template file, you can edit it from the command line or using the py4web Dashboard.
The file name “layout.html” is just a convention.

Here is a minimalist page that extends the “layout.html” template and
includes the “page.html” template:

.. code:: html

   <!--minimalist_page.html-->
   [[extend 'layout.html']]
   <h1>Hello World</h1>
   [[include 'page.html']]

The extended layout file must contain an ``[[include]]`` directive,
something like:

.. code:: html

   <!--layout.html-->
   <html>
     <head>
       <title>Page Title</title>
     </head>
     <body>
       [[include]]
     </body>
   </html>

When the template is called, the extended (layout) template is loaded, and the
calling template replaces the ``[[include]]`` directive inside the layout.
If you don't write the ``[[include]]`` directive inside the layout, then it will
be included at the beginning of the file. Also, if you use multiple ``[[extend]]`` 
directives only the last one will be processed.
Processing continues recursively until all ``extend`` and ``include``
directives have been processed. The resulting template is then
translated into Python code. 

Note, when an application is bytecode
compiled, it is this Python code that is compiled, not the original template
files themselves. So, the bytecode compiled version of a given template is a
single .pyc file that includes the Python code not just for the original
template file, but for its entire tree of extended and included templates.

Any content or code that **precedes** the ``[[extend ...]]`` directive will
be inserted (and therefore executed) before the beginning of the
extended template's content/code. Although this is not typically used to
insert actual HTML content before the extended template's content, it can be
useful as a means to define variables or functions that you want to make
available to the extended template. For example, consider a template
“index.html”:

.. code:: html

   <!--index.html-->
   [[sidebar_enabled=True]]
   [[extend 'layout.html']]
   <h1>Home Page</h1>

and an excerpt from “layout.html”:

.. code:: html

   <!--layout.html-->
   [[include]]
   [[if sidebar_enabled:]]
       <div id="sidebar">
           Sidebar Content
       </div>
   [[pass]]

Because the ``sidebar_enabled`` assignment in “index.html” comes before
the ``extend``, that line gets inserted before the beginning of
“layout.html”, making ``sidebar_enabled`` available anywhere within the
“layout.html” code.

It is also worth pointing out that the variables returned by the
controller function are available not only in the function’s main template,
but in all of its extended and included templates as well.

Extending using variables
~~~~~~~~~~~~~~~~~~~~~~~~~

The argument of an ``extend`` or ``include`` (i.e., the extended or
included template name) can be a Python variable (though not a Python
expression). However, this imposes a limitation – templates that use
variables in ``extend`` or ``include`` statements cannot be bytecode
compiled. As noted above, bytecode-compiled templates include the entire
tree of extended and included templates, so the specific extended and
included templates must be known at compile time, which is not possible if
the template names are variables (whose values are not determined until run
time). Because bytecode compiling templates can provide a significant speed
boost, using variables in ``extend`` and ``include`` should generally be
avoided if possible.

In some cases, an alternative to using a variable in an ``include`` is
simply to place regular ``[[include ...]]`` directives inside an
``if...else`` block.

.. code:: html

   [[if some_condition:]]
      [[include 'this_template.html']]
   [[else:]]
      [[include 'that_template.html']]
   [[pass]]

The above code does not present any problem for bytecode compilation
because no variables are involved. Note, however, that the bytecode
compiled template will actually include the Python code for both
“this_template.html” and “that_template.html”, though only the code for one of
those templates will be executed, depending on the value of
``some_condition``.

Keep in mind, this only works for ``include`` – you cannot place
``[[extend ...]]`` directives inside ``if...else`` blocks.

Layouts are used to encapsulate page commonality (headers, footers,
menus), and though they are not mandatory, they will make your
application easier to write and maintain. 

Template Functions
~~~~~~~~~~~~~~~~~~

Consider this “layout.html”:

.. code:: html

   <!--layout.html-->
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

and this extending template

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
is included in the extended template without the ``=`` prefix.

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
layout calls the template function using ``[[mysidebar()]]`` rather than
``[[=mysidebar()]]``. Functions defined in this way can take arguments.

``block`` and ``super`` 
~~~~~~~~~~~~~~~~~~~~~~~

The main way to make a template more modular is by using
``[[block ...]]``\ s and this mechanism is an alternative to the
mechanism discussed in the previous section.

To understand how this works, consider apps based on the scaffolding app
welcome, which has a template layout.html. This template is extended by the template
``default/index.html`` via ``[[extend 'layout.html']]``. The contents of
layout.html predefine certain blocks with certain default content, and
these are therefore included into default/index.html.

You can override these default content blocks by enclosing your new
content inside the same block name. The location of the block in the
layout.html is not changed, but the contents is.

Here is a simplified version. Imagine this is “layout.html”:

.. code:: html

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

and this is a simple extending template ``default/index.html``:

.. code:: html

   [[extend 'layout.html']]
   Hello World!!!
   [[block mysidebar]]
   my new sidebar!!!
   [[end]]

It generates the following output, where the content is provided by the
over-riding block in the extending template, yet the enclosing DIV and class
comes from layout.html. This allows consistency across templates:

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

You can have many blocks, and if a block is present in the extended template
but not in the extending template, the content of the extended template is used.
Also, notice that unlike with functions, it is not necessary to define
blocks before the ``[[extend ...]]`` – even if defined after the
``extend``, they can be used to make substitutions anywhere in the
extended template.

Inside a block, you can use the expression ``[[super]]`` to include the
content of the parent. For example, if we replace the above extending
template with:

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




Page layout standard structure
------------------------------


Default page layout
~~~~~~~~~~~~~~~~~~~

The “templates/layout.html” that currently ships with the py4web **_scaffold**
application is quite complex but it has the following structure:

.. code-block:: html
  :linenos:

   <!DOCTYPE html>
   <html>
     <head>
       <base href="[[=URL('static')]]/">
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <link rel="shortcut icon" href="data:image/x-icon;base64,AAABAAEAAQEAAAEAIAAwAAAAFgAAACgAAAABAAAAAgAAAAEAIAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAAAAAA=="/>
       <link rel="stylesheet" href="css/no.css">
       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==" crossorigin="anonymous" />
       <style>.py4web-validation-error{margin-top:-16px; font-size:0.8em;color:red}</style>
       [[block page_head]]<!-- individual pages can customize header here -->[[end]]
     </head>
     <body>
       <header>
         <!-- Navigation bar -->
         <nav class="black">
           <!-- Logo -->
           <a href="[[=URL('index')]]">
             <b>py4web <script>document.write(window.location.href.split('/')[3]);</script></b>
           </a>
           <!-- Do not touch this -->
           <label for="hamburger">☰</label>
           <input type="checkbox" id="hamburger">
           <!-- Left menu ul/li -->
           [[block page_left_menu]][[end]]
           <!-- Right menu ul/li -->
           <ul>
             [[if globals().get('user'):]]
             <li>
               <a class="navbar-link is-primary">
                 [[=globals().get('user',{}).get('email')]]
               </a>
               <ul>
                 <li><a href="[[=URL('auth/profile')]]">Edit Profile</a></li>
                 <li><a href="[[=URL('auth/change_password')]]">Change Password</a></li>
                 <li><a href="[[=URL('auth/logout')]]">Logout</a></li>
               </ul>
             </li>
             [[else:]]
             <li>
               Login
               <ul>
                 <li><a href="[[=URL('auth/register')]]">Sign up</a></li>
                 <li><a href="[[=URL('auth/login')]]">Log in</a></li>
               </ul>
             </li>
             [[pass]]
           </ul>
         </nav>
       </header>
       <!-- beginning of HTML inserted by extending template -->
       <center>
         <div>
           <!-- Flash alert messages, first optional one in data-alert -->
           <flash-alerts class="padded" data-alert="[[=globals().get('flash','')]]"></flash-alerts>
         </div>
         <main class="padded">
           <!-- contect injected by extending page -->
           [[include]]
         </main>
       </center>
       <!-- end of HTML inserted by extending template -->
       <footer class="black padded">
         <p>
           Made with py4web
         </p>
       </footer>
     </body>
     <!-- You've gotta have utils.js -->
     <script src="js/utils.js"></script>
     [[block page_scripts]]<!-- individual pages can add scripts here -->[[end]]
   </html>


There are a few features of this default layout that make it very easy
to use and customize:

-  it is written in HTML5
-  on line 7 it's used the ``no.css`` stylesheet, see
   `here <https://github.com/mdipierro/no.css/>`__
-  on line 58 ``[[include]]`` is replaced by the content of the extending template when
   the page is rendered
-  it contains the following blocks: page_head, page_left_menu, page_scripts
-  on line 30 it checks if the user is logged on and changes the menu accordingly
-  on line 54 it checks for flash alert messages


Of course you can also completely replace the “layout.html” and
the stylesheet with your own. 


Mobile development
~~~~~~~~~~~~~~~~~~

Although the default layout.html is designed to be mobile-friendly, one
may sometimes need to use different templates when a page is visited by a
mobile device.
