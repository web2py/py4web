import logging
import os
import ssl
import sys

from ombott.server_adapters import ServerAdapter

try:
    from .utils.wsservers import *
except ImportError:
    wsservers_list = []

__all__ = [
    "gunicorn",
    "gunicornGevent",
    "gevent",
    "geventWebSocketServer",
    "geventWs",  # short_name
    "wsgirefThreadingServer",
    "wsgiTh",  # short_name
    "rocketServer",
] + wsservers_list

# ---------------------- utils -----------------------------------------------


# export PY4WEB_LOGS=/tmp # export PY4WEB_LOGS=
def get_log_file(out_banner=True):
    log_dir = os.environ.get("PY4WEB_LOGS", None)
    if log_dir and os.path.isdir(log_dir):
        log_file = os.path.join(log_dir, "server-py4web.log")
        if out_banner:
            print(f"log_file: {log_file}")
        return log_file
    return None


def check_level(level):

    # lib/python3.7/logging/__init__.py
    # CRITICAL = 50
    # FATAL = CRITICAL
    # ERROR = 40
    # WARNING = 30
    # WARN = WARNING
    # INFO = 20
    # DEBUG = 10
    # NOTSET = 0

    return (
        level
        if level
        in (
            logging.CRITICAL,
            logging.ERROR,
            logging.WARN,
            logging.INFO,
            logging.DEBUG,
            logging.NOTSET,
        )
        else logging.WARN
    )


def logging_conf(level=logging.WARN, logger_name=__name__, fmode="w", test_log=False):

    log_file = get_log_file()
    log_to = dict()

    if log_file:
        if sys.version_info >= (3, 9):
            log_to["filename"] = log_file
            log_to["filemode"] = fmode
            log_to["encoding"] = "utf-8"
        else:
            try:
                h = logging.FileHandler(log_file, mode=fmode, encoding="utf-8")
                log_to.update({"handlers": [h]})
            except (LookupError, KeyError, ValueError) as ex:
                print(f"{ex}, bad  encoding {__file__}")
                pass

    short_msg = "%(message)s > %(threadName)s > %(asctime)s.%(msecs)03d"
    # long_msg = short_msg + " > %(funcName)s > %(filename)s:%(lineno)d > %(levelname)s"

    time_msg = "%H:%M:%S"
    # date_time_msg = '%Y-%m-%d %H:%M:%S'

    try:
        logging.basicConfig(
            format=short_msg,
            datefmt=time_msg,
            level=check_level(level),
            **log_to,
        )
    except (OSError, LookupError, KeyError, ValueError) as ex:
        print(f"{ex}, {__file__}")
        print(f"cannot open {log_file}")
        logging.basicConfig(
            format="%(message)s",
            level=check_level(level),
        )

    if logger_name is None:
        return None

    log = logging.getLogger("SA:" + logger_name)
    log.propagate = True

    if test_log:
        for func in (
            log.debug,
            log.info,
            log.warn,
            log.error,
            log.critical,
        ):
            func("func: " + func.__name__)

    return log


def get_workers(opts, default=10):
    try:
        return opts["workers"] if opts["workers"] else default
    except KeyError:
        return default


def check_port(host="127.0.0.1", port=8000):
    import socket
    import errno
    import subprocess

    def os_cmd(run_cmd):
        try:
            subprocess.run(
                run_cmd,
                shell=True,
                check=True,
                text=True,
            )
        except subprocess.CalledProcessError:
            pass

    if host.startswith("unix:/"):
        socket_path = host[5:]
        if os.path.exists(socket_path):
            if port == 0:
                os_cmd(f"ls -alFi {socket_path}")
                sys.exit(f"can't run gunicorn: {socket_path} exists")
            elif port == 1:
                os_cmd("ps -ef | head -1; ps -ef | grep py4web | grep -v grep")
                os_cmd(f"ls -alFi {socket_path}")
                os_cmd(f"lsof -w {socket_path}")
            elif port == 8000:
                pass
        print(f"gunicorn listening at: {host}")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, int(port)))
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            os_cmd(
                f"command -v lsof >/dev/null 2>&1 && ps -ef | head -1; ps -ef |"
                f" grep py4web | grep -v grep && lsof -nPi:{port}"
            )
            sys.exit(f"{host}:{port} is already in use")
        else:
            sys.exit(f"{e}\n{host}:{port} cannot be acessed")
    s.close()


# ---------------------- servers -----------------------------------------------


def gunicorn():
    from gevent import local  # pip install gevent gunicorn setproctitle
    import threading

    if isinstance(threading.local(), local.local):
        print("gunicorn: monkey.patch_all() applied")

    class GunicornServer(ServerAdapter):
        def run(self, app_handler):
            try:
                from gunicorn.app.base import Application
            except ImportError as ex:
                sys.exit(f"{ex}\nTry: pip install gunicorn gevent setproctitle")

            from ast import literal_eval

            check_port(self.host, self.port)

            logger = None

            sa_bind = (
                self.host
                if self.host.startswith("unix:/")
                else f"{self.host}:{self.port}"
            )

            sa_config = {
                "bind": sa_bind,  # f"{self.host}:{self.port}",
                "workers": get_workers(self.options),
                "certfile": self.options.get("certfile", None),
                "keyfile": self.options.get("keyfile", None),
                "accesslog": None,
                "errorlog": None,
                "proc_name": "sa_py4web",  # ps a | grep py4web
                "config": "sa_config",
                # ( 'sa_config',  'GUNICORN_', 'gunicorn.saenv', 'gunicorn.conf.py' )
            }

            if not self.quiet:
                level = check_level(self.options["logging_level"])
                log_file = get_log_file(out_banner=False)

                logger = logging_conf(level)
                log_to = "-" if log_file is None else log_file

                sa_config.update(
                    {
                        "loglevel": logging.getLevelName(level),
                        "access_log_format": '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"',
                        "accesslog": log_to,
                        "errorlog": log_to,
                    }
                )

            class GunicornApplication(Application):
                def get_gunicorn_options(
                    self,
                    gu_default="gunicorn.conf.py",
                    env_file="gunicorn.saenv",
                    env_key="GUNICORN_",
                ):
                    def check_kv(kx, vx):
                        if (
                            kx
                            and vx
                            and (
                                kx
                                not in (
                                    "bind",
                                    "config",
                                )
                            )
                        ):
                            if vx.startswith("{") and vx.endswith("}"):
                                vx = literal_eval(vx)
                            if vx == "None":
                                vx = None
                            return kx, vx
                        return None, None

                    if os.path.isfile(gu_default):
                        return {"use_python_config": gu_default, "config": gu_default}

                    res_opts = dict()

                    if os.path.isfile(env_file):
                        try:
                            with open(env_file, "r") as f:
                                lines = f.read().splitlines()
                                for line in lines:
                                    line = line.strip()
                                    if not line or line.startswith(("#", "[")):
                                        continue
                                    for e in ("export ", env_key):
                                        line = line.replace(e, "", 1)
                                    k, v = None, None
                                    try:
                                        k, v = line.split("=", 1)
                                        k, v = k.strip().lower(), v.strip()
                                    except (ValueError, AttributeError):
                                        continue
                                    k, v = check_kv(k, v)
                                    if k is None:
                                        continue
                                    res_opts[k] = v

                                if res_opts:
                                    res_opts["config"] = env_file
                                    return res_opts

                        except (IOError, OSError) as ex:
                            sys.exit(f"{ex}\nError: {env_file}")

                    for k, v in os.environ.items():
                        if k.startswith(env_key):
                            k = k.split("_", 1)[1].lower()
                            k, v = check_kv(k, v)
                            if k is None:
                                continue
                            res_opts[k] = v

                    if res_opts:
                        res_opts["config"] = env_key

                    return res_opts

                def load_config(self):
                    sa_config.update(self.get_gunicorn_options())
                    logger and logger.debug(sa_config)

                    for k, v in sa_config.items():
                        if k not in self.cfg.settings:
                            continue
                        self.cfg.set(k, v)

                    for e in (
                        "use_python_config",
                        "usepy",
                    ):
                        if e in sa_config:
                            Application.load_config_from_file(self, sa_config[e])
                            break

                def load(self):
                    return app_handler

            GunicornApplication().run()

    return GunicornServer


gunicornGevent = gunicorn


def gevent():
    # gevent version 23.9.1

    import threading

    from gevent import local, pywsgi  # pip install gevent

    if not isinstance(threading.local(), local.local):
        msg = "Ombott requires gevent.monkey.patch_all() (before import)"
        raise RuntimeError(msg)

    # ./py4web.py run apps --watch=off -s gevent -L 20
    #
    # ./py4web.py run apps -s gevent --watch=off --port=8443 --ssl_cert=cert.pem --ssl_key=key.pem -L 0
    # ./py4web.py run apps -s gevent --watch=off --host=192.168.1.161 --port=8443 --ssl_cert=server.pem -L 0

    class GeventServer(ServerAdapter):
        def run(self, app_handler):
            logger = None  # "default"

            if not self.quiet:
                logger = logging_conf(
                    self.options["logging_level"],
                    "gevent",
                )
                # logger.addHandler(logging.StreamHandler())

            certfile = self.options.get("certfile", None)

            ssl_args = (
                dict(
                    certfile=certfile,
                    keyfile=self.options.get("keyfile", None),
                    ssl_version=ssl.PROTOCOL_SSLv23,
                    server_side=True,
                    do_handshake_on_connect=False,
                )
                if certfile
                else dict()
            )

            server = pywsgi.WSGIServer(
                (self.host, self.port),
                app_handler,
                log=logger,
                error_log=logger,
                **ssl_args,
            )

            server.serve_forever()

    return GeventServer


def geventWebSocketServer():
    from gevent import pywsgi

    # from geventwebsocket.handler import WebSocketHandler # pip install gevent-websocket
    from gevent_ws import WebSocketHandler  # pip install gevent gevent-ws

    # https://stackoverflow.com/questions/5312311/secure-websockets-with-self-signed-certificate
    # https://pypi.org/project/gevent-ws/
    # ./py4web.py run apps -s geventWebSocketServer --watch=off --ssl_cert=server.pem -H 192.168.1.161 -P 9000 -L 10
    # vi apps/_websocket/templates/index.html    set: ws, wss, host, port
    # firefox http://localhost:8000/_websocket
    # firefox https://192.168.1.161:9000/_websocket  test wss
    # curl --insecure -I -H 'Upgrade: websocket' \
    #   -H "Sec-WebSocket-Key: `openssl rand -base64 16`" \
    #   -H 'Sec-WebSocket-Version: 13' \
    #   -sSv  https://192.168.1.161:9000/

    class GeventWebSocketServer(ServerAdapter):
        def run(self, app_handler):
            logger = None  # "default"

            if not self.quiet:
                logger = logging_conf(
                    self.options["logging_level"],
                    "gevent-ws",
                )

            certfile = self.options.get("certfile", None)

            ssl_args = (
                dict(
                    certfile=certfile,
                    keyfile=self.options.get("keyfile", None),
                )
                if certfile
                else dict()
            )

            server = pywsgi.WSGIServer(
                (self.host, self.port),
                app_handler,
                handler_class=WebSocketHandler,
                log=logger,
                error_log=logger,
                **ssl_args,
            )

            server.serve_forever()

    return GeventWebSocketServer


geventWs = geventWebSocketServer


def wsgirefThreadingServer():
    # https://www.electricmonk.nl/log/2016/02/15/multithreaded-dev-web-server-for-the-python-bottle-web-framework/

    import socket
    from concurrent.futures import ThreadPoolExecutor  # pip install futures
    from socketserver import ThreadingMixIn
    from wsgiref.simple_server import WSGIRequestHandler, WSGIServer, make_server

    class WSGIRefThreadingServer(ServerAdapter):
        def run(self, app_handler):

            self.log = None

            if not self.quiet:
                self.log = logging_conf(
                    self.options["logging_level"],
                    "wsgiref",
                )

            self_run = self  # used in internal classes to access options and logger

            class PoolMixIn(ThreadingMixIn):
                def process_request(self, request, client_address):
                    self.pool.submit(
                        self.process_request_thread, request, client_address
                    )

            class ThreadingWSGIServer(PoolMixIn, WSGIServer):
                daemon_threads = True
                pool = ThreadPoolExecutor(
                    max_workers=get_workers(self.options, default=40)
                )

            class Server:
                def __init__(
                    self, server_address=("127.0.0.1", 8000), handler_cls=None
                ):
                    self.wsgi_app = None
                    self.listen, self.port = server_address
                    self.handler_cls = handler_cls

                def set_app(self, app):
                    self.wsgi_app = app

                def get_app(self):
                    return self.wsgi_app

                def serve_forever(self):
                    self.server = make_server(
                        self.listen,
                        self.port,
                        self.wsgi_app,
                        ThreadingWSGIServer,
                        self.handler_cls,
                    )

                    # openssl req -newkey rsa:4096 -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
                    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
                    # ./py4web.py run apps -s wsgirefThreadingServer --watch=off --port=8443 --ssl_cert=cert.pem --ssl_key=key.pem
                    # openssl s_client -showcerts -connect 127.0.0.1:8443

                    certfile = self_run.options.get("certfile", None)

                    if certfile:
                        self.server.socket = ssl.wrap_socket(
                            self.server.socket,
                            certfile=certfile,
                            keyfile=self_run.options.get("keyfile", None),
                            ssl_version=ssl.PROTOCOL_SSLv23,
                            server_side=True,
                            do_handshake_on_connect=False,
                        )

                    self.server.serve_forever()

            class LogHandler(WSGIRequestHandler):
                def address_string(self):  # Prevent reverse DNS lookups please.
                    return self.client_address[0]

                def log_request(self, *args, **kw):
                    if not self_run.quiet:
                        return WSGIRequestHandler.log_request(self, *args, **kw)

                def log_message(self, format, *args):
                    if not self_run.quiet:  # and ( not args[1] in ['200', '304']) :
                        msg = "%s - - [%s] %s" % (
                            self.client_address[0],
                            self.log_date_time_string(),
                            format % args,
                        )
                        self_run.log.info(msg)

            # handler_cls = self.options.get("handler_class", LogHandler)
            server_cls = Server

            if ":" in self.host:  # Fix wsgiref for IPv6 addresses.
                if getattr(server_cls, "address_family") == socket.AF_INET:

                    class ServerClass(Server):
                        address_family = socket.AF_INET6

                    server_cls = ServerClass

            srv = make_server(
                self.host, self.port, app_handler, server_cls, LogHandler
            )  # handler_cls)
            srv.serve_forever()

    return WSGIRefThreadingServer


wsgiTh = wsgirefThreadingServer


def rocketServer():
    try:
        from rocket3 import Rocket3 as Rocket
    except ImportError:
        from .rocket3 import Rocket3 as Rocket

    class RocketServer(ServerAdapter):
        def run(self, app_handler):

            if not self.quiet:

                logging_conf(
                    self.options["logging_level"],
                )

            interface = (
                (
                    self.host,
                    self.port,
                    self.options["keyfile"],
                    self.options["certfile"],
                )
                if (
                    self.options.get("certfile", None)
                    and self.options.get("keyfile", None)
                )
                else (self.host, self.port)
            )

            server = Rocket(interface, "wsgi", dict(wsgi_app=app_handler))
            server.start()

    return RocketServer


"""
# how to write to server-adapters.log from controllers.py
# cp -a _scaffold test-salog

import sys
import logging
from .common import logger
from .settings import APP_NAME
from threading import Lock


_srv_log=None
def log_info(mess, dbg=True, ):
    def salog(pat='SA:'):
        global _srv_log
        if _srv_log and isinstance( _srv_log, logging.Logger ):
           return _srv_log
        hs= [e for e in logging.root.manager.loggerDict if e.startswith(pat) ]
        if len(hs) == 0:
            return logger

        sa_lock = Lock()
        with sa_lock:
            _srv_log = logging.getLogger(hs[0])

        return _srv_log

    caller = f" > {APP_NAME} > {sys._getframe().f_back.f_code.co_name}"
    dbg and salog().info(mess + caller)

log_warn=log_info
log_debug=log_info

log_warn('0'* 30 + ' ' +APP_NAME)

@action("index")
@action.uses("index.html", auth, T)
def index():

    log_warn('7'* 30 + ' ' +APP_NAME)
    log_info('9'* 30 + ' ' +APP_NAME)

    user = auth.get_user()
    message = T("Hello {first_name}").format(**user) if user else T("Hello")
    actions = {"allowed_actions": auth.param.allowed_actions}
    return dict(message=message, actions=actions)

"""
