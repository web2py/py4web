import urllib
import re

from gluon.helpers import *
from gluon.form import Form
from gluon.storage import Storage
from gluon.current import current
from gluon.url import URL

# TODO:
# handle dbio=False
# [x] request.env
# [x] request.ajax -> is_ajax
# SQLFORM, SQLFORM.factory, SQLFORM.widgets, SQLFORM.custom, SQLFORM.grid, SQLFORM.smartgrid
# FORM.process(), FORM.validate(), FORM.accepts()
# [x] MENU (needs testing)
# [x] auth.navbar()

class Env(object):
    def __init__(self, environ):
        self.environ = environ
    def __getattr__(self, key):
        return self.environ.get(key.upper()) or self.environ.get(key.lower())
    def __getitem__(self, key):
        return self.__getattr__(key)

def fix_request(request):
    request.cid = request.environ.get('HTTP_WEB2PY_COMPONENT_ELEMENT')
    request.is_shell = False
    request.is_scheduler = False
    request.ajax = request.is_ajax
    request.env = Env(request.environ)

def fix_response(response):
    response.meta = Storage()

def SQLFORM(
        self,
        table,
        record=None,
        deletable=False,
#        linkto=None,
#        upload=None,
        fields=None,
#        labels=None,
#        col3={},
#        submit_button='Submit',
#        delete_label='Check to delete',
#        showid=True,
        readonly=False,
#        comments=True,
#        keepopts=[],
#        ignore_rw=False,
        record_id=None,
#        formstyle=None,
#        buttons=['submit'],
#        separequest\n  File "/Users/massimodipierro/Dropbox/web3py/gluon/compatibility.py", line 85\n    crator=None,
#        extra_fields=None,
        **attr):
    if fields is not None:
        for field in table:
            field.writable = (field.name in fields)
    record = record or record_id
    form = Form(table, record, readonly=readonly, deletable=deletable)
    helper = form.helper()

    for key in attr:
        helper[key] = attr[key]

    helper.submitted = form.submitted
    helper.accepted = form.accepted
    helper.vars = form.vars
    helper.errors = form.errors
    helper.record = form.record

    def accepts(self, 
                request_vars=None, session=None, formname=None,
                keepvalues=False, onvalidation=None, hideerror=False):        
        # FIX THIS, formname cannot be set at this point!
        if formname is not None: raise NotImplementedError
        if keepvalues is not None: raise NotImplementedError
        if onvalidation is not None: raise NotImplementedError
        if hideerror is not False: raise NotImplementedError
        
        return self.accepted

    helper.accepts = accepts
    helper.validate = lambda self, **kwargs: self.accepts(**kwargs)
    helper.process = lambda self, **kwargs: self.accepts(**kwargs) and False or self

    return helper


class MENU(TAGGER):
    """
    Used to build menus

    Args:
        _class: defaults to 'web2py-menu web2py-menu-vertical'
        ul_class: defaults to 'web2py-menu-vertical'
        li_class: defaults to 'web2py-menu-expand'
        li_first: defaults to 'web2py-menu-first'
        li_last: defaults to 'web2py-menu-last'

    Use like::

        menu = MENU([['name', False, URL(...), [submenu]], ...])
        {{=menu}}

    """

    name = 'ul'

    def __init__(self, data, **args):
        self.data = data
        self.attributes = args
        self.children = []
        if not '_class' in self.attributes:
            self['_class'] = 'web2py-menu web2py-menu-vertical'
        if not 'ul_class' in self.attributes:
            self['ul_class'] = 'web2py-menu-vertical'
        if not 'li_class' in self.attributes:
            self['li_class'] = 'web2py-menu-expand'
        if not 'li_first' in self.attributes:
            self['li_first'] = 'web2py-menu-first'
        if not 'li_last' in self.attributes:
            self['li_last'] = 'web2py-menu-last'
        if not 'li_active' in self.attributes:
            self['li_active'] = 'web2py-menu-active'
        if not 'mobile' in self.attributes:
            self['mobile'] = False

    def serialize(self, data, level=0):
        if level == 0:
            ul = UL(**self.attributes)
        else:
            ul = UL(_class=self['ul_class'])
        for item in data:
            if isinstance(item, TAGGER) and item.name=='li':
                ul.append(item)
            else:
                (name, active, link) = item[:3]
                if isinstance(link, TAGGER):
                    li = LI(link)
                elif 'no_link_url' in self.attributes and self['no_link_url'] == link:
                    li = LI(DIV(name))
                elif isinstance(link, dict):
                    li = LI(A(name, **link))
                elif link:
                    li = LI(A(name, _href=link))
                elif not link and isinstance(name, TAGGER) and name.name=='a':
                    li = LI(name)
                else:
                    li = LI(A(name, _href='#',
                              _onclick='javascript:void(0);return false;'))
                if level == 0 and item == data[0]:
                    li['_class'] = self['li_first']
                elif level == 0 and item == data[-1]:
                    li['_class'] = self['li_last']
                if len(item) > 3 and item[3]:
                    li['_class'] = self['li_class']
                    li.append(self.serialize(item[3], level + 1))
                if active or ('active_url' in self.attributes and self['active_url'] == link):
                    if li['_class']:
                        li['_class'] = li['_class'] + ' ' + self['li_active']
                    else:
                        li['_class'] = self['li_active']
                if len(item) <= 4 or item[4] == True:
                    ul.append(li)
        return ul

    def serialize_mobile(self, data, select=None, prefix=''):
        if not select:
            select = SELECT(**self.attributes)
        custom_items = []
        for item in data:
            # Custom item aren't serialized as mobile
            if len(item) >= 3 and (not item[0]) or (isinstance(item[0], TAGGER) and not (item[2])):
                # ex: ('', False, A('title', _href=URL(...), _title="title"))
                # ex: (A('title', _href=URL(...), _title="title"), False, None)
                custom_items.append(item)
            elif len(item) <= 4 or item[4] == True:
                select.append(OPTION(CAT(prefix, item[0]),
                                     _value=item[2], _selected=item[1]))
                if len(item) > 3 and len(item[3]):
                    self.serialize_mobile(
                        item[3], select, prefix=CAT(prefix, item[0], '/'))
        select['_onchange'] = 'window.location=this.value'
        # avoid to wrap the select if no custom items are present
        html = DIV(select,  self.serialize(custom_items)) if len(custom_items) else select
        return html

    def xml(self):
        if self['mobile']:
            return self.serialize_mobile(self.data, 0).xml()
        else:
            return self.serialize(self.data, 0).xml()


def fix_auth(auth):

    DEFAULT = lambda:0

    def navbar(self, prefix='Welcome', action=None,
               separators=(' [ ', ' | ', ' ] '), user_identifier=DEFAULT,
               referrer_actions=DEFAULT, mode='default'):
        """ Navbar with support for more templates
        This uses some code from the old navbar.

        Args:
            mode: see options for list of

        """
        items = []  # Hold all menu items in a list
        self.bar = ''  # The final
        T = current.T
        referrer_actions = [] if not referrer_actions else referrer_actions
        if not action:
            action = self.url(self.settings.function)

        request = current.request
        if URL() == action:
            next = ''
        else:
            next = '?_next=' + urllib.quote(URL(args=request.args,
                                                vars=request.get_vars))
        href = lambda function: '%s/%s%s' % (action, function, next
                                             if referrer_actions is DEFAULT
                                             or function in referrer_actions
                                             else '')
        if isinstance(prefix, str):
            prefix = T(prefix)
        if prefix:
            prefix = prefix.strip() + ' '

        def Anr(*a, **b):
            b['_rel'] = 'nofollow'
            return A(*a, **b)

        if self.user_id:  # User is logged in
            logout_next = self.settings.logout_next
            items.append({'name': T('Log Out'),
                          'href': '%s/logout?_next=%s' % (action,
                                                          urllib.quote(
                                                          logout_next)),
                          'icon': 'icon-off'})
            if 'profile' not in self.settings.actions_disabled:
                items.append({'name': T('Profile'), 'href': href('profile'),
                              'icon': 'icon-user'})
            if 'change_password' not in self.settings.actions_disabled:
                items.append({'name': T('Password'),
                              'href': href('change_password'),
                              'icon': 'icon-lock'})

            if user_identifier is DEFAULT:
                user_identifier = '%(first_name)s'
            if callable(user_identifier):
                user_identifier = user_identifier(self.user)
            elif ((isinstance(user_identifier, str) or
                  type(user_identifier).__name__ == 'lazyT') and
                  re.search(r'%\(.+\)s', user_identifier)):
                user_identifier = user_identifier % self.user
            if not user_identifier:
                user_identifier = ''
        else:  # User is not logged in
            items.append({'name': T('Log In'), 'href': href('login'),
                          'icon': 'icon-off'})
            if 'register' not in self.settings.actions_disabled:
                items.append({'name': T('Sign Up'), 'href': href('register'),
                              'icon': 'icon-user'})
            if 'request_reset_password' not in self.settings.actions_disabled:
                items.append({'name': T('Lost password?'),
                              'href': href('request_reset_password'),
                              'icon': 'icon-lock'})
            if (self.settings.use_username and not
                    'retrieve_username' in self.settings.actions_disabled):
                items.append({'name': T('Forgot username?'),
                             'href': href('retrieve_username'),
                             'icon': 'icon-edit'})

        def menu():  # For inclusion in MENU
            self.bar = [(items[0]['name'], False, items[0]['href'], [])]
            del items[0]
            for item in items:
                self.bar[0][3].append((item['name'], False, item['href']))

        def bootstrap3():  # Default web2py scaffolding
            def rename(icon): return icon+' '+icon.replace('icon', 'glyphicon')
            self.bar = UL(LI(Anr(I(_class=rename('icon '+items[0]['icon'])),
                                 ' ' + items[0]['name'],
                                 _href=items[0]['href'])), _class='dropdown-menu')
            del items[0]
            for item in items:
                self.bar.insert(-1, LI(Anr(I(_class=rename('icon '+item['icon'])),
                                           ' ' + item['name'],
                                           _href=item['href'])))
            self.bar.insert(-1, LI('', _class='divider'))
            if self.user_id:
                self.bar = LI(Anr(prefix, user_identifier,
                                  _href='#', _class="dropdown-toggle",
                                  data={'toggle': 'dropdown'}),
                              self.bar, _class='dropdown')
            else:
                self.bar = LI(Anr(T('Log In'),
                                  _href='#', _class="dropdown-toggle",
                                  data={'toggle': 'dropdown'}), self.bar,
                              _class='dropdown')

        def bare():
            """ In order to do advanced customization we only need the
            prefix, the user_identifier and the href attribute of items

            Examples:
                Use as::

                # in module custom_layout.py
                from gluon import *
                def navbar(auth_navbar):
                    bar = auth_navbar
                    user = bar["user"]

                    if not user:
                        btn_login = A(current.T("Login"),
                                      _href=bar["login"],
                                      _class="btn btn-success",
                                      _rel="nofollow")
                        btn_register = A(current.T("Sign up"),
                                         _href=bar["register"],
                                         _class="btn btn-primary",
                                         _rel="nofollow")
                        return DIV(btn_register, btn_login, _class="btn-group")
                    else:
                        toggletext = "%s back %s" % (bar["prefix"], user)
                        toggle = A(toggletext,
                                   _href="#",
                                   _class="dropdown-toggle",
                                   _rel="nofollow",
                                   **{"_data-toggle": "dropdown"})
                        li_profile = LI(A(I(_class="icon-user"), ' ',
                                          current.T("Account details"),
                                          _href=bar["profile"], _rel="nofollow"))
                        li_custom = LI(A(I(_class="icon-book"), ' ',
                                         current.T("My Agenda"),
                                         _href="#", rel="nofollow"))
                        li_logout = LI(A(I(_class="icon-off"), ' ',
                                         current.T("logout"),
                                         _href=bar["logout"], _rel="nofollow"))
                        dropdown = UL(li_profile,
                                      li_custom,
                                      LI('', _class="divider"),
                                      li_logout,
                                      _class="dropdown-menu", _role="menu")

                        return LI(toggle, dropdown, _class="dropdown")

                # in models db.py
                import custom_layout as custom

                # in layout.html
                <ul id="navbar" class="nav pull-right">
                    {{='auth' in globals() and \
                      custom.navbar(auth.navbar(mode='bare')) or ''}}</ul>

            """
            bare = {'prefix': prefix, 'user': user_identifier if self.user_id else None}

            for i in items:
                if i['name'] == T('Log In'):
                    k = 'login'
                elif i['name'] == T('Sign Up'):
                    k = 'register'
                elif i['name'] == T('Lost password?'):
                    k = 'request_reset_password'
                elif i['name'] == T('Forgot username?'):
                    k = 'retrieve_username'
                elif i['name'] == T('Log Out'):
                    k = 'logout'
                elif i['name'] == T('Profile'):
                    k = 'profile'
                elif i['name'] == T('Password'):
                    k = 'change_password'

                bare[k] = i['href']

            self.bar = bare

        options = {'asmenu': menu,
                   'dropdown': bootstrap3,
                   'bare': bare
                   }  # Define custom modes.

        if mode in options and callable(options[mode]):
            options[mode]()
        else:
            s1, s2, s3 = separators
            if self.user_id:
                self.bar = SPAN(prefix, user_identifier, s1,
                                Anr(items[0]['name'],
                                _href=items[0]['href']), s3,
                                _class='auth_navbar')
            else:
                self.bar = SPAN(s1, Anr(items[0]['name'],
                                _href=items[0]['href']), s3,
                                _class='auth_navbar')
            for item in items[1:]:
                self.bar.insert(-1, s2)
                self.bar.insert(-1, Anr(item['name'], _href=item['href']))

        return self.bar
    auth.navbar = navbar
    auth.wikimenu = lambda self:None

B = STRONG
I = EM
