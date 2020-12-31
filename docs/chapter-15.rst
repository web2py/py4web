=====================
From web2py to py4web
=====================

This chapter is dedicated to help users for porting old web2py applications to py4web.

Web2py and py4web share any similiaries and some differences. For example they share the same database abstraction layer (PyDAL) which means pydal table definitions and queries are identical between the two frameworks. They also share the same template language with the minor caveat that web2py defaults to `{{...}}` delimiters while py4web defaultes to `[[...]]` delimiters. They also share the same validators, part of PyDAL, and very similar helpers. The py4web ones are a lighet/faster/minimalist re-implementation but they serve the same purpose and support a very similar syntax. They both provide a `Form` object (equivalent to `SQLFORM` in web2py) and a `Grid` object (equivalent to `SQLFORM.grid` in web2py). They both provice a `XML` object that can sanitize HTML and `URL` helper to generate URL. They both can raise `HTTP` to return non-200 OK pages. They both provide an `Auth` object that can generate register/login/change password/lost password/edit profile forms. Both web2py and py4web track and log all errors.

Some of the main differences are the following:

- web2py apps consist of collection of files which are execuited at every HTTP request (in a predetermined order). In py4web apps are regular python modules. Apps are imported automatically by the frameworks.

- In web2py every app has a fixed folder structure. A function is an action if and only if is is defined in a `controllers/*.py` file. py4web is much less constraining. In py4web an app must have an entry point `__init__.py` and a `static` folder. Every other convention such as the location of templates, uploaded files, translation files, sessions, etc. is user specificed.
 
- In web2py the scaffolding app (the blue print for creating new apps) is called "weblcome". In py4web it is called "_scaffold". _scaffold contains a "settings.py" file and a "common.py". The latter provides an example of how to enable Auth and configure all the options for the specific app. _scaffold has also a "model.py" file and a "controller.pY' file but, unlike web2py, those files are not trated in any special manner. They names imply follow a convention (not enforced by the framework) and they are imported by the `__init__.py` file as for any regular python module.

- In web2py every function in "controllers/*.py" is an action. In py4web a function is an action if it has the `@action("...")` decorator. That means that actins can be defined anywhere. The admin interface will help you locate where a particular action is defined.

- In web2py the mapping between URLs and file/function names is automatic but it can be overwritten in routes.py (like in Django). In py4web the mapping is specified in the decorator as in `@action('my_url_path')` (like in Bottle and Flask). Notice that if the path starts with "/" it is assumed to be an absolute path. If not, it is assumed to be reative and prepended by the "/{appname}/" prefix. Also, if the path ends with "/index", the latter postfix is assumed to be optional.

- In web2py the path extention matters and "http://...html" is expected to return HTMl while "http://...json" is expected to return JSON, etc. In py4web there is no such convention. If the action returns a dict() and has a template, the dict() will be rendered by the template, else if will be renedred in JSON. More complex behavior can be applished using decorators.

- In web2py there are many wrappers around each action and, for example, it handles sessions, pluralization, database connections, and more whether the action needs it or not. This makes web2py performances hard to compare with other frameworks. In py4web everything is optional and features must be enabled and configured for each action using the `@action.uses(...)` decorator. The arguments of `@action.uses(...)` are called fixtures in analogy with the fixtures in a house. They add functionality by providing preprocessing and postprocessing to the action. For example `@action.uses(session, T, db, flash)` indicates that the action needs to uses session, internationlization/pluralization (T), the database (db), and carry on state for flash messages upon redirection.

- web2py uses its own request/response objects. py4web uses the request/responseobjects from the underlying bottlepy framework. While this may change in the future we are committed to keep them compatible with Bottle because of their excellent documentation.
Bottle also handles for py4web the interface with the web server, routing, partial requests, if modified since, and file streaming.

- Both web2py and py4web use the same PyDAL therefore tables are defined using the same exact syntax, and so do queries. The main caveat is that in web2py tables are re-defined at every HTTP request, when the entire models are executed. In py4web only the action is executed for every HTTP request, while the code defined outside of actions is only executed at startup. That makes py4web much faster, in particular when there are many tables. The downside of this approach is that the develope should be careful to never overried PyDAL variables inside action or in any what that depends on the content of the request object, else the code is not thread safe. The only variables that can be changed at will are the following field attributes: readable, writable, requires, update, default, requires. All the others are for practical purposes to be considered global and non thread safe.

- Both web2py and pyweb have an Auth object which serve the same purpose. Both objects have the ability to generate forms pretty much in the same manner. The py4web ones is defined to be more modular and extensible and support both Forms and APIs, but it lacks the `auth.requires_*` decorators and group membership/permissions. This does not mean that the feature is not available. In fact py4web is even more powerful and that is why the syntax is different. While the web2py Auth objects tries to do everything, the corresponding py4web object is only in change of establishing the identity of a user, not what the user can do. The latter can be achieved by attaching Tags to users. So group membership is assigned by labeling users with the Tags of the groups they belong to and checking permissions beased on the user tags. Py4web provides a mechanism for assigning and checking tags efficiently to any object, including but not limited to, users.

- Web2py comes with the Rocket web server. py4web at the time of writing defaults to the Tornado web server but this may change.

Examples
========

web2py
~~~~~~

.. code:: python

   # in controllrs/default.py
   def index():
      return "hello world"

py4web
~~~~~~

.. code:: python

   # file imported by __init__.py
   @action('index')
   def index():
       return "hello world"

web2py
~~~~~~

.. code:: python

   request.get_vars.name
   request.post_vars.name
   request.env.name
   raise HTTP(301)
   redirect(url)
   URL('c','f',args=[1,2],vars={})

py4web
~~~~~~

.. code:: python

   request.query.get('name')
   request.forms.get('name') or request.json.get('name')
   request.environ.get('name')
   raise HTTP(301)
   redirect(url)
   URL('c', 'f', 1, 2, vars={})

web2py
~~~~~~

.. code:: python

   def index():
      a = request.get_vars.a
      return locals()

py4web
~~~~~~

.. code:: python

   @action("index")
      def index():
      a = request.query.get('a')
      return locals()

web2py
~~~~~~

.. code:: python

   def index():
      a, b, c = request.args
      b, c = int(b), int(c)
      return locals()

py4web
~~~~~~

.. code:: python

   @action("index/<a>/<b:int>/<c:int>")
   def index(a,b,c):
      return locals()

web2py
~~~~~~

.. code:: python

   def index():
      if request.method == "GET":
         return "GET"
      if request.method == "POST":
         return "POST"
      raise HTTP(400)

py4web
~~~~~~

.. code:: python

   @action("index", method="GET")
   def index():
      return "GET"

   @action("index", method="GET")
   def index()
      return "POST"

web2py
~~~~~~

.. code:: python

   def counter():
      session.counter = (session.counter or 0) + 1
      return str(session.counter)

py4web
~~~~~~

.. code:: python

   def counter():
      session['counter'] = session.get('counter, 0) + 1
      return str(session['counter'])

web2py
~~~~~~

.. code:: html

   {{ extend 'layout.html' }}
   <div>
   {{ for k in range(1): }}
   <span>{{= k }}<span>
   {{ pass }}
   </div>

py4web
~~~~~~

.. code:: html

   [[ extend 'layout.html' ]]
   <div>
   [[ for k in range(1): ]]
   <span>[[= k ]]<span>
   [[ pass ]]
   </div>


web2py
~~~~~~

.. code:: python

   db.define_table('thing', Field('name'))

   def index():
      form = SQLFORM(db.thing)
      form.process()
      if form.accepted:
         flash = 'Done!'
      rows = db(db.thing).select()
      return locals()

py4web
~~~~~~

.. code:: python

   db.define_table('thing', Field('name'))

   @action("index")
   @action.uses(db, flash)
   def index():
      form = Form(db.thing)
      if form.accepted:
         flash.set("Done!", "green")
      rows = db(db.thing).select()
      return locals()

web2py
~~~~~~

.. code:: python

   def index():
      grid = SQLFORM.grid(db.thing, editable=True)
      return locals()


py4web
~~~~~~

.. code:: python

   @action("index")
   @action.uses(db, flash)
   def index():
      grid = Grid(db.thing)
      form.param.editable = True
      return locals()