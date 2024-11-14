import copy
import json

import jwt
from yatl.helpers import TAG

from py4web import URL, action, request
from py4web.core import Fixture, Session


class Inject(Fixture):
    def __init__(self, **variables):
        self.variables = variables

    def on_success(self, context):
        output = context["output"]
        if isinstance(output, dict):
            output.update(**self.variables)


class ActionFactory:
    def __init__(self, *fixtures):
        self.fixtures = fixtures

    def get(self, path=None, template=None, uses=None):
        return self._action_maker("GET", path, template, uses)

    def post(self, path=None, template=None, uses=None):
        return self._action_maker("POST", path, template, uses)

    def put(self, path=None, template=None, uses=None):
        return self._action_maker("PUT", path, template, uses)

    def delete(self, path=None, template=None, uses=None):
        return self._action_maker("DELETE", path, template, uses)

    def head(self, path=None, template=None, uses=None):
        return self._action_maker("HEAD", path, template, uses)

    def __call__(
        self,
        path=None,
        template=None,
        method=["GET", "POST", "PUT", "HEAD", "DELETE"],
        uses=None
    ):
        return self._action_maker(method, path, template, uses)

    def _action_maker(self, method, path, template, uses):
        uses = uses or [] # handle uses=None
        def make_action(func, path=path, method=method, template=template):
            if not path:
                path = func.__name__
                for name in func.__code__.co_varnames[: func.__code__.co_argcount]:
                    path += "/<%s>" % name
            fixtures = [*self.fixtures, *uses]
            if template is None:
                template = func.__name__ + ".html"
            if template:
                fixtures.insert(0, template)
            new_func = action.uses(*fixtures)(func)
            action(path, method=method)(new_func)
            return func

        return make_action

    def callback(self, path=None, uses=None):
        uses = uses or [] # handle uses=None
        return CallbackFactory(path, [*self.fixtures, *uses])


class CallbackFactory:
    def __init__(self, path, fixtures):
        self.path = path
        self.fixtures = fixtures

    def __call__(self, func):
        path = self.path or func.__name__

        @action(path, method="POST")
        @action.uses(*self.fixtures)
        def tmp(func=func):
            data = jwt.decode(
                json.loads(request.body.read()), Session.SECRET, algorithms=["HS256"]
            )
            return func(**data)

        def get_link(**data):
            return (URL(path), jwt.encode(data, Session.SECRET))

        def button(*components, **attributes):
            def button_maker(**data):
                onclick = (
                    'Q.ajax("POST", "%s", "%s").then(function(res){if(res.data)Q.eval(res.data);});this.classList.add("clicked")'
                    % get_link(**data)
                )
                new_attributes = copy.copy(attributes)
                new_attributes["_onclick"] = onclick
                return TAG.BUTTON(*components, **new_attributes)

            return button_maker

        func.get_link = get_link
        func.button = button
        return func
