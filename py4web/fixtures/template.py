import os

from omfitt import BaseFixture
import yatl

from ..core import Cache, URL, render


_HELPERS = {name: getattr(yatl.helpers, name) for name in yatl.helpers.__all__}


class Template(BaseFixture):

    cache = Cache(100)

    def __init__(self, filename, path=None, delimiters="[[ ]]"):
        self.filename = filename
        self.path = path
        self.delimiters = delimiters

    def on_output(self, app_ctx, route_ctx):
        output = route_ctx.output
        if not isinstance(output, dict):
            pass
        shared_data = route_ctx.shared_data
        path_join = os.path.join

        context = dict(
            _HELPERS,
            request=route_ctx.request,
            URL=URL
        )
        if shared_data:
            context.update(shared_data.get("template_context", {}))
        context.update(output)
        context["__vars__"] = output
        path = self.path
        if not path:
            path = path_join(
                path_join(os.environ["PY4WEB_APPS_FOLDER"], app_ctx['app_name']),
                "templates"
            )
        filename = path_join(path, self.filename)
        if not os.path.exists(filename):
            generic_filename = path_join(path, "generic.html")
            if os.path.exists(generic_filename):
                filename = generic_filename
        route_ctx.output = render(
            filename=filename, path=path, context=context, delimiters=self.delimiters
        )
