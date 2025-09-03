import copy
import os
import time
import uuid
from abc import ABC
from typing import Any, Dict, List, Optional, Type, Union

import jwt
from pydal._compat import to_native
from pydal.objects import Field, FieldVirtual, SQLCustomType
from yatl.helpers import (
    CAT,
    DIV,
    FORM,
    INPUT,
    LABEL,
    OPTION,
    SELECT,
    SPAN,
    TAGGER,
    TEXTAREA,
    XML,
    A,
    P,
)

from py4web import HTTP, request, response
from py4web.utils.param import Param


def to_id(field):
    """get an identified for a field"""
    return "%s_%s" % (getattr(field, "_tablename", field.tablename), field.name)


def compat_represent(field, value, row):
    """Same as field.represent(value, row) but backward compatible in case field.represent only takes value"""
    represent = field.represent
    if not represent:
        return value or ""
    try:
        return represent(value, row)
    except TypeError:
        return represent(value)


def get_options(validators):
    """given a validator chain, if one has .options, return them"""
    options = None
    if validators:
        if not isinstance(validators, (list, tuple)):
            validators = [validators]
        for item in validators:
            if hasattr(item, "options"):
                options = item.options
                break
        if callable(options):
            options = options(zero=True)
    return options


def get_min_max(validators):
    min = None
    max = None
    if validators:
        if not isinstance(validators, (list, tuple)):
            validators = [validators]
        for item in validators:
            if hasattr(item, "minimum") and hasattr(item, "maximum"):
                min = item.minimum
                max = item.maximum
                break
    return min, max


def join_classes(*args):
    lists = [[] if a is None else a.split() if isinstance(a, str) else a for a in args]
    classes = set(
        cls.strip() for classlist in lists for cls in classlist if cls.strip()
    )
    return " ".join(sorted(classes))


class IgnoreWidget(Exception):
    "Exception which widgets can raise to be completely skipped"

    pass


class Widget(ABC):
    """Prototype widget object for all form widgets"""

    @classmethod
    def matches(cls, field: Field) -> bool:
        "Checks if this widget can be used for the field"
        return False  # if this method hasn't been overwritten, this widget should never be matched

    def __init__(
        self,
        field: Field = None,
        form_style: "FormStyleFactory" = None,
        vars: Any = None,
        error: Optional[str] = None,
    ):
        if field is None or form_style is None or vars is None:
            raise TypeError(
                "The usage of custom widgets has changed.\n"
                "If you used to override the widget for a field, "
                "don't instantiate the class anymore:\n"
                'old: FormStyle.widgets["fieldname"] = RadioWidget()\n'
                'new: FormStyle.widgets["fieldname"] = RadioWidget\n',
            )
        self.field = field
        self.form_style = form_style
        self.vars = vars
        self.error = error
        self.title = self.field.__dict__.get("_title")
        self.placeholder = self.field.__dict__.get("_placeholder")
        _class = "type-" + str(self.field.type).split()[0].replace(":", "-")
        self.attributes = {
            "_id": to_id(self.field),
            "_name": self.field.name,
            "_class": _class,
            "_type": str(self.field.type).replace(" ", "-"),
            "_label": self.field.label,
            "_comment": self.field.comment or "",
            "_title": self.title,
            "_placeholder": self.placeholder,
            "_error": error,
        }
        self.form_values = {
            self.field.name: None,
        }
        self.controls = {
            "labels": self.field.label,
            "comments": self.field.comment or "",
            "titles": self.title,
            "placeholders": self.placeholder,
            "errors": error,
        }
        # Primary usecase: FileUploadWidget
        self.extra_attributes = []

    @property
    def field_value(self):
        return self.form_values[self.field.name]

    @field_value.setter
    def field_value(self, value: Any):
        self._field_value = value
        self.form_values[self.field.name] = value
        self.attributes["_disabled"] = True

    def make(self, readonly: bool = False) -> TAGGER:
        if isinstance(self.field, FieldVirtual):
            value = None
        if self.field.name in self.vars:
            value = self.vars.get(self.field.name)
        else:
            default = getattr(self.field, "default", None)
            if callable(default):
                default = default()
            value = default

        if readonly:
            control = self.make_readonly(value)
        else:
            control = self.make_editable(value)
        self.controls["widgets"] = control
        return control

    def make_editable(self, value: Any) -> TAGGER: ...

    def make_readonly(self, value: Any) -> TAGGER:
        "fallback readonly style, most widgets use their input set to readonly + disabled"
        if isinstance(self.field, FieldVirtual):
            self.field_value = self.field.f(self.vars)
        else:
            self.field_value = compat_represent(self.field, value, self.vars)
        return DIV(
            self.field_value,
            _class=self.form_style.classes.get("div"),
        )

    def form_html(self, readonly=False):
        control = self.make(readonly=readonly)
        c = self.form_style.classes
        wrapped = DIV(
            control,
            _class=self.form_style.class_inner_exceptions.get(
                control.name, c.get("inner")
            ),
        )
        return (
            wrapped,
            DIV(
                LABEL(self.field.label, _for=to_id(self.field), _class=c.get("label")),
                wrapped,
                P(self.error, _class=c.get("error")) if self.error else "",
                P(self.field.comment or "", _class=c.get("info")),
                _class=c.get("outer"),
            ),
        )


class WidgetRegistry:
    def __init__(self):
        self.widgets: List[Type[Widget]] = []

    # class-decorator for registering a widget
    def register_widget(self, cls: Type[Widget]):
        self.widgets.append(cls)
        # so that the class isn't set to None when this is used as a decorator
        return cls

    def get_widget_for(
        self,
        field: Field,
        form_style: "FormStyleFactory",
        vars: Any,
        error: Optional[str] = None,
    ) -> Widget:
        # default to TextInputWidget if none found
        widget = TextInputWidget

        # loop over in reverse order, so custom user widgets are preferred
        for w in reversed(self.widgets):
            if w.matches(field):
                widget = w
                break
        return widget(field, form_style, vars, error=error)


# global widget registry, for associating widgets to types
widgets = WidgetRegistry()


class FieldDefinedWidget(Widget):
    "Handles widgets defined by a field"

    def __init__(self, field, form_style, table, vars, error=None):
        super().__init__(field, form_style, error)
        self.table = table
        self.vars = vars

    def make_editable(self, value: Any):
        control: TAGGER = self.field.widget(self.table, self.vars)

        key = control.name.rstrip("/")
        if key == "input":
            key += "[type=%s]" % (control["_type"] or "text")

        if hasattr(control, "attributes"):
            control["_class"] = join_classes(
                control.attributes.get("_class"), self.form_style.classes.get(key)
            )
        return control


class OldWidgetCompat(Widget):
    """Handles custom widgets from the older style,
    which have a .make(self, field, value, error, title, placeholder="", readonly=False)
    and don't inherit from Widget"""

    def __init__(self, old_widget, field, form_style, vars, error=None):
        super().__init__(field, form_style, vars, error)
        self.old_widget = old_widget

    def make(self, readonly):
        if isinstance(self.field, FieldVirtual):
            value = None
        if self.field.name in self.vars:
            value = self.vars.get(self.field.name)
        else:
            default = getattr(self.field, "default", None)
            if callable(default):
                default = default()
            value = default

        control = self.old_widget.make(
            self.field,
            value,
            self.error,
            self.title,
            placeholder=self.placeholder,
            readonly=readonly,
        )
        self.controls["widgets"] = control
        return control


class MakeReadonlyMixin:
    def make_readonly(self, value):
        control = self.make_editable(value)
        control["_readonly"] = True
        control["_disabled"] = True
        return control


class InputTypeWidget(Widget, MakeReadonlyMixin):
    html_input_type = "text"

    @classmethod
    def matches(cls, field: Field) -> bool:
        return cls.type_name == str(field.type)

    def make_editable(self, value):
        """converts the widget to a HTML helper"""
        return INPUT(
            _value=self.field.formatter("" if value is None else value),
            _type=self.html_input_type,
            _id=to_id(self.field),
            _name=self.field.name,
            _placeholder=self.placeholder,
            _title=self.title,
            _class=self.form_style.classes.get(f"input[type={self.html_input_type}]"),
        )


@widgets.register_widget
class TextInputWidget(InputTypeWidget):
    type_name = "string"
    html_input_type = "text"


@widgets.register_widget
class DateInputWidget(InputTypeWidget):
    type_name = "date"
    html_input_type = "date"


@widgets.register_widget
class TimeInputWidget(InputTypeWidget):
    type_name = "time"
    html_input_type = "time"


@widgets.register_widget
class IntegerInputWidget(InputTypeWidget):
    type_name = "integer"
    html_input_type = "number"

    def make_editable(self, value):
        """converts the widget to a HTML helper"""
        input_elem = super().make_editable(value)
        min, max = get_min_max(self.field.requires)
        input_elem["_min"] = min
        input_elem["_max"] = max
        input_elem["_step"] = 1
        return input_elem


@widgets.register_widget
class FloatInputWidget(InputTypeWidget):
    type_name = "numeric"
    html_input_type = "number"

    def make_editable(self, value):
        """converts the widget to a HTML helper"""
        input_elem = super().make_editable(value)
        min, max = get_min_max(self.field.requires)
        input_elem["_min"] = min
        input_elem["_max"] = max
        input_elem["_step"] = 0.01
        return input_elem


@widgets.register_widget
class DateTimeWidget(InputTypeWidget):
    type_name = "datetime"
    html_input_type = "datetime-local"

    def make_editable(self, value):
        input_elem = super().make_editable(value)
        min, max = get_min_max(self.field.requires)
        input_elem["_min"] = min and min.strftime("%Y-%m-%dT%H:%M")
        input_elem["_max"] = max and max.strftime("%Y-%m-%dT%H:%M")
        return input_elem


@widgets.register_widget
class TextareaWidget(Widget, MakeReadonlyMixin):
    @classmethod
    def matches(cls, field: Field) -> bool:
        return str(field.type) == "text"

    def make_editable(self, value):
        return TEXTAREA(
            self.field.formatter(value or ""),
            _id=to_id(self.field),
            _name=self.field.name,
            _placeholder=self.placeholder,
            _title=self.title,
            _class=self.form_style.classes.get("textarea"),
        )


@widgets.register_widget
class JsonWidget(TextareaWidget):
    @classmethod
    def matches(cls, field: Field) -> bool:
        return str(field.type) == "json"


@widgets.register_widget
class CheckboxWidget(Widget, MakeReadonlyMixin):
    @classmethod
    def matches(cls, field: Field) -> bool:
        return str(field.type) == "boolean"

    def make_editable(self, value):
        return INPUT(
            _type="checkbox",
            _id=to_id(self.field),
            _name=self.field.name,
            _value="ON",
            _checked=value,
            _class=self.form_style.classes.get("input[type=checkbox]"),
        )

    def form_html(self, readonly=False):
        control = self.make(readonly=readonly)
        c = self.form_style.classes
        wrapped = SPAN(control, _class=c.get("inner"))
        return (
            wrapped,
            DIV(
                wrapped,
                LABEL(
                    " ",
                    self.field.label,
                    _for=to_id(self.field),
                    _class=c.get("label"),
                    _style="display: inline !important",
                ),
                P(self.error, _class=c.get("error")) if self.error else "",
                P(self.field.comment or "", _class=c.get("info")),
                _class=c.get("outer"),
            ),
        )


@widgets.register_widget
class ListWidget(Widget, MakeReadonlyMixin):
    @classmethod
    def matches(cls, field: Field):
        return str(field.type).startswith("list:")

    def make_editable(self, value):
        # Seems like this is a less flexible version of the _class in Widget.__init__?
        if self.field.type == "list:string":
            _class = "type-list-string"
        elif self.field.type == "list:integer":
            _class = "type-list-integer"
        else:
            _class = ""
        return INPUT(
            _value=self.field.formatter("" if value is None else value),
            _type="text",
            _id=to_id(self.field),
            _name=self.field.name,
            _placeholder=self.placeholder,
            _title=self.title,
            _class=_class + self.form_style.classes.get("input[type=text]"),
        )


@widgets.register_widget
class PasswordWidget(Widget, MakeReadonlyMixin):
    @classmethod
    def matches(cls, field: Field) -> bool:
        return str(field.type) == "password"

    def make_editable(self, value):
        return INPUT(
            _value=self.field.formatter("" if value is None else value),
            _type="password",
            _id=to_id(self.field),
            _name=self.field.name,
            _placeholder=self.placeholder,
            _title=self.title,
            _autocomplete="off",
            _class=self.form_style.classes.get("input[type=password]"),
        )


@widgets.register_widget
class SelectWidget(Widget, MakeReadonlyMixin):
    @classmethod
    def matches(cls, field: Field) -> bool:
        return str(field.type) == "select"

    @classmethod
    def matches(cls, field: Field) -> bool:
        return get_options(field.requires) is not None

    def make_editable(self, value):
        multiple = self.field.type.startswith("list:")
        value = list(map(str, value if isinstance(value, list) else [value]))

        field_options = [
            [k, v, (k is not None and k in value)]
            for k, v in get_options(self.field.requires)
        ]
        option_tags = [
            OPTION(v, _value=k, _selected=_selected)
            for (k, v, _selected) in field_options
        ]

        control = SELECT(
            *option_tags,
            _id=to_id(self.field),
            _name=self.field.name,
            _multiple=multiple,
            _title=self.title,
            _class=self.form_style.classes.get("select"),
        )

        return control


@widgets.register_widget
class RadioWidget(Widget):
    @classmethod
    def matches(cls, field: Field) -> bool:
        return str(field.type) == "radio"

    def make_editable(self, value):
        control = CAT()
        field_id = to_id(self.field)
        value = list(map(str, value if isinstance(value, list) else [value]))
        field_options = [
            [k, v, (k is not None and k in value)]
            for k, v in get_options(self.field.requires)
            if k != ""
        ]
        for k, v, selected in field_options:
            _id = "%s-%s" % (field_id, k)
            inp = INPUT(
                _id=_id,
                _value=k,
                _label=v,
                _name=self.field.name,
                _type="radio",
                _checked=selected,
                _class=self.form_style.classes.get("input[type=radio]"),
            )
            control.append(
                LABEL(
                    inp, " ", v, _class=self.form_style.classes.get("label[type=radio]")
                )
            )
        return control

    # currently RadioWidget uses default readonly display, which is probably not ideal


@widgets.register_widget
class FileUploadWidget(Widget):
    @classmethod
    def matches(cls, field: Field) -> bool:
        return str(field.type) == "upload"

    def url(self, value):
        return getattr(self.field, "download_url", lambda value: "#")(value)

    def make_editable(self, value):
        field_id = to_id(self.field)
        delete_name = "_delete_" + self.field.name
        control = DIV(_class=self.form_style.classes.get("div[type=file]"))
        if value and not self.error:
            control.append(
                DIV(
                    LABEL(
                        "Currently:  ",
                    ),
                    A(" download ", _href=self.url(value)),
                    INPUT(
                        _type="checkbox",
                        _value="ON",
                        _name=delete_name,
                        _title=self.title,
                    ),
                    " (check to remove)",
                )
            )
            control.append(LABEL("Change: "))
        else:
            control.append(LABEL("Upload: "))
        control.append(
            INPUT(
                _type="file",
                _id=field_id,
                _name=self.field.name,
                _class=self.form_style.classes.get("input[type=file]"),
            )
        )

        # Set the download url.
        self.attributes["_download_url"] = self.url(value)
        # Set the flag determining whether the file is an image.
        self.attributes["_is_image"] = (self.url(value) != "#") and Form.is_image(value)

        # do we need the variables below?
        self.extra_attributes.append(
            {
                "_label": "Remove",
                "_value": "ON",
                "_type": "checkbox",
                "_name": delete_name,
            }
        )
        self.form_values[delete_name] = None
        return control

    def make_readonly(self, value):
        control = DIV(_class=self.form_style.classes.get("div[type=file]"))
        if value and not self.error:
            control.append(A("Download", _href=self.url(value)))
        else:
            control.append(A("No file"))
        return control


@widgets.register_widget
class BlobWidget(Widget):
    @classmethod
    def matches(cls, field: Field) -> bool:
        return str(field.type) == "blob"

    def make(self, readonly=False):
        raise IgnoreWidget("Blob fields have no default widget")


class FormStyleFactory:
    _classes = {
        "outer": "",
        "inner": "",
        "label": "",
        "info": "",
        "error": "py4web-validation-error",
        "submit": "",
        "input": "",
        "input[type=text]": "",
        "input[type=date]": "",
        "input[type=time]": "",
        "input[type=datetime-local]": "",
        "input[type=radio]": "",
        "label[type=radio]": "",
        "input[type=checkbox]": "",
        "input[type=submit]": "",
        "input[type=password]": "",
        "input[type=file]": "",
        "div[type=file]": "",
        "select": "",
        "textarea": "",
    }
    _class_inner_exceptions = {}
    _widgets: Dict[str, Type[Widget]] = {}

    def __init__(self):
        self.classes = copy.copy(self._classes)
        self.class_inner_exceptions = copy.copy(self._class_inner_exceptions)
        self.widgets: Dict[str, Type[Widget]] = copy.copy(self._widgets)

    def clone(self):
        return copy.deepcopy(self)

    def __call__(
        self,
        table,
        vars,
        errors,
        readonly,
        deletable,
        showreadonly,
        show_id,
        kwargs=None,
    ):
        kwargs = kwargs if kwargs else {}

        kwargs["_accept-charset"] = "utf8"
        form_method = "POST"
        form_action = request.url.split(":", 1)[1]
        form_enctype = "multipart/form-data"

        if "_method" in kwargs:
            form_method = kwargs.pop("_method")

        form = FORM(
            _method=form_method, _action=form_action, _enctype=form_enctype, **kwargs
        )

        controls = Param(
            labels=dict(),
            widgets=dict(),
            wrappers=dict(),
            comments=dict(),
            hidden_widgets=dict(),
            placeholders=dict(),
            titles=dict(),
            errors=dict(),
            begin=XML(form.xml().split("</form>")[0]),
            submit="",
            delete="",
            end=XML("</form>"),
        )

        json_controls = dict(
            form_fields=[],
            form_values=dict(),
            form_buttons=[],
            form_method=form_method,
            form_action=form_action,
            form_enctype=form_enctype,
            **kwargs,
        )

        class_outer = self.classes.get("outer") or None
        class_inner = self.classes.get("inner") or None

        all_fields = [x for x in table]
        if "_virtual_fields" in dir(table):
            all_fields += table._virtual_fields
        for field in all_fields:
            is_virtual = isinstance(field, FieldVirtual)

            # only display field if readable or writable
            if not field.readable and not field.writable:
                continue

            # if this is a readonly field only show readable fields
            if readonly:
                if not field.readable:
                    continue

            # do not display virtual fields in edit forms
            if not readonly and is_virtual:
                continue

            # do not show the id if not desired
            if field.type == "id" and not show_id:
                continue

            #  if this is an create form (unkown id) then only show writable fields.
            #  Some if an edit form was made from a list of fields and showreadonly=True
            elif not showreadonly and not field.writable:
                continue

            # ignore fields of type id its value is equal to None
            if field.type == "id" and vars.get(field.name) is None:
                field.writable = False
                continue

            error = errors.get(field.name)

            # if we have a field.widget for the field use it but this logic is deprecated
            if field.widget:
                widget = FieldDefinedWidget(field, self, table, vars, error=error)
            elif field.name in self.widgets:
                usr_widget = self.widgets[field.name]
                # allow specifying `formstyle.widgest["field"] = SelectWidget` (note: class, not instance)
                if issubclass(usr_widget, Widget):
                    widget = usr_widget
                else:
                    # compat with widgets expecting widget.make(self, field, value, error, title, placeholder="", readonly=False)
                    widget = OldWidgetCompat(usr_widget, field, self, vars, error)
            else:
                widget = widgets.get_widget_for(field, self, vars, error)

            # if the form is readonly or this is an id type field, display it as readonly
            is_readonly = (
                readonly or not field.writable or field.type == "id" or is_virtual
            )

            try:
                wrapped, html = widget.form_html(readonly=is_readonly)
            except IgnoreWidget:
                continue

            # Add to the controls dict
            controls.wrappers[field.name] = wrapped
            for key, value in widget.controls.items():
                controls[key][field.name] = value

            # Add to the json controls.
            json_controls["form_fields"].extend(
                [widget.attributes, *widget.extra_attributes]
            )
            json_controls["form_values"].update(widget.form_values)

            form.append(html)

        if vars.get("id"):
            form.append(INPUT(_name="id", _value=vars["id"], _hidden=True))

        if deletable:
            deletable_record_attributes = dict()

            deletable_field_name = "_delete"
            deletable_field_type = "checkbox"

            # Set the deletable json field attributes.
            deletable_record_attributes["_label"] = " check to delete"
            deletable_record_attributes["_name"] = deletable_field_name
            deletable_record_attributes["_type"] = deletable_field_type
            deletable_record_attributes["_class"] = self.classes["input[type=checkbox]"]
            deletable_record_attributes["_value"] = "ON"

            # Add to the json controls.
            json_controls["form_fields"] += [deletable_record_attributes]
            json_controls["form_values"][deletable_field_name] = None

            controls["delete"] = INPUT(
                _type=deletable_field_type,
                _value=deletable_record_attributes["_value"],
                _id=deletable_field_name,
                _name=deletable_field_name,
                _class=self.classes["input[type=checkbox]"],
            )

            form.append(
                DIV(
                    SPAN(
                        controls["delete"],
                        _class=class_inner,
                    ),
                    LABEL(
                        deletable_record_attributes["_label"],
                        _for=deletable_field_name,
                        _class="help",
                        _style="display: inline !important",
                    ),
                    _class=class_outer,
                )
            )

        submit_button_attributes = dict()

        submit_button_field_type = "submit"

        # Set the deletable json field attributes.
        submit_button_attributes["_label"] = "Submit"
        submit_button_attributes["_type"] = submit_button_field_type
        submit_button_attributes["_class"] = self.classes["input[type=submit]"]

        # Add to the json controls.
        json_controls["form_buttons"] += [submit_button_attributes]

        controls["submit"] = INPUT(
            _type=submit_button_field_type,
            _value="Submit",
            _class=self.classes["input[type=submit]"],
        )

        submit = DIV(
            DIV(
                controls["submit"],
                _class=class_inner,
            ),
            _class=class_outer,
        )
        form.append(submit)

        return dict(form=form, controls=controls, json_controls=json_controls)


FormStyleDefault = FormStyleFactory()

FormStyleBulma = FormStyleFactory()
FormStyleBulma.classes.update(
    {
        "outer": "field",
        "inner": "control",
        "label": "label",
        "info": "help",
        "error": "help is-danger py4web-validation-error mt-1",
        "submit": "button is-primary",
        "input": "input",
        "input[type=text]": "input",
        "input[type=date]": "input",
        "input[type=time]": "input",
        "input[type=datetime-local]": "input",
        "input[type=radio]": "radio",
        "input[type=checkbox]": "checkbox",
        "input[type=submit]": "button is-primary",
        "input[type=password]": "input password",
        "input[type=file]": "file",
        "select": "control select",
        "textarea": "textarea",
    }
)
FormStyleBulma.class_inner_exceptions = {"select": "select"}


FormStyleBootstrap4 = FormStyleFactory()
FormStyleBootstrap4.classes.update(
    {
        "outer": "form-group",
        "inner": "",
        "label": "h4",
        "info": "form-text",
        "error": "form-text text-danger py4web-validation-error",
        "submit": "btn btn-outline-info",
        "input": "form-control",
        "input[type=text]": "form-control",
        "input[type=date]": "form-control",
        "input[type=time]": "form-control",
        "input[type=datetime-local]": "form-control",
        "input[type=radio]": "form-check-input",
        "input[type=checkbox]": "form-check-input",
        "input[type=submit]": "btn btn-outline-info",
        "input[type=password]": "form-control",
        "input[type=file]": "form-control-file",
        "select": "form-control",
        "textarea": "form-control",
    }
)

FormStyleBootstrap5 = FormStyleFactory()
FormStyleBootstrap5.classes.update(
    {
        "outer": "mb-3 col-auto",  # Replaced 'form-group' with 'mb-3' for margin-bottom
        "inner": "",
        "label": "form-label",  # Explicitly use 'form-label' for labels
        "info": "form-text",
        "error": "form-text text-danger py4web-validation-error",
        "submit": "btn btn-primary",
        "input": "form-control",
        "input[type=text]": "form-control",
        "input[type=date]": "form-control",
        "input[type=time]": "form-control",
        "input[type=datetime-local]": "form-control",
        "input[type=radio]": "form-check-input",
        "input[type=checkbox]": "form-check-input",
        "input[type=submit]": "btn btn-primary",
        "input[type=password]": "form-control",
        "input[type=file]": "form-control",  # Bootstrap 5 doesn't have a specific 'form-control-file' class
        "select": "form-select",  # 'form-select' is used in Bootstrap 5 instead of 'form-control' for select elements
        "textarea": "form-control",
    }
)

FormStyleTailwind = FormStyleFactory()
FormStyleTailwind.classes.update(
    {
        "outer": "mb-4",
        "inner": "w-full flex flex-col space-y-1",
        "label": "block text-gray-700 font-medium",
        "info": "text-gray-500 text-sm",
        "error": "text-red-600 text-sm mt-1",
        "submit": "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition",
        "input": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
        "input[type=text]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
        "input[type=date]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
        "input[type=time]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
        "input[type=datetime-local]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
        "input[type=radio]": "form-radio h-5 w-5 text-blue-600",
        "input[type=checkbox]": "form-checkbox h-5 w-5 text-blue-600",
        "input[type=submit]": "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition",
        "input[type=password]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
        "input[type=file]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm",
        "select": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
        "textarea": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
    }
)

# ################################################################
# Form object (replaced SQLFORM)
# ################################################################


class Form(object):
    """
    Usage in py4web controller:

       def index():
           form = Form(db.thing, record=1)
           if form.accepted: ...
           elif form.errors: ...
           else: ...
           return dict(form=form)

    Arguments:
    :param table: a DAL table or a list of fields (equivalent to old SQLFORM.factory)
    :param record: a DAL record or record id
    :param readonly: set to True to make a readonly form
    :param deletable: set to False to disallow deletion of record
    :param showreadonly: show readonly fields True, False, or None for default behavior)
    :param formstyle: a function that renders the form using helpers (FormStyleDefault)
    :param dbio: set to False to prevent any DB writes
    :param keep_values: if set to true, it remembers the values of the previously submitted form
    :param form_name: the optional name of this form
    :param csrf_session: if None, no csrf token is added.  If a session, then a CSRF token is added and verified.
    :param lifespan: lifespan of CSRF token in seconds, to limit form validity.
    :param signing_info: information that should not change between when the CSRF token is signed and
        verified.  This information is not leaked to the form.  For instance, if you wish to verify
        that the identity of the logged in user has not changed, you can do as below.
        signing_info = session.get('user', {}).get('id', '')
        The content of the field should be convertible to a string via json.
    :param auto_process: bool - whether the form should automatically process POST data. If you set this to False,
        you are responsible for calling form.process(). useful for custom logic in a `if self.submitted:` block.
    """

    def __init__(
        self,
        table,
        record=None,
        readonly=False,
        deletable=True,
        showreadonly=True,
        formstyle=FormStyleDefault,
        dbio=True,
        keep_values=False,
        form_name=None,
        hidden=None,
        validation=None,
        csrf_session=None,
        csrf_protection=True,
        lifespan=None,
        signing_info=None,
        submit_value="Submit",
        show_id=False,
        auto_process=True,
        **kwargs,
    ):
        self.param = Param(
            formstyle=formstyle,
            hidden=hidden,
            submit_value=submit_value,
            sidecar=[],
        )

        if isinstance(table, list):
            if len(table) == 0:
                raise ValueError("Cannot build form with empty list of fields")
            # using _table to check if Field.bind was called
            # and the field is bound to a table, since unlike `tablename`, `_table` is
            # only set in Field.bind()
            all_tablenames = list(
                set(
                    str(getattr(field, "_table", None) or "no_table") for field in table
                )
            )

            # only disable dbio if the fields are from multiple tables
            # this allows making forms for a subset of fields easily:
            #   Form([db.tbl.field1, db.tbl.field2])
            if len(all_tablenames) > 1 or all_tablenames[0] in "no_table":
                dbio = False
                # Mimic a table from a list of fields without calling define_table
                form_name = form_name or "no_table"
                for field in table:
                    field.tablename = getattr(field, "tablename", form_name)
            else:
                # if we just have 1 table, use it as the form name
                form_name = form_name or all_tablenames[0]

        if isinstance(record, (int, str)):
            record_id = int(str(record))
            self.record = table[record_id]
            if not self.record:
                raise HTTP(404)
        else:
            self.record = record

        # computed from input and not changed
        self.table = table
        self.deletable = self.record and deletable and not readonly
        self.dbio = dbio
        self.keep_values = True if keep_values or self.record else False
        self.form_name = form_name or table._tablename
        self.csrf_session = csrf_session
        self.signing_info = signing_info
        self.validation = validation
        self.lifespan = lifespan
        self.csrf_protection = csrf_protection
        self.show_id = show_id
        # initialized and can change
        self.vars = {}
        self.errors = {}
        self.readonly = readonly
        # if showreadoanly is None only display readonly fields for edit for or non db based forms
        if showreadonly is None:
            showreadonly = self.record or isinstance(table, (list, tuple))
        self.showreadonly = showreadonly
        self.submitted = False
        self.deleted = False
        self.accepted = False
        self.formkey = None
        self.cached_helper = None
        self.action = None

        self.kwargs = kwargs if kwargs else {}
        self.method = self.kwargs.get("_method", "POST")

        if self.record:
            self.vars = self._read_vars_from_record(table)

        try:
            self.post_vars = request.GET if self.method == "GET" else request.POST
        except KeyError:
            self.post_vars = {}

        try:
            form_vars = copy.deepcopy(request.forms)
        except KeyError:
            form_vars = {}
        for k in form_vars:
            self.vars[k] = form_vars[k]

        # We only a process a form if it is POST and the formkey matches (correct formname and crsf)
        # Notice: we never expose the crsf uuid, we only use to sign the form uuid
        if self.post_vars:
            self.submitted = True

        if not readonly and auto_process:
            self.process()
        if self.csrf_protection:
            self._sign_form()

    def process(self):
        if not self.submitted:
            return

        if self.csrf_protection and not self._verify_form(self.post_vars):
            return

        if self.post_vars.get("_delete") and self.dbio:
            self.accepted = True
            self.deleted = True
            self.record.delete_record()
            return

        record_id = self.record and self.record.get("id")
        validated_vars = {}
        uploaded_fields = set()
        for field in self.table:
            if field.writable and field.type != "id":
                original_value = self.post_vars.get(field.name)
                if isinstance(original_value, list):
                    if len(original_value) == 1:
                        original_value = original_value[0]
                    elif len(original_value) == 0:
                        original_value = None
                (value, error) = field.validate(original_value, record_id)
                if field.type == "password" and record_id and value is None:
                    continue
                if field.type == "upload":
                    uploaded_fields.add(field.name)
                    value = request.files.get(field.name)
                    delete = self.post_vars.get("_delete_" + field.name)
                    if value is not None:
                        if field.uploadfield == True and field.uploadfolder:
                            validated_vars[field.name] = field.store(
                                value.file,
                                value.raw_filename,
                                field.uploadfolder,
                            )
                        elif field.uploadfield and field.db:
                            validated_vars[field.name] = field.store(
                                value.file,
                                value.raw_filename,
                                field.uploadfolder,
                            )
                        else:
                            validated_vars[field.name] = value
                    elif self.record:
                        if not delete:
                            validated_vars[field.name] = self.record.get(field.name)
                        else:
                            validated_vars[field.name] = value = None
                elif field.type == "boolean":
                    validated_vars[field.name] = value is not None
                else:
                    validated_vars[field.name] = value
                if error:
                    self.errors[field.name] = error
        if self.errors:
            for field_name in uploaded_fields:
                validated_vars[field_name] = (
                    self.record and self.record.get(field_name) or None
                )
        self.vars.update(validated_vars)
        if self.record and self.dbio:
            self.vars["id"] = self.record.id
        if self.validation:
            self.validation(self)
        if not self.errors:
            self.accepted = True
            if self.dbio:
                self.update_or_insert(validated_vars)

    def _read_vars_from_record(self, table):
        if isinstance(table, list):
            # The table is just a list of fields.
            return {field.name: self.record.get(field.name) for field in table}
        else:
            return {
                name: self.record[name] for name in table.fields if name in self.record
            }

    def _make_key(self):
        if self.csrf_session is not None:
            key = str(uuid.uuid1())
            self.csrf_session["_formkey"] = key
        else:
            key = str(uuid.uuid1())
            response.set_cookie("_formkey", key, same_site="Strict")
        return key

    def _get_key(self):
        if self.csrf_session is not None:
            key = self.csrf_session.get("_formkey")
        else:
            key = request.get_cookie("_formkey")
        return key

    def _sign_form(self):
        """Signs the form, for csrf"""
        # Adds a form key.  First get the signing key from the session.
        payload = {"ts": str(time.time())}
        if self.lifespan is not None:
            payload["exp"] = time.time() + self.lifespan
        key = self._get_key() or self._make_key()
        self.formkey = to_native(jwt.encode(payload, key, algorithm="HS256"))

    def _verify_form(self, post_vars):
        """Verifies the csrf signature and form name."""
        if post_vars.get("_formname") != self.form_name:
            return False
        token = post_vars.get("_formkey")
        key = self._get_key()
        if not key:
            return False
        try:
            jwt.decode(token, key, algorithms=["HS256"])
            return True
        except Exception:
            return False

    def update_or_insert(self, validated_vars):
        if self.record:
            self.record.update_record(**validated_vars)
        else:
            # warning, should we really insert if record
            self.vars["id"] = self.table.insert(**validated_vars)

    def clear(self, vars, errors):
        errors.clear()
        if not self.record and not self.keep_values:
            vars.clear()
            for field in self.table:
                vars[field.name] = (
                    field.default() if callable(field.default) else field.default
                )

    def helper(self):
        vars, errors = copy.copy(self.vars), copy.copy(self.errors)
        if self.accepted:
            self.clear(vars, errors)
        if not self.cached_helper:
            helper = self.param.formstyle(
                self.table,
                vars,
                errors,
                self.readonly,
                self.deletable,
                self.showreadonly,
                show_id=self.show_id,
                kwargs=self.kwargs,
            )
            for item in self.param.sidecar:
                helper["form"][-1][-1].append(item)

                button_attributes = item.attributes
                button_attributes["_label"] = item.children[0]
                helper["json_controls"]["form_buttons"] += [button_attributes]

            if self.action:
                helper["form"]["_action"] = self.action

            if self.param.submit_value:
                helper["controls"]["submit"]["_value"] = self.param.submit_value

            if self.form_name:
                helper["controls"]["hidden_widgets"]["formname"] = INPUT(
                    _type="hidden", _name="_formname", _value=self.form_name
                )
                helper["form"].append(helper["controls"]["hidden_widgets"]["formname"])

                helper["json_controls"]["form_values"]["_formname"] = self.form_name

            if self.formkey:
                helper["controls"]["hidden_widgets"]["formkey"] = INPUT(
                    _type="hidden", _name="_formkey", _value=self.formkey
                )
                helper["form"].append(helper["controls"]["hidden_widgets"]["formkey"])

                helper["json_controls"]["form_values"]["_formkey"] = self.formkey

            for key in self.param.hidden or {}:
                helper["controls"]["hidden_widgets"][key] = INPUT(
                    _type="hidden", _name=key, _value=self.param.hidden[key]
                )
                helper["form"].append(helper["controls"]["hidden_widgets"][key])

            helper["controls"]["begin"] = XML(
                str(helper["controls"]["begin"])
                + "".join(
                    str(helper["controls"]["hidden_widgets"][hidden_field])
                    for hidden_field in helper["controls"]["hidden_widgets"]
                )
            )
            self.cached_helper = helper

        return self.cached_helper

    @staticmethod
    def is_image(value):
        """
        Tries to check if the filename provided references to an image

        Checking is based on filename extension. Currently recognized:
           gif, png, jp(e)g, bmp

        Args:
            value: filename
        """
        if value:
            (_, extension) = os.path.splitext(value)
            if extension in [".gif", ".png", ".jpg", ".jpeg", ".bmp"]:
                return True
        return False

    @property
    def custom(self):
        return self.helper()["controls"]

    @property
    def structure(self):
        return self.helper()["form"]

    def as_json(self):
        return self.helper()["json_controls"]

    def xml(self):
        return self.structure.xml()

    def __str__(self):
        return self.xml()
