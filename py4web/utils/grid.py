import math
import urllib.parse

from pydal.restapi import RestAPI, Policy
from yatl.helpers import TABLE, TR, TH, TD, DIV, A, I, SPAN, INPUT, SCRIPT, UL, LI

from py4web import request, HTTP
from py4web.utils.form import Form


def safeint(s):
    if s is None:
        return s
    try:
        return int(s)
    except ValueError:
        return None


class Grid:

    """
    Example:

    @unauthenticated()
    def index():
       grid = Grid(db.thing, query=None, create=True, editable=True, deletable=True)
       grid.labels = {key: key.title() for key in db.thing.fields}
       grid.renderers['name'] = lambda name: SPAN(name, _class='name')
       return dict(form=grid.make())
    """

    def __init__(
        self,
        table,
        query=None,
        fields=None,
        limit=100,
        create=True,
        editable=True,
        deletable=True,
    ):
        self.db = table._db
        self.table = table
        self.query = query
        self.fields = fields or [f.name for f in table if f.readable]
        self.limit = limit
        self.create = create
        self.editable = editable
        self.deletable = deletable
        self.policy = Policy()
        self.policy.set(
            table._tablename,
            "GET",
            query=query,
            authorize=True,
            allowed_patterns=["*"],
            fields=fields,
            limit=limit,
        )
        self.restapi = RestAPI(self.db, self.policy)
        self.labels = {}
        self.renderers = {"id": self.idlink}
        self.form_attributes = {}
        self.T = lambda value: value
        self.denormalize = {}

    def make(self):
        """makes the grid, must be called inside an action"""

        T, db, table, query = self.T, self.db, self.table, self.query
        # bypass rest API if it is a form
        id = safeint(request.query.get("id") or request.forms.get("id"))
        if id is not None:
            if (id == 0 and not self.create) or (id > 0 and not self.editable):
                raise HTTP(404)
            record = db(query)(table.id == id).select().first() if id else None
            form = Form(table, record, deletable=self.deletable, **self.form_attributes)
            form.action = (
                request.url.split("?")[0] + "?" + urllib.parse.urlencode(request.query)
            )
            del request.query["id"]
            if form.deleted:
                message = T("Record deleted")
            elif form.accepted:
                message = T("Record created") if not id else T("Record Saved")
            else:
                return DIV(self.header(id), form, _class="py4web-grid")
        else:
            message = ""

        if self.denormalize:
            lookup = []
            for k, fs in self.denormalize.items():
                lookup.append('%s!:%s[%s]' % (k, k, ','.join(fs)))
            request.query['@lookup'] = ','.join(lookup)

        id = None
        data = self.restapi("GET", self.table._tablename, None, request.query)
        items = data.get("items", [])
        count = data.get("count") or self.db(self.query or table.id > 0).count()
        table = TABLE(_class="table")
        fields = items[0].keys() if items else self.fields
        table.append(TR(*[TH(self.sortlink(key)) for key in fields]))
        table.append(TR(*[TH(self.filterlink(key)) for key in fields]))
        for item in items:
            table.append(
                TR(*[TD(self.render(key, value)) for key, value in item.items()])
            )
        header = self.header(id, message)
        footer = self.footer(
            count, safeint(request.query.get("@offset", 0)), len(items)
        )
        return DIV(header, table, footer, _class="py4web-grid")

    def render(self, key, value):
        """renders a value"""
        if key in self.renderers:
            return self.renderers[key](value)
        if isinstance(value, list):
            return UL(*[LI(self.render(key, item)) for item in value])
        if isinstance(value, dict):
            return TABLE(
                *[
                    TR(TH(k, ":"), TD(self.render(key + "." + k, v)))
                    for k, v in value.items()
                ]
            )
        return value

    def idlink(self, id):
        """returns the link to edit an id"""
        query = dict(request.query)
        query["id"] = id
        url = request.url.split("?")[0] + "?" + urllib.parse.urlencode(query)
        return A(id, _class="button", _href=url)

    def is_simple_field(self, key):
        FIELD_TYPES = [
            "string",
            "integer",
            "float",
            "bool",
            "decimal",
            "time",
            "date",
            "datetime",
        ]
        return key in self.table.fields and self.table[key].type in FIELD_TYPES

    def sortlink(self, key):
        """returns the link to sort by key"""
        label = self.labels.get(key, key)
        if not self.is_simple_field(key):
            return label
        order = request.query.get("@order")
        if order == key:
            new_order, caret = "~" + key, "▼"
        elif order == "~" + key:
            new_order, caret = key, "▲"
        else:
            new_order, caret = key, ""
        return A(label + caret, _href=self.url(page=0, order=new_order))

    def filterlink(self, key):
        """creates an input to filter by key"""
        if not self.is_simple_field(key):
            return ""
        return INPUT(_id="py4web-grid-filter-" + key, _class="py4web-grid-filter")

    def url(self, page, order=None):
        """generates a url for a page and a sorting"""
        query = dict(request.query)
        query["@offset"] = page * self.limit
        if order:
            query["@order"] = order
        return request.url.split("?")[0] + "?" + urllib.parse.urlencode(query)

    def header(self, id, message=""):
        """generates the header"""
        T = self.T
        div = DIV(_class="py4web-grid-header")
        if message:
            div.append(DIV(message, _class="py4web-grid-message"))
        if self.create and id is None:
            div.append(
                A(
                    T("Create Record"),
                    _class="button",
                    _href=request.url.split("?")[0] + "?id=0",
                )
            )
        elif (self.create and id is 0) or (self.editable and id and id > 0):
            query = dict(request.query)
            query.pop("id", None)
            url = request.url.split("?")[0] + "?" + urllib.parse.urlencode(query)
            div.append(A(T("Back"), _class="button", _href=url))
            div.append(T("New Record") if id is 0 else T("Edit Record"))
        return div

    def footer(self, count, offset, len_items):
        """generates the footer"""
        T = self.T
        page = int(offset / self.limit)
        last_page = math.floor(count / self.limit)
        return DIV(
            A("First", _href=self.url(0), _class="button") if page > 1 else "",
            A("Previous", _href=self.url(page - 1), _class="button")
            if page > 0
            else "",
            SPAN(
                T("page %s/%s (%s/%s records)")
                % (page + 1, last_page + 1, len_items, count)
            ),
            A("Next", _href=self.url(page + 1), _class="button")
            if page < last_page
            else "",
            A("Last", _href=self.url(last_page - 1), _class="button")
            if page < last_page - 1
            else "",
            SCRIPT(Grid.script),
            _class="py4web-grid-footer",
        )

    script = r"""
    var filters = document.getElementsByClassName('py4web-grid-filter');
    var url = window.location.href;
    for (var i=0;i<filters.length;i++) {
       var name = filters[i].id.substr("py4web-grid-filter-".length);
       var matches = url.match(new RegExp("\\b" + name + "\\.\\w+=[^&]+", "gi"));
       if (matches && matches.length>0) {
          var parts = matches[0].split('=');
          console.log(parts[0].split('.')[1]);
          var op = {'lt':'<', 'le':'<=', 'eq':'', 'ge':'>=', 'gt':'>', 'ne':'!='}[parts[0].split('.')[1]]||'';
          filters[i].value = op + decodeURIComponent(parts[1]);
       }
       filters[i].onkeyup = (function(elem, name){return function(event){ 
         if(event.keyCode==13) {
           var value;
           var url = window.location.href;
           url = url.replace(new RegExp("\\b@offset=[^&]+", "gi"), "");
           url = url.replace(new RegExp("\\b" + name + "\\.\\w+=[^&]+", "gi"), "");
           if(elem.value.substr(0,2) == '!=') {op='ne'; value=elem.value.substr(2);}
           else if(elem.value.substr(0,2) == '<=') {op='le'; value=elem.value.substr(2);}
           else if(elem.value.substr(0,2) == '>=') {op='ge'; value=elem.value.substr(2);}
           else if(elem.value.substr(0,1) == '<') {op='lt'; value=elem.value.substr(1);}
           else if(elem.value.substr(0,1) == '>') {op='gt'; value=elem.value.substr(1);}
           else {op='eq'; value=elem.value;}
           if (value!=="") {
              if(value=='""') value='';
              var sep = (url.indexOf('?')>0)?"&":"?";
              url = url + sep + name+'.' + op + '=' +encodeURIComponent(value);
           }
           url = url.replace(/[&?]$/, '').replace(/[&]+/, '&').replace(/[?][&]/, '?');
           window.location = url;
         }
       };})(filters[i], name);
    }
    """
