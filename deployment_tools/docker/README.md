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
Download all the files in this directory to an empty one your system, then run:

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


