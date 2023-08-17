import os
import site
site.addsitedir(os.path.join(os.path.dirname(__file__), 'lib'))
from py4web.core import Reloader, bottle, Session
os.environ['PY4WEB_DASHBOARD_MODE'] = 'none'
os.environ['PY4WEB_SERVICE_DB_URI'] = 'sqlite:memory'
os.environ['PY4WEB_APPS_FOLDER'] = os.path.join(os.path.dirname(__file__), 'apps')
os.environ['PY4WEB_SERVICE_FOLDER'] = os.path.join(os.path.dirname(__file__), 'apps/.service')
# Session.SECRET = open(os.path.join(os.path.dirname(__file__), 'apps/.service/session.secret'), 'rb').read()
Session.SECRET = "81738cc8-44a3-4bfd-b535-9973492gfufg6374"
Reloader.import_apps()
app = bottle.default_app()
