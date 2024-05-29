import collections
import datetime

from pydal.validators import *
from yatl.helpers import XML

from py4web import HTTP, URL, action, request
from py4web.core import Fixture
from py4web.utils.url_signer import URLSigner


class VueForm(Fixture):
    """This is a prototype class for building client-side forms with
    validation."""

    FORM = '<vueform url="{url}" check_url="{check_url}" cancel_url="{cancel_url}"></vueform>'

    TYPE_CONVERSION = {
        "boolean": "checkbox",
        "date": "date",
        "datetime": "datetime",
        "password": "password",
        "text": "textarea",
        "integer": "number",
        "double": "number",
        "string": "text",
    }

    def __init__(
        self,
        fields_or_table,
        session,
        path,
        readonly=False,
        signer=None,
        db=None,
        auth=None,
        use_id=False,
        validate=None,
    ):
        """fields_or_table is a list of Fields from DAL, or a table.
        If a table is passed, the fields that are marked writable
        (or readable, if readonly=True) are included.
        session is used to sign the URLs.
        The other parameters are optional, and are used only
        if they will be needed to process the get and post metods.
        @param fields_or_table: list of Field for a database table, or table itself.
        @param session: session, used to validate access and sign.
        @param path: path used for form GET/POST
        @param readonly: If true, the form is readonly.
        @param signer: signer for URLs, or else, a new signer is created.
        @param db: database.  Used by implementation.
        @param auth: auth.  Used by implementation.
        @param use_id: use an ID in the AJAX callbacks.
        @param validate: A function that takes as arguments the dictionary of
            fields, and performs any desired extra validation.  If an error is
            set, then the form is not acted upon, and the error is shown to the user.
        """
        assert session is not None, "You must provide a session."
        self.path_form = path + "/form"
        self.path_check = path + "/check"
        self.db = db
        self.signer = signer or URLSigner(session)
        self.__prerequisites__ = [db, self.signer]  # session to be added by the signer
        self.validate = validate
        # Creates entry points for giving the blank form, and processing form submissions.
        # There are three entry points:
        # - Form setup GET: This gets how the form is set up, including the types of the fields.
        # - Form GET: This gets the values of the fields.
        # - Form PUT: This gives the values of the fields, and performs whatever
        #   action needs to be peformed.
        # This division is done so that the GET and PUT action, but not the setup_GET,
        # need to be over-ridden when the class is subclassed.
        url_params = ["<id>"] if use_id else []
        self.use_id = use_id
        # NOTE: we need a list below, as the iterator otherwise can be used only once.
        # Iterators by default are a very lame idea indeed.
        args = list(filter(None, [session, db, auth, self.signer.verify()]))
        f = action.uses(*args)(self.get)
        # print("Registering:", "/".join([self.path_form] + url_params))
        action("/".join([self.path_form] + url_params), method=["GET"])(f)
        f = action.uses(*args)(self.post)
        action("/".join([self.path_form] + url_params), method=["POST"])(f)
        f = action.uses(*args)(self.validate_field)
        action("/".join([self.path_check] + url_params), method=["POST"])(f)
        # Stores the parameters that are necessary for creating the form.
        # Generates the list of field descriptions.
        self.readonly = readonly
        self.fields = collections.OrderedDict()
        for field in fields_or_table:
            self.fields[field.name] = dict(
                field=field,  # Field in the form specification.
                error=None,  # Any error found.
                value=None,
                validated_value=None,
            )

    def _get_fields_for_web(self, values):
        """Returns a dictionary mapping each field to information that is ready
        to be sent to the web app.
        """
        fields = collections.OrderedDict()
        for f in self.fields.values():
            # We only include readable fields.
            ff = f["field"]
            if ff.readable:
                # Formats the field.
                v = values.get(ff.name)
                if v is None and hasattr(ff, "default"):
                    v = ff.default() if callable(ff.default) else ff.default
                # Builds a default web field.
                web_field = dict(
                    name=ff.name,
                    writable=ff.writable and not self.readonly,
                    label=ff.label,
                    type=VueForm.TYPE_CONVERSION.get(ff.type, "text"),
                    placeholder=ff.placeholder if hasattr(ff, "placeholder") else None,
                    comment=ff.comment if hasattr(ff, "comment") else None,
                    error=f["error"],
                    value=v,
                )
                # Adapts the web field to specific types of fields.
                # Datetime
                if ff.type == "datetime":
                    web_field["value"] = v
                # Dropdown
                if isinstance(ff.requires, IS_IN_SET):
                    if not ff.writable:
                        if isinstance(v, list):
                            web_field["value"] = ", ".join(v)
                        else:
                            web_field["value"] = v
                    else:
                        theset = ff.requires.theset
                        labels = ff.requires.labels or theset
                        if ff.requires.zero:
                            theset.insert(0, "")
                        vals = [dict(text=l, label=k) for (l, k) in zip(labels, theset)]
                        web_field["type"] = "dropdown"
                        web_field["values"] = vals
                        web_field["multiple"] = ff.requires.multiple
                fields[ff.name] = web_field
        return fields

    def read_values(self, record_id):
        """
        Can be overridden.
        The function must return the data to fill the form.
        This must return a dictionary mapping each field name to a field value.
        This function should be over-ridden.
        @param record_id: can be either None, e.g. for an insertion form, or the id of
            something that has to be read to be edited / viewed.
        """
        values = {}
        for f in self.fields.values():
            ff = f["field"]
            values[ff.name] = ff.formatter(None)
        return values

    def get(self, id=None):
        """Returns the info necessary to dispay the form: a list of fields,
        filled with values."""
        # Gets the values from the fields.
        record_id = None if id == "None" else id
        values = self.read_values(record_id)
        fields = self._get_fields_for_web(values)
        response = []
        for n, f in fields.items():
            response.append(f)
        return dict(fields=list(fields.values()), readonly=self.readonly)

    def __call__(self, id=None, cancel_url=""):
        """This method returns the element that can be included in the page.
        The *args and **kwargs are used when subclassing, to allow for forms
        that are 'custom built' for some need.
        """
        return XML(
            VueForm.FORM.format(
                url=self.url(id),
                check_url=self.check_url(id),
                cancel_url=cancel_url,
            )
        )

    def url(self, id):
        return URL(*filter(None, [self.path_form, id]), signer=self.signer)

    def check_url(self, id):
        return URL(*filter(None, [self.path_check, id]), signer=self.signer)

    def _validate_one_field(self, f_name, f_value, record_id=None):
        """Validates one field, returning the error if any, else None.
        The record_id is used by the validators."""
        f = self.fields[f_name]
        ff = f["field"]
        f["value"] = f_value
        f["error"] = None
        if hasattr(ff, "validate"):
            f["validated_value"], f["error"] = ff.validate(f_value, record_id)
        else:
            f["validated_value"] = f_value
        return f["error"]

    def validate_field(self, id=None):
        """Validates one field, called from the client."""
        name = request.json["name"]
        # Gets the default for that field, if specified.
        f = self.fields[name]
        ff = f["field"]
        value = request.json.get("value", ff.default)
        return dict(error=self._validate_one_field(name, value, record_id=id))

    def validate_form(self, record_id=None):
        """Validates an entire form, setting the error field in each"""
        # First performs the normal valuation.
        for f_name, f_value in request.json.items():
            self._validate_one_field(f_name, f_value, record_id=record_id)
        # If an additional validation function is specified, uses it.
        if self.validate is not None:
            self.validate(self.fields)
        return not any([ff["error"] for ff in self.fields.values()])

    def post(self, id=None):
        """Processes the form submission. The return value is the same as for get."""
        record_id = None if id == "None" else id
        is_valid = self.validate_form(record_id=record_id)
        values = {n: f["validated_value"] for n, f in self.fields.items()}
        if not is_valid:
            # Returns the values with the errors.
            fs = self._get_fields_for_web(values)
            return dict(fields=list(fs.values()), readonly=self.readonly)
        else:
            # We do not want to overwrite the record id.
            if "id" in values:
                del values["id"]
            return self.process_post(record_id, values)

    def process_post(self, id, values):
        """This function should be over-ridden.  It processes the post.
        @param id: id of the item; can be None for a create;
        @param values: dictionary from field name to field value."""
        return None
