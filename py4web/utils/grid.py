# TODO:
# - details, edit, delete URLs should be signed
#
#
import base64
import copy
from functools import reduce
from urllib.parse import urlparse

from yatl.helpers import (
    CAT,
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
from py4web.utils.form import Form, FormStyleDefault, join_classes
from py4web.utils.param import Param

NAV = TAG.nav
HEADER = TAG.header


def title(text):
    """Turns text into a title"""
    return str(text).replace("_", " ").title()


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
        "grid-thead": "",
        "grid-tr": "",
        "grid-th": "",
        "grid-td": "",
        "grid-td-buttons": "",
        "grid-button": "info",
        "grid-details-button": "grid-details-button info",
        "grid-edit-button": "grid-edit-button info",
        "grid-delete-button": "grid-delete-button info",
        "grid-search-button": "grid-search-button",
        "grid-clear-button": "grid-clear-button",
        "grid-footer": "grid-footer",
        "grid-info": "grid-info",
        "grid-pagination": "grid-pagination",
        "grid-pagination-button": "grid-pagination-button info",
        "grid-pagination-button-current": "grid-pagination-button-current default",
        "grid-cell-type-string": "grid-cell-type-string",
        "grid-cell-type-text": "grid-cell-type-text",
        "grid-cell-type-boolean": "grid-cell-type-boolean",
        "grid-cell-type-float": "grid-cell-type-float",
        "grid-cell-type-decimal": "grid-cell-type-decimal",
        "grid-cell-type-int": "grid-cell-type-int",
        "grid-cell-type-date": "grid-cell-type-date",
        "grid-cell-type-time": "grid-cell-type-time",
        "grid-cell-type-datetime": "grid-cell-type-datetime",
        "grid-cell-type-upload": "grid-cell-type-upload",
        "grid-cell-type-list": "grid-cell-type-list",
        "grid-cell-type-id": "grid-cell-type-id",
        # specific for custom form
        "grid-search-form": "grid-search-form",
        "grid-search-form-table": "grid-search-form-table",
        "grid-search-form-tr": "grid-search-form-tr",
        "grid-search-form-td": "grid-search-form-td",
        "grid-search-boolean": "grid-search-boolean",
    }

    styles = {
        "grid-wrapper": "",
        "grid-header": "display: table; width: 100%;",
        "grid-new-button": "margin-top:4px; height:34px; line-height:34px;",
        "grid-search": "display: table-cell; float:right;",
        "grid-table-wrapper": "overflow-x: auto; width:100%;",
        "grid-table": "",
        "grid-sorter-icon-up": "",
        "grid-sorter-icon-down": "",
        "grid-thead": "",
        "grid-tr": "",
        "grid-th": "white-space: nowrap; vertical-align: middle;",
        "grid-td": "white-space: nowrap; vertical-align: middle;",
        "grid-td-buttons": "",
        "grid-button": "margin-bottom: 0;",
        "grid-details-button": "margin-bottom: 0;",
        "grid-edit-button": "margin-bottom: 0;",
        "grid-delete-button": "margin-bottom: 0;",
        "grid-search-button": "height: 34px;",
        "grid-clear-button": "height: 34px;",
        "grid-footer": "display: table; width:100%;",
        "grid-info": "display: table-cell;",
        "grid-pagination": "display: table-cell; text-align:right;",
        "grid-pagination-button": "min-width: 20px;",
        "grid-pagination-button-current": "min-width: 20px; pointer-events:none; opacity: 0.7;",
        "grid-cell-type-string": "white-space: nowrap; vertical-align: middle; text-align: left; text-overflow: ellipsis; max-width: 200px;",
        "grid-cell-type-text": "vertical-align: middle; text-align: left; text-overflow: ellipsis; max-width: 200px;",
        "grid-cell-type-boolean": "white-space: nowrap; vertical-align: middle; text-align: center;",
        "grid-cell-type-float": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-decimal": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-int": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-date": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-time": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-datetime": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-upload": "white-space: nowrap; vertical-align: middle; text-align: center;",
        "grid-cell-type-list": "white-space: nowrap; vertical-align: middle; text-align: left;",
        "grid-cell-type-int": "white-space: nowrap; vertical-align: middle; text-align: right;",
        # specific for custom form
        "grid-search-form": "",
        "grid-search-form-table": "",
        "grid-search-form-tr": "border-bottom: none;",
        "grid-search-form-td": "",
        "grid-search-boolean": "",
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
        "grid-header": "grid-header pb-2 is-clearfix",
        "grid-new-button": "grid-new-button button",
        "grid-search": "grid-search is-pulled-right pb-2",
        "grid-table-wrapper": "grid-table-wrapper table_wrapper table-container mb-1",
        "grid-table": "grid-table table is-bordered is-striped is-hoverable is-fullwidth is-clearfix",
        "grid-sorter-icon-up": "grid-sort-icon-up fas fa-sort-up is-pulled-right",
        "grid-sorter-icon-down": "grid-sort-icon-down fas fa-sort-down is-pulled-right",
        "grid-thead": "",
        "grid-tr": "",
        "grid-th": "",
        "grid-td": "is-small",
        "grid-td-buttons": "is-small is-narrow",
        "grid-button": "grid-button button is-small",
        "grid-details-button": "grid-details-button button is-small",
        "grid-edit-button": "grid-edit-button button is-small",
        "grid-delete-button": "grid-delete-button button is-small",
        "grid-search-button": "grid-search-button button",
        "grid-clear-button": "grid-clear-button button",
        "grid-footer": "grid-footer pb-8",
        "grid-info": "grid-info is-pulled-left",
        "grid-pagination": "grid-pagination is-pulled-right",
        "grid-pagination-button": "grid-pagination-button button is-small",
        "grid-pagination-button-current": "grid-pagination-button-current button is-primary is-small",
        "grid-cell-type-string": "grid-cell-type-string",
        "grid-cell-type-text": "grid-cell-type-text",
        "grid-cell-type-boolean": "grid-cell-type-boolean has-text-centered",
        "grid-cell-type-float": "grid-cell-type-float",
        "grid-cell-type-decimal": "grid-cell-type-decimal",
        "grid-cell-type-int": "grid-cell-type-int",
        "grid-cell-type-date": "grid-cell-type-date",
        "grid-cell-type-time": "grid-cell-type-time",
        "grid-cell-type-datetime": "grid-cell-type-datetime",
        "grid-cell-type-upload": "grid-cell-type-upload",
        "grid-cell-type-list": "grid-cell-type-list",
        "grid-cell-type-id": "grid-cell-type-id has-text-centered",
        # specific for custom form
        "grid-search-form": "grid-search-form is-pulled-right pb-2",
        "grid-search-form-table": "grid-search-form-table",
        "grid-search-form-tr": "grid-search-form-tr",
        "grid-search-form-td": "grid-search-form-td pr-1",
        "grid-search-boolean": "grid-search-boolean",
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
        "grid-thead": "",
        "grid-tr": "",
        "grid-th": "text-align: center; text-transform: uppercase; vertical-align: bottom;",
        "grid-td": "",
        "grid-td-buttons": "",
        "grid-button": "",
        "grid-details-button": "",
        "grid-edit-button": "",
        "grid-delete-button": "",
        "grid-search-button": "",
        "grid-clear-button": "",
        "grid-footer": "padding-top: .5em; padding-bottom: 2em;",
        "grid-info": "",
        "grid-pagination": "",
        "grid-pagination-button": "margin-left: .25em;",
        "grid-pagination-button-current": "margin-left: .25em;",
        "grid-cell-type-string": "vertical-align: top; text-overflow: ellipsis;",
        "grid-cell-type-text": "vertical-align: top; text-overflow: ellipsis;",
        "grid-cell-type-boolean": "vertical-align: top; text-align: center",
        "grid-cell-type-float": "vertical-align: top; text-align: right",
        "grid-cell-type-decimal": "vertical-align: top; text-align: right",
        "grid-cell-type-int": "vertical-align: top; text-align: center;",
        "grid-cell-type-date": "vertical-align: top; text-align: center;",
        "grid-cell-type-time": "vertical-align: top; text-align: center;",
        "grid-cell-type-datetime": "vertical-align: top; text-align: center;",
        "grid-cell-type-upload": "vertical-align: top; text-align: center;",
        "grid-cell-type-list": "vertical-align: top; text-align: left;",
        "grid-cell-type-id": "",
        # specific for custom form
        "grid-search-form": "",
        "grid-search-form-table": "",
        "grid-search-form-tr": "",
        "grid-search-form-td": "",
        "grid-search-boolean": "padding-top: .5rem;",
    }


class Column:
    """class used to represent a column in a grid"""

    def __init__(
        self,
        name,
        represent,
        required_fields=None,
        orderby=None,
        td_class_style=None,
    ):
        self.name = name
        self.represent = represent
        self.orderby = orderby
        self.required_fields = []
        if required_fields:
            if isinstance(required_fields, list):
                self.required_fields = required_fields
            else:
                self.required_fields = [required_fields]

        self.td_class_style = td_class_style

    def render(self, row, index=None):
        """renders a row al position index (optional)"""
        return self.represent(row)


class Grid:

    FORMATTERS_BY_TYPE = {
        "boolean": lambda value: INPUT(
            _type="checkbox", _checked=value, _disabled="disabled"
        )
        if value
        else "",
        "datetime": lambda value: XML(
            "<script>document.write((new Date(%s,%s,%s,%s,%s,%s)).toLocaleString())</script>"
            % (
                value.year,
                value.month - 1,
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
            % (
                value.year,
                value.month - 1,
                value.day,
            )
        )
        if value
        else "",
        "list:string": lambda value: ", ".join(str(x) for x in value) if value else "",
        "list:integer": lambda value: ", ".join(x for x in value) if value else "",
        "default": lambda value: str(value) if value is not None else "",
    }

    def __init__(
        self,
        path,
        query,
        search_form=None,
        search_queries=None,
        columns=None,
        field_id=None,
        show_id=False,
        orderby=None,
        left=None,
        headings=None,
        create=True,
        details=True,
        editable=True,
        deletable=True,
        validation=None,
        pre_action_buttons=None,
        post_action_buttons=None,
        auto_process=True,
        rows_per_page=15,
        include_action_button_text=True,
        search_button_text="Filter",
        formstyle=FormStyleDefault,
        grid_class_style=GridClassStyle,
        T=lambda text: text,
        # deprecated
        fields=None,
    ):
        """
        Grid is a searchable/sortable/pageable grid

        :param path: The part of the URL to be parsed by this grid
        :param query: the query used to filter the data
        :param search_form: py4web FORM to be included as the search form
        :param search_queries: future use - pass a dict of name and a search query
        :param columns: list of columns to display on the list page, if blank, glean tablename from first query
        :              and use all fields of that table
        :param field_id: the id field of the primary table for the grid - if there are multiple tables (joined)
                            then the table for this field is used as the table for edit/details/delete
        :param show_id: show the record id field on list page - default = False
        :param orderby: pydal orderby field or list of fields
        :param left: if joining other tables, specify the pydal left expression here
        :param headings: list of headings to be used for list page - if not provided use the field label
        :param create: URL to redirect to for creating records - set to False to not display the button
        :param editable: URL to redirect to for editing records - set to False to not display the button
        :param deletable: URL to redirect to for deleting records - set to False to not display the button
        :param validation: optional validation function to pass to create and edit forms
        :param pre_action_buttons: list of Column instances to include before the standard action buttons
        :param post_action_buttons: list of Column instances to include after the standard action buttons
        :param auto_process: True/False - automatically process the sql for the form - if False, user is
                              responsible for calling process().
        :param T: optional pluralize object
        """

        # in case the query is a Table instead
        if isinstance(query, query._db.Table):
            query = query._id != None

        self.path = path or ""
        self.db = query._db
        self.T = T
        self.param = Param(
            query=query,
            columns=columns or fields,
            field_id=field_id,
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
            validation=validation,
            pre_action_buttons=pre_action_buttons,
            post_action_buttons=post_action_buttons,
            rows_per_page=rows_per_page,
            include_action_button_text=include_action_button_text,
            search_button_text=search_button_text,
            formstyle=formstyle,
            grid_class_style=grid_class_style,
            new_sidecar=None,
            new_submit_value=None,
            new_action_button_text="New",
            details_sidecar=None,
            details_submit_value=None,
            details_action_button_text="Details",
            edit_sidecar=None,
            edit_submit_value=None,
            edit_action_button_text="Edit",
            delete_action_button_text="Delete",
        )

        #  instance variables that will be computed
        self.action = None
        self.current_page_number = None
        self.endpoint = request.fullpath
        if self.path:
            self.endpoint = self.endpoint[: -len(self.path)].rstrip("/")
        self.hidden_fields = None
        self.form = None
        self.number_of_pages = None
        self.page_end = None
        self.page_start = None
        self.query_parms = request.params
        self.record_id = None
        self.rows = None
        self.tablename = None
        self.total_number_of_rows = None
        self.use_tablename = self.is_join()
        self.formatters = {}
        self.formatters_by_type = copy.copy(Grid.FORMATTERS_BY_TYPE)
        self.attributes_plugin = AttributesPlugin(request)

        if auto_process:
            self.process()

    def is_editable(self, row):
        if callable(self.param.editable):
            return self.param.editable(row)
        return self.param.editable

    def is_deletable(self, row):
        if callable(self.param.deletable):
            return self.param.deletable(row)
        return self.param.deletable

    def process(self):
        query = None
        db = self.db
        if not self.param.search_form and self.param.search_queries:
            search_type = safe_int(request.query.get("search_type", 0), default=0)
            search_string = request.query.get("search_string")
            if search_type < len(self.param.search_queries) and search_string:
                query_lambda = self.param.search_queries[search_type][1]
                try:
                    query = query_lambda(search_string)
                except:
                    pass  # flash a message here

        if not query:
            query = self.param.query
        else:
            query &= self.param.query

        parts = self.path.split("/")
        self.action = parts[0] or "select"
        if self.param.field_id:
            self.tablename = str(self.param.field_id._table)
        else:
            self.tablename = self.get_tablenames(self.param.query)[0]
            self.param.field_id = db[self.tablename]._id

        self.record_id = safe_int(parts[1] if len(parts) > 1 else None, default=None)

        table = db[self.tablename]
        if not self.param.columns:
            # if no column specified use all fields
            self.param.columns = [field for field in table if field.readable]
            self.needed_fields = self.param.columns[:]
        elif any(isinstance(col, Column) for col in self.param.columns):
            # if we use columns we have to get all fields and assume a single table
            self.needed_fields = [field for field in db[self.tablename]]
            for col in self.param.columns:
                if isinstance(col, Column):
                    for rf in col.required_fields:
                        if rf.longname not in [x.longname for x in self.needed_fields]:
                            self.needed_fields.append(rf)
        elif any(isinstance(col, FieldVirtual) for col in self.param.columns):
            # if virtual fields are specified the fields may come from a join
            needed_fields = set()
            for col in self.param.columns:
                if isinstance(col, Field):
                    needed_fields.add(col)
                elif isinstance(col, FieldVirtual):
                    for field in db[col.tablename]:
                        needed_fields.add(field)
            self.needed_fields = list(needed_fields)
        else:
            self.needed_fields = self.param.columns[:]

        # make sure all specified fields are available
        if self.param.columns:
            for col in self.param.columns:
                if not isinstance(col, (Column, FieldVirtual)):
                    if col.longname not in [x.longname for x in self.needed_fields]:
                        self.needed_fields.append(col)

        # except the primary key may be missing and must be fetched even if not displayed
        if not any(col.name == table._id.name for col in self.needed_fields):
            self.needed_fields.insert(0, table._id)

        self.referrer = None

        if not self.tablename:
            raise HTTP(400)

        # SECURITY: if the record does not exist or does not match query, than we are not allowed
        table = db[self.tablename]
        if self.record_id:
            record = table(self.record_id)
            if not record:
                redirect(self.endpoint)
        else:
            record = None

        if self.action in ["new", "details", "edit"]:

            readonly = self.action == "details"

            attrs = self.attributes_plugin.form(url=request.url.split(":", 1)[1])
            self.form = Form(
                table,
                record=record,
                readonly=readonly,
                deletable=self.param.deletable,
                formstyle=self.param.formstyle,
                validation=self.param.validation,
                show_id=self.param.show_id,
                **attrs,
            )
            if self.action == "new" and self.param.create:
                if self.param.new_sidecar:
                    self.form.param.sidecar.append(self.param.new_sidecar)
                if self.param.new_submit_value:
                    self.form.param.submit_value = self.param.new_submit_value
            if self.action == "details":
                if self.param.details_sidecar:
                    self.form.param.sidecar.append(self.param.details_sidecar)
                if self.param.details_submit_value:
                    self.form.param.submit_value = self.param.details_submit_value
            if self.action == "edit" and self.is_editable(record):
                if self.param.edit_sidecar:
                    self.form.param.sidecar.append(self.param.edit_sidecar)
                if self.param.edit_submit_value:
                    self.form.param.submit_value = self.param.edit_submit_value

            # redirect to the referrer
            if self.form.accepted or (readonly and request.method == "POST"):
                referrer = request.query.get("_referrer")
                if referrer:
                    redirect(base64.b16decode(referrer.encode("utf8")).decode("utf8"))
                else:
                    redirect(self.endpoint)

        elif self.action == "delete" and self.is_deletable(record):
            db(db[self.tablename].id == self.record_id).delete()

            url = parse_referer(request)
            if url and url.query:
                self.endpoint += "?%s" % url.query
            redirect(self.endpoint)

        elif self.action == "select":
            self.referrer = "_referrer=%s" % base64.b16encode(
                request.url.encode("utf8")
            ).decode("utf8")

            #  find the primary key of the primary table
            pt = db[self.tablename]
            key_is_missing = True
            for field in self.param.columns:
                if (
                    isinstance(field, Field)
                    and field.table._tablename == pt._tablename
                    and field.name == pt._id.name
                ):
                    key_is_missing = False
            if key_is_missing:
                #  primary key wasn't included, add it and set show_id to False so it doesn't display
                self.param.columns.append(pt._id)
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

            # get the data
            self.rows = db(query).select(*self.needed_fields, **select_params)

            self.number_of_pages = self.total_number_of_rows // self.param.rows_per_page
            if self.total_number_of_rows % self.param.rows_per_page > 0:
                self.number_of_pages += 1

        if (
            self.param.pre_action_buttons
            or self.param.details
            or self.param.editable
            or self.param.deletable
            or self.param.post_action_buttons
        ):
            self.param.columns.append(
                Column("", self.make_action_buttons, td_class_style="grid-td-buttons")
            )

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

    def _make_action_button(
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
        onclick=None,
        row_id=None,
        name="grid-button",
        row=None,
        ignore_attribute_plugin=False,
        **attrs,
    ):
        separator = "?"
        if row_id:
            url += "/%s" % row_id

        classes = self.param.grid_class_style.classes.get(name, "")
        styles = self.param.grid_class_style.styles.get(name, "")

        def join_style(items):
            return "".join(items) if isinstance(items, (list, tuple)) else " %s" % items

        if callable(additional_classes):
            additional_classes = additional_classes(row)

        if callable(additional_styles):
            additional_styles = additional_styles(row)

        if callable(override_classes):
            override_classes = override_classes(row)

        if callable(override_styles):
            override_styles = override_styles(row)

        if override_classes:
            classes = join_classes(override_classes)
        elif additional_classes:
            classes = join_classes(classes, additional_classes)
        if override_styles:
            styles = join_style(override_styles)
        elif additional_styles:
            styles += join_style(additional_styles)

        if callable(url):
            url = url(row)

        if ignore_attribute_plugin:
            attrs.update({"_href": url})
        else:
            attrs.update(self.attributes_plugin.link(url=url))

        link = A(
            I(_class="fa %s" % icon),
            _role="button",
            _class=classes,
            _message=message,
            _title=button_text,
            _style=styles,
            **attrs,
        )
        if self.param.include_action_button_text:
            link.append(
                SPAN(XML("&nbsp;"), button_text, _class="grid-action-button-text")
            )

        return link

    def _make_default_form(self):
        search_type = safe_int(request.query.get("search_type", 0), default=0)
        search_string = request.query.get("search_string")
        options = [
            OPTION(items[0], _value=k, _selected=(k == search_type))
            for k, items in enumerate(self.param.search_queries)
        ]
        hidden_fields = [
            INPUT(_name=key, _value=request.query.get(key), _type="hidden")
            for key in request.query
            if not key in ("search_type", "search_string")
        ]
        attrs = self.attributes_plugin.form(url=self.endpoint)
        form = FORM(*hidden_fields, **attrs)
        select = SELECT(
            *options,
            **dict(
                _name="search_type",
            ),
        )
        input = INPUT(
            _type="text",
            _name="search_string",
            _value=search_string,
        )
        sc = self.param.grid_class_style.get("grid-search-button")
        submit = INPUT(_type="submit", _value=self.T("Search"), **sc)
        clear_script = "document.querySelector('[name=search_string]').value='';"
        sc = self.param.grid_class_style.get("grid-clear-button")
        clear = INPUT(
            _type="submit", _value=self.T("Clear"), _onclick=clear_script, **sc
        )
        div = DIV(_id="grid-search", **self.param.grid_class_style.get("grid-search"))

        sc = self.param.grid_class_style.get("grid-search-form-tr")
        tr = TR(**sc)
        sc = self.param.grid_class_style.get("grid-search-form-td")
        if len(options) > 1:
            tr.append(TD(select, **sc))
        tr.append(TD(input, **sc))
        tr.append(TD(submit, clear, **sc))
        sc = self.param.grid_class_style.get("grid-search-form-table")
        form.append(TABLE(tr, **sc))
        div.append(form)
        return div

    def _make_search_form(self):
        # TODO: Do we need this?
        div = DIV(_id="grid-search", **self.param.grid_class_style.get("grid-search"))
        div.append(self.param.search_form.custom["begin"])
        tr = TR(**self.param.grid_class_style.get("grid-search-form-tr"))
        for field in self.param.search_form.table:
            td = TD(**self.param.grid_class_style.get("grid-search-form-td"))
            if field.type == "boolean":
                sb = DIV(**self.param.grid_class_style.get("grid-search-boolean"))
                sb.append(self.param.search_form.custom["widgets"][field.name])
                sb.append(field.label)
                td.append(sb)
            else:
                td.append(self.param.search_form.custom["wrappers"][field.name])
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
                        _value=self.T(self.param.search_button_text),
                    ),
                    **self.param.grid_class_style.get("grid-search-form-td"),
                )
            )
        else:
            tr.append(
                TD(
                    self.param.search_form.custom["submit"],
                    **self.param.grid_class_style.get("grid-search-form-td"),
                )
            )
        div.append(
            TABLE(tr, **self.param.grid_class_style.get("grid-search-form-table"))
        )
        for hidden_widget in self.param.search_form.custom["hidden_widgets"].keys():
            div.append(self.param.search_form.custom["hidden_widgets"][hidden_widget])

        div.append(self.param.search_form.custom["end"])

        return div

    def _make_table_header(self):
        sort_order = request.query.get("orderby", "")

        thead = THEAD(_class=self.param.grid_class_style.classes.get("grid-thead", ""))
        for index, column in enumerate(self.param.columns):
            col = None
            if isinstance(column, (Field, FieldVirtual)):
                field = column
                if field.readable and (field.type != "id" or self.param.show_id):
                    key, col = self._make_field_header(column, index, sort_order)
            elif isinstance(column, Column):
                key = column.name.lower().replace(" ", "-")
                col = column.name
                if column.orderby:
                    key, col = self._make_field_header(column, index, sort_order)
            else:
                raise RuntimeError("Invalid Grid Column type")
            if col is not None:
                classes = join_classes(
                    self.param.grid_class_style.classes.get("grid-th"),
                    "grid-col-%s" % key,
                )
                style = self.param.grid_class_style.styles.get("grid-th")
                thead.append(TH(col, _class=classes, _style=style))

        return thead

    def _make_field_header(self, field, field_index, sort_order):
        up = I(**self.param.grid_class_style.get("grid-sorter-icon-up"))
        dw = I(**self.param.grid_class_style.get("grid-sorter-icon-down"))

        if isinstance(field, Column):
            key = str(field.orderby)
        else:
            key = "%s.%s" % (field.tablename, field.name)

        heading = (
            self.param.headings[field_index]
            if field_index < len(self.param.headings)
            else field.label
            if "label" in field.__dict__
            else field.name
        )
        heading = title(heading)
        #  add the sort order query parm
        sort_query_parms = dict(self.query_parms)

        attrs = {}
        if isinstance(field, FieldVirtual):
            col = SPAN(heading)
        elif key == sort_order:
            sort_query_parms["orderby"] = "~" + key
            url = URL(self.endpoint, vars=sort_query_parms)
            attrs = self.attributes_plugin.link(url=url)
            col = A(heading, up, **attrs)
        else:
            sort_query_parms["orderby"] = key
            url = URL(self.endpoint, vars=sort_query_parms)
            attrs = self.attributes_plugin.link(url=url)
            col = A(heading, dw if "~" + key == sort_order else "", **attrs)
        return key, col

    def _make_field(self, row, field, field_index):
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
        if isinstance(field, FieldVirtual):
            #  handle virtual fields in table display
            if self.use_tablename:
                field_value = field.f(row[field.tablename])
            else:
                field_value = field.f(row)
        elif self.use_tablename:
            field_value = row[field.tablename][field.name]
        else:
            field_value = row[field.name]
        key = "%s.%s" % (field.tablename, field.name)
        formatter = (
            self.formatters.get(key)
            or self.formatters_by_type.get(field.type)
            or self.formatters_by_type.get("default")
        )

        class_type = "grid-cell-type-%s" % str(field.type).split(":")[0].split("(")[0]
        class_col = " grid-col-%s" % key.replace(".", "_")
        classes = join_classes(
            self.param.grid_class_style.classes.get("grid-td"),
            self.param.grid_class_style.classes.get(class_type),
            class_col,
        )
        td = TD(
            formatter(field_value)
            if formatter.__code__.co_argcount == 1  # if formatter has only 1 argument
            else formatter(field_value, row),
            _class=classes,
            _style=(
                self.param.grid_class_style.styles.get(class_type)
                or self.param.grid_class_style.styles.get("grid-td")
            ),
        )

        return td

    def _make_table_body(self):
        tbody = TBODY()
        for row in self.rows:
            #  find the row id - there may be nested tables....
            if self.use_tablename and self.tablename in row and "id" not in row:
                row_id = row[self.tablename]["id"]
            else:
                row_id = row["id"]
                self.use_tablename = False

            key = "%s.%s" % (self.tablename, "__row")
            if self.formatters.get(key):
                extra_class = self.formatters.get(key)(row)["_class"]
                extra_style = self.formatters.get(key)(row)["_style"]
            else:
                extra_class = ""
                extra_style = ""
            tr = TR(
                _role="row",
                _class=join_classes(
                    self.param.grid_class_style.classes.get("grid-tr"), extra_class
                ),
                _style=join_classes(
                    self.param.grid_class_style.styles.get("grid-tr"), extra_style
                ),
            )
            #  add all the fields to the row
            for index, column in enumerate(self.param.columns):
                if isinstance(column, (Field, FieldVirtual)):
                    field = column
                    if field.readable and (field.type != "id" or self.param.show_id):
                        tr.append(self._make_field(row, field, index))
                elif isinstance(column, Column):
                    classes = self.param.grid_class_style.classes.get(
                        column.td_class_style,
                        self.param.grid_class_style.classes.get("grid-td"),
                    )
                    style = self.param.grid_class_style.styles.get(
                        column.td_class_style,
                        self.param.grid_class_style.styles.get("grid-td"),
                    )
                    tr.append(
                        TD(column.render(row, index), _class=classes, _style=style)
                    )

            td = None
            tbody.append(tr)

        return tbody

    def make_action_buttons(self, row):
        cat = CAT()
        row_id = row[self.param.field_id] if self.param.field_id else row.id
        if self.param.pre_action_buttons and len(self.param.pre_action_buttons) > 0:
            for btn in self.param.pre_action_buttons:
                if callable(btn):
                    # a button can be a callable, to indicate whether or not a button should
                    # be displayed. call the function with the row object
                    btn = btn(row)
                    if btn == None:
                        # if None was returned, no button is available for this row: ignore this value in the
                        # list
                        continue
                cat.append(
                    self._make_action_button(
                        url=btn.url,
                        button_text=self.T(btn.text),
                        icon=btn.icon,
                        additional_classes=btn.additional_classes,
                        message=btn.message,
                        row_id=row_id if btn.append_id else None,
                        row=row,
                        ignore_attribute_plugin=btn.ignore_attribute_plugin
                        if "ignore_attribute_plugin" in btn.__dict__
                        else False,
                    )
                )

        if self.param.details:
            if isinstance(self.param.details, str):
                details_url = self.param.details
            else:
                details_url = self.endpoint + "/details"
            details_url += "/%s?%s" % (row_id, self.referrer)
            cat.append(
                self._make_action_button(
                    url=details_url,
                    button_text=self.T(self.param.details_action_button_text),
                    icon="fa-id-card",
                    name="grid-details-button",
                )
            )
        if self.param.editable:
            if isinstance(self.param.editable, str):
                edit_url = self.param.editable
            else:
                edit_url = self.endpoint + "/edit"
            edit_url += "/%s?%s" % (row_id, self.referrer)
            cat.append(
                self._make_action_button(
                    url=edit_url,
                    button_text=self.T(self.param.edit_action_button_text),
                    icon="fa-edit",
                    name="grid-edit-button",
                    _disabled=not self.is_editable(row),
                )
            )
        if self.param.deletable:
            if isinstance(self.param.deletable, str):
                delete_url = self.param.deletable
            else:
                delete_url = self.endpoint + "/delete"
            delete_url += "/%s?%s" % (row_id, self.referrer)
            attrs = self.attributes_plugin.confirm(
                message=self.T("Are you sure you want to delete?")  # FIXME
            )
            cat.append(
                self._make_action_button(
                    url=delete_url,
                    button_text=self.T(self.param.delete_action_button_text),
                    icon="fa-trash",
                    additional_classes="confirmation",
                    message="Delete record",
                    name="grid-delete-button",
                    _disabled=not self.is_deletable(row),
                    **attrs,
                )
            )

        if self.param.post_action_buttons and len(self.param.post_action_buttons) > 0:
            for btn in self.param.post_action_buttons:
                if callable(btn):
                    # a button can be a callable, to indicate whether or not a button should
                    # be displayed. call the function with the row object
                    btn = btn(row)
                    if btn == None:
                        # if None was returned, no button is available for this row: ignore this value in the
                        # list
                        continue
                cat.append(
                    self._make_action_button(
                        url=btn.url,
                        button_text=self.T(btn.text),
                        icon=btn.icon,
                        additional_classes=btn.additional_classes,
                        message=btn.message,
                        row_id=row_id if btn.append_id else None,
                        row=row,
                        ignore_attribute_plugin=btn.ignore_attribute_plugin
                        if "ignore_attribute_plugin" in btn.__dict__
                        else False,
                    )
                )

        return cat

    def _make_table_pager(self):
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
            attrs = self.attributes_plugin.link(
                url=URL(self.endpoint, vars=pager_query_parms)
            )
            pager.append(
                A(
                    page_number,
                    **self.param.grid_class_style.get(page_name),
                    _role="button",
                    **attrs,
                )
            )
            previous_page_number = page_number
        return pager

    def _make_table(self):

        html = DIV(**self.param.grid_class_style.get("grid-wrapper"))
        grid_header = DIV(**self.param.grid_class_style.get("grid-header"))

        #  build the New button if needed
        if self.param.create and self.param.create != "":
            if isinstance(self.param.create, str):
                create_url = self.param.create
            else:
                create_url = self.endpoint + "/new"

            create_url += "?%s" % self.referrer

            grid_header.append(
                self._make_action_button(
                    create_url,
                    self.T(self.param.new_action_button_text),
                    "fa-plus",
                    icon_size="normal",
                    override_classes=self.param.grid_class_style.classes.get(
                        "grid-new-button", ""
                    ),
                    override_styles=self.param.grid_class_style.styles.get(
                        "grid-new-button"
                    ),
                )
            )

        #  build the search form if provided
        if self.param.search_form:
            grid_header.append(self._make_search_form())
        elif self.param.search_queries and len(self.param.search_queries) > 0:
            grid_header.append(self._make_default_form())

        html.append(grid_header)

        table = TABLE(**self.param.grid_class_style.get("grid-table"))

        # build the header
        table.append(self._make_table_header())

        #  build the rows
        table.append(self._make_table_body())

        #  add the table to the html
        html.append(DIV(table, **self.param.grid_class_style.get("grid-table-wrapper")))

        #  add the row counter information
        footer = DIV(**self.param.grid_class_style.get("grid-footer"))

        row_count = DIV(**self.param.grid_class_style.get("grid-info"))
        row_count.append(
            str(self.T("Displaying rows %s thru %s of %s"))
            % (
                self.page_start + 1 if self.number_of_pages > 1 else 1,
                self.page_end
                if self.page_end < self.total_number_of_rows
                else self.total_number_of_rows,
                self.total_number_of_rows,
            )
        ) if self.number_of_pages > 0 else row_count.append("No rows to display")
        footer.append(row_count)

        #  build the pager
        if self.number_of_pages > 1:
            footer.append(self._make_table_pager())

        html.append(footer)
        return html

    def render(self):
        """
        build the query table

        :return: html representation of the table or the py4web Form object
        """
        if self.action == "select":
            return XML(self._make_table())
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


def parse_referer(r):
    """
    Get the referrer from the request query and use urlparse to parse it into a url object

    :param r: The request object to be interrogated

    :return: the URL object or None if no URL object obtained/decoded
    """
    referrer = r.query.get("_referrer")
    url = None
    if referrer:
        url_string = base64.b16decode(referrer.encode("utf8")).decode("utf8")
        if url_string:
            url = urlparse(url_string)

    return url


def get_parent(path, parent_field):
    """
    try to find the parent id for a parent/child table relationship

    :param path: the path var from the method calling the grid
    :param child_table: the child table of the parent/child relationship ex. db.child_table
    :param parent_field_name: this is the name of the field in the child table that points to the parent table
                              this is a string value

    :return parent_id: the id of the parent record
    """
    parent_id = request.query.get("parent_id")

    child_table = parent_field._table
    fn = parent_field.name

    #  find the record id of the parent from the child table record
    if path:
        parts = path.split("/")
        record_id = parts[1] if len(parts) > 1 else None
        if record_id:
            r = child_table(record_id)
            if r:
                parent_id = r[fn]

    #  not passed in, check in the form
    if not parent_id:
        parent_id = request.forms.get(fn)

    #  not found yet, check in the referer
    if not parent_id:
        referrer = request.query.get("_referrer")
        if referrer:
            kvp = base64.b16decode(referrer.encode("utf8")).decode("utf8")
            if "parent_id" in kvp:
                parent_id = kvp.split("parent_id=")[1]

    try:
        parent_id = parent_id.split("&")[0]
    except:
        pass

    return parent_id


class AttributesPlugin:
    def __init__(self, target_element=None):
        self.target_element = target_element
        self.default_attrs = {}

    def form(self, url):
        attrs = copy.copy(self.default_attrs)
        return attrs

    def link(self, url):
        attrs = copy.copy(self.default_attrs)
        attrs["_href"] = url
        return attrs

    def confirm(self, message):
        attrs = copy.copy(self.default_attrs)
        attrs["_onclick"] = "if(!confirm('%s')) return false;" % message
        return attrs


class AttributesPluginHtmx(AttributesPlugin):
    def __init__(self, target_element):
        super().__init__(target_element)
        self.default_attrs = {
            "_hx-target": self.target_element,
            "_hx-swap": "innerHTML",
        }

    def form(self, url):
        attrs = copy.copy(self.default_attrs)
        attrs["_hx-post"] = url
        attrs["_hx-encoding"] = "multipart/form-data"
        return attrs

    def link(self, url):
        attrs = copy.copy(self.default_attrs)
        attrs["_hx-get"] = url
        return attrs

    def confirm(self, message):
        attrs = copy.copy(self.default_attrs)
        attrs["_hx-confirm"] = message
        return attrs
