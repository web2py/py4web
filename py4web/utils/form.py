import json
import jwt
import time
import uuid
from py4web import request, Session
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
            "error": "error",
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

    def produce(self, table, vars, errors, readonly, deletable, classes=None):
        self.classes.update(classes or {})
        form = FORM(_method="POST", _action=request.url, _enctype="multipart/form-data")
        controls = dict(
            labels=dict(),
            widgets=dict(),
            hidden_widgets=dict(),
            errors=dict(),
            begin=XML(form.xml().split("</form>")[0]),
            end=XML("</form>"),
        )
        class_label = self.classes["label"]
        class_outer = self.classes["outer"]
        class_inner = self.classes["inner"]
        class_error = self.classes["error"]
        class_info = self.classes["info"]

        for field in table:

            input_id = "%s_%s" % (field.tablename, field.name)
            value = vars.get(field.name, field.default)
            error = errors.get(field.name)
            field_class = field.type.split()[0].replace(":", "-")

            if not field.readable and not field.writable:
                continue
            if not readonly and not field.writable:
                continue
            if field.type == "blob":  # never display blobs (mistake?)
                continue
            if field.type == "id" and value is None:
                field.writable = False
                continue
            if readonly or field.type == "id":
                control = DIV(field.represent and field.represent(value) or value or "")
            elif field.widget:
                control = field.widget(table, value)
            elif field.type == "text":
                control = TEXTAREA(value or "", _id=input_id, _name=field.name)
            elif field.type == "date":
                control = INPUT(
                    _value=value, _type="date", _id=input_id, _name=field.name
                )
            elif field.type == "datetime":
                if isinstance(value, str):
                    value = value.replace(" ", "T")
                control = INPUT(
                    _value=value, _type="datetime-local", _id=input_id, _name=field.name
                )
            elif field.type == "time":
                control = INPUT(
                    _value=value, _type="time", _id=input_id, _name=field.name
                )
            elif field.type == "boolean":
                control = INPUT(
                    _type="checkbox",
                    _id=input_id,
                    _name=field.name,
                    _value="ON",
                    _checked=value,
                )
            elif field.type == "upload":
                control = DIV(INPUT(_type="file", _id=input_id, _name=field.name))
                if value:
                    control.append(A("download", _href=field.download_url(value)))
                    control.append(
                        INPUT(
                            _type="checkbox", _value="ON", _name="_delete_" + field.name
                        )
                    )
                    control.append("(check to remove)")
            elif get_options(field.requires) is not None:
                multiple = field.type.startswith("list:")
                value = list(map(str, value if isinstance(value, list) else [value]))
                option_tags = [
                    OPTION(v, _value=k, _selected=(not k is None and k in value))
                    for k, v in get_options(field.requires)
                ]
                control = SELECT(
                    *option_tags, _id=input_id, _name=field.name, _multiple=multiple
                )
            else:
                field_type = "password" if field.type == "password" else "text"
                control = INPUT(
                    _type=field_type,
                    _id=input_id,
                    _name=field.name,
                    _value=value,
                    _class=field_class,
                )

            key = control.name.rstrip("/")
            if key == "input":
                key += "[type=%s]" % (control["_type"] or "text")
            control["_class"] = self.classes.get(key, "")

            controls["labels"][field.name] = field.label
            controls["widgets"][field.name] = control
            if error:
                controls["errors"][field.name] = error

            form.append(
                DIV(
                    LABEL(field.label, _for=input_id, _class=class_label),
                    DIV(control, _class=class_inner),
                    P(error, _class=class_error) if error else "",
                    P(field.comment or "", _class=class_info),
                    _class=class_outer,
                )
            )
            if "id" in vars:
                form.append(INPUT(_name="id", _value=vars["id"], _hidden=True))
        if deletable:
            controls["delete"] = INPUT(
                _type="checkbox",
                _value="ON",
                _name="_delete",
                _class=self.classes["input[type=checkbox]"],
            )
            form.append(
                DIV(
                    DIV(controls["delete"], _class=class_inner,),
                    P("check to delete", _class="help"),
                    _class=class_outer,
                )
            )
        controls["submit"] = INPUT(
            _type="submit", _value="Submit", _class=self.classes["input[type=submit]"],
        )
        submit = DIV(DIV(controls["submit"], _class=class_inner,), _class=class_outer,)
        form.append(submit)
        return dict(form=form, controls=controls)


FormStyleDefault = FormStyleFactory().produce


def FormStyleBulma(table, vars, errors, readonly, deletable):
    classes = {
        "outer": "field",
        "inner": "control",
        "label": "label",
        "info": "help",
        "error": "help is-danger",
        "submit": "button",
        "input": "input",
        "input[type=text]": "input",
        "input[type=date]": "input",
        "input[type=time]": "input",
        "input[type=datetime-local]": "input",
        "input[type=radio]": "radio",
        "input[type=checkbox]": "checkbox",
        "input[type=submit]": "button",
        "input[type=password]": "password",
        "input[type=file]": "file",
        "select": "select",
        "textarea": "textarea",
    }
    return FormStyleDefault(table, vars, errors, readonly, deletable, classes)


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
    :param formstyle: a function that renders the form using helpers (FormStyleDefault)
    :param dbio: set to False to prevent any DB writes
    :param keep_values: if set to true, it remembers the values of the previously submitted form
    :param form_name: the optional name of this form
    :param csrf_session: if None, no csrf token is added.  If a session, then a CSRF token is added and verified.
    :param lifespan: lifespan of CSRF token in seconds, to limit form validity.
    :param signing_info: information that should not change between when the CSRF token is signed and
        verified.  This information is not leaked to the form.  For instance, if you wish to verify
        that the identity of the logged in user has not changed, you can do as below.
        signing_info = session.get("user", {}).get("id", "")
        The content of the field should be convertible to a string via json.
    """

    def __init__(
        self,
        table,
        record=None,
        readonly=False,
        deletable=True,
        formstyle=FormStyleDefault,
        dbio=True,
        keep_values=False,
        form_name=None,
        hidden=None,
        validation=None,
        csrf_session=None,
        lifespan=None,
        signing_info=None,
    ):

        if isinstance(table, list):
            dbio = False
            # Mimic a table from a list of fields without calling define_table
            form_name = form_name or "none"
            for field in table:
                field.tablename = getattr(field, "tablename", form_name)

        if isinstance(record, (int, str)):
            record_id = int(str(record))
            self.record = table[record_id]
        else:
            self.record = record

        self.table = table
        self.readonly = readonly
        self.deletable = deletable and not readonly and self.record
        self.formstyle = formstyle
        self.dbio = dbio
        self.keep_values = True if keep_values or self.record else False
        self.vars = {}
        self.errors = {}
        self.submitted = False
        self.deleted = False
        self.accepted = False
        self.form_name = form_name or table._tablename
        self.hidden = hidden
        self.formkey = None
        self.cached_helper = None
        self.csrf_session = csrf_session
        self.lifespan = lifespan
        self.signing_info = signing_info
        self.action = None

        if readonly or request.method == "GET":
            if self.record:
                self.vars = self._read_vars_from_record(table)
        else:
            post_vars = self.vars = request.forms
            self.submitted = True
            process = False

            # We only a process a form if it is POST and the formkey matches (correct formname and crsf)
            # Notice: we never expose the crsf uuid, we only use to sign the form uuid
            if request.method == "POST":
                if self._verify_form(post_vars):
                    process = True
            if process:
                record_id = self.record and self.record.get("id")
                if not post_vars.get("_delete"):
                    validated_vars = {}
                    for field in self.table:
                        if field.writable and field.readable and field.type != "id":
                            original_value = post_vars.get(field.name)
                            (value, error) = field.validate(original_value, record_id)
                            if field.type == "password" and record_id and value is None:
                                continue
                            if field.type == "upload":
                                value = request.files.get(field.name)
                                delete = post_vars.get("_delete_" + field.name)
                                if value is not None and hasattr(value, "file"):
                                    value = field.store(
                                        value.file, value.filename, field.uploadfolder
                                    )
                                elif self.record and not delete:
                                    value = self.record.get(field.name)
                                else:
                                    value = None
                            validated_vars[field.name] = value
                            if error:
                                self.errors[field.name] = error
                    if validation:
                        validation(self)
                    if self.record and dbio:
                        self.vars["id"] = self.record.id
                    if not self.errors:
                        self.accepted = True
                        if dbio:
                            self.update_or_insert(validated_vars)
                elif dbio:
                    self.deleted = True
                    self.record.delete_record()
            elif self.record:
                # This form should not be processed.  We return the same as for GET.
                self.vars = self._read_vars_from_record(table)
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

    def _get_key(self):
        if self.csrf_session is not None:
            key = self.csrf_session.get("_form_key")
            if key is None:
                key = str(uuid.uuid1())
                self.csrf_session["_form_key"] = key
        else:
            key = Session.SECRET
        additional_info = {
            "signing_info": self.signing_info,
            "form_name": self.form_name,
        }
        return key + "." + json.dumps(additional_info)

    def _sign_form(self):
        """Signs the form, for csrf"""
        # Adds a form key.  First get the signing key from the session.
        payload = {"ts": str(time.time())}
        if self.lifespan is not None:
            payload["exp"] = time.time() + self.lifespan
        self.formkey = jwt.encode(payload, self._get_key(), algorithm="HS256").decode(
            "utf-8"
        )

    def _verify_form(self, post_vars):
        """Verifies the csrf signature and form name."""
        if post_vars.get("_formname") != self.form_name:
            return False
        if not self.csrf_session:
            return True
        token = post_vars.get("_formkey")
        try:
            jwt.decode(token, self._get_key(), algorithms=["HS256"])
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
                self.vars[field.name] = field.default

    def helper(self):
        if self.accepted:
            self.clear()
        if not self.cached_helper:
            helper = self.formstyle(
                self.table, self.vars, self.errors, self.readonly, self.deletable
            )
            if self.action:
                helper["_action"] = self.action
            if self.form_name:
                helper["controls"]["hidden_widgets"]["formname"] = INPUT(
                    _type="hidden", _name="_formname", _value=self.form_name
                )
                helper["form"].append(helper["controls"]["hidden_widgets"]["formname"])
            if self.formkey:
                helper["controls"]["hidden_widgets"]["formkey"] = INPUT(
                    _type="hidden", _name="_formkey", _value=self.formkey
                )
                helper["form"].append(helper["controls"]["hidden_widgets"]["formkey"])
            for key in self.hidden or {}:
                helper["controls"]["hidden_widgets"][key] = INPUT(
                    _type="hidden", _name=key, _value=self.hidden[key]
                )
                helper["form"].append(helper["controls"]["hidden_widgets"][key])
            self.cached_helper = helper
        return self.cached_helper

    @property
    def custom(self):
        return self.helper()["controls"]

    def xml(self):
        return self.helper()["form"].xml()

    def __str__(self):
        return self.xml()
