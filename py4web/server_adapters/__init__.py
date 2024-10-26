__all__ = ["available", "unavailable", "blocking"]

unavailable = []
available = {}
blocking = {}

# Web servers supported natively by ombott

available["wsgiref"] = "wsgiref"
blocking["wsgiref"] = True

try:
    import tornado

    available["tornado"] = "tornado"
    blocking["tornado"] = False
except ModuleNotFoundError:
    unavailable.append("tornado")


try:
    import waitress

    available["waitress"] = "waitress"
    blocking["waitress"] = True
except ModuleNotFoundError:
    unavailable.append("waitress")

try:
    import gunicorn

    available["gunicorn"] = "gunicorn"
    blocking["gunicorn"] = False
except ModuleNotFoundError:
    unavailable.append("gunicorn")

# additional custom adaptrs

try:
    from .adapter_wsgiref import WSGIRefAdapter

    available["wsgiref+threaded"] = WSGIRefAdapter
    blocking["wsgiref+threaded"] = True
except ModuleNotFoundError:
    unavailable.append("wsgiref+threaded")

try:
    from .adapter_rocket3 import Rocket3Adapter

    available["rocket"] = Rocket3Adapter
    blocking["rocket"] = True
except ModuleNotFoundError:
    unavailable.append("rocket")

try:
    from .adapter_gevent import GeventAdapter

    available["gevent"] = GeventAdapter
    blocking["gevent"] = False
except ModuleNotFoundError:
    unavailable.append("gevent")

try:
    from .adapter_gunicorn_gevent import GunicornGeventAdapter

    available["gunicorn+gevent"] = GunicornGeventAdapter
    blocking["gunicorn+gevent"] = False
except ModuleNotFoundError:
    unavailable.append("gunicorn+gevent")

try:
    from .adapter_gevent_websockets import GeventWebsocketsAdapter

    available["gevent+websockets"] = GeventWebsocketsAdapter
    blocking["gevent+websockets"] = False

except ModuleNotFoundError:
    unavailable.append("gevent+websockets")
