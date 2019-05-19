from web3py import action, request, abort, redirect
from .common import db, session, T, cache, auth

# define your actions below, here is an example of /<app_name>/index
@action('index', method='GET')
@action.uses('generic.html', session, db, T, auth)
def index():
    message = T('Hello World from {name}')
    return dict(message=message.format(name=request.app_name))


# (optional) expose translations in case a single page app needs them in JSON
action('translations')(action.uses(T)(lambda: T.local.language))
action('auth/<path:path>', method=['GET','POST'])(action.uses(auth)(auth.action))
