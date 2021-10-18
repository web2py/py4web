#!/bin/bash
#

# ========================================================================
#   machine-setup.sh
#
# installation script for py4web on Ubuntu server
#    see https://github.com/web2py/py4web/blob/master/docs/updateDocs.sh
#
#   tested with Ubuntu Server 20.04.03 LTS
#
# Usage:
#       copy and run it in any directory with 'sudo ./machine-setup.sh'
#       
# ========================================================================

# Parameters:

# python_bin is used to state your python version
# by default python_bin=python3.8
python_bin=python3.8

# use_iptables is set to yes if
# you want to setup linux firewall from scratch
# allowing only ssh and http/https
use_iptables=yes

if [ "$EUID" -ne 0 ] 2>/dev/null
  then echo "Please run as root or with sudo"
  exit
fi

# iptables persistent configuration in Ubuntu >= 10.04 and Debian >= 6.0
if [ $use_iptables = 'yes' ]
then
    echo "======================================="
    echo "Configuring iptables firewall"
    echo "======================================="

    cat > iptables-py4web.sh <<EOF

    ip6tables -P INPUT DROP
    ip6tables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

    # Starting IPv4 firewall
    iptables -F
    iptables -X
    iptables -t nat -F
    iptables -t nat -X
    iptables -t mangle -F
    iptables -t mangle -X
     
    #unlimited loopback
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A OUTPUT -o lo -j ACCEPT
    
    #unlimited output
    iptables -P OUTPUT ACCEPT
   
    # Block sync
    iptables -A INPUT -p tcp ! --syn -m state --state NEW  -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "Drop Sync"
    iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP
     
    # Block Fragments
    iptables -A INPUT -f  -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "Fragments Packets"
    iptables -A INPUT -f -j DROP
     
    # Block bad stuff
    iptables  -A INPUT -p tcp --tcp-flags ALL FIN,URG,PSH -j DROP
    iptables  -A INPUT -p tcp --tcp-flags ALL ALL -j DROP
     
    iptables  -A INPUT -p tcp --tcp-flags ALL NONE -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "NULL Packets"
    iptables  -A INPUT -p tcp --tcp-flags ALL NONE -j DROP # NULL packets
     
    iptables  -A INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP
     
    iptables  -A INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "XMAS Packets"
    iptables  -A INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP #XMAS
     
    iptables  -A INPUT -p tcp --tcp-flags FIN,ACK FIN -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "Fin Packets Scan"
    iptables  -A INPUT -p tcp --tcp-flags FIN,ACK FIN -j DROP # FIN packet scans
     
    iptables  -A INPUT -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP
     
    # Allow established connections and outcoming stuff
    iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    iptables -A OUTPUT -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
     
    # Allow ssh 
    iptables -A INPUT -p tcp --destination-port 22 -j ACCEPT
     
    # allow incomming ICMP ping pong stuff
    iptables -A INPUT -p icmp --icmp-type 8 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
    iptables -A OUTPUT -p icmp --icmp-type 0 -m state --state ESTABLISHED,RELATED -j ACCEPT
     
    # Allow port 53 tcp/udp (DNS Server)
    iptables -A INPUT -p udp --dport 53 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
    iptables -A OUTPUT -p udp --sport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT
     
    iptables -A INPUT -p tcp --destination-port 53 -m state --state NEW,ESTABLISHED,RELATED  -j ACCEPT
    iptables -A OUTPUT -p tcp --sport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT
     
    # Open port 80
    iptables -A INPUT -p tcp --destination-port 80 -j ACCEPT
    iptables -A INPUT -p tcp --destination-port 443 -j ACCEPT
    ##### Add your rules below ######
     
    ##### END your rules ############

    # log everything else and drop it
    iptables -A INPUT -j LOG
    iptables -A FORWARD -j LOG
    iptables -A INPUT -j DROP

EOF

    chmod +x iptables-py4web.sh
    ./iptables-py4web.sh
    
    # make ipchain persistent on Ubuntu
    echo iptables-persistent iptables-persistent/autosave_v4 boolean true | sudo debconf-set-selections
    echo iptables-persistent iptables-persistent/autosave_v6 boolean true | sudo debconf-set-selections
    sudo apt-get -y install iptables-persistent
    sudo bash -c 'iptables-save > /etc/iptables/rules.v4'
    sudo bash -c 'ip6tables-save > /etc/iptables/rules.v6'


else
    echo Skipping iptables
fi

echo "======================================="
echo "Installing Packages"
echo "======================================="
apt-get update
apt-get -y install emacs
apt-get -y install zip unzip
apt-get -y install tar
apt-get -y install postgresql
apt-get -y install libpq-dev
apt-get -y install sendmail
apt-get -y install fail2ban
apt-get -y install supervisor
apt-get -y install nginx
apt-get -y install ${python_bin}
apt-get -y install python3-pip
apt-get -y install ${python_bin}-dev
apt-get -y install postgresql-client
apt-get -y install postgresql-client-common
apt-get -y install sendmail
apt-get -y install redis-server


echo "======================================="
echo "Installing Python Packages for py4web"
echo "======================================="
cat > requirements-py4web.txt <<EOF
tornado
gevent
gunicorn
requests
redis
psycopg2
py4web
EOF

${python_bin} -m pip install -r requirements-py4web.txt

if [ -f requirements.txt ]
then
    echo "======================================="
    echo "Installing Packages for apps"
    echo "======================================="
    ${python_bin} -m pip install -r requirements.txt
fi

echo "======================================="
echo "configuring database"
echo "======================================="
echo Postgres password
sudo -u postgres createuser -s default -P --interactive
sudo -u postgres createdb default

if [ ! -f /home/www-data/py4web ]
then
    echo "========================================="
    echo "creating missing py4web folders and apps"
    echo "========================================="
    mkdir -p /home/www-data/py4web
    py4web setup /home/www-data/py4web/apps
    chown -R www-data:www-data /home/www-data/py4web/apps
fi

if [ ! -d /etc/nginx/sites-available/py4web ]
then
    echo "======================================="
    echo "configuring NGINX"
    echo "======================================="
    mkdir -p /etc/nginx/conf.d/py4web
# Create configuration file /etc/nginx/sites-available/py4web
echo 'server {
        listen          80;
        server_name     $hostname;
        location ~* ^/(\w+)/static(?:/_[\d]+\.[\d]+\.[\d]+)?/(.*)$ {
            alias /home/www-data/py4web/apps/$1/static/$2;
            expires max;
        }
        location / {
            proxy_set_header   X-Forwarded-Proto $scheme;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   Host $http_host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-Host $http_host;
            proxy_redirect off;
            proxy_pass      http://127.0.0.1:8000;
        }
}
server {
        listen 443 default_server ssl;
        server_name     $hostname;
        ssl_certificate         /etc/nginx/ssl/py4web.crt;
        ssl_certificate_key     /etc/nginx/ssl/py4web.key;
        ssl_prefer_server_ciphers on;
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 10m;
        ssl_ciphers ECDHE-RSA-AES256-SHA:DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        keepalive_timeout    70;
        location / {
            proxy_set_header   X-Forwarded-Proto $scheme;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   Host $http_host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-Host $http_host;
            proxy_redirect off;
            proxy_pass      http://127.0.0.1:8000;
        }
        location ~* ^/(\w+)/static(?:/_[\d]+\.[\d]+\.[\d]+)?/(.*)$ {
            alias /home/www-data/py4web/apps/$1/static/$2;
            expires max;
        }
}' >/etc/nginx/sites-available/py4web
ln -s /etc/nginx/sites-available/py4web /etc/nginx/sites-enabled/py4web
rm /etc/nginx/sites-enabled/default
fi

if [ ! -f /etc/nginx/ssl/py4web.crt ]
then
    echo "======================================="
    echo "creating a self signed certificate"
    echo "======================================="
    mkdir -p /etc/nginx/ssl
    # pushd and popd do not work with sudo because it uses sh shell
    oldpath=`pwd`
    cd /etc/nginx/ssl
    # a 2048 bit key is needed nowadays
    openssl genrsa 2048 > py4web.key
    chmod 400 py4web.key
    openssl req -new -x509 -nodes -sha1 -days 1780 -key py4web.key > py4web.crt
    openssl x509 -noout -fingerprint -text < py4web.crt > py4web.info
    cd $oldpath
fi

if [ ! -f /etc/init.d/py4web ]
then

echo '
#! /bin/sh

NAME=py4web
DESC="py4web process"
PIDFILE="/var/run/${NAME}.pid"
LOGFILE="/var/log/${NAME}.log"
DAEMON="/usr/local/bin/py4web"
DAEMON_OPTS="run --password_file /home/www-data/py4web/password.txt /home/www-data/py4web/apps"
START_OPTS="--start --background --make-pidfile --pidfile ${PIDFILE} --exec ${DAEMON} -- ${DAEMON_OPTS}"
STOP_OPTS="--stop --oknodo --pidfile ${PIDFILE}"

test -x $DAEMON || exit 0
set -e

case "$1" in
start)
  echo -n "Starting ${DESC}: "
  start-stop-daemon $START_OPTS >> $LOGFILE
  echo "$NAME."
  ;;
stop)
  echo -n "Stopping $DESC: "
  start-stop-daemon $STOP_OPTS
  echo "$NAME."
  rm -f $PIDFILE
  ;;
restart|force-reload)
  echo -n "Restarting $DESC: "
  start-stop-daemon $STOP_OPTS
  sleep 1
  start-stop-daemon $START_OPTS >> $LOGFILE
  ;;
*)
  N=/etc/init.d/$NAME
  echo "Usage: $N {start|stop|restart|force-reload}" >&2
  exit 1
  ;;
esac
exit 0
' > /etc/init.d/py4web

fi

chmod +x /etc/init.d/py4web
echo Enter the password for py4web Dashboard:
py4web set_password --password_file=/home/www-data/py4web/password.txt
/etc/init.d/py4web restart
/etc/init.d/nginx restart
