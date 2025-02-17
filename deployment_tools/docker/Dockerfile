FROM ubuntu:latest

ARG user=py4web

RUN apt update && \
    apt install -y git python3 python3-pip python3-venv memcached && \
    service memcached restart && \
    groupadd -r $user && \
    useradd -m -r -g $user $user

USER $user
WORKDIR /home/$user/

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install -U py4web && \
    py4web setup --yes apps

EXPOSE 8000

CMD . venv/bin/activate && py4web run --password_file password.txt --host 0.0.0.0 --port 8000 apps
