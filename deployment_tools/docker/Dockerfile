# please change :
# password.txt with your desire filename
# password_admin with your desire password admin
# 8000 with your available port

FROM ubuntu:latest

RUN apt update && \
 apt install -y git python3-pip python-pip memcached && \
 service memcached restart

RUN groupadd -r web3py && \
 useradd -m -r -g web3py web3py

USER web3py

RUN rm -rf /home/web3py/web3py && \
 cd /home/web3py/ && \
 git clone https://github.com/web2py/web3py && \
 cd web3py && \
 pip3 install pytest mechanize twine && \
 pip3 install -U -r requirements.txt && \
 make test && \
 python3 -c "from pydal.validators import CRYPT; open('password.txt','w').write(str(CRYPT()('password_admin' )[0] ) )" && \
 mkdir apps/examples/databases 

WORKDIR /home/web3py/web3py

EXPOSE 8000

CMD ["./web3py-start", "-p", "./password.txt", "-a", "0.0.0.0:8000", "./apps"]
