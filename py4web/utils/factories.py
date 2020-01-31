import os
from functools import wraps
from yatl.helpers import TAG
from py4web import action, URL, request


class ActionFactory:
    def __init__(self, *fixtures):
        self.fixtures = fixtures
    def get(self, template=None, requires_login=False):
        return self._action_maker('GET', template)
    def post(self, template=None, requires_login=False):
        return self._action_maker('POST', template)
    def put(self, template=None, requires_login=False):
        return self._action_maker('PUT', template, requires_login)
    def delete(self, template=None, requires_login=False):
        return self._action_maker('DELETE', template)
    def _action_maker(self, method, template):
        def make_action(func, method=method, template=template):
            path = func.__name__
            for name in func.__code__.co_varnames[:func.__code__.co_argcount]:
                path += '/<%s>' % name
            fixtures = [f for f in self.fixtures]
            if template is None:
                template = func.__name__ + '.html'
            if template:
                fixtures.append(template)
            new_func = action.uses(*fixtures)(func)
            action(path)(new_func)
            return func
        return make_action
         

class ButtonFactory:
    def __init__(self, *fixtures):
        self.fixtures = fixtures
    def __call__(self, text, path, func, _class=''):
        func = action.uses(*self.fixtures)(func)
        action(path, method=['GET','POST'])(func)
        def make_button(**d):
            url = path
            for key in d:
                url = url.replace('<%s>' % key, str(d[key]))
            onclick= 'axios.post("%s");this.classList.add("clicked")' % URL(url)
            return TAG.BUTTON(text, _class=_class, _onclick=onclick)
        return make_button
