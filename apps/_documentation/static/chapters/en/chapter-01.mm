## Installation and Startup

### Installing from pip

From the command line

``
python3 -m pip install --upgrade web3py
``:bash

This will install web3py and all its dependencies. Once installed you can start it with:

``
web3py-start apps
``:bash

This should produce an output like:

``
 _______  ____________  ____  ______  __
|  ____/ / / ____/ __ |/___ \/ __ \ \/ /
| |     / / /_  / /_/ /___/ / /_/ /\  /
| | /| / / __/ / __  //__  / ____/ / /
| |/ |/ / /___/ /_/ /___/ / / ____/ /
|___/|_/_____/_____/_____/_/ /_____/

Dashboard is at: http://127.0.0.1:8000/_dashboard
[X] loaded _dashboard     
[X] loaded _default     
Bottle v0.12.16 server starting up (using TornadoServer())...
Listening on http://127.0.0.1:8000/
Hit Ctrl-C to quit.
``

Here ``apps`` is the name of the folder where you keep your apps. If the folder does not exist it is created. Web3py expects to find two apps in this folder: Dashboard (_dashboard) and Default (_default). If it does not find them, it installs them.

Mind that if you upgrade web3py, it will not automatically upgrade Dashboard and Default. You have to remove these apps for web3py to re-install them. This is a safety precaution, in case you made changes to those apps.

Deashboard is a web based IDE. Default is an app does not nothing other then welcome the user. In general "apps/_default" can be an app or a symlink to your default app.

Notice that some apps like Dashboard and Default have a special role in web3py and therefore their actual name starts with ``_`` to avoid conflict with apps created by the you.

Once web3py is installed you can access the apps at the following urls:

``
http://localhost:8000
http://localhost:8000/_default 
http://localhost:8000/_dashboard
http://localhost:8000/{yourappname}/index
``

Notice that ONLY the default app does not need a path prefix ``/_default`` is optional.
Also notice that a trailing ``/index`` is also optional.

### installing from source

From the command line

``
git clone https://github.com/web2py/web3py.git
cd web3py
python3 -m pip install -r requirements.txt
``:bash

Once installed you should start with

``
./web3py-start apps
``:bash

Notice the ``./`` makes sure you are running the local web3py and not the installed one.

### Dashboard password

Every time web3py starts it asks for a one-time password for you to access the dashboard. This is annoying. You can avoid by storying a password hashed in a file:

``
python3 -c "from pydal.validators import CRYPT; open('password.txt','w').write(str(CRYPT()(input('password:'))[0]))"
``:bash

and then ask web3py to re-use that password:

``
web3py-start -p password.txt apps
``:bash

### Command line options

web3py provides multiple command line options which can be listed with ``-h``.

``
usage: web3py-start [-h] [-a ADDRESS] [-n NUMBER_WORKERS]
                    [--ssl_cert_filename SSL_CERT_FILENAME]
                    [--ssl_key_filename SSL_KEY_FILENAME]
                    [--service_db_uri SERVICE_DB_URI] [-d DASHBOARD_MODE]
                    [-p PASSWORD_FILE] [-c]
                    apps_folder

positional arguments:
  apps_folder           path to the applications folder

optional arguments:
  -h, --help            show this help message and exit
  -a ADDRESS, --address ADDRESS
                        serving address
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
