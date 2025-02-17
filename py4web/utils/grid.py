# TODO:
# - details, edit, delete URLs should be signed
#
#
import base64
import copy
import datetime
import functools
from urllib.parse import urlparse

from pydal.objects import Expression, Field, FieldVirtual
from yatl.helpers import (CAT, DIV, FORM, INPUT, OPTION, SELECT, SPAN, TABLE,
                          TAG, TBODY, TD, TH, THEAD, TR, XML, A, I)

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
        "grid-search-form-input": "grid-search-form-input",
        "grid-search-form-select": "grid-search-form-select",
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

class Column:
    """class used to represent a column in a grid"""

    def __init__(
        self,
        name,
        represent,
        key=None,
        required_fields=None,  # must be a list or none
        orderby=None,
        col_type="string",
        td_class_style=None,
    ):
        self.name = name
        self.represent = represent
        self.orderby = orderby
        self.required_fields = required_fields or []
        self.key = key
        self.type = (col_type,)
        self.td_class_style = td_class_style


class Grid:
    FORMATTERS_BY_TYPE = {
        "NoneType": lambda value: "",
        "bool": lambda value: "☑" if value else "☐" if value is False else "",
        "float": lambda value: "%.2f" % value,
        "double": lambda value: "%.2f" % value,
        "datetime": lambda value: (
            XML(
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
            if value and isinstance(value, datetime.datetime)
            else (value or "")
        ),
        "time": lambda value: (
            XML(
                "<script>document.write((new Date(0, 0, 0,%s,%s,%s)).toLocaleString().split(', ')[1])</script>"
                % (value.hour, value.minute, value.second)
            )
            if value and isinstance(value, datetime.time)
            else (value or "")
        ),
        "date": lambda value: (
            XML(
                '<script>document.write((new Date(%s,%s,%s)).toLocaleString().split(",")[0])</script>'
                % (
                    value.year,
                    value.month - 1,
                    value.day,
                )
            )
            if value and isinstance(value, datetime.date)
            else (value or "")
        ),
        "list": lambda value: ", ".join(x for x in value) or "",
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
        if path in (None, "", "index"):
            fullpath = request.fullpath.rstrip("/")
            if path == "index":
                fullpath = fullpath[:-6]
            redirect(
                f"{fullpath}/select"
                + (f"?{request.query_string}" if request.query_string else "")
            )

        # in case the query is a Table insteance
        if isinstance(query, query._db.Table):
            query = query._id != None

        if fields and any(field.type == "id" for field in fields):
            show_id = True

        self.path = path
        self.db = query._db
        self.T = T
        self.form_maker = form_maker
        self.icon_style = icon_style
        self.param = Param(
            query=query,
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
            new_action_button_text="New",
            details_sidecar=None,
            details_submit_value=None,
            details_action_button_text="Details",
            edit_sidecar=None,
            edit_submit_value=None,
            edit_action_button_text="Edit",
            delete_action_button_text="Delete",
            header_elements=None,
            footer_elements=None,
            required_fields=required_fields or [],
        )

        #  instance variables that will be computed
        self.action = None
        self.current_page_number = None
        self.endpoint = request.fullpath[: -len(self.path)].rstrip("/")
        self.hidden_fields = None
        self.form = None
        self.number_of_pages = None
        self.page_end = None
        self.page_start = None
        self.query_parms = safely(lambda: request.params, default={})
        self.record_id = None
        self.rows = None
        self.tablename = None
        self.total_number_of_rows = None
        self.formatters_by_type = copy.copy(Grid.FORMATTERS_BY_TYPE)
        self.attributes_plugin = AttributesPlugin(request)

        if auto_process:
            self.process()

    def is_creatable(self):
        if self.param.groupby:
            return False
        if callable(self.param.create):
            return self.param.create()
        return self.param.create

    def is_editable(self, row):
        if self.param.groupby:
            return False
        if callable(self.param.editable):
            return self.param.editable(row)
        return self.param.editable

    def is_readable(self, row):
        if callable(self.param.details):
            return self.param.details(row)
        return self.param.details

    def is_deletable(self, row):
        # cannot delete a record that does not exist
        if row is None:
            return False
        # cannot delete if the a record is grouped
        if self.param.groupby:
            return False
        # if deletable is callable, call it
        if callable(self.param.deletable):
            return self.param.deletable(row)
        # if deletable is boolean, check it
        return self.param.deletable

    def get_style(self, element, default=None):
        return self.param.grid_class_style.get(element, default)

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
                except Exception:
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
        # if no column specified use all fields
        if not self.param.columns:
            self.param.columns = [field for field in table if field.readable]
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

                def compute(row, col=col):
                    value = row(str(col))
                    if col.represent:
                        value = col.represent(value, row)
                    # deal with download links in special manner if no representation
                    if col.type == "upload" and value and hasattr(col, "download_url"):
                        value = A("download", _href=col.download_url(value))
                    return value

                self.columns.append(
                    Column(
                        col.label,
                        compute,
                        orderby=col,
                        required_fields=[col],
                        key=col2key(col),
                        col_type=col.type,
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
            functools.reduce(lambda a, b: a | b, sets) | set([table._id])
        )

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

        #  ensure the user has access for new/details/edit/delete if chosen
        if self.action == "new" and not self.is_creatable():
            raise HTTP(
                403,
                f"You do not have access to create a record in the {self.tablename} table.",
            )
        if self.action == "details" and not self.is_readable(record):
            raise HTTP(
                403,
                f"You do not have access to read a record from the {self.tablename} table.",
            )
        if self.action == "edit" and not self.is_editable(record):
            raise HTTP(
                403,
                f"You do not have access to edit a record in the {self.tablename} table.",
            )
        if self.action == "delete" and not self.is_deletable(record):
            raise HTTP(
                403,
                f"You do not have access to delete a record in the {self.tablename} table.",
            )

        if self.action in ["new", "details", "edit"]:
            readonly = self.action == "details"

            attrs = self.attributes_plugin.form(url=request.url.split(":", 1)[1])
            self.form = self.form_maker(
                table,
                record=record,
                readonly=readonly,
                deletable=self.is_deletable(record),
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
            if self.action == "details" and self.is_readable(record):
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
            db(db[self.tablename]._id == self.record_id).delete()

            referrer = parse_referer(request)
            url = self.endpoint + "/select"
            if referrer and referrer.query:
                url += "?%s" % referrer.query
            redirect(url)

        elif self.action == "select":
            self.referrer = "_referrer=%s" % base64.b16encode(
                request.url.encode("utf8")
            ).decode("utf8")

            self.current_page_number = safe_int(request.query.get("page"), default=1)

            select_params = dict()
            #  try getting sort order from the request
            sort_order = request.query.get("orderby")

            select_params["orderby"] = self.param.orderby
            if sort_order:
                parts = sort_order.lstrip("~").split(".")
                if (
                    len(parts) == 2
                    and parts[0] in db.tables
                    and parts[1] in db[parts[0]]
                ):
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
            key = f"column-{len(self.columns)}"
            self.columns.append(
                Column(
                    "",
                    self.make_action_buttons,
                    key=key,
                    td_class_style=self.get_style("grid-td-buttons"),
                )
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
        icon_size="small",  # deprecated
        additional_classes=None,
        override_classes=None,
        message=None,
        onclick=None,  # deprecated
        row_id=None,
        name="grid-button",
        row=None,
        ignore_attribute_plugin=False,
        **attrs,
    ):
        if row_id:
            url += "/%s" % row_id

        classes = self.get_style(name)

        if callable(additional_classes):
            additional_classes = additional_classes(row)

        if callable(override_classes):
            override_classes = override_classes(row)

        if override_classes:
            classes = join_classes(override_classes)
        elif additional_classes:
            classes = join_classes(classes, additional_classes)

        if callable(url):
            url = url(row)

        if ignore_attribute_plugin:
            attrs.update({"_href": url})
        else:
            attrs.update(self.attributes_plugin.link(url=url))

        link = A(
            I(_class=self.icon_style.complete(icon)),
            _role="button",
            _message=message,
            _title=button_text,
            _class=classes,
            **attrs,
        )
        if self.param.include_action_button_text:
            link.append(
                SPAN(
                    XML("&nbsp;"),
                    button_text,
                    _class=self.get_style("grid-action-button-text"),
                )
            )

        return link

    def reformat(self, value):
        type_name = type(value).__name__
        if type_name in self.formatters_by_type:
            return self.formatters_by_type[type_name](value)
        return value

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
        attrs = self.attributes_plugin.link(url=self.endpoint)
        form = FORM(*hidden_fields, **attrs)
        classes = self.get_style("grid-search-form-select")
        select = SELECT(*options, **dict(_name="search_type", _class=classes))
        classes = self.get_style("grid-search-form-input")
        input = INPUT(
            _type="text",
            _name="search_string",
            _value=search_string,
            _class=classes,
        )
        classes = self.get_style("grid-search-button")
        submit = INPUT(_type="submit", _value=self.T("Search"), _class=classes)
        clear_script = "document.querySelector('[name=search_string]').value='';"
        classes = self.get_style("grid-clear-button")
        clear = INPUT(
            _type="submit",
            _value=self.T("Clear"),
            _onclick=clear_script,
            _class=classes,
        )
        div = DIV(_id="grid-search", _classes=self.get_style("grid-search"))

        tr = TR(_class=self.get_style("grid-search-form-tr"))
        classes = self.get_style("grid-search-form-td")
        if len(options) > 1:
            tr.append(TD(select, _class=classes))
        tr.append(TD(input, _class=classes))
        tr.append(TD(submit, clear, _class=classes))
        classes = self.get_style("grid-search-form-table")
        form.append(TABLE(tr, _class=classes))
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
                "grid-col-%s" % col.key,
            )
            thead.append(TH(col_header, _class=classes))

        return thead

    def _make_col_header(self, col, index, sort_order):
        up = I(
            _class=join_classes(
                self.get_style("grid-sorter-icon-up"), self.icon_style.sort_up
            )
        )
        dw = I(
            _class=join_classes(
                self.get_style("grid-sorter-icon-down"), self.icon_style.sort_down
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
                url = URL(self.endpoint, "select", vars=sort_query_parms)
                attrs = self.attributes_plugin.link(url=url)
                col_header = A(heading, up, **attrs)
            else:
                sort_query_parms["orderby"] = orderby
                url = URL(self.endpoint, "select", vars=sort_query_parms)
                attrs = self.attributes_plugin.link(url=url)
                col_header = A(
                    heading, dw if "~" + orderby == sort_order else "", **attrs
                )
        else:
            col_header = heading
        return col_header

    def _make_table_body(self):
        tbody = TBODY()
        for index, row in enumerate(self.rows):
            #  find the row id - there may be nested tables....

            tr = TR(
                _role="row",
                _class=self.get_style("grid-tr"),
            )

            #  add all the fields to the row
            for col in self.columns:
                classes = join_classes(
                    [
                        self.get_style(
                            col.td_class_style,
                            (
                                col.td_class_style(row)
                                if callable(col.td_class_style)
                                else self.get_style("grid-td")
                            ),
                        ),
                        f"grid-cell-{col.key}",
                    ]
                )
                value = col.represent(row)
                reformatted_value = self.reformat(value)
                tr.append(TD(reformatted_value, _class=classes))

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
                    if btn is None:
                        # if None was returned, no button is available for this row: ignore this value in the
                        # list
                        continue
                attrs = (
                    self.attributes_plugin.confirm(message=self.T(btn.message))
                    if btn.message and btn.message != ""
                    else btn.__dict__.get("attrs", dict())
                )

                cat.append(
                    self._make_action_button(
                        url=btn.url,
                        button_text=self.T(btn.text),
                        icon=btn.icon,
                        additional_classes=btn.additional_classes,
                        override_classes=btn.__dict__.get("override_classes"),
                        message=btn.message,
                        row_id=row_id if btn.append_id else None,
                        name=btn.__dict__.get("name"),
                        row=row,
                        ignore_attribute_plugin=(
                            btn.ignore_attribute_plugin
                            if "ignore_attribute_plugin" in btn.__dict__
                            else False
                        ),
                        **attrs,
                    )
                )

        if self.is_readable(row):
            if isinstance(self.param.details, str):
                details_url = self.param.details
            else:
                details_url = self.endpoint + "/details"
            details_url += "/%s?%s" % (row_id, self.referrer)
            cat.append(
                self._make_action_button(
                    url=details_url,
                    button_text=self.T(self.param.details_action_button_text),
                    icon=self.icon_style.details_button,
                    name="grid-details-button",
                )
            )
        if self.is_editable(row):
            if isinstance(self.param.editable, str):
                edit_url = self.param.editable
            else:
                edit_url = self.endpoint + "/edit"
            edit_url += "/%s?%s" % (row_id, self.referrer)
            cat.append(
                self._make_action_button(
                    url=edit_url,
                    button_text=self.T(self.param.edit_action_button_text),
                    icon=self.icon_style.edit_button,
                    name="grid-edit-button",
                    _disabled=not self.is_editable(row),
                )
            )
        if self.is_deletable(row):
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
                    icon=self.icon_style.delete_button,
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
                    if btn is None:
                        # if None was returned, no button is available for this row: ignore this value in the
                        # list
                        continue
                attrs = (
                    self.attributes_plugin.confirm(message=self.T(btn.message))
                    if btn.message and btn.message != ""
                    else btn.__dict__.get("attrs", dict())
                )
                cat.append(
                    self._make_action_button(
                        url=btn.url,
                        button_text=self.T(btn.text),
                        icon=btn.icon,
                        additional_classes=btn.additional_classes,
                        override_classes=btn.__dict__.get("override_classes"),
                        message=btn.message,
                        row_id=row_id if btn.append_id else None,
                        name=btn.__dict__.get("name"),
                        row=row,
                        ignore_attribute_plugin=(
                            btn.ignore_attribute_plugin
                            if "ignore_attribute_plugin" in btn.__dict__
                            else False
                        ),
                        **attrs,
                    )
                )

        return cat

    def _make_table_pager(self):
        pager = DIV(_class=self.get_style("grid-pagination"))
        previous_page_number = None
        for page_number in self.iter_pages(
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
            attrs = self.attributes_plugin.link(
                url=URL(self.endpoint, "select", vars=pager_query_parms)
            )
            pager.append(
                A(
                    page_number,
                    _class=self.get_style(page_name),
                    _role="button",
                    **attrs,
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
                create_url = self.endpoint + "/new"

            create_url += "?%s" % self.referrer

            grid_header.append(
                self._make_action_button(
                    create_url,
                    self.T(self.param.new_action_button_text),
                    icon=self.icon_style.add_button,
                    icon_size="normal",
                    override_classes=self.get_style("grid-new-button"),
                )
            )
        if self.param.header_elements and len(self.param.header_elements) > 0:
            for element in self.param.header_elements:
                if isinstance(element, str):
                    html.append(XML(element))
                elif callable(element):
                    grid_header.append(element())
                else:
                    override_classes = element.__dict__.get("override_classes", None)
                    if not override_classes:
                        override_classes = join_classes(
                            self.get_style("grid-header-element"),
                            element.additional_classes,
                        )
                    grid_header.append(
                        self._make_action_button(
                            url=element.url,
                            button_text=self.T(element.text),
                            icon=element.icon,
                            icon_size="normal",
                            additional_classes=element.additional_classes,
                            override_classes=override_classes,
                            message=element.message,
                            name=element.__dict__.get("name"),
                            ignore_attribute_plugin=element.ignore_attribute_plugin,
                            **element.__dict__.get("attrs", dict()),
                        )
                    )

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

        html.append(footer)

        if self.param.footer_elements and len(self.param.footer_elements) > 0:
            for element in self.param.footer_elements:
                if isinstance(element, str):
                    html.append(XML(element))
                elif callable(element):
                    html.append(element())
                else:
                    override_classes = element.__dict__.get("override_classes", None)
                    if not override_classes:
                        override_classes = join_classes(
                            self.get_style("grid-footer-element"),
                            element.additional_classes,
                        )
                    html.append(
                        self._make_action_button(
                            url=element.url,
                            button_text=self.T(element.text),
                            icon=element.icon,
                            icon_size="normal",
                            additional_classes=element.additional_classes,
                            override_classes=override_classes,
                            message=element.message,
                            name=element.__dict__.get("name"),
                            ignore_attribute_plugin=element.ignore_attribute_plugin,
                            **element.__dict__.get("attrs", dict()),
                        )
                    )

        return html

    def render(self):
        """
        build the query table

        :return: html representation of the table or the py4web Form object
        """
        if self.action == "select":
            return self._make_table()
        elif self.action in ["new", "details", "edit"]:
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
    if parent_id is not None:
        return int(parent_id)

    child_table = parent_field._table
    fn = parent_field.name

    #  if not found, search the record id of the parent from the child table record
    if path:
        parts = path.split("/")
        record_id = parts[1] if len(parts) > 1 else None
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

    #  else, check in the referer
    referrer = request.query.get("_referrer")
    if referrer:
        kvp = base64.b16decode(referrer.encode("utf8")).decode("utf8")
        if "parent_id" in kvp:
            parent_id = kvp.split("parent_id=")[1].split("&")[0]
            return int(parent_id)

    return None


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
