## Installation and Startup

### Supported platforms and prerequisites

PY4WEB runs fine on Windows, MacOS and Linux. Its only prerequisite is Python 3, which must be installed in advance.

### Installing from pip

From the command line

``
python3 -m pip install --upgrade py4web
``:bash

(if python3 does not work, try with the python command instead).
This will install py4web and all its dependencies. Once installed you can start it with:

``
py4web-start.py apps
``:bash

This should produce an output like:

``
██████╗ ██╗   ██╗██╗  ██╗██╗    ██╗███████╗██████╗
██╔══██╗╚██╗ ██╔╝██║  ██║██║    ██║██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ███████║██║ █╗ ██║█████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ╚════██║██║███╗██║██╔══╝  ██╔══██╗
██║        ██║        ██║╚███╔███╔╝███████╗██████╔╝
╚═╝        ╚═╝        ╚═╝ ╚══╝╚══╝ ╚══════╝╚═════╝
Dashboard is at: http://127.0.0.1:8000/_dashboard
[X] loaded _dashboard
[X] loaded _default
Bottle v0.12.16 server starting up (using TornadoServer())...
Listening on http://127.0.0.1:8000/
Hit Ctrl-C to quit.
``

Here ``apps`` is the name of the folder where you keep your apps. If the folder does not exist, it is created. PY4WEB expects to find two apps in this folder: **Dashboard** (_dashboard) and **Default** (_default). If it does not find them, it installs them.

Mind that if you upgrade py4web, it will not automatically upgrade **Dashboard** and **Default**. You have to remove these apps for py4web to re-install them. This is a safety precaution, in case you made changes to those apps.

**Dashboard** is a web based IDE. **Default** is an app that does not nothing other than welcome the user. In general "apps/_default" can be either an app or a symlink to your default app.

Notice that some apps - like **Dashboard** and **Default** - have a special role in py4web and therefore their actual name starts with ``_`` to avoid conflicts with apps created by you.

Once py4web is installed you can access the apps at the following urls:

``
http://localhost:8000
http://localhost:8000/_default
http://localhost:8000/_dashboard
http://localhost:8000/{yourappname}/index
``

Notice that ONLY the **Default** app does require a path prefix. In the example above ``http://localhost:8000`` and ``http://localhost:8000/_default`` are identical to py4web; all other apps require the /{appname}.
NOTE: For all apps the trailing ``/index`` is optional.

### Installing from source

From the command line

``
git clone https://github.com/web2py/py4web.git
cd py4web
python3 -m pip install -r requirements.txt
``:bash

Once installed, you should start with

``
./py4web-start.py apps
``:bash

Notice the ``./`` ; it forces the run of the local folder's py4web and not the installed one.

### Dashboard password

Every time py4web starts, it asks for a one-time password for you to access the dashboard. This is annoying. You can avoid it by storying a password hashed in a file:

``
python3 -c "from pydal.validators import CRYPT; open('password.txt','w').write(str(CRYPT()(input('password:'))[0]))"
``:bash

and then ask py4web to re-use that password:

Pip Install:

``python3 -m py4web-start -p password.txt apps``

Console:
``python3 py4web-start.py -p password.txt apps``:bash
or
``./py4web-start.py -p password.txt apps``:bash

### Command line options

py4web provides multiple command line options which can be listed with ``-h``.

``
usage: py4web-start.py [-h] [--host HOSTNAME] [--port PORT] [--headless] [-n NUMBER_WORKERS]

                       [--ssl_cert_filename SSL_CERT_FILENAME]
                       [--ssl_key_filename SSL_KEY_FILENAME]
                       [--service_db_uri SERVICE_DB_URI] [-d DASHBOARD_MODE]
                       [-p PASSWORD_FILE] [-c]
                       apps_folder

positional arguments:
  apps_folder           path to the applications folder

optional arguments:
  -h, --help            show this help message and exit
  --host HOSTNAME       server address (IP or hostname)
  --port PORT           server port number (e.g., 8000)
  --headless            hide artwork for console based servers
  -n NUMBER_WORKERS, --number_workers NUMBER_WORKERS
                        number of gunicorn workers
  --ssl_cert_filename SSL_CERT_FILENAME
                        ssl certificate file
  --ssl_key_filename SSL_KEY_FILENAME
                        ssl key file
  --service_db_uri SERVICE_DB_URI
                        db uri for logging
  -d DASHBOARD_MODE, --dashboard_mode DASHBOARD_MODE
                        dashboard mode: demo, readonly, full (default), none
  -p PASSWORD_FILE, --password_file PASSWORD_FILE
                        file containing the encrypted (CRYPT) password
  -c, --create          created the missing folder and apps
``

## Deployment on GCloud (aka Google App Engine)

Login into the Gcloud console (https://console.cloud.google.com/) and create a new project. You will obtain a project id that looks like "{project_name}-{number}".


In your local file system make a new working folder and cd into it:

``
mkdir gae
cd gae
``:bash

Copy the example files from py4web (assuming you have the source from github)

``
cp /path/to/py4web/development_tools/gcloud/* ./
``

Copy or symlink your ``apps`` folder into the gae folder, or maybe make a new apps folder containing an empty ``__init__.py`` and symlink the individual apps you want to deploy. You should see the following files/folders:

``
Makefile
apps
  __init__.py
  ... your apps ...
lib
app.yaml
main.py
``

Install the Google SDK, py4web and setup the working folder:

``
make install-gcloud-linux
make setup
gcloud config set {your email}
gcloud config set {project id}
``:bash
(replace {your email} with your google email account and {project id} with the project id obtained from Google).

Now every time you want to deploy your apps, simply do:

``
make deploy
``:bash

You may want to customize the Makefile and app.yaml to suit your needs. You should not need to edit ``main.py``.