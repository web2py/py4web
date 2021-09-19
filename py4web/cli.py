"""PY4WEB - a web framework for rapid development of efficient database driven web applications"""

import os
import code
import click
import sys
import platform
import json
import pydal
import zipfile
import signal
import asyncio
import logging
import ombott
import inspect

from .watcher import watch

# Optional web servers for speed
try:
    import gunicorn
except ImportError:
    gunicorn = None

from .core.install import install_args
from .core import import_apps
from . import server_adapters


PY4WEB_CMD = sys.argv[0]

ART = r"""
██████╗ ██╗   ██╗██╗  ██╗██╗    ██╗███████╗██████╗
██╔══██╗╚██╗ ██╔╝██║  ██║██║    ██║██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ███████║██║ █╗ ██║█████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ╚════██║██║███╗██║██╔══╝  ██╔══██╗
██║        ██║        ██║╚███╔███╔╝███████╗██████╔╝
╚═╝        ╚═╝        ╚═╝ ╚══╝╚══╝ ╚══════╝╚═════╝
Is still experimental...
"""

#########################################################################################
# CLI
#########################################################################################

__ssl__ = __import__("ssl")
_ssl = getattr(__ssl__, "_ssl") or getattr(__ssl__, "_ssl2")


def keyboardInterruptHandler(signal, frame):
    """Catch interrupts like Ctrl-C"""
    click.echo(
        "KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal)
    )
    sys.exit(0)


@click.group(
    context_settings=dict(help_option_names=["-h", "-help", "--help"]),
    help='%s\n\nType "%s COMMAND -h" for available options on commands'
    % (__doc__, PY4WEB_CMD),
)
def cli():
    pass


@cli.command()
@click.option(
    "-a", "--all", is_flag=True, default=False, help="List version of all modules"
)
def version(all):
    """Show versions and exit"""
    from . import __version__

    click.echo("py4web: %s" % __version__)
    if all:
        click.echo("system: %s" % platform.platform())
        click.echo("python: %s" % sys.version.replace("\n", " "))
        for name in sorted(sys.modules):
            if hasattr(sys.modules[name], "__version__"):
                click.echo("%s: %s" % (name, sys.modules[name].__version__))


@cli.command()
@click.argument("apps_folder")
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
def setup(**kwargs):
    """Setup new apps folder or reinstall it"""
    install_args(kwargs, reinstall_apps=True)


@cli.command()
@click.argument("apps_folder", type=click.Path(exists=True))
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
def shell(**kwargs):
    """Open a python shell with apps_folder's parent added to the path"""
    install_args(kwargs)
    code.interact(local=dict(globals(), **locals()))


@cli.command()
@click.argument("apps_folder", type=click.Path(exists=True))
@click.argument("func")
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
@click.option(
    "--args",
    default="{}",
    help="Arguments passed to the program/function",
    show_default=True,
)
def call(apps_folder, func, yes, args):
    """Call a function inside apps_folder"""
    kwargs = json.loads(args)
    install_args(dict(apps_folder=apps_folder, yes=yes))
    apps_folder_name = os.path.basename(os.environ["PY4WEB_APPS_FOLDER"])
    module, name = ("%s.%s" % (apps_folder_name, func)).rsplit(".", 1)
    env = {}
    exec("from %s import %s" % (module, name), {}, env)
    env[name](**kwargs)


@cli.command(name="set_password")
@click.option(
    "--password",
    prompt=True,
    confirmation_prompt=True,
    hide_input=True,
    help="Password value (asked if missing)",
)
@click.option(
    "-p",
    "--password_file",
    default="password.txt",
    help="File for the encrypted password",
    show_default=True,
)
def set_password(password, password_file):
    """Set administrator's password for the Dashboard"""
    click.echo('Storing the hashed password in file "%s"\n' % password_file)
    with open(password_file, "w") as fp:
        fp.write(str(pydal.validators.CRYPT()(password)[0]))


@cli.command(name="new_app")
@click.argument("apps_folder")
@click.argument("app_name")
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
@click.option(
    "-s",
    "--scaffold_zip",
    default=None,
    help="Path to the zip with the scaffolding app",
    show_default=False,
)
def new_app(apps_folder, app_name, yes, scaffold_zip):
    """Create a new app copying the scaffolding one"""
    install_args(dict(apps_folder=apps_folder, yes=yes))
    source = scaffold_zip or os.path.join(
        os.path.dirname(__file__), "assets", "py4web.app._scaffold.zip"
    )
    target_dir = os.path.join(os.environ["PY4WEB_APPS_FOLDER"], app_name)
    if not os.path.exists(source):
        click.echo("Source app %s does not exists" % source)
        sys.exit(1)
    elif os.path.exists(target_dir):
        click.echo("Target folder %s already exists" % target_dir)
        sys.exit(1)
    else:
        zfile = zipfile.ZipFile(source, "r")
        zfile.extractall(target_dir)
        zfile.close()


@cli.command()
@click.argument("apps_folder", type=click.Path(exists=True))
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
@click.option("-H", "--host", default="127.0.0.1", help="Host name", show_default=True)
@click.option(
    "-P", "--port", default=8000, type=int, help="Port number", show_default=True
)
@click.option(
    "-p",
    "--password_file",
    default="password.txt",
    help="File for the encrypted password",
    show_default=True,
)
@click.option(
    "-s",
    "--server",
    default="default",
    type=click.Choice(
        ["default", "wsgiref", "tornado", "gunicorn", "gevent", "waitress"]
        + server_adapters.__all__
    ),
    help="server to use",
    show_default=True,
)
@click.option(
    "-w",
    "--number_workers",
    default=0,
    type=int,
    help="Number of workers",
    show_default=True,
)
@click.option(
    "-d",
    "--dashboard_mode",
    default="full",
    help="Dashboard mode: demo, readonly, full, none",
    show_default=True,
)
@click.option(
    "--watch",
    default="lazy",
    type=click.Choice(["off", "sync", "lazy"]),
    help="Watch python changes and reload apps automatically, modes: off, sync, lazy",
    show_default=True,
)
@click.option(
    "--ssl_cert", type=click.Path(exists=True), help="SSL certificate file for HTTPS"
)
@click.option("--ssl_key", type=click.Path(exists=True), help="SSL key file for HTTPS")
def run(**kwargs):
    """Run all the applications on apps_folder"""
    install_args(kwargs)

    from . import __version__

    click.secho(ART, fg="blue")
    click.echo("Py4web: %s on Python %s\n\n" % (__version__, sys.version))

    # If we know where the password is stored, read it, otherwise ask for one
    if os.path.exists(os.path.join(os.environ["PY4WEB_APPS_FOLDER"], "_dashboard")):
        if (
            kwargs["dashboard_mode"] not in ("demo", "none")
            and not os.path.exists(kwargs["password_file"])
        ):
            click.echo(
                'You have not set a dashboard password. Run "%s set_password" to do so.'
                % PY4WEB_CMD
            )
        else:
            click.echo(
                "Dashboard is at: http://%s:%s/_dashboard"
                % (kwargs["host"], kwargs["port"])
            )

    # Catch interrupts like Ctrl-C
    orig_ctrl_c_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, keyboardInterruptHandler)

    # Start
    import_apps()
    start_server(kwargs, orig_ctrl_c_handler)


def start_server(kwargs, ctrl_c_orig):
    host = kwargs["host"]
    port = int(kwargs["port"])
    apps_folder = kwargs["apps_folder"]
    number_workers = kwargs["number_workers"]
    params = dict(host=host, port=port, reloader=False)
    server_config = dict(
        platform=platform.system().lower(),
        server=None if kwargs["server"] == "default" else kwargs["server"],
        number_workers=number_workers,
    )

    if server_config["server"]:
        for e in ("rocket", "Twisted"):
            if e in server_config["server"]:
                signal.signal(signal.SIGINT, ctrl_c_orig)
                break

    if not server_config["server"]:
        if server_config["platform"] == "windows":
            server_config["server"] = "tornado"
            if sys.version_info >= (
                3,
                8,
            ):  # see  https://bugs.python.org/issue37373 FIX: tornado/py3.8 on windows
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        elif number_workers <= 1:
            server_config["server"] = "tornado"
        else:
            if not gunicorn:
                logging.error("gunicorn not installed")
                return
            server_config["server"] = "gunicorn"
    params["server"] = server_config["server"]
    if params["server"] in server_adapters.__all__:
        params["server"] = getattr(server_adapters, params["server"])()
    if number_workers > 1:
        params["workers"] = number_workers
    if server_config["server"] == "gunicorn":
        sys.argv[:] = sys.argv[:1]  # else break gunicorn
    if kwargs["ssl_cert"] is not None:
        params["certfile"] = kwargs["ssl_cert"]
        params["keyfile"] = kwargs["ssl_key"]

    if server_config["server"] == "gevent":
        if not hasattr(_ssl, "sslwrap"):
            _ssl.sslwrap = new_sslwrap

    if kwargs["watch"] != "off":
        watch(apps_folder, server_config, kwargs["watch"])
    ombott.run(**params)


def new_sslwrap(
    sock,
    server_side=False,
    keyfile=None,
    certfile=None,
    cert_reqs=__ssl__.CERT_NONE,
    ssl_version=__ssl__.PROTOCOL_SSLv23,
    ca_certs=None,
    ciphers=None,
):
    context = __ssl__.SSLContext(ssl_version)
    context.verify_mode = cert_reqs or __ssl__.CERT_NONE
    if ca_certs:
        context.load_verify_locations(ca_certs)
    if certfile:
        context.load_cert_chain(certfile, keyfile)
    if ciphers:
        context.set_ciphers(ciphers)
    caller_self = inspect.currentframe().f_back.f_locals["self"]
    return context._wrap_socket(sock, server_side=server_side, ssl_sock=caller_self)
