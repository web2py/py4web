# [py4web](http://py4web.com)

[![Build Status](https://img.shields.io/travis/web2py/py4web/master.svg?style=flat-square&label=Travis-CI)](https://travis-ci.org/web2py/py4web)

## Try me (from pip)

```
python3 -m pip install -U py4web --no-cache-dir --user
py4web-start apps
open http://localhost:8000/todo/index
```

(The apps folder will be created with some apps inside)

## Try me (from source)

```
git clone https://github.com/web2py/py4web.git
cd py4web 
python3 -m pip install -r requirements.txt
./py4web-start.py apps
open http://localhost:8000/todo/index
```

## Try me (install from source)

```
git clone https://github.com/web2py/py4web.git
cd py4web
make assets
make test
make install
py4web-start.py apps
open http://localhost:8000/todo/index
```

Notice "py4web-start" uses the pip installed py4web, "./py4web-start.py" uses the local one. Do not get confused.
Also notice when installing from source the content of py4web/assets is missing and it is created by make assets.

## Tell me more

- this is a work in progress and not stable yet but close to being stable
- python3 only
- uses https://github.com/web2py/pydal (same DAL as web2py)
- uses https://github.com/web2py/yatl (same as web2py but defaults to [[...]] instead of {{...}} delimiters)
- uses the same validators as web2py (they are in pyDAL)
- uses the very similar helpers to web2py (A, DIV, SPAN, etc.)
- uses https://github.com/web2py/pluralize for i18n and pluralization
- request, response, abort are from https://bottlepy.org
- HTTP and redirect are our own objects
- like web2py, it supports static asset management /{appname}/static/_0.0.0/{path}
- implements sessions in cookies (jwt encrypted), db, memcache, redis and custom
- implements a cache.memoize (Ram cache with O(1) access) [Memoize](https://dbader.org/blog/python-memoization)
- supports multiple apps under apps folder (same as web2py)
- unlike web2py does not use a custom importer or eval
- admin has been replaced by a _dashboard (90% done)
- appadmin has been replaced by dbadmin (within dashboard) (90% done)
- auth logic is implemented via a "auth" vue.js custom component (90% done)
- SQLFORM has been replaced by py4web/utils/form.py
- SQLFORM.grid was been replaced by a "mtable" vue.js custom component (90% done)
- there are not enough tests
- it is not as stable as web2py yet
- it is 10-20x faster than web2py

## Components

- pydal + dbapi (done)
- yatl (done)
- pluralize (done)
- auth (WIP, 90%)
- mailer (done)
- session (cookies, db, redis, memcache)
- form (done up to downloads)
- mtable (WIP, 75%)
- dashboard (90% done)
- scaffold (done)
- bus (0%)
- tornado (done)
- gevent (done)
- gunicorn (done)
- bottle (done)

## Storing _dashboard password 

When py4web starts it asks for a _dashboard password and stores its pdkdf2 hash 
in password.txt, in the working folder. It will not ask again unless the file is deleted. 
If the ``--dashboard_mode`` is ``demo`` or ``none`` it will not ask.
If you want to store it somewhere else, you can specify a name with ``--password_file``.

You can create the file yourself with:

```
$ python3 -c "from pydal.validators import CRYPT; open('password.txt','w').write(str(CRYPT()(input('password:'))[0]))"
password: *****
```

## Launch Arguments

```
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
```

Example:


```
py4web-start -a 127.0.0.1:8000 -d demo apps
```

## WSGI

py4web is a WSGI application. To obtain the WSGI app simply do:

```
from py4web.core import wsgi
application = wsgi()
```

The wsgi function takes arguments with the same name as the command line arguments.


## Contributors

- [Cassio Botaro](https://github.com/cassiobotaro)
- [Dan Carroll](https://github.com/dan-carroll)
- [Jim Steil](https://github.com/jpsteil)
- [John M. Wolf](https://github.com/jmwolff3)
- [Massimo Di Pierro](https://github.com/mdipierro)
- [Micah Beasley](https://github.com/MBfromOK)
- [Nico Zanferrari](https://github.com/nicozanf)
- [Pirsch](https://github.com/Pirsch)
- [sugizo](https://github.com/sugizo)
- [valq7711](https://github.com/valq7711)

## Screenshots

![](https://raw.githubusercontent.com/web2py/py4web/master/apps/_documentation/static/screenshots/dashboard_login.png)

![](https://raw.githubusercontent.com/web2py/py4web/master/apps/_documentation/static/screenshots/dashboard_main.png)

![](https://raw.githubusercontent.com/web2py/py4web/master/apps/_documentation/static/screenshots/dashboard_edit.png)

![](https://raw.githubusercontent.com/web2py/py4web/master/apps/_documentation/static/screenshots/dashboard_restapi.png)

![](https://raw.githubusercontent.com/web2py/py4web/master/apps/_documentation/static/screenshots/dashboard_error.png)

![](https://raw.githubusercontent.com/web2py/py4web/master/apps/_documentation/static/screenshots/dashboard_ticket.png)
