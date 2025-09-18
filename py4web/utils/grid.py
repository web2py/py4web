# TODO:
# - details, edit, delete URLs should be signed
#
#
import base64
import copy
import datetime
import functools
import re
from urllib.parse import urlparse

from pydal.objects import Expression, Field, FieldVirtual
from pydal.querybuilder import QueryBuilder
from yatl.helpers import (
    CAT,
    DIV,
    FORM,
    INPUT,
    OPTION,
    SELECT,
    SPAN,
    TABLE,
    TAG,
    TBODY,
    TD,
    TH,
    THEAD,
    TR,
    XML,
    A,
    I,
)

from py4web import HTTP, URL, redirect, request, safely
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


def query_join(a, b):
    return a + ("&" if "?" in a else "?") + b


def make_default_search_query(table):
    field_aliases = {
        str(field.label).replace(" ", "_").lower(): field.name
        for field in table
        if field.readable
    }
    builder = QueryBuilder(table, field_aliases=field_aliases)
    return ["Query", lambda text, builder=builder: builder.parse(text), None]


def strip_field_type(type_name, regex=re.compile(r"^\w+")):
    """list:string -> list, reference table->reference, decimal(3,7)->decimal"""
    return regex.match(str(type_name)).group()


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
        "grid-back-button": "info",
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
        "grid-search-form-input": "grid-search-form-input",
        "grid-search-form-select": "grid-search-form-select",
        "grid-search-form-error": "py4web-validation-error",
        "grid-search-boolean": "grid-search-boolean",
        "grid-header-element": "grid-header-element info",
        "grid-footer-element": "grid-footer-element info",
    }

    @classmethod
    def get(cls, element, default=None):
        """returns a dict with _class and _style for the element name"""
        return cls.classes.get(element, element if default is None else default)


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
        "grid-back-button": "grid-button button",
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
        "grid-search-form-input": "grid-search-form-input input",
        "grid-search-form-select": "grid-search-form-input control select",
        "grid-search-form-error": "py4web-validation-error",
        "grid-search-boolean": "grid-search-boolean",
        "grid-header-element": "grid-header-element button",
        "grid-footer-element": "grid-footer-element button",
    }


class GridClassStyleBootstrap5(GridClassStyle):
    """The Grid style for Bootstrap 5"""

    classes = {
        "grid-wrapper": "grid-wrapper",
        "grid-header": "grid-header clearfix pb-2",
        "grid-new-button": "grid-new-button btn btn-outline-primary",
        "grid-search": "grid-search float-end pb-2",
        "grid-table-wrapper": "grid-table-wrapper table-responsive",
        "grid-table": "grid-table table table-striped table-hover table-bordered clearfix",
        "grid-sorter-icon-up": "grid-sort-icon-up fas fa-sort-up float-end",
        "grid-sorter-icon-down": "grid-sort-icon-down fas fa-sort-down float-end",
        "grid-thead": "",
        "grid-tr": "",
        "grid-th": "small",
        "grid-td": "small",
        "grid-td-buttons": "",
        "grid-back-button": "grid-button btn",
        "grid-button": "grid-button btn btn-sm btn-outline-secondary",
        "grid-details-button": "grid-details-button btn btn-sm btn-outline-secondary",
        "grid-edit-button": "grid-edit-button btn btn-sm btn-outline-secondary",
        "grid-delete-button": "grid-delete-button btn btn-sm btn-outline-secondary",
        "grid-search-button": "grid-search-button btn btn-outline-info",
        "grid-clear-button": "grid-clear-button btn btn-outline-info",
        "grid-footer": "grid-footer pb-8",
        "grid-info": "grid-info float-start",
        "grid-pagination": "grid-pagination float-end",
        "grid-pagination-button": "grid-pagination-button btn btn-sm btn-outline-primary",
        "grid-pagination-button-current": "grid-pagination-button-current btn btn-primary btn-sm",
        "grid-cell-type-string": "grid-cell-type-string",
        "grid-cell-type-text": "grid-cell-type-text",
        "grid-cell-type-boolean": "grid-cell-type-boolean text-center",
        "grid-cell-type-float": "grid-cell-type-float",
        "grid-cell-type-decimal": "grid-cell-type-decimal",
        "grid-cell-type-int": "grid-cell-type-int",
        "grid-cell-type-date": "grid-cell-type-date",
        "grid-cell-type-time": "grid-cell-type-time",
        "grid-cell-type-datetime": "grid-cell-type-datetime",
        "grid-cell-type-upload": "grid-cell-type-upload",
        "grid-cell-type-list": "grid-cell-type-list",
        "grid-cell-type-id": "grid-cell-type-id text-center",
        # specific for custom form
        "grid-search-form": "grid-search-form float-end pb-2",
        "grid-search-form-table": "grid-search-form-table",
        "grid-search-form-tr": "grid-search-form-tr",
        "grid-search-form-td": "grid-search-form-td pr-1",
        "grid-search-form-input": "grid-search-form-input form-control",
        "grid-search-form-select": "grid-search-form-input control select",
        "grid-search-form-error": "py4web-validation-error",
        "grid-search-boolean": "grid-search-boolean",
        "grid-header-element": "grid-header-element btn btn-sm",
        "grid-footer-element": "grid-footer-element btn btn-sm",
    }


class IconStyle:
    sort_up = "icon-sort-up"
    sort_down = "icon-sort-down"
    add_button = "icon-add-button"
    details_button = "icon-details-button"
    edit_button = "icon-edit-button"
    delete_button = "icon-delete-button"

    @classmethod
    def complete(self, icontxt: str) -> str:
        return icontxt


class IconStyleFontawsome(IconStyle):
    sort_up = "fas fa-sort-up"
    sort_down = "fas fa-sort-down"
    add_button = "fas fa-plus"
    details_button = "fas fa-id-card"
    edit_button = "fas fa-edit"
    delete_button = "fas fa-trash"

    @classmethod
    def complete(self, icontxt: str) -> str:
        if "fas " not in icontxt:
            return f"fas {icontxt}"
        return icontxt


class IconStyleBootstrapIcons(IconStyle):
    sort_up = "bi bi-sort-up"
    sort_down = "bi bi-sort-down"
    add_button = "bi bi-plus"
    details_button = "bi bi-person-vcard"
    edit_button = "bi bi-pencil-square"
    delete_button = "bi bi-trash"

    @classmethod
    def complete(self, icontxt: str) -> str:
        if "bi " not in icontxt:
            return f"bi {icontxt}"
        return icontxt


class GridClassStyleTailwind(GridClassStyle):
    classes = {
        "grid-wrapper": "grid-wrapper space-y-4 bg-white shadow-md rounded-lg p-4",
        "grid-header": "grid-header flex justify-between items-center pb-4 border-b border-gray-300",
        "grid-new-button": "grid-new-button px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600",
        "grid-search": "grid-search flex items-center gap-2",
        "grid-table-wrapper": "grid-table-wrapper overflow-x-auto",
        "grid-table": "grid-table w-full border-collapse bg-white shadow-md rounded-lg overflow-hidden",
        "grid-sorter-icon-up": "grid-sort-icon-up fas fa-sort-up text-gray-600",
        "grid-sorter-icon-down": "grid-sort-icon-down fas fa-sort-down text-gray-600",
        "grid-thead": "bg-gray-200 text-gray-700",
        "grid-tr": "border-b border-gray-300",
        "grid-th": "px-4 py-2 text-left font-semibold",
        "grid-td": "px-4 py-2 text-gray-700",
        "grid-td-buttons": "px-4 py-2 flex gap-2",
        "grid-back-button": "px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 shadow",
        "grid-button": "px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 shadow",
        "grid-details-button": "px-3 py-1 bg-gray-500 text-white rounded hover:bg-gray-600 shadow",
        "grid-edit-button": "px-3 py-1 bg-yellow-500 text-white rounded hover:bg-yellow-600 shadow",
        "grid-delete-button": "px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600 shadow",
        "grid-search-button": "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition",
        "grid-clear-button": "px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600 transition",
        "grid-footer": "grid-footer flex justify-between items-center pt-4 border-t border-gray-300",
        "grid-info": "grid-info text-gray-600",
        "grid-pagination": "grid-pagination flex gap-2",
        "grid-pagination-button": "px-3 py-1 bg-gray-200 rounded hover:bg-gray-300",
        "grid-pagination-button-current": "px-3 py-1 bg-blue-500 text-white rounded",
        # Cell styling
        "grid-cell-type-string": "text-left",
        "grid-cell-type-text": "text-left",
        "grid-cell-type-boolean": "text-center",
        "grid-cell-type-float": "text-right",
        "grid-cell-type-decimal": "text-right",
        "grid-cell-type-int": "text-right",
        "grid-cell-type-date": "text-center",
        "grid-cell-type-time": "text-center",
        "grid-cell-type-datetime": "text-center",
        "grid-cell-type-upload": "text-center",
        "grid-cell-type-list": "text-left",
        "grid-cell-type-id": "text-center",
        # Search form
        "grid-search-form": "flex flex-wrap gap-2 items-center border p-2 rounded-lg bg-gray-100",
        "grid-search-form-table": "w-full",
        "grid-search-form-tr": "border-b border-gray-300",
        "grid-search-form-td": "p-2",
        "grid-search-form-input": "px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 w-full",
        "grid-search-form-select": "px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 w-full",
        "grid-search-form-error": "p-2",
        "grid-search-boolean": "form-checkbox h-5 w-5 text-blue-600",
        "grid-header-element": "px-3 py-1 bg-gray-500 text-white rounded hover:bg-gray-600",
        "grid-footer-element": "px-3 py-1 bg-gray-500 text-white rounded hover:bg-gray-600",
    }


class Column:
    """class used to represent a column in a grid"""

    def __init__(
        self,
        name,
        represent_col,
        key=None,
        required_fields=None,  # must be a list or none
        orderby=None,
        col_type="string",
        td_class_style=None,
    ):
        self.name = name
        self.represent_col = represent_col
        self.orderby = orderby
        self.required_fields = required_fields or []
        self.key = key
        # col type is not quite a field type but we support field types
        self.type = col_type
        self.td_class_style = td_class_style


def maybe_call(obj, *args, **kwargs):
    """If the object is callable, call it with the args, kwargs"""
    if not callable(obj):
        return obj
    return obj(*args, **kwargs)


def reference_represent(field, value):
    """
    Assumes value is a pydal.objects.Reference value and represts is using the
    table._format of the referenced table
    """
    if not value:
        return ""
    table = field.referenced_table()
    if not table:
        return "#{value}"
    row = table(value)
    if not row:
        return "#{value}(missing)"
    if isinstance(table._format, str):
        return table._format % row
    elif callable(table._format):
        return table._format(row)
    return str(value)


def datetime_represent(value):
    """Represents a datetime value"""
    if not value or not isinstance(value, datetime.datetime):
        return value or ""
    return XML(
        "<script>document.currentScript.insertAdjacentText('afterend',"
        f"(new Date('{value.isoformat(timespec='seconds')}')).toLocaleString())</script>"
    )


def date_represent(value):
    """Represents a date value"""
    if not value or not isinstance(value, datetime.date):
        return value or ""
    return XML(
        "<script>document.currentScript.insertAdjacentText('afterend',"
        f"(new Date('{value.isoformat()}')).toLocaleDateString())</script>"
    )


def time_represent(value):
    """Represents a time value"""
    if not value or not isinstance(value, datetime.time):
        return value or ""
    return XML(
        "<script>document.currentScript.insertAdjacentText('afterend',"
        f"(new Date('0000T{value.isoformat('seconds')}')).toLocaleTimeString())</script>"
    )


class Grid:
    represent_by_type = {
        "id": lambda field, value: f"#{value}",
        "boolean": lambda field, value: "☑" if value else "☐" if value is False else "",
        "integer": lambda field, value: str(value) if value is not None else "",
        "bigint": lambda field, value: str(value) if value is not None else "",
        "float": lambda field, value: "%.2f" % value if value is not None else "",
        "double": lambda field, value: "%.2f" % value if value is not None else "",
        "decimal": lambda field, value: "%.2f" % value if value is not None else "",
        "reference": reference_represent,
        "big-reference": reference_represent,
        "datetime": lambda field, value: datetime_represent(value),
        "date": lambda field, value: date_represent(value),
        "time": lambda field, value: time_represent(value),
        "list": lambda field, value: ", ".join(str(x) for x in value) or "",
        "password": lambda field, value: "******",
    }

    def __init__(
        self,
        query,
        search_form=None,
        search_queries=None,
        columns=None,
        field_id=None,
        show_id=None,
        orderby=None,
        left=None,
        headings=None,
        create=True,
        details=True,
        editable=True,
        deletable=True,
        validation=None,
        required_fields=None,
        pre_action_buttons=None,
        post_action_buttons=None,
        auto_process=True,
        rows_per_page=15,
        include_action_button_text=True,
        search_button_text="Filter",
        formstyle=FormStyleDefault,
        grid_class_style=GridClassStyle,
        icon_style=IconStyleFontawsome,
        T=lambda text: text,
        groupby=None,
        # deprecated
        fields=None,
        form_maker=Form,
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

        if show_id is None:
            show_id = fields and any(field.type == "id" for field in fields)

        self.param = Param(
            columns=columns or fields,
            field_id=field_id,
            show_id=show_id,
            orderby=orderby,
            left=left,
            groupby=groupby,
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
            new_action_button_text=T("New"),
            details_sidecar=None,
            details_submit_value=T("Back"),
            details_action_button_text=T("Details"),
            edit_sidecar=None,
            edit_submit_value=None,
            edit_action_button_text=T("Edit"),
            delete_action_button_text=T("Delete"),
            delete_submit_value=T("Confirm Delete"),
            back_button_value=T("Back"),
            header_elements=None,
            footer_elements=None,
            required_fields=required_fields or [],
            icon_style=icon_style,
        )

        # in case the query is a Table insteance
        if isinstance(query, query._db.Table):
            query = query._id != None

        #  instance variables that will be computed
        self.db = query._db  # the database
        self.query = query  # the filter query
        self.query_parms = safely(lambda: request.params, default={})
        self.search_query_error = None  # error to be displayed in case failed search
        self.T = T  # the translator
        self.form_maker = form_maker  # the object that makes forms
        self.this_url = None  # page referring this one
        self.mode = None  # select, new, details, edit, delete
        self.table = None  # selected table
        self.tablename = None  # name of the selected table
        self.total_number_of_rows = None  # total number of rows
        self.rows = None  # selected rows
        self.number_of_pages = None  # total number of pages for pagination
        self.current_page_number = None  # number of the current page
        self.page_end = None  # index of last element in page
        self.page_start = None  # index of first element in page
        self.record_id = None  # the record id to display or None
        self.record = None  # the record to display or None
        self.form = None  # the edit, new, details form
        self.hidden_fields = None  # hidden fields to be embedded in form
        self.represent_by_type = copy.copy(Grid.represent_by_type)

        if auto_process:
            self.process()

    def is_creatable(self):
        return False if self.param.groupby else maybe_call(self.param.create)

    def is_editable(self, row):
        return (
            False
            if not row or self.param.groupby
            else maybe_call(self.param.editable, row)
        )

    def is_readable(self, row):
        return False if not row else maybe_call(self.param.details, row)

    def is_deletable(self, row):
        return (
            False
            if not row or self.param.groupby
            else maybe_call(self.param.deletable, row)
        )

    def get_style(self, element, default=None):
        return self.param.grid_class_style.get(element, default)

    @staticmethod
    def parse(query):
        mode = query.get("mode", "select")
        record_id = query.get("id", None)
        if record_id and mode == "select":
            mode = "details"
        referrer = query.get("referrer")
        if referrer:
            referrer = base64.b16decode(referrer.encode("utf8")).decode("utf8")
        return {"mode": mode, "record_id": record_id, "referrer": referrer}

    def process(self):
        query = None
        db = self.db
        self.search_query_error = None

        parsed = Grid.parse(request.query)
        self.mode = parsed["mode"]
        self.record_id = parsed["record_id"]
        self.referrer = parsed["referrer"]
        # check invalid parameters]
        if self.mode not in ("new", "edit", "select", "details", "delete"):
            raise HTTP(400)
        elif self.mode in ("edit", "details", "delete") and self.record_id is None:
            raise HTTP(400)

        if self.param.field_id:
            self.tablename = str(self.param.field_id._table)
        else:
            self.tablename = self._get_tablenames(self.query)[0]
            self.param.field_id = db[self.tablename]._id

        if not self.tablename:
            raise HTTP(400)

        # SECURITY: if the record does not exist or does not match query, than we are not allowed
        self.table = db[self.tablename]

        # if we have a record id retrieve the record
        if self.record_id:
            self.record = self.table(self.record_id)
            if not self.record:
                redirect(URL())
        else:
            self.record = None

        #  ensure the user has access for new/details/edit/delete if chosen
        if self.mode == "select":
            self._handle_mode_select()
        elif self.mode == "new":
            self._handle_mode_new()
        elif self.mode == "details":
            self._handle_mode_details()
        elif self.mode == "edit":
            self._handle_mode_edit()
        elif self.mode == "delete":
            self._handle_mode_delete()

    def _handle_mode_new(self):
        if not self.is_creatable():
            raise HTTP(
                403,
                f"You do not have access to create a record in the {self.tablename} table.",
            )
        self.form = self._make_form(readonly=False)
        if self.param.new_sidecar:
            self.form.param.sidecar.append(self.param.new_sidecar)
        if self.param.new_submit_value:
            self.form.param.submit_value = self.param.new_submit_value
        self._handle_redirect_to_referrer(True, False)

    def _handle_mode_details(self):
        if not self.is_readable(self.record):
            raise HTTP(
                403,
                f"You do not have access to read a record from the {self.tablename} table.",
            )
        self.form = self._make_form(readonly=True)
        if self.param.details_sidecar:
            self.form.param.sidecar.append(self.param.details_sidecar)
        if self.param.details_submit_value:
            self.form.param.submit_value = self.param.details_submit_value
        self._handle_redirect_to_referrer(False, True)

    def _handle_mode_edit(self):
        if not self.is_editable(self.record):
            raise HTTP(
                403,
                f"You do not have access to edit a record in the {self.tablename} table.",
            )
        self.form = self._make_form(readonly=False)
        if self.param.edit_sidecar:
            self.form.param.sidecar.append(self.param.edit_sidecar)
        if self.param.edit_submit_value:
            self.form.param.submit_value = self.param.edit_submit_value
        self._handle_redirect_to_referrer(True, False)

    def _handle_mode_delete(self):
        if not self.is_deletable(self.record):
            self._handle_mode_delete()
        self.form = self._make_form(readonly=True)
        if self.param.delete_submit_value:
            self.form.param.submit_value = self.param.delete_submit_value
        if request.method == "POST":
            self.record.delete_record()
        self._handle_redirect_to_referrer(True, True)

    def _handle_redirect_to_referrer(self, inject_back, redirect_on_post):
        if self.referrer and inject_back:
            classes = self.get_style("grid-back-button")
            self.form.param.sidecar.insert(
                0,
                A(
                    self.param.back_button_value,
                    _role="button",
                    _class=classes,
                    _href=self.referrer,
                ),
            )

        # redirect to the referrer
        if self.form.accepted or (redirect_on_post and request.method == "POST"):
            redirect(self.referrer or URL())

    def _handle_mode_select(self):
        db = self.db
        query = self.query

        # use the default search for the table (we have to do this here because need self.table)
        if self.param.search_queries is None:
            self.param.search_queries = [make_default_search_query(self.table)]

        # apply the search query
        if not self.param.search_form and self.param.search_queries:
            search_type = safe_int(request.query.get("search_type", 0), default=0)
            search_string = request.query.get("search_string")
            if search_type < len(self.param.search_queries) and search_string:
                parts = self.param.search_queries[search_type]
                query_lambda = parts[1]
                if len(parts) == 3 and parts[2]:
                    requires = parts[2]
                    search_string, self.search_query_error = requires(search_string)
                if not self.search_query_error:
                    try:
                        query = self.query & query_lambda(search_string)
                    except Exception as e:
                        self.search_query_error = str(e)

        # if no column specified use all fields
        if not self.param.columns:
            self.param.columns = [field for field in self.table if field.readable]
        # convert to column object
        self.columns = []

        def title(col):
            return str(col).replace('"', "")

        def col2key(col):
            return str(col).lower().replace(".", "-")

        for index, col in enumerate(self.param.columns):
            if isinstance(col, Column):
                if not col.key:
                    col.key = f"column-{index}"
                self.columns.append(col)

            elif isinstance(col, Field):
                # deal with download links in special manner if no representation
                type_name = strip_field_type(col.type)
                # upload type is always special!
                if type_name == "upload" and hasattr(col, "download_url"):
                    represent_col = (
                        lambda row, name=str(col), f=col.download_url: row[name]
                        and A("download", _href=f(row[name]))
                        or ""
                    )
                # field represent override default representation by type
                elif col.represent:
                    represent_col = lambda row, name=str(col), f=col.represent: f(
                        row[name], row
                    )
                # we do not know better, use formarepresent by type (type is the stripped Field type)
                elif type_name in self.represent_by_type:
                    represent_col = lambda row, col=col, f=self.represent_by_type[
                        col.type_name
                    ]: f(col, row[str(col)])
                else:
                    represent_col = lambda row, name=str(col): row[name]

                self.columns.append(
                    Column(
                        col.label,
                        represent_col,
                        orderby=col,
                        required_fields=[col],
                        key=col2key(col),
                        col_type=type_name,
                    )
                )
            elif isinstance(col, FieldVirtual):

                def compute(row, col=col):
                    return col.f(row) if "id" in row else col.f(row[col.tablename])

                self.columns.append(
                    Column(
                        col.label,
                        compute,
                        orderby=None,
                        required_fields=db[col.tablename],
                        key=col2key(col),
                    )
                )
            elif isinstance(col, Expression):

                def compute(row, name=str(col)):
                    return row._extra(name)

                self.columns.append(
                    Column(
                        title(col),
                        compute,
                        orderby=None,
                        required_fields=[col],
                        key=f"column-{index}",
                    )
                )
            else:
                raise RuntimeError(f"Column not support {col}")

        # join the set of all required fields
        sets = [set(self.param.required_fields or [])]
        sets += [set(col.required_fields) for col in self.columns]
        self.needed_fields = list(
            functools.reduce(lambda a, b: a | b, sets) | set([self.table._id])
        )

        self.this_url = base64.b16encode(request.url.encode("utf8")).decode("utf8")
        self.current_page_number = safe_int(request.query.get("page"), default=1)

        select_params = dict()
        #  try getting sort order from the request
        sort_order = request.query.get("orderby")

        select_params["orderby"] = self.param.orderby
        if sort_order:
            parts = sort_order.lstrip("~").split(".")
            if len(parts) == 2 and parts[0] in db.tables and parts[1] in db[parts[0]]:
                orderby = db[parts[0]][parts[1]]
                if sort_order.startswith("~"):
                    orderby = ~orderby
                select_params["orderby"] = orderby

        if self.param.left:
            select_params["left"] = self.param.left

        if self.param.groupby:
            select_params["groupby"] = self.param.groupby

        if self.param.groupby or self.param.left:
            #  need groupby fields in select to get proper count
            self.total_number_of_rows = len(
                db(query).select(db[self.tablename]._id, **select_params)
            )
        else:
            self.total_number_of_rows = db(query).count()

        #  if at a high page number and then filter causes less records to be displayed, reset to page 1
        if (
            self.current_page_number - 1
        ) * self.param.rows_per_page > self.total_number_of_rows:
            self.current_page_number = 1

        if self.total_number_of_rows > self.param.rows_per_page:
            self.page_start = self.param.rows_per_page * (self.current_page_number - 1)
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
            key = f"column-{len(self.columns)}"
            self.columns.append(
                Column(
                    "",
                    self.make_action_buttons,
                    key=key,
                    td_class_style=self.get_style("grid-td-buttons"),
                )
            )

    def _make_form(self, readonly):
        return self.form_maker(
            self.table,
            record=self.record,
            readonly=readonly,
            deletable=self.is_deletable(self.record),
            formstyle=self.param.formstyle,
            validation=self.param.validation,
            show_id=self.param.show_id,
        )

    def _iter_pages(
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
        text,
        url,
        icon=None,
        classes=None,
        kind="grid-button",
        **attrs,
    ):
        if kind:
            classes = join_classes(classes, self.get_style(kind))

        if not "_role" in attrs:
            attrs["_role"] = "button"
        link = A(
            I(_class=self.param.icon_style.complete(icon)) if icon else "",
            _class=classes,
            _href=url,
            **attrs,
        )
        if self.param.include_action_button_text:
            link.append(
                SPAN(
                    XML("&nbsp;"),
                    text,
                    _class=self.get_style(kind + "-text") if kind else None,
                )
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
            if key not in ("search_type", "search_string")
        ]
        form = FORM(*hidden_fields, _class=self.get_style("grid-search-form"))
        select = SELECT(
            *options,
            _name="search_type",
            _class=self.get_style("grid-search-form-select"),
        )
        input = INPUT(
            _type="text",
            _name="search_string",
            _value=search_string,
            _class=self.get_style("grid-search-form-input"),
        )
        submit = INPUT(
            _type="submit",
            _value=self.T("Search"),
            _class=self.get_style("grid-search-button"),
        )
        clear_script = "document.querySelector('[name=search_string]').value='';"
        clear = INPUT(
            _type="submit",
            _value=self.T("Clear"),
            _onclick=clear_script,
            _class=self.get_style("grid-clear-button"),
        )
        div = DIV(_id="grid-search", _classes=self.get_style("grid-search"))

        tr = TR(_class=self.get_style("grid-search-form-tr"))
        td_classes = self.get_style("grid-search-form-td")
        if len(options) > 1:
            tr.append(TD(select, _class=td_classes))
        tr.append(TD(input, _class=td_classes))
        tr.append(TD(submit, clear, _class=td_classes))
        table = TABLE(tr, _class=self.get_style("grid-search-form-table"))
        if self.search_query_error:
            table.append(
                TR(
                    TD(
                        self.search_query_error,
                        _colspan=3 if len(options) > 1 else 2,
                        _class=self.get_style("grid-search-form-error"),
                    )
                )
            )
        form.append(table)
        div.append(form)
        return div

    def _make_search_form(self):
        # TODO: Do we need this?
        div = DIV(_id="grid-search", _class=self.get_style("grid-search"))
        div.append(self.param.search_form.custom["begin"])
        tr = TR(_class=self.get_style("grid-search-form-tr"))
        for field in self.param.search_form.table:
            td = TD(_class=self.get_style("grid-search-form-td"))
            if field.type == "boolean":
                sb = DIV(_class=self.get_style("grid-search-boolean"))
                sb.append(self.param.search_form.custom["widgets"][field.name])
                sb.append(field.label)
                td.append(sb)
            else:
                td.append(self.param.search_form.custom["wrappers"][field.name])
            if (
                field.name in self.param.search_form.custom["errors"]
                and self.param.search_form.custom["errors"][field.name]
            ):
                td.append(DIV(self.param.search_form.custom["errors"][field.name]))
            tr.append(td)
        if self.param.search_button_text:
            tr.append(
                TD(
                    INPUT(
                        _class="button",
                        _type="submit",
                        _value=self.T(self.param.search_button_text),
                    ),
                    _class=self.get_style("grid-search-form-td"),
                )
            )
        else:
            tr.append(
                TD(
                    self.param.search_form.custom["submit"],
                    _class=self.get_style("grid-search-form-td"),
                )
            )
        div.append(TABLE(tr, _class=self.get_style("grid-search-form-table")))
        for hidden_widget in self.param.search_form.custom["hidden_widgets"].keys():
            if hidden_widget not in ("formname", "formkey"):
                div.append(
                    self.param.search_form.custom["hidden_widgets"][hidden_widget]
                )

        div.append(self.param.search_form.custom["end"])

        return div

    def _make_table_header(self):
        sort_order = request.query.get("orderby", "")

        thead = THEAD(_class=self.get_style("grid-thead"))
        for index, col in enumerate(self.columns):
            col_header = self._make_col_header(col, index, sort_order)
            classes = join_classes(
                self.get_style("grid-th"),
                f"grid-col-{col.key}",
            )
            thead.append(TH(col_header, _class=classes))

        return thead

    def _make_col_header(self, col, index, sort_order):
        up = I(
            _class=join_classes(
                self.get_style("grid-sorter-icon-up"), self.param.icon_style.sort_up
            )
        )
        dw = I(
            _class=join_classes(
                self.get_style("grid-sorter-icon-down"), self.param.icon_style.sort_down
            )
        )

        orderby = col.orderby and str(col.orderby)

        heading = (
            self.param.headings[index] if index < len(self.param.headings) else col.name
        )
        #  add the sort order query parm
        sort_query_parms = dict(self.query_parms)

        attrs = {}
        if orderby:
            if orderby == sort_order:
                sort_query_parms["orderby"] = "~" + orderby
                url = URL(vars=sort_query_parms)
                col_header = A(heading, up, _href=url)
            else:
                sort_query_parms["orderby"] = orderby
                url = URL(vars=sort_query_parms)
                col_header = A(
                    heading, dw if "~" + orderby == sort_order else "", _href=url
                )
        else:
            col_header = heading
        return col_header

    def _make_table_body(self):
        tbody = TBODY()
        for row in self.rows:
            #  find the row id - there may be nested tables....

            tr = TR(_role="row", _class=self.get_style("grid-tr"))

            #  add all the fields to the row
            for col in self.columns:
                classes = join_classes(
                    [
                        self.get_style(maybe_call(col.td_class_style, row), "grid-td"),
                        f"grid-cell-{col.key}",
                    ]
                )
                value = col.represent_col(row)
                tr.append(TD(value, _class=classes))

            tbody.append(tr)

        return tbody

    def make_action_buttons(self, row):
        cat = CAT()
        row_id = row[self.param.field_id] if self.param.field_id else row.id
        if self.param.pre_action_buttons and len(self.param.pre_action_buttons) > 0:
            for btn in self.param.pre_action_buttons:
                btn = maybe_call(btn, row)
                if btn is None:
                    # if None, no button
                    continue
                if isinstance(btn, dict):
                    cat.append(self._make_action_button(**btn))
                else:
                    cat.append(btn)

        if self.is_readable(row):
            if isinstance(self.param.details, str):
                details_url = self.param.details.format(id=row_id)
            else:
                details_url = URL(vars=dict(id=row_id, referrer=self.this_url))
            cat.append(
                self._make_action_button(
                    text=self.T(self.param.details_action_button_text),
                    url=details_url,
                    icon=self.param.icon_style.details_button,
                    kind="grid-details-button",
                )
            )
        if self.is_editable(row):
            if isinstance(self.param.editable, str):
                edit_url = self.param.editable.format(id=row_id)
            else:
                edit_url = URL(
                    vars=dict(mode="edit", id=row_id, referrer=self.this_url)
                )
            cat.append(
                self._make_action_button(
                    text=self.T(self.param.edit_action_button_text),
                    url=edit_url,
                    icon=self.param.icon_style.edit_button,
                    kind="grid-edit-button",
                    _disabled=not self.is_editable(row),
                )
            )
        if self.is_deletable(row):
            if isinstance(self.param.deletable, str):
                delete_url = self.param.deletable.format(id=row_id)
            else:
                delete_url = URL(
                    vars=dict(mode="delete", id=row_id, referrer=self.this_url)
                )
            cat.append(
                self._make_action_button(
                    text=self.T(self.param.delete_action_button_text),
                    url=delete_url,
                    icon=self.param.icon_style.delete_button,
                    additional_classes="confirmation",
                    kind="grid-delete-button",
                    _disabled=not self.is_deletable(row),
                )
            )

        if self.param.post_action_buttons and len(self.param.post_action_buttons) > 0:
            for btn in self.param.post_action_buttons:
                btn = maybe_call(btn, row)
                if btn is None:
                    # if None, no button
                    continue
                if isinstance(btn, dict):
                    cat.append(self._make_action_button(**btn))
                else:
                    cat.append(btn)

        return cat

    def _make_table_pager(self):
        pager = DIV(_class=self.get_style("grid-pagination"))
        previous_page_number = None
        for page_number in self._iter_pages(
            self.current_page_number, self.number_of_pages
        ):
            pager_query_parms = dict(self.query_parms)
            pager_query_parms["page"] = page_number
            # if there is a gat add a spacer
            if previous_page_number and page_number - previous_page_number > 1:
                pager.append(SPAN("..."))
            is_current = self.current_page_number == page_number
            page_name = (
                "grid-pagination-button-current"
                if is_current
                else "grid-pagination-button"
            )
            pager.append(
                A(
                    page_number,
                    _class=self.get_style(page_name),
                    _role="button",
                    _href=URL(vars=pager_query_parms),
                )
            )
            previous_page_number = page_number
        return pager

    def _make_table(self):
        html = DIV(_class=self.get_style("grid-wrapper"))
        grid_header = DIV(_class=self.get_style("grid-header"))

        #  build the New button if needed
        if self.param.create and self.param.create != "":
            if isinstance(self.param.create, str):
                create_url = self.param.create
            else:
                create_url = URL(vars=dict(mode="new", referrer=self.this_url))

            grid_header.append(
                self._make_action_button(
                    self.T(self.param.new_action_button_text),
                    create_url,
                    icon=self.param.icon_style.add_button,
                    kind="grid-new-button",
                )
            )
        if self.param.header_elements and len(self.param.header_elements) > 0:
            for element in self.param.header_elements:
                element = maybe_call(element)
                if isinstance(element, dict):
                    element = copy.copy(element)
                    element["kind"] = element.get("kind", "grid-header-element")
                    grid_header.append(self._make_action_button(**element))
                else:
                    grid_header.append(element)

        #  build the search form if provided
        if self.param.search_form:
            grid_header.append(self._make_search_form())
        elif self.param.search_queries and len(self.param.search_queries) > 0:
            grid_header.append(self._make_default_form())

        html.append(grid_header)

        table = TABLE(_class=self.get_style("grid-table"))

        # build the header
        table.append(self._make_table_header())

        #  build the rows
        table.append(self._make_table_body())

        #  add the table to the html
        html.append(DIV(table, _class=self.get_style("grid-table-wrapper")))

        #  add the row counter information
        footer = DIV(_class=self.get_style("grid-footer"))

        row_count = DIV(_class=self.get_style("grid-info"))
        (
            row_count.append(
                str(self.T("Displaying rows %s thru %s of %s"))
                % (
                    self.page_start + 1 if self.number_of_pages > 1 else 1,
                    (
                        self.page_end
                        if self.page_end < self.total_number_of_rows
                        else self.total_number_of_rows
                    ),
                    self.total_number_of_rows,
                )
            )
            if self.number_of_pages > 0
            else row_count.append(self.T("No rows to display"))
        )
        footer.append(row_count)

        #  build the pager
        if self.number_of_pages > 1:
            footer.append(self._make_table_pager())

        if self.param.footer_elements and len(self.param.footer_elements) > 0:
            for element in self.param.footer_elements:
                element = maybe_call(element)
                if isinstance(element, dict):
                    element = copy.copy(element)
                    element["kind"] = element.get("kind", "grid-footer-element")
                    footer.append(self._make_action_button(**element))
                else:
                    footer.append(element)

        html.append(footer)
        return html

    def render(self):
        """
        build the query table

        :return: html representation of the table or the py4web Form object
        """
        if self.mode == "select":
            return self._make_table()
        elif self.mode in ["new", "details", "edit", "delete"]:
            return self.form
        raise HTTP(404)

    def xml(self):
        return self.render().xml()

    def __str__(self):
        return str(self.xml())

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

    def _get_tablenames(self, *args):
        """Returns the tablenames used by this grid"""
        return list(self.db._adapter.tables(*args).keys())

    def _is_join(self):
        """is this a left join?"""
        items = [self.query]
        if self.param.left is not None:
            if isinstance(self.param.left, (list, tuple)):
                items += [item for item in self.param.left]
            else:
                items += [self.param.left]
        return len(self._get_tablenames(*items)) > 1


def parse_referrer(r):
    """
    Get the referrer from the request query and use urlparse to parse it into a url object

    :param r: The request object to be interrogated

    :return: the URL object or None if no URL object obtained/decoded
    """
    referrer = r.query.get("referrer")
    url = None
    if referrer:
        url_string = base64.b16decode(referrer.encode("utf8")).decode("utf8")
        if url_string:
            url = urlparse(url_string)

    return url


def get_parent(parent_field):
    """
    try to find the parent id for a parent/child table relationship

    :param path: the path var from the method calling the grid
    :param child_table: the child table of the parent/child relationship ex. db.child_table
    :param parent_field_name: this is the name of the field in the child table that points to the parent table
                              this is a string value

    :return parent_id: the id of the parent record
    """
    parent_id = request.query.get("parent_id")
    if parent_id is not None:
        return int(parent_id)

    child_table = parent_field._table
    fn = parent_field.name

    #  if not found, search the record id of the parent from the child table record
    record_id = request.query.get("id")
    if record_id:
        record = child_table(record_id)
        if record:
            parent_id = record[fn]
            if parent_id is not None:
                return int(parent_id)

    #  else, check in the form
    parent_id = request.forms.get(fn)
    if parent_id is not None:
        return int(parent_id)

    #  else, check in the referrer
    referrer = request.query.get("referrer")
    if referrer:
        kvp = base64.b16decode(referrer.encode("utf8")).decode("utf8")
        if "parent_id" in kvp:
            parent_id = kvp.split("parent_id=")[1].split("&")[0]
            return int(parent_id)

    return None
