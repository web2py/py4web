## Fixtures

A fixture is defined as "a piece of equipment or furniture which is fixed in position in a building or vehicle". In our case a fixture is something attached to the action that
processes an HTTP request in order to produce a response.

When processing any HTTP requests there are some optional operations we may want to perform. For example parse the cookie to look for session information, commit a database
transaction, determine the preferred language from the HTTP header and lookup proper internationalization, etc. These operations are optional. Some actions need them and some
actions do not. They may also depend on each other. For example, if sessions are stored in the database and our action needs it, we may need to parse the session cookie from
the header, pick up a connection from the database connection pool, and - after the action has been executed - save the session back in the database if data has changed.

PY4WEB fixtures provide a mechanism to specify what an action needs so that py4web can accomplish the required tasks (and skip non required ones) in the most efficient manner.
Fixtures make the code efficient and reduce the need for boilerplate code.

PY4WEB fixtures are similar to WSGI middleware and BottlePy plugin except that they apply to individual actions, not to all of them, and can depend on each other.

PY4WEB comes with some pre-defined fixtures for actions that need sessions, database connections, internationalization, authentication, and templates. Their usage will be
explained in this chapter. The Developer is also free to add fixtures, for example, to handle a third party template language or third party session logic.

### Important about Fixtures

In the examples below we will explain how to apply individual fixtures.
In practice fixtures can be applied in groups. For example:

``
preferred = action.uses(Session, Auth, T, Flash)
``

Then you can apply all of the at once with:

``
@action('index.html')
@preferred
def index():
    return dict()
``

### Templates

PY4WEB, by default uses the yatl template language and provides a fixture for it.

``
from py4web import action
from py4web.core import Template

@action('index')
@action.uses(Template('index.html', delimiters='[[ ]]'))
def index(): 
    return dict(message="Hello world")
``:python

Note: This example assumes that you created the application from the scaffolding app, so that the template index.html is already created for you.

The Template object is a Fixture. It transforms the ``dict()`` returned by the action into a string by using the ``index.html`` template file. In a later chapter we will
provide an example of how to define a custom fixture to use a different template language, for example Jinja2.

Notice that since the use of templates is very common and since, most likely, every action uses a different template, we provide some syntactic sugar, and the two following
lines are equivalent:

``
@action.uses('index.html')
@action.uses(Template('index.html', delimiters='[[ ]]')
``:python

Notice that py4web template files are cached in RAM. The py4web caching object is described later.

### Sessions

The session object is also a Fixture. Here is a typical example of usage to implement a counter.

``
from py4web import Session, action
session = Session(secret='my secret key')

@action('index')
@action.uses(session)
def index():
    counter = session.get('counter', -1)
    counter += 1
    session['counter'] = counter
    return "counter = %i" % counter
``

Notice that the session object has the same interface as a Python dictionary.

By default the session object is stored in a cookie called, signed and encrypted, using the provided secret. If the secret changes existing sessions are invalidated. If the
user switches from HTTP to HTTPS or vice versa, the user session is invalidated. Session in cookies have a small size limit (4Kbytes after being serialized and encrypted) so
do not put too much into them.

In py4web sessions are dictionaries but they are stored using JSON (JWT specifically) therefore you should only store objects that are JSON serializable. If the object is not
JSON serializable, it will be serialized using the ``__str__`` operator and some information may be lost.

By default py4web sessions never expire (unless they contain login information, but that is another story) even if an expiration can be set. Other parameters can be specified
as well:

``
session = Session(secret='my secret key',
                  expiration=3600,
                  algorithm='HS256',
                  storage=None,
                  same_site='Lax')
``

- Here ``algorithm`` is the algorithm to be used for the JWT token signature. 
- ``storage`` is a parameter that allows to specify an alternate session storage method (for example redis, or database).
- ``same_site`` is an option that prevents CSRF attacks and is enabled by default. You can read more about it [here](https://www.owasp.org/index.php/SameSite).

#### Session in memcache

``
import memcache, time
conn = memcache.Client(['127.0.0.1:11211'], debug=0)
session = Session(storage=conn)
``:python

Notice that a secret is not required when storing cookies in memcache because in this case the cookie only contains the UUID of the session.

#### Session in redis

``
import redis
conn = redis.Redis(host='localhost', port=6379)
conn.set = lambda k, v, e, cs=conn.set, ct=conn.ttl: (cs(k, v), e and ct(e))
session = Session(storage=conn)
``:python

Notice: a storage object must have ``get`` and ``set`` methods and the ``set`` method must allow to specify an expiration. The redis connection object has a `ttl`` method to
specify the expiration, hence we monkey patch the ``set`` method to have the expected signature and functionality.

#### Session in database

``
from py4web import Session, DAL
from py4web.utils.dbstore import DBStore
db = DAL('sqlite:memory')
session =  Session(storage=DBStore(db))
``:python

A secret is not required when storing cookies in the database because in this case the cookie only contains the UUID of the session.

Also this is one case when the a fixture (session) requires another fixture (db). This is handled automatically by py4web and the following are equivalent:

``
@action.uses(session)
@action.uses(db, session)
``:python


#### Session anywhere

You can easily store sessions in any place you want. All you need to do is provide to the ``Session`` object a ``storage`` object with both ``get`` and ``set`` methods. For
example, imagine you want to store sessions on your local filesystem:

``
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
``:python

We leave to you as an exercise to implement expiration, limit the number of files per folder by using subfolders, and implement file locking. Yet we do not recomment storing
sessions on the filesystem: it is inefficient and does not scale well.


## Translator

Here is an example of usage:

``
from py4web import action, Translator
import os

T_FOLDER = os.path.join(os.path.dirname(__file__), 'translations')
T = Translator(T_FOLDER)

@action('index')
@action.uses(T)
def index(): return str(T('Hello world'))
``:python

The string 'hello world` will be translated based on the internationalization file in the specified "translations" folder that best matches the HTTP ``accept-language`` header.

Here ``Translator`` is a py4web class that extends ``pluralize.Translator`` and also implements the ``Fixture`` interface.

We can easily combine multiple fixtures. Here, as example, we make action with a counter that counts "visits".

``
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
``:python

Now create the following translation file ``translations/en.json``:

``
{"You have been here {n} times": 
  {
    "0": "This your first time here", 
    "1": "You have been here once before", 
    "2": "You have been here twice before",
    "3": "You have been here {n} times",
    "6": "You have been here more than 5 times"
  }
}
``:json

When visiting this site with the browser language preference set to english and reloading multiple times you will get the following messages:

``
This your first time here
You have been here once before
You have been here twice before
You have been here 3 times
You have been here 4 times
You have been here 5 times
You have been here more than 5 times
``

Now try create a file called ``translations/it.json`` which contains:

``
{"You have been here {n} times":
  {
    "0": "Non ti ho mai visto prima",
    "1": "Ti ho gia' visto",
    "2": "Ti ho gia' visto 2 volte",
    "3": "Ti ho visto {n} volte",
    "6": "Ti ho visto piu' di 5 volte"
  }
}
``:json

and set your browser preference to Italian.

### The Flash fixture

It is common to want to display "alerts" to the suers. Here we refer to them as flash messeges.
There is a little more to it than just displaying a message to the view because flash messages can have state that must be preserved after redirection. Also they can be
generated both server side and client side, there can be only one at the time, they may have a type, and they should be dismissible.

The Flash helper handles the server side of them. Here is an example:

``
from py4web import Flash

flash = Flash()

@action('index')
@action.uses(Flash)
def index():
    flash.set("Hello World", _class="info", sanitize=True)
    return dict()
``

and in the template:

``
...
<div id="py4web-flash"></div>
...
<script src="js/utils.js"></script>
[[if globals().get('flash'):]]<script>utils.flash([[=XML(flash)]]);</script>[[pass]]
``

By setting the value of the message in the flash helper, a flash variable is returned by the action
and this trigger the JS in the template to inject the message in the ``#py4web-flash`` DIV which you
can position at your convenience. Also the optional class is applied to the injected HTML.

If a page is redirected after a flash is set, the flash is remembered. This is achieved by asking the
browser to keep the message temporarily in a one-time cookie. After redirection the message is sent
back by the browser to the server and the server sets it again automatically before returning content,
unless it is overwritten by another set.

The client can also set/add flash messages by calling:

``
utils.flash({'message': 'hello world', 'class': 'info'});
``

py4web defaults to an alert class called ``default`` and most CSS frameworks define classes for
alerts called ``success``, ``error``, ``warning``, ``default``, and ``info``. Yet,
there is nothing in py4web that hardcodes those names. You can use your own class names.


### The DAL fixture

We have already used the ``DAL`` fixture in the context of sessions but maybe you want direct access to the DAL object for the purpose of accessing the database, not just
sessions.

PY4WEB, by default, uses the PyDAL (Python Database Abstraction Layer) which is documented in a later chapter. Here is an example, please remember to create the
``databases`` folder under your project in case it doesn't exist:

``
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
``:python

Notice that the database fixture defines (creates/re-creates tables) automatically when py4web starts (and every time it reloads this app) and picks a connection from the
connection pool at every HTTP request. Also each call to the ``index()`` action is wrapped into a transaction and it commits ``on_success`` and rolls back ``on_error``.

### Caveats about Fixtures

Since fixtures are shared by multiple actions you are not allowed to change their state because it would not be thread safe.
There is one exception to this rule. Actions can change some attributes of database fields:

``
from py4web import Field, action, request, DAL, Field
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
)
``:python

Note thas this code will only be able to display a form, to process it after submit, additional code needs to be added, as we will see later on.
This example is assuming that you created the application from the scaffolding app, so that a generic.html is already created for you.

The ``readable``, ``writable``, ``default``, ``update``, and ``require`` attributes of ``db.{table}.{field}`` are special objects of class ``ThreadSafeVariable`` defined
the ``threadsafevariable`` module. These objects are very much like Python thread local objects but they are re-initialized at every request using the value specified outside
of the action. This means that actions can safely change the values of these attributes.

### Custom fixtures

A fixture is an object with the following minimal structure:

``
from py4web import Fixture

class MyFixture(Fixture):
    def on_request(self): pass
    def on_success(self): pass
    def on_error(self): pass
    def transform(self, data): return data
``:python

if an action uses this fixture:

``
@action('index')
@action.uses(MyFixture())
def index(): return 'hello world'
``

Then ``on_request()`` is guaranteed to be called before the ``index()`` function is called. The ``on_success()`` is guaranteed to be called if the ``index()`` function returns
successfully or raises ``HTTP`` or performs a ``redirect``. The ``on_error()`` is guaranteed to be called when the ``index()`` function raises any exception other than
``HTTP``. The ``transform`` function is called to perform any desired transformation of the value returned by the ``index()`` function.

### Auth and Auth.user

``auth`` and ``auth.user`` are both fixtures. They depend on ``session``. The role of access is to provide the action with authentication information. It is used as follows:

``
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
``:python

The constructor of the ``Auth`` object defines the ``auth_user`` table with the following fields: username, email, password, first_name, last_name, sso_id, and action_token
(the last two are mostly for internal use).

``auth.enable()`` registers multiple actions including ``{appname}/auth/login`` and it requires the presence of the ``auth.html`` template and the ``auth`` value component
provided by the ``_scaffold`` app.

The ``auth`` object is the fixture. It manages the user information. It exposes a single method:

``
auth.get_user()
``

which returns a python dictionary containing the information of the currently logged in user. If the user is not logged-in, it returns ``None``. The code of the example
redirects to the 'auth/login' page if there is no user.

Since this check is very common, py4web provides an additional fixture ``auth.user``:

``
@action('index')
@action.uses(auth.user)
def index():
    user = auth.get_user()
    return 'Welcome %s' % user.get('first_name')
``:python

This fixture automatically redirects to the ``auth/login`` page if user is not logged-in. It depends on ``auth``, which depends on ``db`` and ``session``.

The ``Auth`` fixture is plugin based and supports multiple plugin methods. They include Oauth2 (Google, Facebook, Twitter), PAM, LDAP, and SMAL2.

Here is an example of using the Google Oauth2 plugin:

``
from py4web.utils.auth_plugins.oauth2google import OAuth2Google
auth.register_plugin(OAuth2Google(
    client_id='...',
    client_secret='...',
    callback_url='auth/plugin/oauth2google/callback'))
``:python

The ``client_id`` and ``client_secret`` are provided by google. The callback url is the default option for py4web and it must be whitelisted with Google. All ``Auth`` plugins
are objects. Different plugins are configured in different ways but they are registered using ``auth.register_plugin(...)``. Examples are provided in ``_scaffold/common.py``. 

### Caching and Memoize

py4web provides a cache in ram object that implements the Last Recently Used (LRU) Algorithm. It can be used to cache any function via a decorator:

``
import uuid
from py4web import Cache, action
cache = Cache(size=1000)

@action('hello/<name>')
@cache.memoize(expiration=60)
def hello(name):
    return "Hello %s your code is %s" % (name, uuid.uuid4())
``:python

It will cache (memoize) the return value of the ``hello`` function, as function of the input ``name``, for up to 60 seconds. It will store in cache the 1000 most recently
    used values. The data is always stored in ram.

The Cache object is not a fixture and it should not and cannot be registered using the ``@action.uses`` object but we mention it here because some of the fixtures use this
    object internally. For example, template files are cached in ram to avoid accessing the file system every time a template needs to be rendered.

### Convenience Decorators

The ``_scaffold`` application, in ``common.py`` defines two special conveniennce decorators:

``
@unauthenticated
def index():
    return dict()
```

and

```
@authenticated
def index():
    return dict()
``

They apply all of the decorators below, use a template with the same name as the function (.html),
and also register a route with the name of action followed the number of arguments of the action
separated by a slash (/). 

@unauthenticated does not require the user to be logged in.
@authenticated required the user to be logged in.

If can be combined with (and precede) other ``@action.uses(...)`` but they should not be combined with
``@action(...)`` because they perform that function automatically.
