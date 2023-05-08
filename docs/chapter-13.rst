================================
Authentication and authorization
================================

Strong authentication and authorization methods are
vital for a modern, multiuser web application.
While they are often used interchangeably, authentication and authorization
are separate processes: 

- Authentication confirms that users are who they say they are
- Authorization gives those users permission to access a resource


Authentication using Auth
-------------------------

py4web comes with a an object ``Auth`` and a system of plugins for user
authentication. It has the same name as the
corresponding web2py one and serves the same purpose but the API and
internal design is very different.

The _scaffold application provides a guideline for its standard usage. By
default it uses a local SQLite database and allows creating new users,
login and logout. Notice that if you don't configure it, you have to manually
approve new users (by visiting the link logged on the console or
by directly editing the database).


To use the Auth object, first of all you need to import it, instantiate it, configure
it, and enable it.

.. code:: python

   from py4web.utils.auth import Auth
   auth = Auth(session, db)
   # (configure here)
   auth.enable()

The import step is obvious. The second step does not perform any
operation other than telling the Auth object which session object to use
and which database to use. Auth data is stored in ``session['user']``
and, if a user is logged in, the user id is stored in
session[‘user’][‘id’]. The db object is used to store persistent info
about the user in a table ``auth_user`` which is created if missing.
The ``auth_user`` table has the following fields:

-  username
-  email
-  password
-  first_name
-  last_name
-  sso_id (used for single sign on, see later)
-  action_token (used to verify email, block users, and other tasks,
   also see later).

The ``auth.enable()`` step creates and exposes the following RESTful
APIs:

-  {appname}/auth/api/register (POST)
-  {appname}/auth/api/login (POST)
-  {appname}/auth/api/request_reset_password (POST)
-  {appname}/auth/api/reset_password (POST)
-  {appname}/auth/api/verify_email (GET, POST)
-  {appname}/auth/api/logout (GET, POST) (+)
-  {appname}/auth/api/profile (GET, POST) (+)
-  {appname}/auth/api/change_password (POST) (+)
-  {appname}/auth/api/change_email (POST) (+)

Those marked with a (+) require a logged in user.

Auth UI
~~~~~~~

You can create your own web UI to login users using the above APIs but
py4web provides one as an example, implemented in the following files:

-  \_scaffold/templates/auth.html
-  \_scaffold/templates/layout.html


The key section is in ``layout.html`` where (using the no.css framework) the menu actions are defined:

.. code-block:: html
   :linenos:

   <ul>
      [[if globals().get('user'):]]
      <li>
      <a class="navbar-link is-primary">
         [[=globals().get('user',{}).get('email')]]
      </a>
      <ul>
         <li><a href="[[=URL('auth/profile')]]">Edit Profile</a></li>
         [[if 'change_password' in globals().get('actions',{}).get('allowed_actions',{}):]]
            <li><a href="[[=URL('auth/change_password')]]">Change Password</a></li>
         [[pass]]
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


The menu is dynamic: on line 2 there is a check if the user is already defined
(i.e. if the user has already logged on). In this case the email is shown in the
top menu, plus the menu options ``Edit Profile``, ``Change Password`` (optional) and
``Logout``.
Instead, if the user is not already logged on, from line 15 there are
only the corresponding menu options allowed: ``Sign up`` and ``Log in``.

Every menu option then redirects the user to the corresponding standard URL,
which in turn activates the Auth action.


Using Auth inside actions
~~~~~~~~~~~~~~~~~~~~~~~~~

There two ways to use the Auth object in an action.

The first one does not force a login.  With ``@action.uses(auth)``
we tell py4web that this action should have information about the user, 
trying to parse the session for a user session.

.. code:: python

   @action('index')
   @action.uses(auth)
   def index():
       user = auth.get_user()
       return 'hello {first_name}'.format(**user) if user else 'not logged in'

The second one forces the login if needed:

.. code:: python

   @action('index')
   @action.uses(auth.user)
   def index():
       user = auth.get_user()
       return 'hello {first_name}'.format(**user)'

Here ``@action.uses(auth.user)`` tells py4web that this action requires
a logged in user and should redirect to login if no user is logged in.

Two Factor Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

Two factor authentication (or Two-step verification) is a way of improving authentication security. When activated an extra step is added in the login process. In the first step, users are shown the standard username/password form. If they successfully pass this challenge by submitting the correct username and password, and two factor authentication is enabled for the user, the server will present a second form before logging them in.

There are a few Auth settings available to control how two factor authentication works.

The follow can be specified on Auth instantiation:

- two_factor_required
- two_factor_send

two_factor_required
^^^^^^^^^^^^^^^^^^^

When you pass a method name to the two_factor_filter parameter you are telling py4web to call that method to determine whether or not this login should be use or bypass two factor authentication.  If your method returns True, then this login requires two factor.  If it returns False, two factor authentication is bypassed for this login.

Sample two_factor_filter method

This example shows how to allow users that are on a specific network.

.. code:: python

   def user_outside_network(user, request):
       import ipaddress

       networks = ["10.10.0.0/22"]

       ip_list = []
       for range in networks:
           ip_list.extend(ipaddress.IPv4Network(range))

       if ipaddress.IPv4Address(request.remote_addr) in ip_list:
           #  if the client address is in the network address list, then do NOT require MFA
           return False

       return True

two_factor_send
^^^^^^^^^^^^^^^

When two factor authentication is active, py4web generates a 6 digit code (using random.randint) and sends it to you. How this code is sent, is up to you. The two_factor_send argument to the Auth class allows you to specify the method that sends the two factor code to the user.

This example shows how to send an email with the two factor code:

.. code:: python

   def send_two_factor_email(user, code):
       try:
           auth.sender.send(
               to=[user.email],
               subject=f"Two factor login verification code",
               body=f"You're verification code is {code}",
               sender="from_address@youremail.com",
           )
       except Exception as e:
           print(e)
       return code

Notice that this method takes to arguments: the current user, and the code to be sent.
Also notice this method can override the code and return a new one.

.. code:: python

   auth.param.two_factor_required = user_outside_network
   auth.param.two_factor_send = send_two_factor_email

two_factor_tries
^^^^^^^^^^^^^^^^

By default, the user has 3 attempts to pass two factor authentication. You can override this after using:

.. code:: python

   auth.param.two_factor_tries = 5

Once this is all setup, the flow for two factor authentication is:

- present the login page
- upon successful login and user passes two_factor_required
   - redirect to py4web auth/two_factor endpoint
   - generate 6 digit verification code
   - call two_factor_send to send the verification code to the user
   - display verification page where user can enter their code
   - upon successful verification, take user to _next_url that was passed to the login page



Auth Plugins
~~~~~~~~~~~~

Plugins are defined in “py4web/utils/auth_plugins” and they have a
hierarchical structure. Some are exclusive and some are not. For example,
default, LDAP, PAM, and SAML are exclusive (the developer has to pick
one). Default, Google, Facebook, and Twitter OAuth are not exclusive
(the developer can pick them all and the user gets to choose using the
UI).

The ``<auth/>`` components will automatically adapt to display login
forms as required by the installed plugins.

In the _scaffold/settings.py and _scaffold/common.py files you can see
the default settings for the supported plugins. 

PAM
^^^

Configuring PAM is the easiest:

.. code:: python

   from py4web.utils.auth_plugins.pam_plugin import PamPlugin
   auth.register_plugin(PamPlugin())

This one like all plugins must be imported and registered.
The constructor of this plugins does not require any
arguments (where other plugins do).

The ``auth.register_plugin(...)`` **must** come before the
``auth.enable()`` since it makes no sense to expose APIs before desired
plugins are mounted.

.. note::

   by design PAM authentication using local users works fine only if py4web is run by root.
   Otherwise you can only authenticate the specific user that runs the py4web process.


LDAP
^^^^

This is a common authentication method, especially using Microsoft Active Directory in enterprises.

.. code:: python

   from py4web.utils.auth_plugins.ldap_plugin import LDAPPlugin
   LDAP_SETTING = {
       'mode': 'ad',
       'server': 'my.domain.controller',
       'base_dn': 'cn=Users,dc=domain,dc=com'
   }
   auth.register_plugin(LDAPPlugin(**LDAP_SETTINGS))

.. warning::
   
   it needs the python-ldap module. On Ubuntu, you should also install some developer's libraries
   in advance with ``sudo apt-get install libldap2-dev libsasl2-dev``.


OAuth2 with Google
^^^^^^^^^^^^^^^^^^

.. code:: python

   from py4web.utils.auth_plugins.oauth2google import OAuth2Google # TESTED
   auth.register_plugin(OAuth2Google(
       client_id=CLIENT_ID,
       client_secret=CLIENT_SECRET,
       callback_url='auth/plugin/oauth2google/callback'))

The client id and client secret must be provided by Google.

OAuth2 with Facebook
^^^^^^^^^^^^^^^^^^^^

.. code:: python

   from py4web.utils.auth_plugins.oauth2facebook import OAuth2Facebook # UNTESTED
   auth.register_plugin(OAuth2Facebook(
       client_id=CLIENT_ID,
       client_secret=CLIENT_SECRET,
       callback_url='auth/plugin/oauth2google/callback'))

The client id and client secret must be provided by Facebook.

OAuth2 with Discord
^^^^^^^^^^^^^^^^^^^

.. code:: python

    from py4web.utils.auth_plugins.oauth2discord import OAuth2Discord
    auth.register_plugin(OAuth2Discord(
        client_id=DISCORD_CLIENT_ID,
        client_secret=DISCORD_CLIENT_SECRET,
        callback_url="auth/plugin/oauth2discord/callback"))

To obtain a Discord client ID and secret, create an application at https://discord.com/developers/applications.
You will also have to register your OAuth2 redirect URI in your created application, in the form of
``http(s)://<your host>/<your app name>/auth/plugin/oauth2discord/callback``

.. note::
    As Discord users have no concept of first/last name, the user in the auth table will contain the
    Discord username as the first name and discriminator as the last name.


Authorization using Tags
------------------------

As already mentioned, authorization is the process of verifying what specific
applications, files, and data a user has access to. This is accomplished
in py4web using ``Tags``.


Tags and Permissions
~~~~~~~~~~~~~~~~~~~~

Py4web provides a general purpose tagging
mechanism that allows the developer to tag any record of any table,
check for the existence of tags, as well as checking for records
containing a tag. Group membership can be thought of a type of tag that
we apply to users. Permissions can also be tags. Developers are free to
create their own logic on top of the tagging system.

.. note::

   Py4web does not have the concept of groups as web2py does. Experience
   showed that while that mechanism is powerful it suffers from two
   problems: it is overkill for most apps, and it is not flexible enough
   for very complex apps. 

To use the tagging system you first need to import the Tags module
from ``pydal.tools``. Then create a Tags object to tag a table:

.. code:: python

   from pydal.tools.tags import Tags
   groups = Tags(db.auth_user)

If you look at the database level, a new table will be created with a
name equals to tagged_db + '_tag' + tagged_name, in this case
``auth_user_tag_groups``:

.. image:: images/tags_db.png

Then you can add one or more tags to records of the table as well as
remove existing tags:

.. code:: python

   groups.add(user.id, 'manager')
   groups.add(user.id, ['dancer', 'teacher'])
   groups.remove(user.id, 'dancer')

On the ``auth_user_tagged_groups`` this will produce two records
with different groups assigned to the same user.id (the "Record ID" field):

.. image:: images/tags2.png

Slashes at the
beginning or the end of a tag are optional. All other chars are allowed
on equal footing.

A common use case is **group based access control**. Here the developer
first checks if a user is a member of the ``'manager'`` group, if the
user is not a manager (or no one is logged in) py4web redirects to the
``'not authorized url'``. Else the user is in the correct group and then
py4web displays ‘hello manager’:

.. code:: python

   @action('index')
   @action.uses(auth.user)
   def index():
       if not 'manager' in groups.get(auth.get_user()['id']):
           redirect(URL('not_authorized'))
       return 'hello manager'

Here the developer queries the db for all records having the desired
tag(s):

.. code:: python

   @action('find_by_tag/{group_name}')
   @action.uses(db)
   def find(group_name):
       users = db(groups.find([group_name])).select(orderby=db.auth_user.first_name | db.auth_user.last_name)
       return {'users': users}

We leave it to you as an exercise to create a fixture ``has_membership``
to enable the following syntax:

.. code:: python

   @action('index')
   @action.uses(has_membership(groups, 'teacher'))
   def index():
       return 'hello teacher'

**Important:** ``Tags`` are automatically hierarchical. For example, if
a user has a group tag ‘teacher/high-school/physics’, then all the
following searches will return the user:

-  ``groups.find('teacher/high-school/physics')``
-  ``groups.find('teacher/high-school')``
-  ``groups.find('teacher')``

This means that slashes have a special meaning for tags. 

Multiple Tags objects
~~~~~~~~~~~~~~~~~~~~~

.. note::
   One table can have multiple associated ``Tags`` objects. The
   name 'groups' here is completely arbitrary but has a specific semantic
   meaning. Different ``Tags`` objects are independent to each other. The
   limit to their use is your creativity.

For example you could create a table ``auth_group``:

.. code:: python

   db.define_table('auth_group', Field('name'), Field('description'))

and two Tags attached to it:

.. code:: python

   groups = Tags(db.auth_user)
   permissions = Tags(db.auth_groups)

Then create a 'zapper' record in ``auth_group``, give it a permission, and make a user member
of the group:

.. code:: python

   zap_id = db.auth_group.insert(name='zapper', description='can zap database')
   permissions.add(zap_id, 'zap database')
   groups.add(user.id, 'zapper')

And you can check for a user permission via an explicit join:

.. code:: python

   @action('zap')
   @action.uses(auth.user)
   def zap():
       user = auth.get_user()
       permission = 'zap database'
       if db(permissions.find(permission))(
             db.auth_group.name.belongs(groups.get(user['id']))
             ).count():
           # zap db
           return 'database zapped'
       else:
           return 'you do not belong to any group with permission to zap db'

Notice here ``permissions.find(permission)`` generates a query for all
groups with the permission and we further filter those groups for those
the current user is member of. We count them and if we find any, then
the user has the permission.
