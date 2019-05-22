"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html') indicates that the action uses the generuc.html template
@action.uses(session)        indicates that the action uses the session
@action.uses(db)             indicates that the action uses the db
@action.uses(T)              indicates that the action uses the i18n & pluralization
@action.uses(auth)           indicates that the action requires a logged in user (WIP)

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from web3py import action, request, abort, redirect
from . common import db, session, T, cache, auth

# define your actions below, here is an example of /<app_name>/index
@action('index', method='GET')
@action.uses('generic.html', session, db, T, auth)
def index():
    message = T('Hello World from {name}')
    return dict(message=message.format(name=request.app_name))


# (optional) expose translations in case a single page app needs them in JSON
action('translations')(action.uses(T)(lambda: T.local.language))
