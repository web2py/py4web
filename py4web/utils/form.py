import uuid
import hmac
from py4web import DAL, request
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
)
from pydal._compat import to_bytes


def FormStyleDefault(table, vars, errors, readonly, deletable, classes=None):
    form = FORM(_method="POST", _action=request.path, _enctype="multipart/form-data")

    classes = classes or {}
    class_label = classes.get("label", "")
    class_outer = classes.get("outer", "")
    class_inner = classes.get("inner", "")
    class_error = classes.get("error", "")
    class_info = classes.get("info", "")

    for field in table:

        input_id = "%s_%s" % (field.tablename, field.name)
        value = field.formatter(vars.get(field.name))
        error = errors.get(field.name)
        field_class = field.type.split()[0].replace(":", "-")

        if not field.readable:
            continue
        if not readonly and not field.writable:
            continue
        if field.type == "blob":  # never display blobs (mistake?)
            continue
        if field.type == "id" and value is None:
            continue
        if readonly or field.type == "id":
            control = DIV(field.represent and field.represent(value) or value or "")            
        elif field.widget:
            control = field.widget(table, value)
        elif field.type == "text":
            control = TEXTAREA(value or "", _id=input_id, _name=field.name)
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
                    INPUT(_type="checkbox", _value="ON", _name="_delete_" + field.name)
                )
                control.append("(check to remove)")
        elif hasattr(field.requires, "options"):
            multiple = field.type.startswith("list:")
            value = list(map(str, value if isinstance(value, list) else [value]))
            options = [
                OPTION(v, _value=k, _selected=(not k is None and k in value))
                for k, v in field.requires.options()
            ]
            control = SELECT(
                *options, _id=input_id, _name=field.name, _multiple=multiple
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
        control["_class"] = classes.get(key, "")

        form.append(
            DIV(
                LABEL(field.label, _for=input_id, _class=class_label),
                DIV(control, _class=class_inner),
                P(error, _class=class_error) if error else "",
                P(field.comment or "", _class=class_info),
                _class=class_outer,
            )
        )

    if deletable:
        form.append(
            DIV(
                DIV(
                    INPUT(
                        _type="checkbox",
                        _value="ON",
                        _name="_delete",
                        _class=classes.get("input[type=checkbox]"),
                    ),
                    _class=class_inner,
                ),
                P("check to delete", _class="help"),
                _class=class_outer,
            )
        )
    submit = DIV(
        DIV(
            INPUT(
                _type="submit",
                _value="Submit",
                _class=classes.get("input[type=submit]"),
            ),
            _class=class_inner,
        ),
        _class=class_outer,
    )
    form.append(submit)
    return form


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
        "input[type=radio]": "radio",
        "input[type=checkbox]": "checkbox",
        "input[type=submit]": "button",
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
    - table: a DAL table or a list of fields (equivalent to old SQLFORM.factory)
    - record: a DAL record or record id
    - readonly: set to True to make a readonly form
    - deletable: set to False to disallow deletion of record
    - formstyle: a function that renders the form using helpers (FormStyleDefault)
    - dbio: set to False to prevent any DB writes
    - keep_values: if set to true, it remembers the values of the previously submitted form
    - form_name: the optional name of this form
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
        form_name=False,
        hidden=None,
        validation=None,
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

        if readonly or request.method == "GET":
            if self.record:
                self.vars = self.record
        else:
            post_vars = request.forms
            self.submitted = True
            process = False

            # We only a process a form if it is POST and the formkey matches (correct formname and crsf)
            # Notice: we never expose the crsf uuid, we only use to sign the form uuid
            if request.method == "POST":
                if post_vars.get("_formkey") == self.form_name:
                    process = True
            if process:
                if not post_vars.get("_delete"):
                    for field in self.table:
                        if field.writable:
                            value = post_vars.get(field.name)
                            record_id = self.record and self.record.get("id")
                            (value, error) = field.validate(value, record_id)
                            if field.type == "upload":
                                delete = post_vars.get("_delete_" + field.name)
                                if value is not None and hasattr(value, "file"):
                                    value = field.store(
                                        value.file, value.filename, field.uploadfolder
                                    )
                                elif self.record and not delete:
                                    value = self.record.get(field.name)
                                else:
                                    value = None
                            self.vars[field.name] = value
                            if error:
                                self.errors[field.name] = error
                    if validation:
                        validation(self)
                    if self.record and dbio:
                        self.vars["id"] = self.record.id
                    if not self.errors:
                        self.accepted = True
                        if dbio:
                            self.update_or_insert()
                elif dbio:
                    self.deleted = True
                    self.record.delete_record()
        # Store key for future CSRF
        self.formkey = self.form_name

    def update_or_insert(self):
        if self.record:
            self.record.update_record(**self.vars)
        else:
            # warning, should we really insert if record
            self.vars["id"] = self.table.insert(**self.vars)

    def clear(self):
        self.vars.clear()
        self.errors.clear()
        for field in self.table:
            self.vars[field.name] = field.default

    def helper(self):
        if self.accepted and not self.keep_values:
            self.vars.clear()
        if not self.cached_helper:
            helper = self.formstyle(
                self.table, self.vars, self.errors, self.readonly, self.deletable
            )
            if self.formkey:
                helper.append(
                    INPUT(_type="hidden", _name="_formkey", _value=self.formkey)
                )
            for key in self.hidden or {}:
                helper.append(INPUT(_type="hidden", _name=key, _value=self.hidden[key]))
            self.cached_helper = helper
        return self.cached_helper

    def xml(self):
        return self.helper().xml()

    def __str__(self):
        return self.xml()
