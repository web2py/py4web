import base64
import copy
from functools import reduce

from yatl.helpers import (
    DIV,
    TABLE,
    TBODY,
    TR,
    TD,
    TH,
    A,
    SPAN,
    I,
    THEAD,
    P,
    TAG,
    INPUT,
    XML,
    FORM,
    SELECT,
    OPTION,
)
from pydal.objects import Field, FieldVirtual
from py4web import request, URL, response, redirect, HTTP
from py4web.utils.form import Form, FormStyleDefault
from py4web.utils.param import Param

NAV = TAG.nav
HEADER = TAG.header


def title(text):
    """Turns text into a title"""
    return text.replace("_", " ").title()


def safe_int(text, default):
    """try parse txt into an int else returns the default"""
    try:
        return int(text)
    except (ValueError, TypeError):
        return default


class GridClassStyle:

    """
    Default grid style
    Internal element names match default class name, other classes can be added
    Style use should be minimized since it cannot be overridden by CSS
    """

    classes = {
        "grid-wrapper": "grid-wrapper",
        "grid-header": "grid-header",
        "grid-new-button": "grid-new-button info",
        "grid-search": "grid-search",
        "grid-table-wrapper": "grid-table-wrapper",
        "grid-table": "grid-table",
        "grid-sorter-icon-up": "grid-sort-icon-up fas fa-sort-up",
        "grid-sorter-icon-down": "grid-sort-icon-down fas fa-sort-down",
        "grid-th-action-button": "grid-col-action-button",
        "grid-td-action-button": "grid-col-action-button",
        "grid-tr": "",
        "grid-th": "",
        "grid-td": "",
        "grid-details-button": "grid-details-button info",
        "grid-edit-button": "grid-edit-button info",
        "grid-delete-button": "grid-delete-button info",
        "grid-footer": "grid-footer",
        "grid-info": "grid-info",
        "grid-pagination": "grid-pagination",
        "grid-pagination-button": "grid-pagination-button info",
        "grid-pagination-button-current": "grid-pagination-button-current default",
        "grid-cell-type-string": "grid-cell-type-string",
        "grid-cell-type-text": "grid-cell-type-text",
        "grid-cell-type-boolean": "grid-cell-type-boolean",
        "grid-cell-type-float": "grid-cell-type-float",
        "grid-cell-type-int": "grid-cell-type-int",
        "grid-cell-type-date": "grid-cell-type-date",
        "grid-cell-type-time": "grid-cell-type-time",
        "grid-cell-type-datetime": "grid-cell-type-datetime",
        "grid-cell-type-upload": "grid-cell-type-upload",
        "grid-cell-type-list": "grid-cell-type-list",
        # specific for custom form
        "search_form": "search-form",
        "search_form_table": "search-form-table",
        "search_form_tr": "search-form-tr",
        "search_form_td": "search-form-td",
    }

    styles = {
        "grid-wrapper": "",
        "grid-header": "display: table; width: 100%",
        "grid-new-button": "display: table-cell;",
        "grid-search": "display: table-cell; float:right",
        "grid-table-wrapper": "overflow-x: auto; width:100%",
        "grid-table": "",
        "grid-sorter-icon-up": "",
        "grid-sorter-icon-down": "",
        "grid-th-action-button": "",
        "grid-td-action-button": "",
        "grid-tr": "",
        "grid-th": "white-space: nowrap; vertical-align: middle",
        "grid-td": "white-space: nowrap; vertical-align: middle",
        "grid-details-button": "margin-bottom: 0",
        "grid-edit-button": "margin-bottom: 0",
        "grid-delete-button": "margin-bottom: 0",
        "grid-footer": "display: table; width:100%",
        "grid-info": "display: table-cell;",
        "grid-pagination": "display: table-cell; text-align:right",
        "grid-pagination-button": "min-width: 20px",
        "grid-pagination-button-current": "min-width: 20px; pointer-events:none; opacity: 0.7",
        "grid-cell-type-string": "white-space: nowrap; vertical-align: middle; text-align: left; text-overflow: ellipsis; max-width: 200px",
        "grid-cell-type-text": "vertical-align: middle; text-align: left; text-overflow: ellipsis; max-width: 200px",
        "grid-cell-type-boolean": "white-space: nowrap; vertical-align: middle; text-align: center",
        "grid-cell-type-float": "white-space: nowrap; vertical-align: middle; text-align: right",
        "grid-cell-type-int": "white-space: nowrap; vertical-align: middle; text-align: right",
        "grid-cell-type-date": "white-space: nowrap; vertical-align: middle; text-align: right",
        "grid-cell-type-time": "white-space: nowrap; vertical-align: middle; text-align: right",
        "grid-cell-type-datetime": "white-space: nowrap; vertical-align: middle; text-align: right",
        "grid-cell-type-upload": "white-space: nowrap; vertical-align: middle; text-align: center",
        "grid-cell-type-list": "white-space: nowrap; vertical-align: middle; text-align: left",
        # specific for custom form
        "search_form": "",
        "search_form_table": "",
        "search_form_tr": "",
        "search_form_td": "",
    }

    @classmethod
    def get(cls, element):
        """returns a dict with _class and _style for the element name"""
        return {
            "_class": cls.classes.get(element),
            "_style": cls.styles.get(element),
        }


class GridClassStyleBulma(GridClassStyle):
    """The Grid style for Bulma"""

    classes = {
        "grid-wrapper": "grid-wrapper field",
        "grid-header": "grid-header pb-2",
        "grid-new-button": "grid-new-button button",
        "grid-search": "grid-search is-pulled-right pb-2",
        "grid-table-wrapper": "grid-table-wrapper table_wrapper",
        "grid-table": "grid-table table is-bordered is-striped is-hoverable is-fullwidth",
        "grid-sorter-icon-up": "grid-sort-icon-up fas fa-sort-up is-pulled-right",
        "grid-sorter-icon-down": "grid-sort-icon-down fas fa-sort-down is-pulled-right",
        "grid-th-action-button": "grid-col-action-button is-narrow",
        "grid-td-action-button": "grid-col-action-button is-narrow",
        "grid-tr": "",
        "grid-th": "",
        "grid-td": "",
        "grid-details-button": "grid-details-button button is-small",
        "grid-edit-button": "grid-edit-button button is-small",
        "grid-delete-button": "grid-delete-button button is-small",
        "grid-footer": "grid-footer",
        "grid-info": "grid-info is-pulled-left",
        "grid-pagination": "grid-pagination is-pulled-right",
        "grid-pagination-button": "grid-pagination-button button is-small",
        "grid-pagination-button-current": "grid-pagination-button-current button is-primary is-small",
        "grid-cell-type-string": "grid-cell-type-string",
        "grid-cell-type-text": "grid-cell-type-text",
        "grid-cell-type-boolean": "grid-cell-type-boolean has-text-centered",
        "grid-cell-type-float": "grid-cell-type-float",
        "grid-cell-type-int": "grid-cell-type-int",
        "grid-cell-type-date": "grid-cell-type-date",
        "grid-cell-type-time": "grid-cell-type-time",
        "grid-cell-type-datetime": "grid-cell-type-datetime",
        "grid-cell-type-upload": "grid-cell-type-upload",
        "grid-cell-type-list": "grid-cell-type-list",
        # specific for custom form
        "search_form": "search-form is-pulled-right pb-2",
        "search_form_table": "search-form-table",
        "search_form_tr": "search-form-tr",
        "search_form_td": "search-form-td pr-1",
    }

    styles = {
        "grid-wrapper": "",
        "grid-header": "",
        "grid-new-button": "",
        "grid-search": "",
        "grid-table-wrapper": "",
        "grid-table": "",
        "grid-sorter-icon-up": "",
        "grid-sorter-icon-down": "",
        "grid-th-action-button": "",
        "grid-td-action-button": "",
        "grid-tr": "",
        "grid-th": "text-align: center; text-transform: uppercase;",
        "grid-td": "",
        "grid-details-button": "",
        "grid-edit-button": "",
        "grid-delete-button": "",
        "grid-footer": "padding-top: .5em;",
        "grid-info": "",
        "grid-pagination": "",
        "grid-pagination-button": "margin-left: .25em;",
        "grid-pagination-button-current": "margin-left: .25em;",
        "grid-cell-type-string": "",
        "grid-cell-type-text": "",
        "grid-cell-type-boolean": "",
        "grid-cell-type-float": "",
        "grid-cell-type-int": "",
        "grid-cell-type-date": "",
        "grid-cell-type-time": "",
        "grid-cell-type-datetime": "",
        "grid-cell-type-upload": "",
        "grid-cell-type-list": "",
        # specific for custom form
        "search_form": "",
        "search_form_table": "",
        "search_form_tr": "",
        "search_form_td": "",
    }


class Grid:

    FORMATTERS_BY_TYPE = {
        "boolean": lambda value: INPUT(_type="checkbox", _checked=value)
        if value
        else "",
        "datetime": lambda value: XML(
            "<script>document.write((new Date(%s,%s,%s,%s,%s,%s)).toLocaleString())</script>"
            % (
                value.year,
                value.month,
                value.day,
                value.hour,
                value.minute,
                value.second,
            )
        )
        if value
        else "",
        "time": lambda value: XML(
            "<script>document.write((new Date(0, 0, 0,%s,%s,%s)).toLocaleString().split(', ')[1])</script>"
            % (value.hour, value.minute, value.second)
        )
        if value
        else "",
        "date": lambda value: XML(
            '<script>document.write((new Date(%s,%s,%s)).toLocaleString().split(",")[0])</script>'
            % (value.year, value.month, value.day,)
        )
        if value
        else "",
        "default": lambda value: str(value) if value is not None else ""
    }

    def __init__(
        self,
        path,
        query,
        search_form=None,
        search_queries=None,
        fields=None,
        show_id=False,
        orderby=None,
        left=None,
        headings=None,
        create=True,
        details=True,
        editable=True,
        deletable=True,
        pre_action_buttons=None,
        post_action_buttons=None,
        auto_process=True,
        rows_per_page=15,
        include_action_button_text=True,
        search_button_text="Filter",
        formstyle=FormStyleDefault,
        grid_class_style=GridClassStyle,
    ):
        """
        Grid is a searchable/sortable/pageable grid

        :param path: The part of the URL to be parsed by this grid
        :param query: the query used to filter the data
        :param search_form: py4web FORM to be included as the search form
        :param search_queries: future use - pass a dict of name and a search query
        :param fields: list of fields to display on the list page, if blank, glean tablename from first query
        :              and use all fields of that table
        :param show_id: show the record id field on list page - default = False
        :param orderby: pydal orderby field or list of fields
        :param left: if joining other tables, specify the pydal left expression here
        :param headings: list of headings to be used for list page - if not provided use the field label
        :param create: URL to redirect to for creating records - set to False to not display the button
        :param editable: URL to redirect to for editing records - set to False to not display the button
        :param deletable: URL to redirect to for deleting records - set to False to not display the button
        :param pre_action_buttons: list of action_button instances to include before the standard action buttons
        :param post_action_buttons: list of action_button instances to include after the standard action buttons
        :param auto_process: True/False - automatically process the sql for the form - if False, user is
                              responsible for calling process().
        """

        # in case the query is a Table instead
        if isinstance(query, query._db.Table):
            query = query._id != None

        self.path = path or ""
        self.db = query._db
        self.param = Param(
            query=query,
            fields=fields,
            show_id=show_id,
            orderby=orderby,
            left=left,
            search_form=search_form,
            search_queries=search_queries,
            headings=headings or [],
            create=create,
            details=details,
            editable=editable,
            deletable=deletable,
            pre_action_buttons=pre_action_buttons,
            post_action_buttons=post_action_buttons,
            rows_per_page=rows_per_page,
            include_action_button_text=include_action_button_text,
            search_button_text=search_button_text,
            formstyle=formstyle,
            grid_class_style=grid_class_style,
        )

        #  instance variables that will be computed
        self.action = None
        self.current_page_number = None
        self.endpoint = request.path
        if self.path:
            self.endpoint = self.endpoint[: -len(self.path)].rstrip("/")
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
        self.use_tablename = self.is_join()
        self.formatters = {}
        self.formatters_by_type = copy.copy(Grid.FORMATTERS_BY_TYPE)

        if auto_process:
            self.process()

    def process(self):
        query = None
        db = self.db
        if not self.param.search_form and self.param.search_queries:
            seach_type = safe_int(request.query.get("seach_type", 0), default=0)
            seach_string = request.query.get("seach_string")
            if seach_type < len(self.param.search_queries) and seach_string:
                query_lambda = self.param.search_queries[seach_type][1]
                try:
                    query = query_lambda(seach_string)
                except:
                    pass  # flash a message here

        if not query:
            query = self.param.query
        else:
            query &= self.param.query

        parts = self.path.split("/")
        self.action = parts[0] or "select"
        self.tablename = self.get_tablenames(self.param.query)[0]  # what if there ar 2?
        self.record_id = safe_int(parts[1] if len(parts) > 1 else None, default=None)

        if self.param.fields:
            if not isinstance(self.param.fields, list):
                self.param.fields = [self.param.fields]
        else:
            table = db[self.tablename]
            self.param.fields = [field for field in table if field.readable]

        self.readonly_fields = [
            field for field in self.param.fields if not field.writable
        ]
        self.referrer = None

        if not self.tablename:
            raise HTTP(400)

        if self.action in ["new", "details", "edit"]:

            # SECURITY: if the record does not exist or does not match query, than we are not allowed
            if self.record_id:
                if (
                    db(
                        (db[self.tablename]._id == self.record_id) & self.param.query
                    ).count()
                    == 0
                ):
                    redirect(self.endpoint)  ## maybe flash

            readonly = self.action == "details"
            for field in self.readonly_fields:
                db[field.tablename][field.name].writable = False

            if not self.param.show_id:
                #  if not show id, find the "id" field and set readable/writable to False
                for field in db[self.tablename]:
                    if field.type == "id":
                        db[self.tablename][field.name].readable = False
                        db[self.tablename][field.name].writable = False

            self.form = Form(
                db[self.tablename],
                record=self.record_id,
                readonly=readonly,
                formstyle=self.param.formstyle,
            )
            # SECURITY: if the new record was created but does not match filter, delete it
            if self.form.accepted and not self.record_id:
                new_record = db[self.tablename]._id == self.form.vars["id"]
                if db(new_record & self.param.query).count() == 0:
                    db(new_record).delete()
                    # TODO: SHOULD FLASH SOME MESSAGE
            # redirect to the referrer
            if self.form.accepted or (readonly and request.method == "POST"):
                referrer = request.query.get("_referrer")
                if referrer:
                    redirect(base64.b16decode(referrer.encode("utf8")).decode("utf8"))
                else:
                    redirect(self.endpoint)

        elif self.action == "delete":
            db(db[self.tablename].id == self.record_id).delete()
            redirect(self.endpoint)

        elif self.action == "select":
            self.referrer = "_referrer=%s" % base64.b16encode(
                request.url.encode("utf8")
            ).decode("utf8")

            #  find the primary key of the primary table
            pt = db[self.tablename]
            key_is_missing = False
            for field in self.param.fields:
                if field.table._tablename == pt._tablename and field.name == pt._id:
                    key_is_missing = True
            if key_is_missing:
                #  primary key wasn't included, add it and set show_id to False so it doesn't display
                self.param.fields.append(pt._id)
                self.param.show_id = False

            self.current_page_number = safe_int(request.query.get("page"), default=1)

            select_params = dict()
            #  try getting sort order from the request
            sort_order = request.query.get("orderby", "")

            try:
                parts = sort_order.lstrip("~").split(".")
                orderby = db[parts[0]][parts[1]]
                if sort_order.startswith("~"):
                    orderby = ~orderby
                select_params["orderby"] = orderby
            except (IndexError, KeyError, TypeError, AttributeError):
                select_params["orderby"] = self.param.orderby

            if self.param.left:
                select_params["left"] = self.param.left

            if self.param.left:
                # TODO: maybe this can be made more efficient
                self.total_number_of_rows = len(
                    db(query).select(db[self.tablename].id, **select_params)
                )
            else:
                self.total_number_of_rows = db(query).count()

            #  if at a high page number and then filter causes less records to be displayed, reset to page 1
            if (
                self.current_page_number - 1
            ) * self.param.rows_per_page > self.total_number_of_rows:
                self.current_page_number = 1

            if self.total_number_of_rows > self.param.rows_per_page:
                self.page_start = self.param.rows_per_page * (
                    self.current_page_number - 1
                )
                self.page_end = self.page_start + self.param.rows_per_page
                select_params["limitby"] = (self.page_start, self.page_end)
            else:
                self.page_start = 0
                if self.total_number_of_rows > 1:
                    self.page_start = 1
                self.page_end = self.total_number_of_rows

            if self.param.fields:
                self.rows = db(query).select(*self.param.fields, **select_params)
            else:
                self.rows = db(query).select(**select_params)

            self.number_of_pages = self.total_number_of_rows // self.param.rows_per_page
            if self.total_number_of_rows % self.param.rows_per_page > 0:
                self.number_of_pages += 1
        else:
            redirect(self.endpoint)

    def iter_pages(
        self,
        current_page,
        num_pages,
        left_current=1,
        right_current=1,
        left_edge=1,
        right_edge=1,
    ):
        """
        generator used to determine which page numbers should be shown on the Grid pager

        :param left_current: # of pages to add to the left of current page
        :param right_current: # of fpages to add to the right of current page
        :param left_edge: # of pages to add to the left end
        :param right_edge: # of fpages to add to the right end
        """
        left_range = set(range(1, min(2 + left_edge, num_pages + 1)))
        mid_range = set(
            range(
                max(1, current_page - left_current),
                min(current_page + right_current + 1, num_pages + 1),
            )
        )
        right_range = set(range(max(1, num_pages - right_edge), num_pages + 1))
        return list(sorted(left_range | mid_range | right_range))

    def render_action_button(
        self,
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
        name="grid-button",
        **attr,
    ):
        separator = "?"
        if row_id:
            url += "/%s" % row_id
 
        classes = self.param.grid_class_style.classes.get(name, "")
        styles = self.param.grid_class_style.styles.get(name, "")

        def join(items):
            return (
                " ".join(items) if isinstance(items, (list, tuple)) else " %s" % items
            )

        if override_classes:
            classes = join(override_classes)
        elif additional_classes:
            classes += join(additional_classes)
        if override_styles:
            styles = join(override_styles)
        elif additional_styles:
            styles += join(additional_styles)

        link = A(
            I(_class="fa %s" % icon),
            _href=url,
            _role="button",
            _class=classes,
            _message=message,
            _title=button_text,
            _style=styles,
            **attr,
        )
        if self.param.include_action_button_text:
            link.append(XML('<span class="grid-action-button-text">&nbsp;%s</span>' % button_text))

        return link

    def render_default_form(self):

        seach_type = safe_int(request.query.get("seach_type", 0), default=0)
        seach_string = request.query.get("seach_string")
        options = [
            OPTION(items[0], _value=k, _selected=(k == seach_type))
            for k, items in enumerate(self.param.search_queries)
        ]
        hidden_fields = [
            INPUT(_name=key, _value=request.query.get(key), _type="hidden")
            for key in request.query
            if not key in ("seach_type", "seach_string")
        ]
        form = FORM(*hidden_fields, **dict(_method="GET", _action=self.endpoint))
        select = SELECT(*options, **dict(_name="seach_type",))
        input = INPUT(_type="text", _name="seach_string", _value=seach_string,)
        submit = INPUT(_type="submit", _value="Search")
        clear_script = "document.querySelector('[name=seach_string]').value='';"
        clear = INPUT(_type="submit", _value="Clear", _onclick=clear_script)
        div = DIV(_id="grid-search", **self.param.grid_class_style.get("grid-search"))

        # we do not need classes for these elements
        tr = TR()
        if len(options) > 1:
            tr.append(TD(select))
        tr.append(TD(input))
        tr.append(TD(submit, clear))
        form.append(TABLE(tr))
        div.append(form)
        return div

    def render_search_form(self):
        # TODO: Do we need this?
        div = DIV(_id="grid-search", **self.param.grid_class_style.get("grid-search"))
        div.append(self.param.search_form.custom["begin"])
        tr = TR(**self.param.grid_class_style.get("search_form_tr"))
        for field in self.param.search_form.table:
            td = TD(**self.param.grid_class_style.get("search_form_td"))
            if field.type == "boolean":
                td.append(self.param.search_form.custom["widgets"][field.name])
                td.append(field.label)
            else:
                td.append(self.param.search_form.custom["widgets"][field.name])
            if (
                field.name in self.param.search_form.custom["errors"]
                and self.param.search_form.custom["errors"][field.name]
            ):
                td.append(
                    DIV(
                        self.param.search_form.custom["errors"][field.name],
                        _style="color:#ff0000",
                    )
                )
            tr.append(td)
        if self.param.search_button_text:
            tr.append(
                TD(
                    INPUT(
                        _class="button",
                        _type="submit",
                        _value=self.param.search_button_text,
                    ),
                    **self.param.grid_class_style.get("search_form_td"),
                )
            )
        else:
            tr.append(
                TD(
                    self.param.search_form.custom["submit"],
                    **self.param.grid_class_style.get("search_form_td"),
                )
            )
        div.append(TABLE(tr, **self.param.grid_class_style.get("search_form_table")))
        for hidden_widget in self.param.search_form.custom["hidden_widgets"].keys():
            div.append(self.param.search_form.custom["hidden_widgets"][hidden_widget])

        div.append(self.param.search_form.custom["end"])

        return div

    def render_table_header(self):

        up = I(**self.param.grid_class_style.get("grid-sorter-icon-up"))
        dw = I(**self.param.grid_class_style.get("grid-sorter-icon-down"))
        columns = []
        sort_order = request.query.get("orderby", "")

        for index, field in enumerate(self.param.fields):
            if field.readable and (field.type != "id" or self.param.show_id):
                key = "%s.%s" % (field.tablename, field.name)
                heading = (
                    self.param.headings[index]
                    if index < len(self.param.headings)
                    else field.label
                )
                heading = title(heading)
                #  add the sort order query parm
                sort_query_parms = dict(self.query_parms)

                if key == sort_order:
                    sort_query_parms["orderby"] = "~" + key
                    href = URL(self.endpoint, vars=sort_query_parms)
                    col = A(heading, up, _href=href)
                else:
                    sort_query_parms["orderby"] = key
                    href = URL(self.endpoint, vars=sort_query_parms)
                    col = A(heading, dw if "~" + key == sort_order else "", _href=href)
                columns.append((key, col))

        thead = THEAD()
        for key, col in columns:
            col_class = "grid-col-%s" % key
            thead.append(
                TH(
                    col,
                    _class=self.param.grid_class_style.classes.get("grid-th", "")
                    + col_class,
                    _style=self.param.grid_class_style.styles.get("grid-th"),
                )
            )

        if self.param.details or self.param.editable or self.param.deletable:
            thead.append(TH("", **self.param.grid_class_style.get('grid-th-action-button')))

        return thead

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
        key = "%s.%s" % (field.tablename, field.name)
        formatter = (
            self.formatters.get(key)
            or self.formatters_by_type.get(field.type)
            or self.formatters_by_type.get('default')
        )

        class_type = "grid-cell-type-%s" % str(field.type).split(":")[0]
        class_col = "grid-col-%s" % key
        td = TD(
            formatter(field_value),
            _class=(
                self.param.grid_class_style.classes.get("grid-td", "")
                + " "
                + class_type if class_type not in self.param.grid_class_style.classes.get(class_type,
                                                                                          "").split(" ") else ""
                + " "
                + self.param.grid_class_style.classes.get(class_type, "")
                + " "
                + class_col
            ).strip(),
            _style=(
                self.param.grid_class_style.styles.get(class_type)
                or self.param.grid_class_style.styles.get("grid-td")
            ),
        )

        return td

    def render_table_body(self):
        tbody = TBODY()
        for row in self.rows:
            #  find the row id - there may be nested tables....
            if self.use_tablename:
                row_id = row[self.tablename]["id"]
            else:
                row_id = row["id"]

            tr = TR(
                _role="row",
                _class=self.param.grid_class_style.classes.get("grid-tr"),
                _style=self.param.grid_class_style.styles.get("grid-tr"),
            )
            #  add all the fields to the row
            for index, field in enumerate(self.param.fields):
                if field.readable and (field.type != "id" or self.param.show_id):
                    tr.append(self.render_field(row, field, index))

            td = None

            #  add the action buttons
            if (
                (self.param.details and self.param.details != "")
                or (self.param.editable and self.param.editable != "")
                or (self.param.deletable and self.param.deletable != "")
            ):
                classes = (self.param.grid_class_style.classes.get("grid-td", "") +
                           " " +
                           self.param.grid_class_style.classes.get("grid-td-action-button")
                ).strip() 
                styles = (self.param.grid_class_style.styles.get("grid-td", "") +
                           " " +
                           self.param.grid_class_style.styles.get("grid-td-action-button")
                ).strip()
                td = TD(_class=classes, _style=styles)
                if self.param.pre_action_buttons:
                    for btn in self.param.pre_action_buttons:
                        td.append(
                            self.render_action_button(
                                btn.url,
                                btn.text,
                                btn.icon,
                                additional_classes=btn.additional_classes,
                                message=btn.message,
                                row_id=row_id if btn.append_id else None,
                            )
                        )
                if self.param.details and self.param.details != "":
                    if isinstance(
                        self.param.details, str
                    ):
                        details_url = self.param.details
                    else:
                        details_url = self.endpoint + "/details"
                    details_url += "/%s?%s" % (row_id, self.referrer)
                    td.append(
                        self.render_action_button(
                            details_url,
                            "Details",
                            "fa-id-card",
                            name="grid-details-button",
                        )
                    )

                if self.param.editable and self.param.editable != "":
                    if isinstance(self.param.editable, str):
                        edit_url = self.param.editable
                    else:
                        edit_url = self.endpoint + "/edit"
                    edit_url += "/%s?%s" % (row_id, self.referrer)
                    td.append(
                        self.render_action_button(
                            edit_url, "Edit", "fa-edit", name="grid-edit-button"
                        )
                    )

                if self.param.deletable and self.param.deletable != "":
                    if isinstance(self.param.deletable, str):
                        delete_url = self.param.deletable
                    else:
                        delete_url = self.endpoint + "/delete"
                    delete_url += "/%s?%s" % (row_id, self.referrer)
                    td.append(
                        self.render_action_button(
                            delete_url,
                            "Delete",
                            "fa-trash",
                            additional_classes="confirmation",
                            message="Delete record",
                            name="grid-delete-button",
                            _onclick="if(!confirm('sure you want to delete')) return false;",
                        )
                    )
                if self.param.post_action_buttons:
                    for btn in self.param.post_action_buttons:
                        td.append(
                            self.render_action_button(
                                btn.url,
                                btn.text,
                                btn.icon,
                                additional_classes=btn.additional_classes,
                                message=btn.message,
                                row_id=row_id if btn.append_id else None,
                            )
                        )
                tr.append(td)
            tbody.append(tr)

        return tbody

    def render_table_pager(self):
        pager = DIV(**self.param.grid_class_style.get("grid-pagination"))
        previous_page_number = None
        for page_number in self.iter_pages(
            self.current_page_number, self.number_of_pages
        ):
            pager_query_parms = dict(self.query_parms)
            pager_query_parms["page"] = page_number
            # if there is a gat add a spacer
            if previous_page_number and page_number - previous_page_number > 1:
                pager.append(SPAN("...", _style="margin:0 10px;"))
            is_current = self.current_page_number == page_number
            page_name = (
                "grid-pagination-button-current"
                if is_current
                else "grid-pagination-button"
            )
            pager.append(
                A(
                    page_number,
                    **self.param.grid_class_style.get(page_name),
                    _role="button",
                    _href=URL(self.endpoint, vars=pager_query_parms),
                )
            )
            previous_page_number = page_number
        return pager

    def render_table(self):
        html = DIV(**self.param.grid_class_style.get("grid-wrapper"))
        grid_header = DIV(**self.param.grid_class_style.get("grid-header"))

        #  build the New button if needed
        if self.param.create and self.param.create != "":
            if isinstance(self.param.create, str):
                create_url = self.param.create
            else:
                create_url = self.endpoint + "/new"

            grid_header.append(
                self.render_action_button(
                    create_url,
                    "New",
                    "fa-plus",
                    icon_size="normal",
                    override_classes=self.param.grid_class_style.classes.get(
                        "grid-new-button", ""
                    ),
                    override_styles=self.param.grid_class_style.get("new_button"),
                )
            )

        #  build the search form if provided
        if self.param.search_form:
            grid_header.append(self.render_search_form())
        else:
            grid_header.append(self.render_default_form())

        html.append(grid_header)

        table = TABLE(**self.param.grid_class_style.get("grid-table"))

        # build the header
        table.append(self.render_table_header())

        #  build the rows
        table.append(self.render_table_body())

        #  add the table to the html
        html.append(DIV(table, **self.param.grid_class_style.get("grid-table-wrapper")))

        #  add the row counter information
        footer = DIV(**self.param.grid_class_style.get("grid-footer"))

        row_count = DIV(**self.param.grid_class_style.get("grid-info"))
        row_count.append(
            "Displaying rows %s thru %s of %s"
            % (
                self.page_start + 1 if self.number_of_pages > 1 else 1,
                self.page_end
                if self.page_end < self.total_number_of_rows
                else self.total_number_of_rows,
                self.total_number_of_rows,
            )
        )
        footer.append(row_count)

        #  build the pager
        if self.number_of_pages > 1:
            footer.append(self.render_table_pager())

        html.append(footer)
        return XML(html)

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
        return (
            self.db[self.tablename](self.record_id)
            if self.tablename and self.record_id
            else None
        )

    def add_search_query(self, name, query, requires):
        if self.param.search_form:
            raise ValueError(
                "Cannot add search queries if a you provide a search_form to the grid call "
                "or if auto_process is set to True.  Ensure no search_form is set, set "
                "auto_process to False, add your search query and then call grid.process()."
            )

        if self.param.search_queries is None:
            self.param.search_queries = []
        self.param.search_queries.append([name, query, requires])

    def get_tablenames(self, *args):
        """Returns the tablenames used by this grid"""
        return list(self.db._adapter.tables(*args).keys())

    def is_join(self):
        items = [self.param.query]
        if self.param.left is not None:
            if isinstance(self.param.left, (list, tuple)):
                items += [item for item in self.param.left]
            else:
                items += [self.param.left]
        return len(self.get_tablenames(*items)) > 1
