import urllib
import threading
from types import SimpleNamespace
from omfitt import BaseAppMethod

url_quote = urllib.parse.quote


class URL(BaseAppMethod):
    def setup(self):
        app = self._app
        ctx = app.ctx
        env_get = app.request.environ.get
        script_name = (
            env_get("SCRIPT_NAME", "")
            or env_get("HTTP_X_SCRIPT_NAME", "")
        ).rstrip("/")
        original_url = env_get("HTTP_ORIGIN") or app.request.url
        scheme, _, domain = original_url.split("/", 3)[:3]

        url_ctx = SimpleNamespace(
            script_name = script_name,
            domain_mapped = env_get("HTTP_X_PY4WEB_APPNAME"),
            static_version = ctx.static_version,
            scheme = scheme,
            domain = domain,
            app_name = ctx.app_name,
            base_url = ctx.base_url,
            static_url = ctx.static_url,
            named_routes = ctx.named_routes,
        )
        URLBuilder.setup(url_ctx)

    def __call__(
            self, *parts, vars=None, hash=None, scheme=False, signer=None,
            use_appname=None, static_version=None, use_signer=False
    ):
        super().__call__()
        return URLBuilder(
            *parts, vars=vars, hash=hash, scheme=scheme, signer=signer,
            use_appname=use_appname, static_version=static_version, use_signer=use_signer
        )


class URLBuilder:
    """
    Examples:
    URL('a','b',vars=dict(x=1),hash='y')       -> /{script_name?}/{app_name?}/a/b?x=1#y
    URL('a','b',vars=dict(x=1),scheme=None)    -> //{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme=True)    -> http://{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme='https') -> https://{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),use_appname=False) -> /{script_name?}/a/b?x=1
    URL(':home')  -> /{script_name?}/{app_name?}/path/to/home_route
    URL(':profile', dict(user='tom'))  -> /{script_name?}/{app_name?}/path/to/profile/tom
    """

    _local = threading.local()
    _local.ctx = None

    @classmethod
    def setup(cls, url_ctx: SimpleNamespace):
        cls._local.ctx = url_ctx

    __slots__ = (
        'parts', 'vars', 'hash', 'scheme', 'signer',
        'use_appname', 'static_version', 'app_name',
        'use_signer',
    )

    def __init__(
            self, *parts, vars=None, hash=None, scheme=False, signer=None,
            use_appname=None, static_version=None, use_signer=False
    ):

        self.parts = parts
        self.vars = vars
        self.hash = hash
        self.scheme = scheme
        self.signer = signer
        self.use_appname = use_appname
        self.static_version = static_version
        self.use_signer = use_signer

    def sign(self, signer=None):
        if signer is not None:
            self.signer = signer
        self.use_signer = True
        return self

    def to_str(self):
        return self.__str__()

    def __str__(self):
        ctx = self._local.ctx
        app_name = ''

        vars = self.vars
        hash = self.hash
        static_version = self.static_version
        use_appname = self.use_appname
        parts = self.parts
        scheme = self.scheme

        if use_appname is None:
            use_appname = not ctx.domain_mapped
            # force use_appname on domain-unmapped apps
            # use_appname = not env.get("HTTP_X_PY4WEB_APPNAME")
        if use_appname:
            # app_name is not set by py4web shell
            # app_name = getattr(request, "app_name", None)
            app_name = ctx.app_name
        has_appname = use_appname and app_name
        script_name = ctx.script_name
        broken_parts = []
        prefix = None
        if parts:
            len_parts = len(parts)
            idx = 0
            if str(parts[idx]).startswith(':'):
                route_name = parts[0][1:]
                route_args = []
                route_kw = {}
                idx += 1
                if idx < len_parts and isinstance(parts[idx], (list, tuple)):
                    route_args = parts[idx]
                    idx += 1
                if idx < len_parts and isinstance(parts[idx], dict):
                    route_kw = parts[idx]
                    idx += 1
                route_url = ctx.named_routes[route_name].url(*route_args, **route_kw)
                # remove app_name
                route_url = route_url.split('/', 1).pop()
                broken_parts = [route_url]
            else:
                [broken_parts.extend(str(part).rstrip("/").split("/")) for part in parts]
                is_static = broken_parts[0] == "static"
                if is_static:
                    if static_version != "":
                        if static_version is None:
                            static_version = ctx.static_version
                        if static_version:
                            broken_parts.insert(1, f"_{static_version}")
                    if ctx.static_url:
                        broken_parts.insert(0, ctx.static_url)
                    prefix = f"{script_name}/"
                else:
                    if broken_parts[0].startswith("/"):
                        prefix = ""
                    elif ctx.base_url:
                        broken_parts.insert(0, ctx.base_url)

        if prefix is None:
            if has_appname and app_name != "_default":
                prefix = f"{script_name}/{app_name}/"
            else:
                prefix = f"{script_name}/"

        url_buff = [prefix, "/".join(url_quote(p) for p in broken_parts)]
        # Signs the URL if required.  Copy vars into urlvars not to modify it.
        urlvars = dict(vars) if vars else {}
        if self.use_signer:
            # Note that we need to sign the non-urlencoded URL, since
            # at verification time, it will be already URLdecoded.
            self.signer.sign(prefix + "/".join(broken_parts), urlvars)
        if urlvars:
            url_buff.append("?" + "&".join(
                f"{k}={url_quote(str(v))}" for k, v in urlvars.items()
            ))
        if hash:
            url_buff.append(f"#{hash}")

        scheme_domain = ''
        if scheme is not False:
            if scheme is True:
                scheme = ctx.scheme
            elif scheme is None:
                scheme = ""
            else:
                scheme += ':'
            scheme_domain = f'{scheme}//{ctx.domain}'
        return f'{scheme_domain}{"".join(url_buff)}'

