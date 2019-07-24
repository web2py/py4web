# please change :
# password.txt with your desire filename
# password_admin with your desire password admin
# 8000 with your available port

FROM ubuntu:latest

RUN apt update && \
 apt install -y git python3-pip python-pip memcached && \
 service memcached restart

RUN groupadd -r py4web && \
 useradd -m -r -g py4web py4web

USER py4web

RUN rm -rf /home/py4web/py4web && \
 cd /home/py4web/ && \
 git clone https://github.com/web2py/py4web && \
 cd py4web && \
 pip3 install pytest mechanize twine && \
 pip3 install -U -r requirements.txt && \
 make test && \
 python3 -c "from pydal.validators import CRYPT; open('password.txt','w').write(str(CRYPT()('password_admin' )[0] ) )" && \
 mkdir apps/examples/databases 

WORKDIR /home/py4web/py4web

EXPOSE 8000

CMD ["./py4web-start", "-p", "./password.txt", "-a", "0.0.0.0:8000", "./apps"]
