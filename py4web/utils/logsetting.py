import logging, os, sys


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