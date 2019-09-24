import os
from py4web.core import wsgi
password_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'password.txt'))
application = wsgi(password_file=password_file, dashboard_mode='full', apps_folder="mysite/apps")


test763894
