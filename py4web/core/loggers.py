import os
import logging
import datetime
import uuid
import sys
import platform
import traceback
import inspect
import cgitb
import linecache

from pydal import DAL, Field

from .utils import safely
from .globs import request


def get_error_snapshot(depth=5):
    """Return a dict describing a given traceback (based on cgitb.text)."""

    etype, evalue, etb = sys.exc_info()
    if isinstance(etype, type):
        etype = etype.__name__

    data = {}
    data["timestamp"] = datetime.datetime.utcnow().isoformat().replace("T", " ")
    data["python_version"] = sys.version
    platform_keys = [
        "machine",
        "node",
        "platform",
        "processor",
        "python_branch",
        "python_build",
        "python_compiler",
        "python_implementation",
        "python_revision",
        "python_version",
        "python_version_tuple",
        "release",
        "system",
        "uname",
        "version",
    ]

    data["platform_info"] = {key: getattr(platform, key)() for key in platform_keys}
    data["os_environ"] = {key: str(value) for key, value in os.environ.items()}
    data["traceback"] = traceback.format_exc()
    data["exception_type"] = str(etype)
    data["exception_value"] = str(evalue)

    # Loopover the stack frames
    items = inspect.getinnerframes(etb, depth)
    del etb  # Prevent circular references that would cause memory leaks
    data["stackframes"] = stackframes = []

    for frame, file, lnum, func, lines, idx in items:
        file = file and os.path.abspath(file) or "?"
        args, varargs, varkw, locals = inspect.getargvalues(frame)
        # Basic frame information
        f = {"file": file, "func": func, "lnum": lnum}
        f["code"] = lines
        # FIXME: disable this for now until we understand why this goes into infinite loop
        if False:
            line_vars = cgitb.scanvars(
                lambda: linecache.getline(file, lnum), frame, locals
            )
            # Dump local variables (referenced in current line only)
            f["vars"] = {
                key: repr(value)
                for key, value in locals.items()
                if not key.startswith("__")
            }
        stackframes.append(f)

    return data


class SimpleErrorLogger:
    def log(self, app_name, snapshot):
        """logs the error"""
        logging.error("%s error:\n%s" % (app_name, snapshot["traceback"]))
        return None


class ErrorLogger:

    """
    To create your own custom logger for an app:

    class MyLogger:
        def log(app_name, error_snap_shop):
            ...
            return ticket_uuid

    error_logger.plugins['app_name'] = MyLogger()
    """

    def __init__(self):
        self.fallback_logger = SimpleErrorLogger()
        self.database_logger = None
        self.plugins = {}

    def initialize(self):
        """try inizalize database if we have service folder"""
        self.database_logger = safely(DatabaseErrorLogger, log=True)

    def _get_logger(self, app_name):
        """get the appropriate logger for the app"""
        return (
            self.plugins.get(app_name) or self.database_logger or self.fallback_logger
        )

    def log(self, app_name, error_snapshot):
        """log the error snapshot"""
        logger = self._get_logger(app_name)
        ticket_uuid = safely(lambda: logger.log(app_name, error_snapshot))
        if not ticket_uuid:
            self.fallback_logger.log(app_name, error_snapshot)
        return ticket_uuid


class DatabaseErrorLogger:
    def __init__(self):
        """creates the py4web_error table in the service database"""
        uri = os.environ["PY4WEB_SERVICE_DB_URI"]
        folder = os.environ["PY4WEB_SERVICE_FOLDER"]
        self.db = DAL(uri, folder=folder)
        self.db.define_table(
            "py4web_error",
            Field("uuid"),
            Field("app_name"),
            Field("method"),
            Field("path", "string"),
            Field("timestamp", "datetime"),
            Field("client_ip", "string"),
            Field("error", "string"),
            Field("snapshot", "json"),
        )
        self.db.commit()

    def log(self, app_name, error_snapshot):
        """store error snapshot (ticket) in the database"""
        # FIXME:
        # self.db._adapter.reconnect() ?
        ticket_uuid = str(uuid.uuid4())
        try:
            self.db.py4web_error.insert(
                uuid=ticket_uuid,
                app_name=app_name,
                method=request.method,
                path=request.path,
                timestamp=datetime.datetime.utcnow(),
                client_ip=request.environ.get("REMOTE_ADDR"),
                error=error_snapshot["exception_value"],
                snapshot=error_snapshot,
            )
            self.db.commit()
            return ticket_uuid
        except Exception as err:
            logging.error(str(err))
            self.db.rollback()
            return None

    def get(self, ticket_uuid=None):
        """retrieve a ticket from error database"""
        db = self.db
        if ticket_uuid:
            query, orderby = db.py4web_error.uuid == ticket_uuid, None
            rows = db(query).select(orderby=orderby, limitby=(0, 1)).as_list()
        else:
            orderby = ~db.py4web_error.timestamp
            groupby = db.py4web_error.path | db.py4web_error.error
            query = (
                db.py4web_error.timestamp
                > datetime.datetime.now() - datetime.timedelta(days=7)
            )
            fields = [field for field in db.py4web_error if not field.type == "json"]
            fields.append(db.py4web_error.id.count())
            list_rows = (
                db(query).select(*fields, orderby=orderby, groupby=groupby).as_list()
            )
            rows = []
            for item in list_rows:
                row = item["py4web_error"]
                row["count"] = item["_extra"][str(db.py4web_error.id.count())]
                rows.append(row)
        return rows if not ticket_uuid else rows[0] if rows else None

    def clear(self):
        """erase all tickets from database"""
        db = self.db
        db(db.py4web_error).delete()
        self.db.commit()


error_logger = ErrorLogger()
