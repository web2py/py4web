import os
from functools import wraps
from yatl.helpers import TAG
from py4web import action, URL, request
from py4web.core import dumps


class ActionFactory:

    def __init__(self, *fixtures):
        self.fixtures = fixtures

    def get(self, path=None, template=None):
        return self._action_maker('GET', path, template)

    def post(self, path=None, template=None):
        return self._action_maker('POST', path, template)

    def put(self, path=None, template=None):
        return self._action_maker('PUT', template, requires_login)

    def delete(self, path=None, template=None):
        return self._action_maker('DELETE', path, template)

    def head(self, path=None, template=None):
        return self._action_maker('HEAD', path, template)

    def __call__(self, path=None, template=None):
        return self._action_maker(['GET','POST','PUT','DELETE'], path, template)

    def _action_maker(self, method, path, template):
        def make_action(func, path=path, method=method, template=template):
            if not path:
                path = func.__name__
                for name in func.__code__.co_varnames[:func.__code__.co_argcount]:
                    path += '/<%s>' % name
            fixtures = [f for f in self.fixtures]
            if template is None:
                template = func.__name__ + '.html'
            if template:
                fixtures.append(template)
            new_func = action.uses(*fixtures)(func)
            action(path, method=method)(new_func)
            return func
        return make_action

    def button(self, text, path=None, _class=''):
        return ButtonFactory(text, path, _class, self.fixtures)


class ButtonFactory:

    def __init__(self, text, path, _class, fixtures):
        self.text = text
        self.path = path
        self._class = _class
        self.fixtures = fixtures

    def __call__(self, func):
        path = self.path or  func.__name__
        @action(path, method='POST')
        @action.uses(*self.fixtures)
        def tmp(func=func):
            return func(**request.json)
        def make_button(**data):        
            url = URL(path)
            onclick= 'axios.post("%s", %s);this.classList.add("clicked")' % (url, dumps(data))
            return TAG.BUTTON(self.text, _class=self._class, _onclick=onclick)
        make_button.call = func
        return make_button
