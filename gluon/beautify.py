# FIX THIS

class BEAUTIFY(TAGGER):

    """
    Turns any list, dictionary, etc into decent looking html.

    Two special attributes are

    - sorted: a function that takes the dict and returned sorted keys
    - keyfilter: a function that takes a key and returns its representation or
      None if the key is to be skipped.
      By default key[:1]=='_' is skipped.

    Examples:

    >>> BEAUTIFY(['a', 'b', {'hello': 'world'}]).xml()
    '<div><table><tr><td><div>a</div></td></tr><tr><td><div>b</div></td></tr><tr><td><div><table><tr><td style="font-weight:bold;vertical-align:top;">hello</td><td style="vertical-align:top;">:</td><td><div>world</div></td></tr></table></div></td></tr></table></div>'

    """

    tag = 'div'

    @staticmethod
    def no_underscore(key):
        if key[:1] == '_':
            return None
        return key

    def __init__(self, component, **attributes):
        self.components = [component]
        self.attributes = attributes
        sorter = attributes.get('sorted', sorted)
        keyfilter = attributes.get('keyfilter', BEAUTIFY.no_underscore)
        components = []
        attributes = copy.copy(self.attributes)
        level = attributes['level'] = attributes.get('level', 6) - 1
        if '_class' in attributes:
            attributes['_class'] += 'i'
        if level == 0:
            return
        for c in self.components:
            if hasattr(c, 'value') and not callable(c.value):
                if c.value:
                    components.append(c.value)
            if hasattr(c, 'xml') and callable(c.xml):
                components.append(c)
                continue
            elif hasattr(c, 'keys') and callable(c.keys):
                rows = []
                try:
                    keys = (sorter and sorter(c)) or c
                    for key in keys:
                        if isinstance(key, (str, unicode)) and keyfilter:
                            filtered_key = keyfilter(key)
                        else:
                            filtered_key = str(key)
                        if filtered_key is None:
                            continue
                        value = c[key]
                        if isinstance(value, types.LambdaType):
                            continue
                        rows.append(
                            TR(
                                TD(filtered_key, _style='font-weight:bold;vertical-align:top;'),
                                TD(':', _style='vertical-align:top;'),
                                TD(BEAUTIFY(value, **attributes))))
                    components.append(TABLE(*rows, **attributes))
                    continue
                except:
                    pass
            if isinstance(c, str):
                components.append(str(c))
            elif isinstance(c, unicode):
                components.append(c.encode('utf8'))
            elif isinstance(c, (list, tuple)):
                items = [TR(TD(BEAUTIFY(item, **attributes)))
                         for item in c]
                components.append(TABLE(*items, **attributes))
            elif isinstance(c, cgi.FieldStorage):
                components.append('FieldStorage object')
            else:
                components.append(repr(c))
        self.components = components


class MENU(DIV):
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

    tag = 'ul'

    def __init__(self, data, **args):
        self.data = data
        self.attributes = args
        self.components = []
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
            if isinstance(item, LI):
                ul.append(item)
            else:
                (name, active, link) = item[:3]
                if isinstance(link, DIV):
                    li = LI(link)
                elif 'no_link_url' in self.attributes and self['no_link_url'] == link:
                    li = LI(DIV(name))
                elif isinstance(link, dict):
                    li = LI(A(name, **link))
                elif link:
                    li = LI(A(name, _href=link))
                elif not link and isinstance(name, A):
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
            if len(item) >= 3 and (not item[0]) or (isinstance(item[0], DIV) and not (item[2])):
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

 
