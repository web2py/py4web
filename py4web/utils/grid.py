from functools import reduce

from yatl.helpers import DIV, TABLE, TBODY, TR, TD, TH, A, SPAN, I, THEAD, P, TAG, INPUT, XML
from pydal.objects import Field, FieldVirtual
from py4web import request, URL, response, redirect
from py4web.utils.form import Form, FormStyleDefault
from py4web.utils.param import Param
import uuid
import json

NAV = TAG.nav
HEADER = TAG.header


def get_storage_key():
    """
    if "storage_key" specified in the query_parms, retrieve it and use that storage_key.  else,
    create a new one

    :return: user storage_key uuid
    """
    return request.query.get("storage_key", uuid.uuid4())


def get_storage_value(storage_key, filter_name, secret, default_value=None):
    """
    retrieve a value from storage

    first check the query parms to see if one is passed

    if not in query parms check the user storage_key cookie for the value

    :param storage_key: user storage_key
    :param filter_name: name of the filter value you want to retrieve
    :secret: secret that will be used to encrypt the cookie
    :param default_value: the default value if value hasn't been stored
    :return: the value of the filter that was either in the query parms or user storage_key cookie
    """
    storage_value = request.query.get(filter_name, default_value)
    if not storage_value or (storage_value == default_value and storage_key and storage_key in request.cookies):
        json_cookie = request.get_cookie(storage_key,
                                         default=None,
                                         secret=secret)
        if json_cookie:
            cookie = json.loads(json_cookie)
        else:
            cookie = dict()

        storage_value = cookie.get(filter_name, default_value)

    return storage_value


def set_storage_values(storage_key, values_dict, secret, token_longevity=3600):
    response.set_cookie(str(storage_key),
                        json.dumps(values_dict),
                        secret=secret,
                        max_age=token_longevity)


def get_common_setting(setting, common_settings, default_value=None):
    try:
        return common_settings[setting]
    except AttributeError:
        return default_value


def parse_route(request):
    """
    -- play with this as a possible way to get the route - but below works

    f = '/'.join(__file__.split('/')[1:])
    for rt in (Reloader.ROUTES):
        if rt['filename'] == f:
            print(rt)
    print(f)
    """
    application = request.environ["bottle.request.ext.app_name"]
    url_parts = request.path.split("/")

    rule_out = ""
    slash = ""
    for part in url_parts:
        if part in ['new', 'details', 'edit', 'delete']:
            break
        elif part == "":
            continue
        elif part == application:
            continue
        else:
            rule_out += "%s%s" % (slash, part)
            slash = "/"

    return rule_out


class Grid:
    def __init__(self,
                 common_settings,
                 queries,
                 search_form=None,
                 search_queries=None,
                 storage_values=None,
                 fields=None,
                 show_id=False,
                 orderby=None,
                 left=None,
                 headings=None,
                 create=True,
                 details=True,
                 editable=True,
                 deletable=True,
                 requires=None,
                 storage_key=None,
                 pre_action_buttons=None,
                 post_action_buttons=None,
                 auto_generate=True):
        """
        Grid is a searchable/sortable/pageable grid

        :param common_settings: Params object with common settings for all grids within the application
        :param queries: list of queries used to filter the data
        :param search_form: py4web FORM to be included as the search form
        :param search_queries: future use - pass a dict of name and a search query
        :param storage_values: values to save between requests
        :param fields: list of fields to display on the list page, if blank, glean tablename from first query
        :              and use all fields of that table
        :param show_id: show the record id field on list page - default = False
        :param orderby: pydal orderby field or list of fields
        :param left: if joining other tables, specify the pydal left expression here
        :param headings: list of headings to be used for list page - if not provided use the field label
        :param create: URL to redirect to for creating records - set to False to not display the button
        :param editable: URL to redirect to for editing records - set to False to not display the button
        :param deletable: URL to redirect to for deleting records - set to False to not display the button
        :param requires: dict of fields and their 'requires' parm for building edit pages - dict key should be
                         tablename.fieldname
        :param storage_key: id of the cookie containing saved values
        :param pre_action_buttons: list of action_button instances to include before the standard action buttons
        :param post_action_buttons: list of action_button instances to include after the standard action buttons
        :param auto_generate: True/False - automatically process the sql for the form - if False, user is
                              responsible for calling generate().
        """
        self.db = common_settings.param.db
        self.secret = common_settings.param.secret

        self.param = Param(token_longevity=common_settings.param.token_longevity,
                           rows_per_page=common_settings.param.rows_per_page,
                           include_action_button_text=common_settings.param.include_action_button_text,
                           search_button_text=common_settings.param.search_button_text,
                           formstyle=common_settings.param.formstyle,
                           grid_class_style=common_settings.param.grid_class_style,
                           mobile_columns=common_settings.param.mobile_columns,
                           queries=queries,
                           fields=fields,
                           show_id=show_id,
                           orderby=orderby,
                           left=left,
                           requires=requires,
                           search_form=search_form,
                           search_queries=search_queries,
                           storage_values=storage_values if storage_values else dict(),
                           storage_key=storage_key,
                           headings=headings,
                           create=create,
                           details=details,
                           editable=editable,
                           deletable=deletable,
                           pre_action_buttons=pre_action_buttons,
                           post_action_buttons=post_action_buttons)

        #  instance variables that will be computed
        self.action = None
        self.current_page_number = None
        self.endpoint = parse_route(request)
        self.hidden_fields = None
        self.form = None
        self.number_of_pages = None
        self.page_end = None
        self.page_start = None
        self.query_parms = request.params
        self.readonly_fields = None
        self.record_id = None
        self.rows = None
        self.tablename = None
        self.total_number_of_rows = None
        self.use_tablename = False

        if auto_generate:
            self.generate()

    def generate(self):
        if not self.param.search_form and self.param.search_queries:
            if not self.param.storage_key:
                self.param.storage_key = get_storage_key()

            field_names = ['sq_' + field[0].replace(' ', '_').lower() for field in self.param.search_queries]
            field_values = dict()
            for field in field_names:
                field_values[field] = get_storage_value(self.param.storage_key, field, secret=self.secret)

            form_fields = []
            for field in field_names:
                label = field.replace('sq_', '').replace('_', ' ').title()
                placeholder = field.replace('sq_', '').replace('_', ' ').capitalize()
                form_fields.append(Field(field,
                                         length=50,
                                         default=field_values[field] if field in field_values else None,
                                         _placeholder=placeholder,
                                         label=label,
                                         _title=placeholder))

            search_form = Form(form_fields,
                               keep_values=True,
                               formstyle=self.param.formstyle)

            self.param.search_form = search_form

            if self.param.search_form.accepted:
                for field in field_names:
                    field_values[field] = self.param.search_form.vars[field]

            for field in field_names:
                self.param.storage_values[field] = field_values[field] if field in field_values else None

            if not self.param.queries:
                self.param.queries = []
            for sq in self.param.search_queries:
                field_name = 'sq_' + sq[0].replace(' ', '_').lower()
                if field_name in field_values and field_values[field_name]:
                    self.param.queries.append(sq[1](field_values[field_name]))

        query = reduce(lambda a, b: (a & b), self.param.queries)

        if self.param.fields:
            if not isinstance(self.param.fields, list):
                self.param.fields = [self.param.fields]
        else:
            q = query
            while q.second != 0:
                q = q.first

            self.param.fields = [self.db[q.first.table][x] for x in q.first.table.fields()]

        self.hidden_fields = [field for field in self.param.fields if not field.readable]

        if "action" in request.url_args:
            self.action = request.url_args["action"]
            self.tablename = request.url_args["tablename"]
            self.record_id = request.url_args["record_id"]
            self.readonly_fields = [field for field in self.param.fields if not field.writable]
            if request.url_args["action"] in ["new", "details", "edit"]:
                readonly = True if request.url_args["action"] == "details" else False
                for field in self.readonly_fields:
                    self.db[field.tablename][field.name].writable = False

                for field in self.hidden_fields:
                    self.db[field.tablename][field.name].readable = False
                    self.db[field.tablename][field.name].writable = False

                if self.param.requires:
                    for field in self.param.requires:
                        tablename, fieldname = field.split(".")
                        self.db[tablename][fieldname].requires = self.param.requires[field]

                if not self.param.show_id:
                    #  if not show id, find the "id" field and set readable/writable to False
                    for field in self.db[self.tablename]:
                        if field.type == "id":
                            self.db[self.tablename][field.name].readable = False
                            self.db[self.tablename][field.name].writable = False

                self.form = Form(self.db[self.tablename], record=self.record_id, readonly=readonly,
                                 formstyle=self.param.formstyle)
                if self.form.accepted:
                    page = request.query.get("page", 1)
                    redirect(URL(self.endpoint, vars=dict(storage_key=request.query.get("storage_key"),
                                                          page=page)))

            if request.url_args["action"] == "delete":
                self.db(self.db[self.tablename].id == self.record_id).delete()
                redirect(URL(self.endpoint, vars=dict(storage_key=request.query.get("storage_key"))))

        else:
            self.action = "select"

            for field in self.param.fields:
                if not isinstance(field, FieldVirtual):
                    if not self.tablename:
                        self.tablename = field.table
                    if field.table != self.tablename:
                        self.use_tablename = True  # tablename is included in "row" - need it to retrieve fields

            #  find the primary key of the primary table
            pt = self.db[self.tablename]
            key_is_missing = False
            for field in self.param.fields:
                if field.table._tablename == pt._tablename and field.name == pt._id:
                    key_is_missing = True
            if key_is_missing:
                #  primary key wasn't included, add it and set show_id to False so it doesn't display
                self.param.fields.append(pt._id)
                self.param.show_id = False

            if not isinstance(self.param.headings, list):
                self.param.headings = [self.param.headings]

            sig_page_number = json.loads(request.query.get(self.param.storage_key, "{}")).get("page", 1)
            current_page_number = request.query.get("page", sig_page_number)
            self.current_page_number = current_page_number if isinstance(current_page_number, int) \
                else int(current_page_number)

            parms = dict()
            #  try getting sort order from the request
            sort_order = request.query.get("sort")
            if not sort_order:
                #  see if there is a stored orderby
                sort_order = get_storage_value(self.param.storage_key, "orderby", self.secret)
                if not sort_order:
                    #  use sort order passed in
                    sort_order = self.param.orderby

            orderby = self.decode_orderby(sort_order)
            if not self.param.storage_values:
                storage_values = dict()

            parms["orderby"] = orderby["orderby_expression"]
            if "orderby" not in self.param.storage_values:
                self.param.storage_values["orderby"] = None
            self.param.storage_values["orderby"] = orderby["orderby_string"]
            if orderby["orderby_string"] != get_storage_value(self.param.storage_key, "orderby", self.secret):
                #  user clicked on a header to change sort order - reset page to 1
                self.current_page_number = 1

            if self.param.left:
                parms["left"] = self.param.left

            if self.param.left:
                self.total_number_of_rows = len(self.db(query).select(self.db[self.tablename].id, **parms))
            else:
                self.total_number_of_rows = self.db(query).count()

            #  if at a high page number and then filter causes less records to be displayed, reset to page 1
            if (self.current_page_number - 1) * self.param.rows_per_page > self.total_number_of_rows:
                self.current_page_number = 1

            if self.total_number_of_rows > self.param.rows_per_page:
                self.page_start = self.param.rows_per_page * (self.current_page_number - 1)
                self.page_end = self.page_start + self.param.rows_per_page
                parms["limitby"] = (self.page_start, self.page_end)
            else:
                self.page_start = 0
                if self.total_number_of_rows > 1:
                    self.page_start = 1
                self.page_end = self.total_number_of_rows

            if self.param.fields:
                self.rows = self.db(query).select(*self.param.fields, **parms)
            else:
                self.rows = self.db(query).select(**parms)

            self.number_of_pages = self.total_number_of_rows // self.param.rows_per_page
            if self.total_number_of_rows % self.param.rows_per_page > 0:
                self.number_of_pages += 1

            self.param.storage_values["page"] = self.current_page_number

            set_storage_values(self.param.storage_key,
                               self.param.storage_values, 
                               self.secret, 
                               self.param.token_longevity)

    def decode_orderby(self, sort_order):
        """
        sort_order can be an int, string, list of strings, pydal fields or list of pydal fields

        need to determine which it is and then return a dict containing the string representation of the
        orderby and the pydal expression to be used in the query

        :param sort_order: can be an int, string, list of strings, pydal fields or list of pydal fields
        :return: dict(orderby_string=<order by string>, orderby_expression=<pydal orderby expression>)
        """
        orderby_expression = None
        orderby_string = None
        if sort_order:
            #  can be an int or a PyDAL field
            try:
                index = int(sort_order)
                #  if we get here, this is a sort request from the table
                #  if it is in the saved order by then reverse the direction
                if (request.query.get("sort_dir") and request.query.get("sort_dir") == "desc") or index < 0:
                    orderby_expression = [~self.param.fields[abs(index)]]
                else:
                    orderby_expression = [self.param.fields[index]]
            except:
                #  this could be:
                #  a string
                #  a list of strings
                #  a list of dal fields or a single pydal field, treat the same
                if isinstance(sort_order, str):
                    #  a string
                    tablename, fieldname = sort_order.split(".")
                    orderby_expression = [self.db[tablename][fieldname]]
                else:
                    sort_type = "dal_field"
                    for x in sort_order:
                        if isinstance(x, str):
                            sort_type = "str"

                    if sort_type == "dal_field":
                        #  a list of dal fields
                        orderby_expression = sort_order
                    else:
                        #  a list of strings
                        orderby_expression = []
                        for x in sort_order:
                            tablename, fieldname = x.replace("~", "").split(".")
                            if "~" in x:
                                orderby_expression.append(~self.db[tablename][fieldname])
                            else:
                                orderby_expression.append(self.db[tablename][fieldname])
        else:
            for field in self.param.fields:
                if field not in self.hidden_fields and (field.name != "id" or 
                                                        (field.name == "id" and self.param.show_id)):
                    orderby_expression = field

        if orderby_expression:
            try:
                orderby_string = []
                for x in orderby_expression:
                    op = ''
                    if hasattr(x, 'op') and x.op and x.op.__name__ == 'invert':
                        x = x.first
                        op = '~'
                    orderby_string.append("%s%s.%s" % (op, x.tablename, x.name))
            except:
                orderby_string = orderby_expression

        return dict(orderby_string=orderby_string, orderby_expression=orderby_expression)

    def iter_pages(self, left_edge=1, right_edge=1, left_current=1, right_current=2):
        """
        generator used to determine which page numbers should be shown on the Grid pager

        :param left_edge: # of pages to show on the left
        :param right_edge: # of pages to show on the right
        :param left_current: # of pages to add to the left of current page
        :param right_current: # of fpages to add to the right of current page
        """
        current = 1
        last_blank = False
        while current <= self.number_of_pages:
            #  current page
            if current == self.current_page_number:
                last_blank = False
                yield current

            #  left edge
            elif current <= left_edge:
                last_blank = False
                yield current

            #  right edge
            elif current > self.number_of_pages - right_edge:
                last_blank = False
                yield current

            #  left of current
            elif self.current_page_number - left_current <= current < self.current_page_number:
                last_blank = False
                yield current

            #  right of current
            elif self.current_page_number < current <= self.current_page_number + right_current:
                last_blank = False
                yield current
            else:
                if not last_blank:
                    yield None
                    last_blank = True

            current += 1

    def render_action_button(self,
                             url,
                             button_text,
                             icon,
                             icon_size="small",
                             additional_classes=None,
                             additional_styles=None,
                             override_classes=None,
                             override_styles=None,
                             message=None,
                             row_id=None,
                             storage_key=None,
                             page=None):
        separator = "?"
        if row_id:
            url += "/%s" % row_id
        if storage_key:
            url += "%sstorage_key=%s" % (separator, storage_key)
            separator = "&"
        if page:
            url += "%spage=%s" % (separator, page)

        classes = self.param.grid_class_style("action_button").get("_class", "")
        styles = self.param.grid_class_style("action_button").get("_style", "")
        if additional_classes:
            if isinstance(additional_classes, list):
                classes += " ".join(additional_classes)
            else:
                classes += " " + additional_classes
        if additional_styles:
            if isinstance(additional_styles, list):
                styles += " ".join(additional_styles)
            else:
                styles += " " + additional_styles

        if override_classes:
            if isinstance(override_classes, list):
                classes = " ".join(override_classes)
            else:
                classes = " " + override_classes

        if override_styles:
            if isinstance(override_styles, list):
                styles = " ".join(override_styles)
            else:
                styles = " " + override_styles

        if self.param.include_action_button_text:
            _a = A(_href=url,
                   _class=classes,
                   _message=message,
                   _title=button_text,
                   _style=styles)
            _span = SPAN(_class="icon is-%s" % icon_size)
            _span.append(I(_class="fa %s" % icon))
            _a.append(_span)
            _a.append(SPAN(' ' + button_text, _class='hide-on-mobile'))
        else:
            _a = A(I(_class="fa %s" % icon),
                   _href=url,
                   _class=classes,
                   _message=message,
                   _title=button_text,
                   _style=styles)

        return _a

    def render_search_form(self):
        _sf = DIV(**self.param.grid_class_style("search_form"))
        _sf.append(self.param.search_form.custom["begin"])
        _tr = TR(**self.param.grid_class_style("search_form_tr"))
        for field in self.param.search_form.table:
            _td = TD(**self.param.grid_class_style("search_form_td"))
            if field.type == "boolean":
                _td.append(self.param.search_form.custom["widgets"][field.name])
                _td.append(field.label)
            else:
                _td.append(self.param.search_form.custom["widgets"][field.name])
            if field.name in self.param.search_form.custom["errors"] and \
                    self.param.search_form.custom["errors"][field.name]:
                _td.append(DIV(self.param.search_form.custom["errors"][field.name], _style="color:#ff0000"))
            _tr.append(_td)
        if self.param.search_button_text:
            _tr.append(TD(INPUT(_class="button", _type="submit", _value=self.param.search_button_text),
                          **self.param.grid_class_style("search_form_td")))
        else:
            _tr.append(TD(self.param.search_form.custom["submit"],
                          **self.param.grid_class_style("search_form_td")))
        _sf.append(TABLE(_tr, **self.param.grid_class_style("search_form_table")))
        for hidden_widget in self.param.search_form.custom["hidden_widgets"].keys():
            _sf.append(self.param.search_form.custom["hidden_widgets"][hidden_widget])

        _sf.append(self.param.search_form.custom["end"])

        return _sf

    def render_table_header(self):
        _thead = THEAD(**self.param.grid_class_style("thead"))
        for index, field in enumerate(self.param.fields):
            if field.name not in [x.name for x in self.hidden_fields] and (
                    field.name != "id" or (field.name == "id" and self.param.show_id)):
                try:
                    heading = self.param.headings[index]
                except:
                    if field.table == self.tablename:
                        heading = field.label
                    else:
                        heading = str(field.table)
                #  add the sort order query parm
                sort_query_parms = dict(self.query_parms)
                sort_query_parms["sort"] = index
                current_sort_dir = "asc"

                if "%s.%s" % (field.tablename, field.name) in self.param.storage_values["orderby"]:
                    sort_query_parms["sort"] = "-%s" % index
                    _h = A(heading.replace("_", " ").upper(),
                           _href=URL(self.endpoint, vars=sort_query_parms))
                    _h.append(SPAN(I(_class="fas fa-sort-up"), **self.param.grid_class_style('sorter_icon')))
                elif "~%s.%s" % (field.tablename, field.name) in self.param.storage_values["orderby"]:
                    _h = A(heading.replace("_", " ").upper(),
                           _href=URL(self.endpoint, vars=sort_query_parms))
                    _h.append(SPAN(I(_class="fas fa-sort-down"), **self.param.grid_class_style('sorter_icon')))
                else:
                    _h = A(heading.replace("_", " ").upper(),
                           _href=URL(self.endpoint, vars=sort_query_parms))

                if "sort_dir" in sort_query_parms:
                    current_sort_dir = sort_query_parms["sort_dir"]
                    del sort_query_parms["sort_dir"]
                if index == int(request.query.get("sort", 0)) and current_sort_dir == "asc":
                    sort_query_parms["sort_dir"] = "desc"

                classes = self.param.grid_class_style("th").get("_class", "")
                if index not in self.param.mobile_columns:
                    classes += " hide-on-mobile"
                _th = TH(_class=classes, _style=self.param.grid_class_style("th").get("_style", ""))
                _th.append(_h)

                _thead.append(_th)

        if self.param.details or self.param.editable or self.param.deletable:
            _thead.append(TH("ACTIONS", **self.param.grid_class_style("action_column_header")))

        return _thead

    def render_field(self, row, field, field_index):
        """
        Render a field

        if only 1 table in the query, the no table name needed when getting the row value - however, if there
        are multiple tables in the query (self.use_tablename == True) then we need to use the tablename as well
        when accessing the value in the row object

        the row object sent in can take
        :param row:
        :param field:
        :return:
        """
        if self.use_tablename:
            field_value = row[field.tablename][field.name]
        else:
            field_value = row[field.name]

        hide_on_mobile = not field_index in self.param.mobile_columns

        if field.type == "date":
            classes = self.param.grid_class_style("td_date").get("_class", "")
            if hide_on_mobile:
                classes += " hide-on-mobile"
            _td = TD(XML("<script>\ndocument.write("
                         "moment(\"%s\").format('L'));\n</script>" % field_value) \
                        if row and field and field_value else "",
                     _class=classes,
                     _style=self.param.grid_class_style("td_date").get("_style", ""))
        elif field.type == "boolean":
            #  True/False - only show on True, blank for False
            classes = self.param.grid_class_style("td_boolean").get("_class", "")
            if hide_on_mobile:
                classes += " hide-on-mobile"
            if row and field and field_value:
                _td = TD(_class=classes, _style=self.param.grid_class_style("td_boolean").get("_style", ""))
                _span = SPAN(_class="icon is-small")
                _span.append(I(_class="fas fa-check-circle"))
                _td.append(_span)
            else:
                _td = TD(XML("&nbsp;"),
                         _class=classes,
                         _style=self.param.grid_class_style("td_boolean").get("_style", ""))
        else:
            classes = self.param.grid_class_style("td").get("_class", "")
            if hide_on_mobile:
                classes += " hide-on-mobile"
            _td = TD(field_value if row and field and field_value else "",
                     _class=classes,
                     _style=self.param.grid_class_style("td").get("_style", ""))

        return _td

    def render_table_body(self):
        _tbody = TBODY(**self.param.grid_class_style("tbody"))
        for row in self.rows:
            #  find the row id - there may be nested tables....
            if self.use_tablename:
                row_id = row[self.tablename]["id"]
            else:
                row_id = row["id"]

            _tr = TR(**self.param.grid_class_style("td"))
            #  add all the fields to the row
            for field_index, field in enumerate(self.param.fields):
                if field.name not in [x.name for x in self.hidden_fields] and \
                        (field.name != "id" or (field.name == "id" and self.param.show_id)):
                    _tr.append(self.render_field(row, field, field_index))

            _td = None

            #  add the action buttons
            if (self.param.details and self.param.details != "") or \
                    (self.param.editable and self.param.editable != "") or \
                    (self.param.deletable and self.param.deletable != ""):
                _td = TD(**self.param.grid_class_style("action_column_cell"))
                if self.param.pre_action_buttons:
                    for btn in self.param.pre_action_buttons:
                        _td.append(self.render_action_button(btn.url,
                                                             btn.text,
                                                             btn.icon,
                                                             additional_classes=btn.additional_classes,
                                                             message=btn.message,
                                                             row_id=row_id if btn.append_id else None,
                                                             storage_key=self.param.storage_key
                                                             if btn.append_storage_key else None,
                                                             page=self.current_page_number
                                                             if btn.append_page else None))
                if self.param.details and self.param.details != "":
                    if isinstance(self.param.details, str):
                        details_url = self.param.details
                    else:
                        details_url = URL(self.endpoint) + "/details/%s" % self.tablename
                    details_url += "/%s?storage_key=%s&page=%s" % (row_id,
                                                                self.param.storage_key,
                                                                self.current_page_number)
                    _td.append(self.render_action_button(details_url, "Details", "fa-id-card"))

                if self.param.editable and self.param.editable != "":
                    if isinstance(self.param.editable, str):
                        edit_url = self.param.editable
                    else:
                        edit_url = URL(self.endpoint) + "/edit/%s" % self.tablename
                    _td.append(self.render_action_button(edit_url, "Edit", "fa-edit", row_id=row_id,
                                                         storage_key=self.param.storage_key,
                                                         page=self.current_page_number))

                if self.param.deletable and self.param.deletable != "":
                    if isinstance(self.param.deletable, str):
                        delete_url = self.param.deletable
                    else:
                        delete_url = URL(self.endpoint) + "/delete/%s" % self.tablename
                    delete_url += "/%s?storage_key=%s" % (row_id, self.param.storage_key)
                    _td.append(self.render_action_button(delete_url, "Delete", "fa-trash",
                                                         additional_classes="confirmation",
                                                         message="Delete record"))
                if self.param.post_action_buttons:
                    for btn in self.param.post_action_buttons:
                        _td.append(self.render_action_button(btn.url,
                                                             btn.text,
                                                             btn.icon,
                                                             additional_classes=btn.additional_classes,
                                                             message=btn.message,
                                                             row_id=row_id if btn.append_id else None,
                                                             storage_key=self.param.storage_key
                                                             if btn.append_storage_key else None,
                                                             page=self.current_page_number
                                                             if btn.append_page else None))
                _tr.append(_td)
            _tbody.append(_tr)

        return _tbody

    def render_table_pager(self):
        _pager = DIV(**self.param.grid_class_style("pager"))
        for page_number in self.iter_pages():
            if page_number:
                pager_query_parms = dict(self.query_parms)
                pager_query_parms["page"] = page_number
                pager_query_parms["storage_key"] = self.param.storage_key
                if self.current_page_number == page_number:
                    _pager.append(A(page_number, **self.param.grid_class_style("active_page_button"),
                                    _href=URL(self.endpoint, vars=pager_query_parms)))
                else:
                    _pager.append(A(page_number, **self.param.grid_class_style("inactive_page_button"),
                                    _href=URL(self.endpoint, vars=pager_query_parms)))
            else:
                _pager.append("...")

        return _pager

    def render_table(self):
        _html = DIV(**self.param.grid_class_style("wrapper"))
        _html.append(
            XML("""
                 <style type="text/css">
                    @media screen and (max-width: 600px) {
                        .body {
                            font-size: smaller;
                        }
                    
                        .hide-on-mobile {
                            display: none;
                        }
                    
                    }
                 </style>
            """)
        )
        _top_div = DIV(**self.param.grid_class_style("top_div"))

        #  build the New button if needed
        if self.param.create and self.param.create != "":
            if isinstance(self.param.create, str):
                create_url = self.param.create
            else:
                create_url = URL(self.endpoint) + "/new/%s/0" % self.tablename

            _top_div.append(self.render_action_button(create_url, "New", "fa-plus", icon_size="normal",
                                          override_classes=self.param.grid_class_style("new_button").get("_class", ""),
                                          override_styles=self.param.grid_class_style("new_button").get("_style", "")))

        #  build the search form if provided
        if self.param.search_form:
            _top_div.append(self.render_search_form())

        _html.append(_top_div)

        _table = TABLE(**self.param.grid_class_style("table"))

        # build the header
        _table.append(self.render_table_header())

        #  include moment.js to present dates in the proper locale
        _html.append(XML('<script src="https://momentjs.com/downloads/moment.js"></script>'))

        #  build the rows
        _table.append(self.render_table_body())

        #  add the table to the html
        _html.append(_table)

        #  add the row counter information
        _footer = DIV(**self.param.grid_class_style("table_footer"))
        _row_count = DIV(**self.param.grid_class_style("row_count"))
        _row_count.append(
            P("Displaying rows %s thru %s of %s" % (self.page_start + 1 if self.number_of_pages > 1 else 1,
                                                    self.page_end if self.page_end < self.total_number_of_rows else
                                                    self.total_number_of_rows,
                                                    self.total_number_of_rows)))
        _footer.append(_row_count)

        #  build the pager
        if self.number_of_pages > 1:
            _footer.append(self.render_table_pager())

        _html.append(_footer)

        if self.param.deletable:
            _html.append(XML("""
                 <script type="text/javascript">
                    document.querySelector(".confirmation").addEventListener("click", function(event) {
                        if (confirm(this.getAttribute('message') +' - Are you sure?')) {
                            return true;
                        } else {
                            event.preventDefault();
                        }
                    });
                 </script>   
            """))

        return XML(_html)

    def render(self):
        """
        build the query table

        :return: html representation of the table or the py4web Form object
        """
        if self.action == "select":
            return self.render_table()
        elif self.action in ["new", "details", "edit"]:
            return self.form

    def data(self):
        """
        get the record that is being edited / displayed

        :return: DAL record of the record being edited
        """
        return self.db[self.tablename](self.record_id) if self.tablename and self.record_id else None


def GridClassStyle(element_name):
    classes = {"wrapper": "",
               "top_div": "",
               "new_button": "",
               "search_form": "",
               "search_form_table": "",
               "search_form_tr": "",
               "search_form_td": "",
               "table": "",
               "thead": "",
               "th": "",
               "sorter_icon": "",
               "action_column_header": "",
               "tbody": "",
               "tr": "",
               "td": "",
               "td_date": "",
               "td_boolean": "",
               "action_column_cell": "",
               "action_button": "",
               "table_footer": "",
               "row_count": "",
               "pager": "",
               "active_page_button": "",
               "inactive_page_button": ""}

    styles = {"wrapper": "",
              "top_div": "border-bottom: 0;",
              "new_button": "",
              "search_form": "float: right; border-bottom: 0; padding-bottom: 0; margin-bottom: 0;",
              "search_form_table": "margin-bottom: 0;",
              "search_form_tr": "border-bottom: 0; padding-bottom: 0;",
              "search_form_td": "border-bottom: 0; padding-bottom: 0;",
              "table": "",
              "thead": "",
              "th": "text-align: center;",
              "sorter_icon": "float: right;",
              "action_column_header": "text-align: center; width: 1px; white-space: nowrap;",
              "tbody": "",
              "tr": "",
              "td": "vertical-align: middle;",
              "td_date": "",
              "td_boolean": "",
              "action_column_cell": "text-align: center; width: 1px; white-space: nowrap; vertical-align: middle;",
              "action_button": ("border: thin solid lightgray; "
                                "color: black; "
                                "cursor: pointer; "
                                "display: inline-block; "
                                "font-size: .75rem;"
                                "min-width: 75px; "
                                "padding-right: 1rem; "
                                "padding-left: 1rem; "
                                "text-align: center; "
                                "text-decoration: none; "
                                "vertical-align: middle; "
                                "white-space: nowrap;"),
              "table_footer": "line-height: 1.8rem; padding-bottom: 20px;",
              "row_count": "float: left; line-height: 1.8rem;",
              "pager": "float: right; line-height: 1.8rem;",
              "active_page_button": "background-color: #0074d9; "
                                    "border: thin solid #0074d9; "
                                    "color: white; "
                                    "cursor: pointer; "
                                    "display: inline-block; "
                                    "font-size: .75rem;"
                                    "padding-right: .75rem; "
                                    "padding-left: .75rem; "
                                    "margin-right: .25rem; "
                                    "text-align: center; "
                                    "text-decoration: none; "
                                    "vertical-align: middle; "
                                    "white-space: nowrap;",
              "inactive_page_button": "background-color: white; "
                                      "border: thin solid #0074d9; "
                                      "color: #0074d9; "
                                      "cursor: pointer; "
                                      "display: inline-block; "
                                      "font-size: .75rem;"
                                      "padding-right: .75rem; "
                                      "padding-left: .75rem; "
                                      "margin-right: .25rem; "
                                      "text-align: center; "
                                      "text-decoration: none; "
                                      "vertical-align: middle; "
                                      "white-space: nowrap;"}

    classes_styles = {}
    if classes.get(element_name) and classes.get(element_name) != "":
        classes_styles["_class"] = classes.get(element_name)

    if styles.get(element_name) and styles.get(element_name) != "":
        classes_styles["_style"] = styles.get(element_name)

    return classes_styles


def GridClassStyleBulma(element_name):
    classes = {"wrapper": "field",
               "top_div": "pb-2",
               "new_button": "button",
               "search_form": "is-pulled-right pb-2",
               "search_form_table": "",
               "search_form_tr": "",
               "search_form_td": "pr-1",
               "table": "table is-bordered is-striped is-hoverable is-fullwidth",
               "thead": "",
               "th": "has-text-centered",
               "sorter_icon": "is-pulled-right",
               "action_column_header": "has-text-centered is-narrow",
               "tbody": "",
               "tr": "",
               "td": "",
               "td_date": "has-text-centered",
               "td_boolean": "has-text-centered",
               "action_column_cell": "has-text-centered is-narrow",
               "action_button": "button is-small",
               "table_footer": "",
               "row_count": "is-pulled-left",
               "pager": "is-pulled-right",
               "active_page_button": "button is-primary is-small",
               "inactive_page_button": "button is-small"}

    styles = {"wrapper": "",
              "top_div": "",
              "new_button": "",
              "search_form": "",
              "search_form_table": "",
              "search_form_tr": "",
              "search_form_td": "",
              "table": "",
              "thead": "",
              "th": "",
              "sorter_icon": "",
              "action_column_header": "",
              "tbody": "",
              "tr": "",
              "td": "",
              "td_date": "",
              "td_boolean": "",
              "action_column_cell": "",
              "action_button": "",
              "table_footer": "",
              "row_count": "",
              "pager": "",
              "active_page_button": "",
              "inactive_page_button": ""}

    classes_styles = {}
    if classes.get(element_name) and classes.get(element_name) != "":
        classes_styles["_class"] = classes.get(element_name)

    if styles.get(element_name) and styles.get(element_name) != "":
        classes_styles["_style"] = styles.get(element_name)

    return classes_styles


class ActionButton:
    def __init__(self,
                 url,
                 text,
                 icon="fa-calendar",
                 additional_classes=None,
                 additional_styles=None,
                 override_classes=None,
                 override_styles=None,
                 message=None,
                 append_id=False,
                 append_storage_key=False,
                 append_page=False):
        self.url = url
        self.text = text
        self.icon = icon
        self.additional_classes = additional_classes
        self.additional_styles = additional_styles
        self.override_classes = override_classes
        self.override_styles = override_styles
        self.message = message
        self.append_id = append_id
        self.append_storage_key = append_storage_key
        self.append_page = append_page


class GridDefaults:
    def __init__(self,
                 db,
                 secret,
                 token_longevity=3600,
                 rows_per_page=15,
                 include_action_button_text=True,
                 search_button_text="Filter",
                 formstyle=FormStyleDefault,
                 grid_class_style=GridClassStyle,
                 mobile_columns=None):
        self.param = Param(db=db,
                           secret=secret,
                           token_longevity=token_longevity,
                           rows_per_page=rows_per_page,
                           include_action_button_text=include_action_button_text,
                           search_button_text=search_button_text,
                           formstyle=formstyle,
                           grid_class_style=grid_class_style,
                           mobile_columns=mobile_columns if mobile_columns else [0, 1, 2, 3,
                                                                                 4, 5, 6, 7,
                                                                                 8, 9, 10, 11,
                                                                                 12, 13,14, 15])
