import ombott
from ombott import SimpleConfig
from types import SimpleNamespace

ombott.DefaultConfig.max_memfile_size = 16 * 1024 * 1024

app = ombott.default_app()
app.setup()

request = app.request
response = app.response
static_file = ombott.static_file

request_hooks = SimpleNamespace(before=set())


def _before_request(*args, **kw):
    [h(*args, **kw) for h in request_hooks.before]


app.add_hook("before_request", _before_request)


@SimpleConfig.keys_holder
class DefaultConfig(SimpleConfig):
    apps_folder = 'apps'
    service_folder = ".service"
    service_db_uri = "sqlite://service.storage"
    password_file = 'password.txt'
    session_secret = None

    host = '127.0.0.1'
    port = 8000
    server = 'default'
    ssl_cert = None
    number_workers = 0

    dashboard_mode = 'full'
    watch = 'lazy'


# patched by install.py
current_config: DefaultConfig = SimpleNamespace()
