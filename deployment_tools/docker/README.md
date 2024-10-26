# Using py4web with Docker

## Purpose

- assuming you already know Docker, this is an easy way to install py4web
- you'll quickly obtain a totally isolated enviroment

Note that the latest program versions will be used, for increased security. If
you instead want to reproduce this exact environment on other systems,
you'll need to specify the version of all the components.


## Basic py4web container

You need a working Docker system, see the official site for installation info
at https://docs.docker.com/get-docker/ 
Download the four files on top of this page to an empty directory on your system. If you download them with chrome based browser there is a big chance you need to remove the .txt part from the file names due to this bug: https://github.com/microsoft/vscode/issues/118436

Then run:

    # build an image called py4web from latest Ubuntu
    $ docker build . -t py4web
    # build & run a container called mypy4web
    $ docker run -d --name mypy4web -p 8000:8000 py4web

You'll obtain the standard py4web app running with the Rocket web server and
listening on http://localhost:8000

Optional:

    # this is needed for providing a password in order to use the Dashboard
    $ docker exec -it mypy4web py4web set_password
    # then restart the container
    $ docker restart mypy4web

## Advanced py4web container with PostgreSQL

In this case you will also need the optional
docker-compose program (V2 is the new one, but
unfortunately they changed the program name from 'docker-compose' to 'docker compose').

For Linux/Mac, modify the Makefile file if needed and then run it:

    $ make up

For Windows without the make utility, or if you prefer not to use the Makefile, you can
use directly the command:

    $ docker-compose up -d

or 

    $ docker compose up -d

You'll still need to set the dashboard password:

    $ docker exec -it py4web-web-1 py4web set_password



## Working with the container

- You can easily setup a free temporary working container online at https://labs.play-with-docker.com/
- Using a modern IDE, you can also directly edit the files inside the containers - and even debug them!


## Combining py4web with Celery and Redis

Celery can be used for handling long running background tasks. 
Celery uses Redis as broker. Redis will be run in a seperate container. 

At the end of the docker-compose file add:

    redis:
        restart: always
        image: redis
        ports:
          - "6379:6379"

In the app (based on _scaffold) settings.py:

    #Celery settings
    USE_CELERY = True
    CELERY_BROKER = "redis://redis:6379/0"
    CELERY_BACKEND = "redis://redis:6379/0"

In common.py:

    # #######################################################
    # Optionally configure celery
    # #######################################################
    if settings.USE_CELERY:
        from celery import Celery
    
        # to use "from .common import scheduler" and then use it according
        # to celery docs, examples in tasks.py
        scheduler = Celery(
            "apps.%s.tasks" % settings.APP_NAME, broker=settings.CELERY_BROKER,  backend=settings.CELERY_BACKEND)      
        scheduler.conf.broker_connection_retry_on_startup = True

In the docker file use entrypoint.sh to get the scheduler going and start py4web.

    entrypoint.sh:

    #!/bin/bash
    . /home/py4web/.venv/bin/activate
    exec .venv/bin/celery -A apps.myapp.tasks beat &
    exec .venv/bin/celery -A apps.myapp.tasks worker --loglevel=info &
    exec py4web run --password_file password.txt --host 0.0.0.0 --port 8000 apps

complete Dockerfile:

    FROM ubuntu:latest
    
    ARG user=py4web
    ENV PY4WEB_ROOT=/home/$user
    
    RUN apt update && \
        apt install -y git locales locales-all python3.12 python3-pip python3.12-venv memcached && \
        service memcached restart && \
        groupadd -r $user && \
        useradd -m -r -g $user $user && \
        python3 -m venv  $PY4WEB_ROOT/.venv && \
        . $PY4WEB_ROOT/.venv/bin/activate && \
        python3 -m pip install -U py4web  psycopg2-binary && \
        python3 -m pip install -U "celery[redis]"
    
    ENV LC_ALL en_US.UTF-8
    ENV LANG en_US.UTF-8
    ENV LANGUAGE en_US.UTF-8  
   
    USER $user
    
    RUN . $PY4WEB_ROOT/.venv/bin/activate && \
        cd $PY4WEB_ROOT/ && py4web setup --yes apps
    # use   ./venv/bin/py4web set_password
    COPY password.txt $PY4WEB_ROOT/.

    EXPOSE 8000
    
    WORKDIR $PY4WEB_ROOT/
    COPY entrypoint.sh /usr/local/bin/
    ENTRYPOINT [ "entrypoint.sh" ]

docker-compose.yml

    services:
    
      web:
        build: .
        ports:
          - "8000:8000"
        environment:
         - PYDAL_URI=postgres://foo:bar@postgres:5432/baz
         - PYDAL_URI2=mysql://root:secret@localhost/ursadina_gtd
        volumes:
         - ./apps:/home/py4web/apps
        stdin_open: true
        tty: true
        depends_on:
          - postgres
          - redis
         
      postgres:
        restart: always
        image: postgres
        environment:
          - POSTGRES_USER=foo
          - POSTGRES_PASSWORD=bar
          - POSTGRES_DB=baz
          - POSTGRES_PORT=5432
        ports:
          - "5432:5432"
        volumes:
           - ./data/postgres:/var/lib/postgresql/data
      redis:
        restart: always
        image: redis
        ports:
          - "6379:6379"

    
