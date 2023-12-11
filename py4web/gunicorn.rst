====================
gunicorn and py4web
====================


The gunicorn server starts in the usual way for the py4web

::

   $./py4web.py run apps -s gunicorn --watch=off
   $
   $./py4web.py run apps -s gunicornGevent --watch=off


gunicornGevent === gunicorn + monkey.patch_all() 

It is possible to use several methods to configure gunicorn options with py4web

Let's show examples (go to py4web root dir)


* set gunicorn options via py4web.py cmd-keys

 use: -H, -P, -w, -L, --ssl_cert, --ssl_key, -Q

 ./py4web.py run apps -s gunicorn --watch=off -w 4 -H 192.168.1.161 -P 9000 -L 20 --ssl_cert=cert.pem --ssl_key=key.pem

 with -L 10 we can see gunicorn options in server-py4web.log

 this is enough for regular applications (you don't have to read further)

* set gunicorn options via bash env variables

  ::

   $export GUNICORN_worker_class=sync
   $ ./py4web.py  run apps  -s gunicorn  -L 20 -w 4 --watch=off
   $
   $export GUNICORN_worker_class=gthread
   $ ./py4web.py  run apps  -s gunicorn  -L 20 -w 4 --watch=off
   $
   $export GUNICORN_worker_class=gevent
   $ ./py4web.py  run apps  -s gunicornGevent  -L 20 -w 4 --watch=off
   $
   $export GUNICORN_worker_class=eventlet
   $ ./py4web.py  run apps  -s gunicornGevent  -L 20 -w 4 --watch=off




* set gunicorn options via config file gunicorn.saenv 

  ::

   # gunicorn.saenv: example file
   #
   # its key=value file
   # export GUNICORN_ will be removed
   #
   # boolean
   # print_config=False
   #
   # str
   export GUNICORN_raw_env=VARIABLE_HERE=VARIABLE_VALUE_HERE, v2=x2,
   # python dict
   export GUNICORN_secure_scheme_headers={'x':'x1', 'y':'y1',}
   # None
   certfile=None

   export GUNICORN_worker_tmp_dir=/dev/shm
   export GUNICORN_max_requests=1200
   worker_class=gthread
   threads=2

   # gunicornGevent
   #worker_class=gevent
   #worker_class=eventlet

   # for use python-config-file
   # use_python_config=myguni.conf.py
   # or short 
   # usepy=myguni.conf.py

   # for use python-config-mod_name
   # use_python_config=python:mod_name
   # or short 
   # usepy=python:mod_name


* set gunicorn options via python file myguni.conf.py

 ::

   set the env variable use_python_config=myguni.conf.py

 .. code:: bash

   $ # via env
   $export GUNCORN_use_python_config=myguni.conf.py
   $ 
   $ # via gunicorn.saenv 
   $echo use_python_config=myguni.conf.py >> gunicorn.saenv

 ::

   write file myguni.conf.py

 .. code:: python

   # myguni.conf.py : example gunicorn configuration file
   # https://docs.gunicorn.org/en/stable/settings.html

   import multiprocessing

   max_requests = 1000
   max_requests_jitter = 50

   log_file = "-"

   workers = multiprocessing.cpu_count() * 2 + 1

 ::

   $ ./py4web.py run apps -s gunicorn --watch=off


* set gunicorn options via python module

 ::

  create a new python module mod_name

 .. code:: bash


  $  mkdir mod_name && cp myguni.conf.py mod_name/__init__.py
  $
  $ # via env
  $export GUNCORN_use_python_config=python:mod_name
  $
  $ # via gunicorn.saenv
  $echo use_python_config=python:mod_name >> gunicorn.saenv

  
 ::

   $ ./py4web.py run apps -s gunicorn --watch=off


* set gunicorn options via gunicorn.conf.py

 ::

 
  write gunicorn settings to the gunicorn.conf.py

  (if gunicorn.conf.py exists, the GUNICORN_ vars and the file gunicorn.saenv will be ignored)

 .. code:: bash

  $ echo "print_config = True"  > gunicorn.conf.py 
  $ # or
  $ cp myguni.con.py gunicorn.conf.py 


 ::

   $ ./py4web.py run apps -s gunicorn --watch=off
                          
* set gunicorn options via gunicorn-cli 

 ::

  run py4web/apps as wsgi-apps

 .. code:: bash

  $ echo 'from py4web.core import wsgi;myapp = wsgi(apps_folder="apps")' > py4web_wsgi.py 
  $


 ::

   $ gunicorn -w 4 py4web_wsgi:myapp 


* test gunicorn response time 

 ::

  add to .bashrc 

 .. code:: bash

   export PY4WEB_LOGS=/tmp
   p4w_todo_get() { time seq 1 500 | xargs -I % curl http://localhost:8000/todo &>/dev/null ;}
   todotest() { for ((i=0; i < $1; i++)); do p4w_todo_get  & done  ;}

 ::

   $ ./py4web.py run apps -s gunicorn -L 10 --watch=off &

   $ todotest 10
   $
   $ less /tmp/server-py4web.log


thats it

