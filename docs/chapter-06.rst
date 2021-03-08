========
Fixtures
========

A fixture is defined as “a piece of equipment or furniture which is
fixed in position in a building or vehicle”. In our case a fixture is
something attached to the action that processes an HTTP request in order
to produce a response.

When processing any HTTP requests there are some optional operations we
may want to perform. For example parse the cookie to look for session
information, commit a database transaction, determine the preferred
language from the HTTP header and lookup proper internationalization,
etc. These operations are optional. Some actions need them and some
actions do not. They may also depend on each other. For example, if
sessions are stored in the database and our action needs it, we may need
to parse the session cookie from the HTTP header, pick up a connection from
the database connection pool, and - after the action has been executed -
save the session back in the database if data has changed.

PY4WEB fixtures provide a mechanism to specify what an action needs so
that py4web can accomplish the required tasks (and skip non required
ones) in the most efficient manner. Fixtures make the code efficient and
reduce the need for boilerplate code.

PY4WEB fixtures are similar to WSGI middleware and BottlePy plugin
except that they apply to individual actions, not to all of them, and
can depend on each other.

PY4WEB comes with some pre-defined fixtures:
sessions, url signing and flash messages will be fully 
explained in this chapter. Database connections, internationalization,
authentication, and templates will instead be just outlined here since
they have dedicated chapters.
The developer is also free to add fixtures, for example, to handle a third
party template language or third party session logic; this is explained
later in the :ref:`Custom fixtures` paragraph.


Using Fixtures
--------------

As we've seen in the previous chapter, fixtures are the arguments of the decorator
``@action.uses(...)``. You can specify
multiple fixtures in one decorator or you can have multiple decorators.

Also, fixtures can be applied in groups. For example:

::

   preferred = action.uses(session, auth, T, flash)

Then you can apply all of them at once with:

::

   @action('index.html')
   @preferred
   def index():
       return dict()

Usually, it's not important the order you use to specify the fixtures, because py4web
knows well how to manage them. But there is an important exception:
the Template fixture must always be the last one.

The Template fixture
--------------------

PY4WEB by default uses the YATL template language and provides a
fixture for it.

.. code:: python

   from py4web import action
   from py4web.core import Template

   @action('index')
   @action.uses(Template('index.html', delimiters='[[ ]]'))
   def index(): 
       return dict(message="Hello world")

Note: this example assumes that you created the application from the
scaffolding app, so that the template index.html is already created for
you.

The Template object is a Fixture. It transforms the ``dict()`` returned
by the action into a string by using the ``index.html`` template file.
In a later chapter we will provide an example of how to define a custom
fixture to use a different template language, for example Jinja2.

Notice that since the use of templates is very common and since, most
likely, every action uses a different template, we provide some
syntactic sugar, and the two following lines are equivalent:

.. code:: python

   @action.uses('index.html')
   @action.uses(Template('index.html', delimiters='[[ ]]')

Notice that py4web template files are cached in RAM. The py4web caching
object is described later on :ref:`Caching and Memoize`.

.. warning::
   If you use multiple fixtures, always place the template as the last one.
   Otherwise, it will not have access to various things it needs from the
   other fixtures.

   For example:

      .. code:: python

         @action.uses(session, db, 'index.html') # right
         @action.uses('index.html', session, db) # wrong

The Translator fixture
----------------------

Here is an example of usage:

.. code:: python

   from py4web import action, Translator
   import os

   T_FOLDER = os.path.join(os.path.dirname(__file__), 'translations')
   T = Translator(T_FOLDER)

   @action('index')
   @action.uses(T)
   def index(): return str(T('Hello world'))

The string `hello world` will be translated based on the
internationalization file in the specified “translations” folder that
best matches the HTTP ``accept-language`` header.

Here ``Translator`` is a py4web class that extends
``pluralize.Translator`` and also implements the ``Fixture`` interface.

We can easily combine multiple fixtures. Here, as example, we make
action with a counter that counts “visits”.

.. code:: python

   from py4web import action, Session, Translator, DAL
   from py4web.utils.dbstore import DBStore
   import os
   db = DAL('sqlite:memory')
   session =  Session(storage=DBStore(db))
   T_FOLDER = os.path.join(os.path.dirname(__file__), 'translations')
   T = Translator(T_FOLDER)

   @action('index')
   @action.uses(session, T)
   def index():
       counter = session.get('counter', -1)
       counter += 1
       session['counter'] = counter
       return str(T("You have been here {n} times").format(n=counter))

Now create the following translation file ``translations/en.json``:

.. code:: json

   {"You have been here {n} times": 
     {
       "0": "This your first time here", 
       "1": "You have been here once before", 
       "2": "You have been here twice before",
       "3": "You have been here {n} times",
       "6": "You have been here more than 5 times"
     }
   }

When visiting this site with the browser language preference set to
english and reloading multiple times you will get the following
messages:

::

   This your first time here
   You have been here once before
   You have been here twice before
   You have been here 3 times
   You have been here 4 times
   You have been here 5 times
   You have been here more than 5 times

Now try create a file called ``translations/it.json`` which contains:

.. code:: json

   {"You have been here {n} times":
     {
       "0": "Non ti ho mai visto prima",
       "1": "Ti ho gia' visto",
       "2": "Ti ho gia' visto 2 volte",
       "3": "Ti ho visto {n} volte",
       "6": "Ti ho visto piu' di 5 volte"
     }
   }

Set your browser preference to Italian: now the messages will be
automatically translated to Italian.

The Flash fixture
-----------------

It is common to want to display “alerts” to the users. Here we refer to
them as **flash messages**. There is a little more to it than just
displaying a message to the view, because flash messages:

-  can have state that must be preserved after redirection
-  can be generated both server side and client side
-  may have a type
-  should be dismissible

The Flash helper handles the server side of them. Here is an example:

.. code:: python

   from py4web import Flash

   flash = Flash()

   @action('index')
   @action.uses(flash)
   def index():
       flash.set("Hello World", _class="info", sanitize=True)
       return dict()

and in the template:

.. code:: html

   ...
   <div id="py4web-flash"></div>
   ...
   <script src="js/utils.js"></script>
   [[if globals().get('flash'):]]
   <script>utils.flash([[=XML(flash)]]);</script>
   [[pass]]

By setting the value of the message in the flash helper, a flash
variable is returned by the action and this triggers the JS in the
template to inject the message in the ``py4web-flash`` DIV which you
can position at your convenience. Also the optional class is applied to
the injected HTML.

If a page is redirected after a flash is set, the flash is remembered.
This is achieved by asking the browser to keep the message temporarily
in a one-time cookie. After redirection the message is sent back by the
browser to the server and the server sets it again automatically before
returning the content, unless it is overwritten by another set.

The client can also set/add flash messages by calling:

::

   utils.flash({'message': 'hello world', 'class': 'info'});

py4web defaults to an alert class called ``info`` and most CSS
frameworks define classes for alerts called ``success``, ``error``,
``warning``, ``default``, and ``info``. Yet, there is nothing in py4web
that hardcodes those names. You can use your own class names.

You can see the basic usage of flash messages in the **examples** app.

The Session fixture
-------------------

Simply speaking, a session can be defined as a way to preserve information that is
desired to persist throughout the user's interaction with the web site or web application.
In other words, sessions render the stateless HTTP connection a stateful one.

In py4web, the session object is also a fixture. Here is a simple example of its usage
to implement a counter.

::

   from py4web import Session, action
   session = Session(secret='my secret key')

   @action('index')
   @action.uses(session)
   def index():
       counter = session.get('counter', -1)
       counter += 1
       session['counter'] = counter
       return "counter = %i" % counter

The counter will start from 0; its value will be remembered and
increased everytime you reload the page.

.. image:: images/simple_counter.png

Opening the page in a new browser tab will give you the updated
counter value. Closing and reopening the browser, or opening a
new *private window*, will instead restart the counter from 0.

Usually the informations saved in the session object are related
to the user - like its username, preferences, last pages visited,
shopping cart and so on. The session object has the same interface
as a Python dictionary but in py4web sessions are always stored using
JSON (**JWT** specifically, i.e. 
`JSON Web Token <https://jwt.io/introduction>`__),
therefore you should only store objects that are JSON serializable.
If the object is not JSON serializable, it will be serialized using
the ``__str__`` operator and some information may be lost.

The information composing the session object can be saved:

- client-side, by only using cookies (default)
- server-side, but you'll still need minimal cookies for identifying
  the clients

By default py4web sessions never expire (unless they contain login
information, but that is another story) even if an expiration can be
set. Other parameters can be specified as well:

::

   session = Session(secret='my secret key',
                     expiration=3600,
                     algorithm='HS256',
                     storage=None,
                     same_site='Lax')

Here:

-  ``secret`` is the passphrase used to sign the informations
-  ``expiration`` is the maximum lifetime of the session, in seconds
   (default = None, i.e. no timeout)  
-  ``algorithm`` is the algorithm to be used for the JWT token
   signature ('HS256' by default)
-  ``storage`` is a parameter that allows to specify an alternate
   session storage method (for example Redis, or database). If not
   specified, the default cookie method will be used
-  ``same_site`` is an option that prevents CSRF attacks (Cross-Site
   Request Forgery) and is enabled by default with the 'Lax' option.
   You can read more about it
   `here <https://owasp.org/www-community/SameSite>`__


If storage is not provided, session is stored in client-side jwt cookie.
Otherwise, we have server-side session: the jwt is stored in storage and
only its UUID key is stored in the cookie. This is the reason why the
secret is not required with server-side sessions.


Client-side session in cookies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default the session object is stored inside a cookie called
``appname_session``. It's a JWT, hence encoded in a URL-friendly string
format and signed using the provided secret for preventing tampering.
Notice that it's not encrypted (in fact it's quite trivial to read its
content from http communications or from disk), so do not place any
sensitive information inside, and use a complex secret.
If the secret changes existing sessions are invalidated.
If the user switches from HTTP to HTTPS or
vice versa, the user session is also invalidated. Session in cookies have a
small size limit (4 kbytes after being serialized and encoded) so do
not put too much into them.

Server-side session in memcache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires memcache installed and configured.

.. code:: python

   import memcache, time
   conn = memcache.Client(['127.0.0.1:11211'], debug=0)
   session = Session(storage=conn)


Server-side session in Redis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires `Redis <https://redis.io/>`__ installed and configured.


.. code:: python

   import redis
   conn = redis.Redis(host='localhost', port=6379)
   conn.set = lambda k, v, e, cs=conn.set, ct=conn.ttl: (cs(k, v), e and ct(e))
   session = Session(storage=conn)

Notice: a storage object must have ``get`` and ``set`` methods and the
``set`` method must allow to specify an expiration. The redis connection
object has a ``ttl`` method to specify the expiration, hence we monkey
patch the ``set`` method to have the expected signature and
functionality.

Server-side session in database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from py4web import Session, DAL
   from py4web.utils.dbstore import DBStore
   db = DAL('sqlite:memory')
   session =  Session(storage=DBStore(db))

.. warning::
   the ``'sqlite:memory'`` database used in this example
   **cannot be used in multiprocess environment**;
   the quirk is that your application will still work but in non-deterministic
   and unsafe mode, since each process/worker will have its own independent
   in-memory database.

This is one case when a fixture (session) requires another
fixture (db). This is handled automatically by py4web and the following lines
are equivalent:

.. code:: python

   @action.uses(session)
   @action.uses(db, session)

Server-side session anywhere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can easily store sessions in any place you want. All you need to do
is provide to the ``Session`` object a ``storage`` object with both
``get`` and ``set`` methods. For example, imagine you want to store
sessions on your local filesystem:

.. code:: python

   import os
   import json

   class FSStorage:
      def __init__(self, folder):
          self.folder = folder
      def get(self, key):
          filename = os.path.join(self.folder, key)
          if os.path.exists(filename):
              with open(filename) as fp:
                 return json.load(fp)
          return None
      def set(self, key, value, expiration=None):
          filename = os.path.join(self.folder, key)
          with open(filename, 'w') as fp:
              json.dump(value, fp)

   session = Session(storage=FSStorage('/tmp/sessions'))

We leave to you as an exercise to implement expiration, limit the number
of files per folder by using subfolders, and implement file locking. Yet
we do not recomment storing sessions on the filesystem: it is
inefficient and does not scale well.

The URLsigner fixture
---------------------

A signed URL is a URL that provides limited permission and time to make an
HTTP request by containing authentication information in its query string.
The typical usage is as follows:

.. code:: python
   
   from py4web.utils import URLSigner

   # We build a URL signer.
   url_signer = URLSigner(session)

   @action('/somepath')
   @action.uses(url_signer)
   def somepath():
      # This controller signs a URL.
      return dict(signed_url = URL('/anotherpath', signer=url_signer))
   
   @action('/anotherpath')
   @action.uses(url_signer.verify())
   def anotherpath():
      # The signature has been verified.
      return dict()

The DAL fixture
---------------

We have already used the ``DAL`` fixture in the context of sessions but
maybe you want direct access to the DAL object for the purpose of
accessing the database, not just sessions.

PY4WEB, by default, uses the **PyDAL** (Python Database Abstraction Layer)
which is documented in the next chapter. Here is an example, please
remember to create the ``databases`` folder under your project in case
it doesn’t exist:

.. code:: python

   from datetime import datetime
   from py4web import action, request, DAL, Field
   import os

   DB_FOLDER = os.path.join(os.path.dirname(__file__), 'databases')
   db = DAL('sqlite://storage.db', folder=DB_FOLDER, pool_size=1)
   db.define_table('visit_log', Field('client_ip'), Field('timestamp', 'datetime'))
   db.commit()

   @action('index')
   @action.uses(db)
   def index():
       client_ip = request.environ.get('REMOTE_ADDR')
       db.visit_log.insert(client_ip=client_ip, timestamp=datetime.utcnow())
       return "Your visit was stored in database"

Notice that the database fixture defines (creates/re-creates) tables
automatically when py4web starts (and every time it reloads this app)
and picks a connection from the connection pool at every HTTP request.
Also each call to the ``index()`` action is wrapped into a transaction
and it commits ``on_success`` and rolls back ``on_error``.

The Auth fixture
----------------

``auth`` and ``auth.user`` are both fixtures that depend on
``session`` and ``db``. Their role is to provide the action with
authentication information.

Auth is used as follows:

.. code:: python

   from py4web import action, redirect, Session, DAL, URL
   from py4web.utils.auth import Auth
   import os

   session = Session(secret='my secret key')
   DB_FOLDER = os.path.join(os.path.dirname(__file__), 'databases')
   db = DAL('sqlite://storage.db', folder=DB_FOLDER, pool_size=1)
   auth = Auth(session, db)
   auth.enable()

   @action('index')
   @action.uses(auth)
   def index():
       user = auth.get_user() or redirect(URL('auth/login'))
       return 'Welcome %s' % user.get('first_name')

The constructor of the ``Auth`` object defines the ``auth_user`` table
with the following fields: username, email, password, first_name,
last_name, sso_id, and action_token (the last two are mostly for
internal use).

The ``auth`` object exposes the method:``auth.enable()`` which
registers multiple actions including ``{appname}/auth/login``.
It requires the presence of the ``auth.html`` template and the
``auth`` value component provided by the
``_scaffold`` app. It also exposes the method:

.. code:: python

   auth.get_user()

which returns a python dictionary containing the information of the
currently logged in user. If the user is not logged-in, it returns
``None`` and in this case the code of the example redirects to the
``auth/login`` page.

Since this check is very common, py4web provides an additional fixture
``auth.user``:

.. code:: python

   @action('index')
   @action.uses(auth.user)
   def index():
       user = auth.get_user()
       return 'Welcome %s' % user.get('first_name')

This fixture automatically redirects to the ``auth/login`` page if user
is not logged-in, hence this example is equivalent to the previous one.

The ``auth`` fixture is plugin based: it supports multiple plugin
methods including OAuth2 (Google, Facebook, Twitter), PAM and LDAP.
The :ref:`Authentication and Access control` chapter will show you
all the related details.

Caveats about fixtures
----------------------

Since fixtures are shared by multiple actions you are not allowed to
change their state because it would not be thread safe. There is one
exception to this rule. Actions can change some attributes of database
fields:

.. code:: python

   from py4web import action, request, DAL, Field
   from py4web.utils.form import Form
   import os

   DB_FOLDER = os.path.join(os.path.dirname(__file__), 'databases')
   db = DAL('sqlite://storage.db', folder=DB_FOLDER, pool_size=1)
   db.define_table('thing', Field('name', writable=False))

   @action('index')
   @action.uses(db, 'generic.html')
   def index():
       db.thing.name.writable = True
       form = Form(db.thing)
       return dict(form=form)

Note thas this code will only be able to display a form, to process it
after submit, additional code needs to be added, as we will see later
on. This example is assuming that you created the application from the
scaffolding app, so that a generic.html is already created for you.

The ``readable``, ``writable``, ``default``, ``update``, and ``require``
attributes of ``db.{table}.{field}`` are special objects of class
``ThreadSafeVariable`` defined the ``threadsafevariable`` module. These
objects are very much like Python thread local objects but they are
re-initialized at every request using the value specified outside of the
action. This means that actions can safely change the values of these
attributes.

Custom fixtures
---------------

A fixture is an object with the following minimal structure:

.. code:: python

   from py4web import Fixture

   class MyFixture(Fixture):
       def on_request(self): pass
       def on_success(self): pass
       def on_error(self): pass
       def transform(self, data): return data

If an action uses this fixture:

::

   @action('index')
   @action.uses(MyFixture())
   def index(): return 'hello world'

then:

* the ``on_request()`` function is guaranteed to be called before the ``index()``
  function is called
* the ``on_success()`` function is guaranteed to be called if
  the ``index()`` function returns successfully or raises ``HTTP`` or
  performs a ``redirect``
* the ``on_error()`` function is guaranteed to be called
  when the ``index()`` function raises any exception other than ``HTTP``.
* the ``transform`` function is called to perform any desired
  transformation of the value returned by the ``index()`` function.


Caching and Memoize
-------------------

py4web provides a cache in RAM object that implements the last recently
used (LRU) algorithm. It can be used to cache any function via a
decorator:

.. code:: python

   import uuid
   from py4web import Cache, action
   cache = Cache(size=1000)

   @action('hello/<name>')
   @cache.memoize(expiration=60)
   def hello(name):
       return "Hello %s your code is %s" % (name, uuid.uuid4())

It will cache (memoize) the return value of the ``hello`` function, as
function of the input ``name``, for up to 60 seconds. It will store in
cache the 1000 most recently used values. The data is always stored in
RAM.

The ``cache`` object is not a fixture and it should not and cannot be
registered using the ``@action.uses`` decorator but we mention it here
because some of the fixtures use this object internally. For example,
template files are cached in RAM to avoid accessing the file system
every time a template needs to be rendered.

Convenience Decorators
----------------------

The ``_scaffold`` application, in ``common.py`` defines two special
convenience decorators:

::

   @unauthenticated
   def index():
       return dict()

and

::

   @authenticated
   def index():
       return dict()

They apply all of the decorators below (db, session, T, flash, auth),
use a template with the same name as the function (.html), and also
register a route with the name of action followed by the number of
arguments of the action separated by a slash (/).

-  @unauthenticated does not require the user to be logged in.
-  @authenticated required the user to be logged in.

They can be combined with (and precede) other ``@action.uses(...)`` but
they should not be combined with ``@action(...)`` because they perform
that function automatically.
