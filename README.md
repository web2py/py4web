# [py4web](http://py4web.com)

[![Build Status](https://img.shields.io/travis/web2py/py4web/master.svg?style=flat-square&label=Travis-CI)](https://travis-ci.org/web2py/py4web)

## What is py4web?
PY4WEB is a web framework for rapid development of efficient database driven web applications. It is an evolution of the popular web2py framework but much faster and slicker. The official documentation is on https://py4web.com/_documentation

## Simple installation

Using ''pip'' is the standard installation procedure for py4web on Windows, MacOS and Linux. Its only prerequisite is Python 3.6+.

```
python3 -m pip install --upgrade py4web --no-cache-dir --user
```

but do **not** type the ''--user'' option with virtualenv or a standard Windows installation which is already per-user.
Also, if ''python3'' does not work, try with the simple ''python'' command instead.


This will install py4web and all its dependencies on the system's path only. After the installation you'll be able to start py4web on any given working folder with

```
py4web setup apps
py4web set_password
py4web run apps
```

## Launch Arguments

```
# py4web run -h
Usage: py4web.py run [OPTIONS] [APPS_FOLDER]

  Run all the applications on apps_folder

Options:
  -Y, --yes                     No prompt, assume yes to questions  [default:
                                False]

  -H, --host TEXT               Host name  [default: 127.0.0.1]
  -P, --port INTEGER            Port number  [default: 8000]
  -p, --password_file TEXT      File for the encrypted password  [default:
                                password.txt]

  -w, --number_workers INTEGER  Number of workers  [default: 0]
  -d, --dashboard_mode TEXT     Dashboard mode: demo, readonly, full
                                (default), none  [default: full]

  --watch [off|sync|lazy]       Watch python changes and reload apps
                                automatically, modes: off (default), sync,
                                lazy
  --ssl_cert PATH               SSL certificate file for HTTPS
  --ssl_key PATH                SSL key file for HTTPS
  -help, -h, --help             Show this message and exit.

```

Example:


```
py4web run -H 127.0.0.1 -P 8000 -d demo apps
```

Note that since the default (as specified above) for the host and port are 127.0.0.1 and 8000 respectively, the above command can be shortened to:

```
py4web run -d demo apps
```

## WSGI

py4web is a WSGI application. To obtain the WSGI app simply do:

```
from py4web.core import wsgi
application = wsgi()
```

The wsgi function takes arguments with the same name as the command line arguments.

## Tell me more

- this is a work in progress and not stable yet but close to being stable
- python3.6+ only
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
