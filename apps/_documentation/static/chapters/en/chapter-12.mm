## Grid

**Warning: the API described in this chapter is new and subject to changes. Make sure you keep your code up to date**

py4web comes with a Grid object providing simple grid and CRUD capabilities.
#### Key Features
- Click column heads for sorting - click again for DESC
- Pagination control
- Filter Form - you supply and control filtering (remember filters between pages)
- Action Buttons - with or without text
- Full CRUD with Delete Confirmation
- Pre and Post Action (add your own buttons to each row)
- Grid dates in local format using moment.js
- Checkboxes in grid for boolean fields

#### Simple Example
In this simple example we will make a grid over the superhero table.  Since there is a foreign key defined we will
take advantage of the DAL `left` keyword to bring in the related values and allow sorting on them.

controllers.py
``
from py4web.utils.grid import Grid, get_storage_key, get_storage_value, GridDefaults, GridClassStyle
from py4web.utils.param import Param
from .settings import SESSION_SECRET_KEY

@action('companies', method=['POST', 'GET'])
@action('companies/<action>/<tablename>/<record_id>', method=['POST', 'GET'])
@action.uses(session, db, auth, 'grid.html')
def companies(**kwargs):
    #  NOTE - this would normally go in common.py and then imported to your controller
    GRID_COMMON = GridDefaults(db=db,
                               secret=SESSION_SECRET_KEY,
                               rows_per_page=5)

    storage_key = get_storage_key()
    search_filter = get_storage_value(storage_key, 'search_filter', common_settings=GRID_COMMON)

    search_form = Form([Field('search_filter',
                              length=50,
                              default=search_filter,
                              _placeholder='...search text...',
                              _title='Enter search text and click on %s' % GRID_COMMON.param.search_button_text)],
                       keep_values=True, formstyle=FormStyleGrid)

    if search_form.accepted:
        search_filter = search_form.vars['search_filter']

    queries = [(db.company.id > 0)]
    if search_filter:
        queries.append(db.company.name.contains(search_filter))

    orderby = [db.company.name]

    grid = Grid(GRID_COMMON,
                queries,
                search_form=search_form,
                storage_values=dict(search_filter=search_filter),
                orderby=orderby,
                create=True,
                details=True,
                editable=True,
                deletable=True,
                storage_key=storage_key)

    return dict(grid=grid)
``:python

grid.html
``
[[extend 'layout.html']]
<div class="container" style="padding-top: 1em;">
    [[if 'action' in request.url_args and request.url_args['action'] in ['details', 'edit']:]]
        [[form = grid.render()]]
        [[=form]]
    [[else:]]
        [[=grid.render()]]
    [[pass]]
</div>
``

#### Signature

``
class Grid:
    def __init__(self,
                 common_settings,
                 queries,
                 search_form=None,
                 storage_values=None,
                 fields=None,
                 show_id=False,
                 orderby=None,
                 left=None,
                 headings=None,
                 create=False,
                 details=False,
                 editable=False,
                 deletable=False,
                 requires=None,
                 storage_key=None,
                 pre_action_buttons=None,
                 post_action_buttons=None):
``:python

- common_settings: Params object with common settings for all grids within the application
- queries: list of queries used to filter the data
- search_form: py4web FORM to be included as the search form
- storage_values: values to save between requests
- fields: list of fields to display on the list page, if blank, glean tablename from first query and use all fields of that table
- show_id: show the record id field on list page - default = False
- orderby: pydal orderby field or list of fields
- left: if joining other tables, specify the pydal left expression here
- headings: list of headings to be used for list page - if not provided use the field label
- create: URL to redirect to for creating records - set to False to not display the button
- editable: URL to redirect to for editing records - set to False to not display the button
- deletable: URL to redirect to for deleting records - set to False to not display the button
- requires: dict of fields and their 'requires' parm for building edit pages - dict key should be tablename.fieldname
- storage_key: id of the cookie containing saved values
- pre_action_buttons: list of action_button instances to include before the standard action buttons
- post_action_buttons: list of action_button instances to include after the standard action buttons

#### Grid Defaults

``
    def __init__(self,
                 db,
                 secret,
                 token_longevity=3600,
                 rows_per_page=15,
                 include_action_button_text=True,
                 search_button_text="Filter",
                 formstyle=FormStyleDefault,
                 grid_class_style=GridClassStyle):
``:python

The GridDefaults class allows you to set app-wide grid defaults that you can use when instantiating grids.0

- db: PyDAL db instance to use within your grid
- secret: secrent encryption key used to encrypt storage values
- token_longevity: number of seconds to remember you storage values for this grid instance
- rows_per_page: number of rows to display on each grid page
- included_action_button_text: boolean telling the grid whether or not you want text on action buttons within your grid
- search_button_text: text to appear on the submit button on your search form
- formstyle: py4web Form formstyle used to style your form when automatically building CRUD forms
- grid_class_style: GridClassStyle object used to override defaults for styling your rendered grid.  Allows you to specify classes or styles to apply at certain points in the grid.

#### Searching / Filtering

The grid will render a form that you provide in the search_form parameter on the Grid __init__ method.  You are responsible for taking the values from the search for and building the queries to pass to the Grid.forms

The grid has helper functions that allow you save/retrieve filter values between page displays using a cookie generate
#### CRUD

#### Templates

#### Customizing Style

#### Custom Action Buttons

#### Reference Fields

#### Examples

To use it, first set your GridDefaults in common.py and then instantiate in your controller function, passing in the defaults from common.py.

``
from py4web.utils.auth import Auth
auth = Auth(session, db)
# (configure here)
auth.enable()
``:python

The import step is obvious. The second step does not perform any operation other than telling the Auth object which session object to use and which database to use. Auth data is stored in ``session['user']`` and, if a user is logged in, the user id is stored in session['user']['id']. The db object is used to store persistent info about the user in a table ``auth_user`` with the following fields:

- username
- email
- password
- first_name
- last_name
- sso_id (used for single sign on, see later)
- action_token (used to verify email, block users, and other tasks, also see later).

If the ``auth_user`` table does not exist it is created.

The configuration step is optional and discussed later.

The ``auth.enable()`` step creates and exposes the following RESTful APIs:

- {appname}/auth/api/register (POST)
- {appname}/auth/api/login (POST)
- {appname}/auth/api/request_reset_password (POST)
- {appname}/auth/api/reset_password (POST)
- {appname}/auth/api/verify_email (GET, POST)
- {appname}/auth/api/logout (GET, POST) (+)
- {appname}/auth/api/profile (GET, POST) (+)
- {appname}/auth/api/change_password (POST) (+)
- {appname}/auth/api/change_email (POST) (+)

Those marked with a (+) require a logged in user.

## Auth UI

You can create your own web UI to login users using the above APIs but py4web provides one as an example, implemented in the following files:

- _scaffold/templates/auth.html
- _scaffold/static/components/auth.js
- _scaffold/static/components/auth.html

The component files (js/html) define a Vue component ``<auth/>`` which is used in the template file auth.html as follows:

``
[[extend "layout.html"]]
<div id="vue">
  <div class="columns">
    <div class="column is-half is-offset-one-quarter" style="border : 1px solid #e1e1e1; border-radius: 10px">
      <auth plugins="local,oauth2google,oauth2facebook"></auth>
    </div>
  </div>
</div>
[[block page_scripts]]
<script src="js/utils.js"></script>
<script src="components/auth.js"></script>
<script>utils.app().start();</script>
[[end]]
``:html

You can pretty much use this file un-modified. It extends the current layout and embeds the ``<auth/>`` component into the page. It then uses ``utils.app().start();`` (py4web magic) to render the content of ``<div id="vue">...</div>`` using Vue.js. ``components/auth.js`` also automatically loads ``components/auth.html`` into the component placeholder (more py4web magic). The component is responsible for rendering the login/register/etc forms using reactive html and GETing/POSTing data to the Auth service APIs.

If you need to change the style of the component you can edit "components/auth.html" to suit your needs. It is mostly HTML with some special Vue ``v-*`` tags.

## Using Auth

There two ways to use the Auth object in an action:

``
@action('index')
@action.uses(auth)
def index():
    user = auth.get_user()
    return 'hello {first_name}'.format(**user) if user else 'not logged in'
``:python

With ``@action.uses(auth)`` we tell py4web that this action needs to have information about the user, then try to parse the session for a user session.

``
@action('index')
@action.uses(auth.user)
def index():
    user = auth.get_user()
    return 'hello {first_name}'.format(**user)'
``:python

Here ``@action.uses(auth.user)`` tells py4web that this action requires a logged in user and should redirect to login if no user is logged in.

## Auth Plugins

Plugins are defined in "py4web/utils/auth_plugins" and they have a hierachical structure. Some are exclusive and some are not. For example, default, LDAP, PAM, and SAML are exclusive (the developer has to pick one). Default, Google, Facebook, and Twitter OAuth are not exclusive (the developer can pick them all and the user gets to choose using the UI).

The ``<auth/>`` components will automatically adapt to display login forms as required by the installed plugins.

**At this time we cannot guarantee that the following plugins work well. They have been ported from web2py where they do work but testing is still needed**

### PAM

Configuring PAM is the easiest:

``
from py4web.utils.auth_plugins.pam_plugin import PamPlugin
auth.register_plugin(PamPlugin())
``:python

This one like all plugins must be imported and registered. Once registered the UI (components/auth) and the RESTful APIs know how to handle it. The constructor of this plugins does not require any arguments (where other plugins do).

The ``auth.register_plugin(...)`` **must** come before the ``auth.enable()`` since it makes no sense to expose APIs before desired plugins are mounted.

### LDAP

``
from py4web.utils.auth_plugins.ldap_plugin import LDAPPlugin
LDAP_SETTING = {
    'mode': 'ad',
    'server': 'my.domain.controller',
    'base_dn': 'ou=Users,dc=domain,dc=com'
}
auth.register_plugin(LDAPPlugin(**LDAP_SETTINGS))
``:python

### OAuth2 with Google (tested OK)

``
from py4web.utils.auth_plugins.oauth2google import OAuth2Google # TESTED
auth.register_plugin(OAuth2Google(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    callback_url='auth/plugin/oauth2google/callback'))
``:python

The client id and client secret must be provided by Google.

### OAuth2 with Facebook (tested OK)

``
from py4web.utils.auth_plugins.oauth2facebook import OAuth2Facebook # UNTESTED
auth.register_plugin(OAuth2Facebook(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    callback_url='auth/plugin/oauth2google/callback'))
``:python

The client id and client secret must be provided by Facebook.

[[tags_and_permissions]]
### Tags and Permissions

Py4web does not have the concept of groups as web2py does. Experience showed that while that mechanism is powerful it suffers from two problems: it is overkill for most apps, and it is not flexible enough for very complex apps. Py4web provides a general purpose tagging mechanism that allows the developer to tag any record of any table, check for the existence of tags, as well as checking for records containing a tag. Group membership can be thought of a type of tag that we apply to users. Permissions can also be tags. Developer are free to create their own logic on top of the tagging system.

To use the tagging system you need to create an object to tag a table:
``
groups = Tags(db.auth_user)
``:python

Then you can add one or more tags to records of the table as well as remove existing tags:

``
groups.add(user.id, 'manager')
groups.add(user.id, ['dancer', 'teacher'])
groups.remove(user.id, 'dancer')
``:python

Here the use case is group based access control where the developer first checks if a user is a member of the ``'manager'`` group, if the user is not a manager (or no one is logged in) py4web redirects to the ``'not authorized url'``. If the user is in the correct group then py4web displays 'hello manager':

``
@action('index')
@action.uses(auth.user)
def index():
    if not 'manager' in groups.get(auth.get_user()['id']):
        redirect(URL('not_authorized'))
    return 'hello manager'
``:python

Here the developer queries the db for all records having the desired tag(s):

``
@action('find_by_tag/{group_name}')
@action.uses(db)
def find(group_name):
    users = db(groups.find([group_name])).select(orderby=db.auth_user.first_name|db.auth_user.last_name)
    return {'users': users}
``:python

We leave it to you as an exercise to create a fixture ``has_membership`` to enable the following syntax:

``
@action('index')
@action.uses(has_membership(groups, 'teacher'))
def index():
    return 'hello teacher'
``:python

**Important:** ``Tags`` are automatically hierarchical. For example, if a user has a group tag 'teacher/high-school/physics', then all the following seaches will return the user:

- `` groups.find('teacher/high-school/physics')``
- `` groups.find('teacher/high-school')``
- `` groups.find('teacher')``

This means that slashes have a special meaning for tags. Slahes at the beginning or the end of a tag are optional. All other chars are allowed on equal footing.

Notice that one table can have multiple associated ``Tags`` objects. The name groups here is completely arbitary but has a specific semantic meaning. Different ``Tags`` objects are orthogonal to each other. The limit to their use is your creativity.

For example you could create a table groups:

``
db.define_table('auth_group', Field('name'), Field('description'))
``:python

and to Tags:

``
groups = Tags(db.auth_user)
permissions = Tags(db.auth_groups)
``:python

Then create a zapper group, give it a permission, and make a user member of the group:

``
zap_id = db.auth_group.insert(name='zapper', description='can zap database')
permissions.add(zap_id, 'zap database')
groups.add(user.id, 'zapper')
``:python

And you can check for a user permission via an explicit join:

``
@action('zap')
@action.uses(auth.user)
def zap():
    user = auth.get_user()
    permission = 'zap database'
    if db(permissions.find(permission))(db.auth_group.name.belongs(groups.get(user['id']))).count():
        # zap db
        return 'database zapped'
    else:
        return 'you do not belong to any group with permission to zap db'
``:python

Notice here ``permissions.find(permission)`` generates a query for all groups with the permission and we further filter those groups for those the current user is member of. We count them and if we find any, then the user has the permission.