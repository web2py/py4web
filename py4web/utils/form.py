import json
import jwt
import time
import uuid
import copy
import os

from pydal.objects import FieldVirtual

from py4web import request, response, HTTP
from py4web.utils.param import Param
from pydal._compat import to_native
from pydal.validators import Validator

from yatl.helpers import (
    A,
    TEXTAREA,
    INPUT,
    TR,
    TD,
    TABLE,
    DIV,
    LABEL,
    FORM,
    SELECT,
    OPTION,
    P,
    SPAN,
    XML,
)


def get_options(validators):
    options = None
    if validators:
        if not isinstance(validators, (list, tuple)):
            validators = [validators]
        for item in validators:
            if hasattr(item, "options"):
                options = item.options
                break
        if callable(options):
            options = options()
    return options


class FormStyleFactory:
    def __init__(self):
        self.classes = {
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
            "input[type=checkbox]": "",
            "input[type=submit]": "",
            "input[type=password]": "",
            "input[type=file]": "",
            "select": "",
            "textarea": "",
        }
        self.class_inner_exceptions = {}

    def produce(
        self,
        table,
        vars,
        errors,
        readonly,
        deletable,
        noncreate,
        classes=None,
        class_inner_exceptions=None,
        kwargs=None,
    ):
        self.classes.update(classes or {})
        self.class_inner_exceptions.update(class_inner_exceptions or {})
        kwargs = kwargs if kwargs else {}

        form_method = "POST"
        form_action = request.url
        form_enctype = "multipart/form-data"

        form = FORM(
            _method=form_method, _action=form_action, _enctype=form_enctype, **kwargs
        )

        controls = Param(
            labels=dict(),
            widgets=dict(),
            wrapped_widgets=dict(),
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
            **kwargs
        )

        class_label = self.classes["label"]
        class_outer = self.classes["outer"]
        class_inner = self.classes["inner"]
        class_error = self.classes["error"]
        class_info = self.classes["info"]

        all_fields = [x for x in table]
        if "_virtual_fields" in dir(table):
            all_fields += table._virtual_fields
        for field in all_fields:

            # Reset the json control fields.
            field_attributes = dict()
            field_value = None

            field_name = field.name
            field_type = field.type
            field_comment = field.comment if field.comment else ""
            field_label = field.label
            input_id = "%s_%s" % (field.tablename, field.name)
            if isinstance(field, FieldVirtual):
                value = None
            else:
                value = vars.get(
                    field.name,
                    field.default() if callable(field.default) else field.default,
                )
            error = errors.get(field.name)
            field_class = "type-" + field.type.split()[0].replace(":", "-")
            placeholder = (
                field._placeholder if "_placeholder" in field.__dict__ else None
            )
            title = field._title if "_title" in field.__dict__ else None
            field_disabled = False

            # only diplay field if readable or writable
            if not field.readable and not field.writable:
                continue

            # if this is a reaonly field only show readable fields
            if readonly:
                if not field.readable:
                    continue

            # if this is an create form (unkown id) then only show writable fields. Some if an edit form was made from a list of fields and noncreate=True
            elif not vars.get("id") and noncreate:
                if not field.writable:
                    continue

            # ignore blob fields
            if field.type == "blob":  # never display blobs (mistake?)
                continue

            # ignore fields of type id its value is equal to None
            if field.type == "id" and value is None:
                field.writable = False
                continue

            # if the form is readonly or this is an id type field, display it as readonly
            if (
                readonly
                or not field.writable
                or field.type == "id"
                or isinstance(field, FieldVirtual)
            ):
                if field.type == "boolean":

                    field_value = value
                    field_type = "checkbox"

                    control = INPUT(
                        _type=field_type,
                        _id=input_id,
                        _name=field_name,
                        _value="ON",
                        _disabled="",
                        _checked=value,
                        _title=title,
                    )
                else:
                    if isinstance(field, FieldVirtual):
                        field_value = field.f(vars)
                    else:
                        field_value = (
                            field.represent and field.represent(value) or value or ""
                        )
                    field_type = "represent"

                    control = DIV(field_value)

                field_disabled = True

            # if we have a widget for the field use it
            elif field.widget:
                control = field.widget(field, vars)

                # Grab the custom widget attributes.
                field_attributes = control.attributes
                field_type = "widget"
                field_value = value

            # else pick the proper default widget
            elif field.type == "text":

                field_value = value or ""
                field_type = "text"

                control = TEXTAREA(
                    field_value,
                    _id=input_id,
                    _name=field_name,
                    _placeholder=placeholder,
                    _title=title,
                )

            elif field.type == "date":

                field_value = value
                field_type = "date"

                control = INPUT(
                    _value=field_value,
                    _type="date",
                    _id=input_id,
                    _name=field_name,
                    _placeholder=placeholder,
                    _title=title,
                )

            elif field.type == "datetime":
                helpervalue = str(value)
                helpervalue = helpervalue.replace(" ", "T")

                field_value = helpervalue
                field_type = "datetime-local"

                control = INPUT(
                    _value=helpervalue,
                    _type="datetime-local",
                    _id=input_id,
                    _name=field_name,
                    _placeholder=placeholder,
                    _title=title,
                )
            elif field.type == "time":

                field_value = value
                field_type = "time"

                control = INPUT(
                    _value=value,
                    _type="time",
                    _id=input_id,
                    _name=field_name,
                    _placeholder=placeholder,
                    _title=title,
                )

            elif field.type == "boolean":

                field_value = value
                field_type = "checkbox"
                field_attributes["_value"] = "ON"

                control = INPUT(
                    _type="checkbox",
                    _id=input_id,
                    _name=field_name,
                    _value=field_attributes["_value"],
                    _checked=value,
                    _title=title,
                )

            elif field.type == "upload":
                control = DIV()
                if value and not error:
                    download_div = DIV()

                    download_div.append(
                        LABEL(
                            "Currently:  ",
                        )
                    )
                    if getattr(field, "download_url", None):
                        url = field.download_url(value)
                    else:
                        url = "#"
                    download_div.append(A(" download ", _href=url))

                    # Set the download url.
                    field_attributes["_download_url"] = url

                    # Set the flag determining whether the file is an image.
                    field_attributes["_is_image"] = (url != "#") and Form.is_image(
                        value
                    )

                    delete_checkbox_name = "_delete_" + field_name

                    download_div.append(
                        INPUT(
                            _type="checkbox",
                            _value="ON",
                            _name=delete_checkbox_name,
                            _title=title,
                        )
                    )
                    download_div.append(" (check to remove)")

                    delete_field_attributes = dict()

                    delete_field_attributes["_label"] = "Remove"
                    delete_field_attributes["_value"] = "ON"
                    delete_field_attributes["_type"] = "checkbox"
                    delete_field_attributes["_name"] = delete_checkbox_name

                    json_controls["form_fields"] += [delete_field_attributes]
                    json_controls["form_values"][delete_checkbox_name] = None

                    control.append(download_div)

                control.append(LABEL("Change: "))
                control.append(INPUT(_type="file", _id=input_id, _name=field_name))

                field_value = None
                field_type = "file"

            elif get_options(field.requires) is not None and field.writable == True:
                multiple = field.type.startswith("list:")
                value = list(map(str, value if isinstance(value, list) else [value]))

                field_options = [
                    [k, v, (not k is None and k in value)]
                    for k, v in get_options(field.requires)
                ]
                option_tags = [
                    OPTION(v, _value=k, _selected=_selected)
                    for (k, v, _selected) in field_options
                ]

                control = SELECT(
                    *option_tags,
                    _id=input_id,
                    _name=field_name,
                    _multiple=multiple,
                    _title=title
                )

                field_value = value
                field_type = "options"
                field_attributes["_multiple"] = multiple
                field_attributes["_options"] = field_options

            else:

                field_type = "password" if field.type == "password" else "text"

                if field.type.startswith("list:"):
                    value = json.dumps(value or [])

                field_value = None if field.type == "password" else value
                field_autocomplete = "off" if field_type == "password" else "on"

                control = INPUT(
                    _type=field_type,
                    _id=input_id,
                    _name=field_name,
                    _value=field_value,
                    _class=field_class,
                    _placeholder=placeholder,
                    _title=title,
                    _autocomplete=field_autocomplete,
                )

                field_attributes["_autocomplete"] = field_autocomplete

            key = control.name.rstrip("/")

            if key == "input":
                key += "[type=%s]" % (control["_type"] or "text")

            control["_class"] = (
                control.attributes.get("_class", "") + " " + self.classes.get(key, "")
            ).strip()

            # Set the form controls.
            controls["labels"][field_name] = field_label
            controls["widgets"][field_name] = control
            controls["comments"][field_name] = field_comment
            controls["titles"][field_name] = title
            controls["placeholders"][field_name] = placeholder

            # Set the remain json field attributes.
            field_attributes["_title"] = title
            field_attributes["_label"] = field_label
            field_attributes["_comment"] = field_comment
            field_attributes["_id"] = input_id
            field_attributes["_class"] = field_class
            field_attributes["_name"] = field_name
            field_attributes["_type"] = field_type
            field_attributes["_placeholder"] = placeholder
            field_attributes["_error"] = error
            field_attributes["_disabled"] = field_disabled

            # Add to the json controls.
            json_controls["form_fields"] += [field_attributes]
            json_controls["form_values"][field_name] = field_value

            if error:
                controls["errors"][field.name] = error

            if field.type == "boolean":
                form.append(
                    DIV(
                        SPAN(control, _class=class_inner),
                        LABEL(
                            " " + field.label,
                            _for=input_id,
                            _class=class_label,
                            _style="display: inline !important",
                        ),
                        P(error, _class=class_error) if error else "",
                        P(field.comment or "", _class=class_info),
                        _class=class_outer,
                    )
                )
                controls["wrapped_widgets"][field_name] = SPAN(
                    control, _class=class_inner
                )
            else:
                form.append(
                    DIV(
                        LABEL(field.label, _for=input_id, _class=class_label),
                        DIV(
                            control,
                            _class=self.class_inner_exceptions.get(
                                control.name, class_inner
                            ),
                        ),
                        P(error, _class=class_error) if error else "",
                        P(field.comment or "", _class=class_info),
                        _class=class_outer,
                    )
                )
                controls["wrapped_widgets"][field_name] = DIV(
                    control,
                    _class=self.class_inner_exceptions.get(control.name, class_inner),
                )

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
                _name=deletable_field_name,
                _class=self.classes["input[type=checkbox]"],
            )

            form.append(
                DIV(
                    SPAN(
                        controls["delete"],
                        _class=class_inner,
                        _stye="vertical-align: middle;",
                    ),
                    P(
                        deletable_record_attributes["_label"],
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


FormStyleDefault = FormStyleFactory().produce


def FormStyleBulma(table, vars, errors, readonly, deletable, noncreate, kwargs=None):
    classes = {
        "outer": "field",
        "inner": "control",
        "label": "label",
        "info": "help",
        "error": "help is-danger py4web-validation-error",
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
    return FormStyleDefault(
        table,
        vars,
        errors,
        readonly,
        deletable,
        noncreate,
        classes=classes,
        class_inner_exceptions={"select": "select"},
        kwargs=kwargs,
    )


def FormStyleBootstrap4(
    table, vars, errors, readonly, deletable, noncreate, kwargs=None
):
    classes = {
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
    return FormStyleDefault(
        table, vars, errors, readonly, deletable, noncreate, classes, kwargs
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
    :param noncreate: make sure when you use a form with a list of fields that does not contain the id field, does not always render the create form.
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
    """

    def __init__(
        self,
        table,
        record=None,
        readonly=False,
        deletable=True,
        noncreate=False,
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
        **kwargs
    ):
        self.param = Param(
            formstyle=formstyle,
            hidden=hidden,
            submit_value=submit_value,
            sidecar=[],
        )

        if isinstance(table, list):
            dbio = False
            # Mimic a table from a list of fields without calling define_table
            form_name = form_name or "none"
            for field in table:
                field.tablename = getattr(field, "tablename", form_name)

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
        # initialized and can change
        self.vars = {}
        self.errors = {}
        self.readonly = readonly
        self.noncreate = noncreate
        self.submitted = False
        self.deleted = False
        self.accepted = False
        self.formkey = None
        self.cached_helper = None
        self.action = None

        self.kwargs = kwargs if kwargs else {}

        if readonly or request.method == "GET":
            if self.record:
                self.vars = self._read_vars_from_record(table)
        else:
            post_vars = request.POST
            self.vars = copy.deepcopy(request.forms)
            self.submitted = True
            process = False

            # We only a process a form if it is POST and the formkey matches (correct formname and crsf)
            # Notice: we never expose the crsf uuid, we only use to sign the form uuid
            if request.method == "POST":
                if not self.csrf_protection or self._verify_form(post_vars):
                    process = True
            if process:
                record_id = self.record and self.record.get("id")
                if not post_vars.get("_delete"):
                    validated_vars = {}
                    uploaded_files = []
                    for field in self.table:
                        if field.writable and field.type != "id":
                            original_value = post_vars.getall(field.name)
                            if isinstance(original_value, list):
                                if len(original_value) == 1:
                                    original_value = original_value[0]

                                elif len(original_value) == 0:
                                    original_value = None

                            if field.type.startswith("list:") and isinstance(
                                original_value, str
                            ):
                                original_value = json.loads(original_value or "[]")
                            (value, error) = field.validate(original_value, record_id)
                            if field.type == "password" and record_id and value is None:
                                continue
                            if field.type == "upload":
                                value = request.files.get(field.name)
                                print(str(value)[:100])
                                delete = post_vars.get("_delete_" + field.name)
                                if value is not None:
                                    if field.uploadfolder:
                                        uploaded_files.append(tuple((field, value)))
                                    validated_vars[field.name] = value
                                elif self.record:
                                    if not delete:
                                        validated_vars[field.name] = self.record.get(
                                            field.name
                                        )
                                    else:
                                        validated_vars[field.name] = None
                            elif field.type == "boolean":
                                validated_vars[field.name] = value is not None
                            else:
                                validated_vars[field.name] = value
                            if error:
                                self.errors[field.name] = error
                    self.vars.update(validated_vars)
                    if validation:
                        validation(self)
                    if self.record and dbio:
                        self.vars["id"] = self.record.id
                    if not self.errors:
                        for file in uploaded_files:
                            field, value = file
                            value = field.store(
                                value.file, value.filename, field.uploadfolder
                            )
                            if value is not None:
                                validated_vars[field.name] = value
                        self.accepted = True
                        self.vars.update(validated_vars)
                        if dbio:
                            self.update_or_insert(validated_vars)
                elif dbio:
                    self.deleted = True
                    self.record.delete_record()
            elif self.record:
                # This form should not be processed.  We return the same as for GET.
                self.vars = self._read_vars_from_record(table)
        if self.csrf_protection:
            self._sign_form()

    def _read_vars_from_record(self, table):
        if isinstance(table, list):
            # The table is just a list of fields.
            return {field.name: self.record.get(field.name) for field in table}
        else:
            return {
                name: table[name].formatter(self.record[name])
                for name in table.fields
                if name in self.record
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
        except:
            return False

    def update_or_insert(self, validated_vars):
        if self.record:
            self.record.update_record(**validated_vars)
        else:
            # warning, should we really insert if record
            self.vars["id"] = self.table.insert(**validated_vars)

    def clear(self):
        self.errors.clear()
        if not self.record and not self.keep_values:
            self.vars.clear()
            for field in self.table:
                self.vars[field.name] = (
                    field.default() if callable(field.default) else field.default
                )

    def helper(self):
        if self.accepted:
            self.clear()
        if not self.cached_helper:
            helper = self.param.formstyle(
                self.table,
                self.vars,
                self.errors,
                self.readonly,
                self.deletable,
                self.noncreate,
                kwargs=self.kwargs,
            )
            for item in self.param.sidecar:
                helper["form"][-1][-1].append(item)

                button_attributes = item.attributes
                button_attributes["_label"] = item.children[0]
                button_attributes["_type"] = (
                    button_attributes.pop("_role")
                    if "_role" in button_attributes
                    else None
                )
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
                "".join(
                    str(helper["controls"]["begin"])
                    + str(helper["controls"]["hidden_widgets"][hidden_field])
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
