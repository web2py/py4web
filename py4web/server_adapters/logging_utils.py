import logging
import os
import sys


def make_logger(name, loggers_info):
    """
    Abstraction layer on logging. Example of usage:

    from py4web.server_adapters.logging_utils import make_logger

    loggers_info = [
        "warning:warning.log",
        "info:info.log",
        "debug:debug.log:$(asctime)s > %(levelname)s > %(message)s",
    ]

    logger = make_logger("py4web:appname", loggers_info)
    """
    default_formatter = (
        "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
    )
    # reset loggers
    root = logging.getLogger(name)
    list(map(root.removeHandler, root.handlers))
    list(map(root.removeFilter, root.filters))
    for logger in loggers_info:
        logger += ":stderr" if logger.count(":") == 0 else ""
        logger += ":" if logger.count(":") == 1 else ""
        level, filename, formatter = logger.split(":", 2)
        if not formatter:
            formatter = default_formatter
        if filename in ("stdout", "stderr"):
            handler = logging.StreamHandler(getattr(sys, filename))
        else:
            handler = logging.FileHandler(filename)
        handler.setFormatter(logging.Formatter(formatter))
        handler.setLevel(getattr(logging, level.upper(), "DEBUG"))
        root.addHandler(handler)
    return root


def get_log_file(out_banner=True):
    """
    Returns the filename for logging or None
    Assumes:
    export PY4WEB_ERRORLOG=/tmp # export PY4WEB_ERRORLOG=
    if PY4WEB_ERRORLOG is :stderr or :stdout returns None
    if PY4WEB_ERRORLOG is a folder returns the name of a logfile in that dir
    if PY4WEB_ERRORLOG is a filename it returns that filename
    if the out_banner argument is true, it outputs the filename
    """
    log_dir = os.environ.get("PY4WEB_ERRORLOG", None)
    if log_dir and not log_dir.startswith(":"):
        if os.path.isdir(log_dir):
            log_file = os.path.join(log_dir, "server-py4web.log")
        else:
            log_file = log_dir
        if out_banner:
            print(f"log_file: {log_file}")
        return log_file
    return None


def check_level(level):
    "Check the level is a valid loglevel"
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


def logging_conf(level=logging.WARN, logger_name=__name__, fmode="w"):
    "Configures logging"

    log_file = get_log_file()
    log_to = {}

    if log_file:
        if sys.version_info >= (3, 9):
            log_to["filename"] = log_file
            log_to["filemode"] = fmode
            log_to["encoding"] = "utf-8"
        else:
            h = logging.FileHandler(log_file, mode=fmode, encoding="utf-8")
            log_to.update({"handlers": [h]})

    short_msg = "%(message)s > %(threadName)s > %(asctime)s.%(msecs)03d"
    # long_msg = short_msg + " > %(funcName)s > %(filename)s:%(lineno)d > %(levelname)s"

    time_msg = "%H:%M:%S"
    # date_time_msg = '%Y-%m-%d %H:%M:%S'

    logging.basicConfig(
        format=short_msg,
        datefmt=time_msg,
        level=check_level(level),
        **log_to,
    )

    if logger_name is None:
        return None

    log = logging.getLogger("SA:" + logger_name)
    log.propagate = True

    return log
