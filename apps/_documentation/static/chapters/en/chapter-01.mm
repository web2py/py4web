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
py4web setup apps
py4web set-password
py4web run apps
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

**Dashboard** is a web based IDE. 

**Default** is an app that does not nothing other than welcome the user.

Notice that some apps - like **Dashboard** and **Default** - have a special role in py4web and therefore their actual name starts with ``_`` to avoid conflicts with apps created by you.

Once py4web is installed you can access the apps at the following urls:

``
http://localhost:8000
http://localhost:8000/_dashboard
http://localhost:8000/{yourappname}/index
``

Notice that ONLY the **Default** app is special because if does not rqeuire the "{appname}/" prefix in the path, like all the other apps do.
In general you you may want to symlink ``apps/_default`` to your default app.

For all apps the trailing ``/index`` is optional.

### Installing from source

From the command line

``
git clone https://github.com/web2py/py4web.git
cd py4web
python3 -m pip install -r requirements.txt
``:bash

Once installed, you should start with

``
./py4web.py setup apps
./py4web.py set-password
./py4web.py run apps
``:bash

Notice the ``./`` ; it forces the run of the local folder's py4web and not the installed one.

### Upgrading

If you installed py4web from source you can upgrade it with
``
python3 -m pip install -U py4web
``:bash
this will install the libraries but not the apps. To upgrade the built-in apps, delete them them run:
``
py4web setup apps
``:bash

### Dashboard password

Every time py4web starts, it asks for a one-time password for you to access the dashboard. This is annoying. You can avoid it by storying a password hashed in a file:

``
py4web set-password
``:bash
(pydal is installed by py4web as a dependency)
and then ask py4web to re-use that password:

Pip Install:

``
py4webt run -p password.txt apps
``:bash

### Command line options

py4web provides multiple command line options which can be listed with ``--help``.

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

## Deployment on PythonAnywhere.com

Watch the video: https://youtu.be/Wxjl_vkLAEY
The bottle_app.py script is in ``py4web/deployment_tools/pythonanywhere.com/bottle_app.py``
