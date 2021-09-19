import ombott
import types

ombott.DefaultConfig.max_memfile_size = 16 * 1024 * 1024

static_file = ombott.static_file

app = ombott.default_app()
app.setup()

request = app.request
response = app.response


request_hooks = types.SimpleNamespace(before=set())


def _before_request(*args, **kw):
    [h(*args, **kw) for h in request_hooks.before]


app.add_hook("before_request", _before_request)
