"""
Documented here: https://youtu.be/Wxjl_vkLAEY
"""
import os
from py4web.core import wsgi

# BEGIN CONFIGURATION
PASSWORD_FILENAME = 'password.txt'
DASHBOARD_MODE = 'full' or 'demo' or 'none'
APPS_FOLDER = 'mysite/apps'
# END CONFIGURATION

password_file = os.path.abspath(os.path.join(os.path.dirname(__file__), PASSWORD_FILENAME))
application = wsgi(password_file=password_file, 
                   dashboard_mode=DASHBOARD_MODE,
                   apps_folder=APPS_FOLDER)
