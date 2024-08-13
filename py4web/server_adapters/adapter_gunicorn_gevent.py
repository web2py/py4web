import ast
import errno
import logging
import os
import socket
import subprocess
import sys
import threading

from gevent import local  # pip install gevent gunicorn setproctitle
from ombott.server_adapters import ServerAdapter

from .logging_utils import check_level, get_log_file, logging_conf


def check_port(host="127.0.0.1", port=8000):
    "Check the specified port is available and print debug info"

    if host.startswith("unix:/"):
        socket_path = host[5:]
        if os.path.exists(socket_path):
            if port == 0:
                if (
                    subprocess.run(
                        ["ls", "-alFi", "socket_path"], shell=False, check=False
                    ).returncode
                    != 0
                ):
                    sys.exit(f"can't run gunicorn: {socket_path} exists")
            elif port == 1:
                subprocess.run(
                    "ps -ef | head -1; ps -ef | grep py4web | grep -v grep",
                    shell=True,
                    check=False,
                )
                subprocess.run(["ls", "-alFi", socket_path], shell=False, check=False)
                subprocess.run(["lsof", "-w", socket_path], shell=False, check=False)
            elif port == 8000:
                pass
        print(f"gunicorn listening at: {host}")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, int(port)))
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            subprocess.run(
                f"command -v lsof >/dev/null 2>&1 && ps -ef | head -1; ps -ef |"
                f" grep py4web | grep -v grep && lsof -nPi:{port}",
                shell=True,
                check=False,
            )
            sys.exit(f"{host}:{port} is already in use")
        else:
            sys.exit(f"{e}\n{host}:{port} cannot be acessed")
    s.close()


def check_kv(kx, vx):
    "convenience function"
    if kx and vx and kx not in ("bind", "config"):
        if vx.startswith("{") and vx.endswith("}"):
            vx = ast.literal_eval(vx)
        if vx == "None":
            vx = None
        return kx, vx
    return None, None


def get_gunicorn_options(
    gu_default="gunicorn.conf.py",
    env_file="gunicorn.saenv",
    env_key="GUNICORN_",
):
    "Returns the default options"
    if os.path.isfile(gu_default):
        return {"use_python_config": gu_default, "config": gu_default}

    res_opts = {}

    if os.path.isfile(env_file):
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


class GunicornGeventAdapter(ServerAdapter):
    "The gunicorn server adapter"

    def run(self, handler):
        "runs the server"

        if isinstance(threading.local(), local.local):
            print("gunicorn: monkey.patch_all() applied")

        try:
            from gunicorn.app.base import Application
        except ImportError as ex:
            sys.exit(f"{ex}\nTry: pip install gunicorn gevent setproctitle")

        check_port(self.host, self.port)

        logger = None

        sa_bind = (
            self.host if self.host.startswith("unix:/") else f"{self.host}:{self.port}"
        )

        sa_config = {
            "bind": sa_bind,  # f"{self.host}:{self.port}",
            "workers": self.options.get("workers", 10),
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
            log_file = get_log_file()

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
            "A  gunicorn application"

            def load_config(self):
                "Loads the config"
                sa_config.update(get_gunicorn_options())
                logger and logger.debug(sa_config)

                for k, v in sa_config.items():
                    if k not in self.cfg.settings:
                        continue
                    self.cfg.set(k, v)

                for key in ("use_python_config", "usepy"):
                    if key in sa_config:
                        Application.load_config_from_file(self, sa_config[key])
                        break

            def load(self):
                return handler

        GunicornApplication().run()
