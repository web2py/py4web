======================
YATL Template Language
======================

py4web uses Python for its models, controllers, and views, although it
uses a slightly modified Python syntax in the views to allow more
readable code without imposing any restrictions on proper Python usage.

py4web uses ``[[ ... ]]`` to escape Python code embedded in HTML. The
advantage of using square brackets instead of angle brackets is that
it’s transparent to all common HTML editors. This allows the developer
to use those editors to create py4web views.

Since the developer is embedding Python code into HTML, the document
should be indented according to HTML rules, and not Python rules.
Therefore, we allow unindented Python inside the ``[[ ... ]]`` tags.
Since Python normally uses indentation to delimit blocks of code, we
need a different way to delimit them; this is why the py4web template
language makes use of the Python keyword ``pass``.

   A code block starts with a line ending with a colon and ends with a
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
   [[for x in range(10):]][[=x]]hello<br />[[pass]]
   </body></html>

it translates it into a program:

.. code:: python

   response.write("""<html><body>""", escape=False)
   for x in range(10):
       response.write(x)
       response.write("""hello<br />""", escape=False)
   response.write("""</body></html>""", escape=False)

``response.write`` writes to the ``response.body``.

When there is an error in a py4web view, the error report shows the
generated view code, not the actual view as written by the developer.
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
to ``True``.

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

This is all done transparently. You never need to (and never should)
call the ``response.write`` method explicitly.

Basic syntax
------------

The py4web template language supports all Python control structures.
Here we provide some examples of each of them. They can be nested
according to usual programming practice.

``for...in``
~~~~~~~~~~~~

In templates you can loop over any iterable object:

.. code:: html

   [[items = ['a', 'b', 'c']]]
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

It is also possible to use ``try...except`` statements in views with one
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

There is one caveat: functions defined inside a view must terminate with
a ``return`` statement, or the automatic indentation will fail.
