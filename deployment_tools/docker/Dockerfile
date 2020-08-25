# please change :
# password.txt with your desire filename
# password_admin with your desire password admin
# 8000 with your available port

FROM ubuntu:latest

ARG user=py4web
ARG password=none

RUN apt update && apt install -y git python3 python3-pip memcached

RUN service memcached restart

RUN groupadd -r $user && useradd -m -r -g $user $user

RUN python3 -m pip install -U py4web

USER $user

RUN cd /home/$user/ && py4web setup --yes apps

RUN cd /home/$user/ && \
    if [ "$password" = "none" ]; then echo "no admin"; else py4web set_password < "$password"; fi

EXPOSE 8000

WORKDIR /home/$user/

CMD py4web run --password_file password.txt --host 0.0.0.0 --port 8000 apps
