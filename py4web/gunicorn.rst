====================
gunicorn with py4web
====================


The gunicorn server starts in the usual way for the py4web

::

   $./py4web.py run apps -s gunicorn --watch=off
   $
   $./py4web.py run apps -s gunicornGevent --watch=off


gunicornGevent === gunicorn + monkey.patch_all() 

It is possible to use several methods to configure gunicorn options with py4web

Let's show examples

* set gunicorn options via bash environment variables

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

   # example gunicorn.saenv
   #
   export GUNICORN_worker_tmp_dir=/dev/shm
   export GUNICORN_max_requests=1200
   worker_class=gthread
   threads=2

   # guncornGevent
   #worker_class=gevent
   #worker_class=eventlet

   # for use python-config-file
   # use_python_config=myguni.conf.py

   # for use python-config-mod_name
   # use_python_config=python:mod_name


* set gunicorn options via python file myguni.conf.py

 ::

   set the env variable use_python_config=myguni.conf.py

 .. code:: bash

   $ # via env
   $export GUNCORN_use_python_config=myguni.conf.py
   $ 
   $ # via gunicorn.saenv 
   $echo use_python_config=mmyguni.conf.py >> gunicorn.saenv

 ::

   write file myguni.conf.py

 .. code:: python

   # Gunicorn configuration file
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

  write python module 

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

