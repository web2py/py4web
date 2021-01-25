import collections
import datetime
from py4web import action, URL, request
from yatl.helpers import XML
from py4web.utils.url_signer import URLSigner
from py4web.core import Fixture
from pydal.validators import *


class VueForm(Fixture):
    """This is a prototype class for building client-side forms with
    validation."""

    FORM = '<vueform url="{url}" check_url="{check_url}"></vueform>'

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
        path,
        session,
        fields_or_table,
        redirect_url=None,
        readonly=False,
        signer=None,
        db=None,
        auth=None,
        url_params=None,
        validate=None,
    ):
        """fields_or_table is a list of Fields from DAL, or a table.
        If a table is passed, the fields that are marked writable
        (or readable, if readonly=True) are included.
        session is used to sign the URLs.
        The other parameters are optional, and are used only
        if they will be needed to process the get and post metods.
        @param path: path used for form GET/POST
        @param session: session, used to validate access and sign.
        @param fields_or_table: list of Field for a database table, or table itself.
        @param redirect_url: redirect URL after success.
        @param readonly: If true, the form is readonly.
        @param signer: signer for URLs, or else, a new signer is created.
        @param db: database.  Used by implementation.
        @param auth: auth.  Used by implementation.
        @param url_params: parameters for AJAX URLs.
        @param validate: A function that takes as arguments the dictionary of
            fields, and performs any desired extra validation.  If an error is
            set, then the form is not acted upon, and the error is shown to the user.
        """
        self.path_form = path + "/form"
        self.path_check = path + "/check"
        self.redirect_url = redirect_url
        self.db = db
        self.__prerequisites__ = [session]
        self.signer = signer or URLSigner(session)
        self.validate = validate
        # Creates entry points for giving the blank form, and processing form submissions.
        # There are three entry points:
        # - Form setup GET: This gets how the form is set up, including the types of the fields.
        # - Form GET: This gets the values of the fields.
        # - Form PUT: This gives the values of the fields, and performs whatever
        #   action needs to be peformed.
        # This division is done so that the GET and PUT action, but not the setup_GET,
        # need to be over-ridden when the class is subclassed.
        url_params = url_params or []
        # NOTE: we need a list below, as the iterator otherwise can be used only once.
        # Iterators by default are a very lame idea indeed.
        args = list(filter(None, [session, db, auth, self.signer.verify()]))
        f = action.uses(*args)(self.get)
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
                if hasattr(ff, "formatter"):
                    v = ff.formatter(v)
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
                    web_field["value"] = v or datetime.datetime.utcnow()
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

    def _get_values(self):
        """The function must return the data to fill the form.
        This must return a dictionary mapping each field name to a field value,
        prior to any formatting.
        This function should be over-ridden.
        """
        return {}

    def get(self):
        """Returns the info necessary to dispay the form: a list of fields,
        filled with values."""
        # Gets the values from the fields.
        values = self._get_values()
        fields = self._get_fields_for_web(values)
        response = []
        for n, f in fields.items():
            response.append(f)
        return dict(fields=list(fields.values()), readonly=self.readonly)

    def __call__(self):
        """This method returns the element that can be included in the page.
        The *args and **kwargs are used when subclassing, to allow for forms
        that are 'custom built' for some need.
        """
        return XML(VueForm.FORM.format(url=self.url(), check_url=self.check_url()))

    def url(self):
        return URL(self.path_form, signer=self.signer)

    def check_url(self):
        return URL(self.path_check, signer=self.signer)

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
        """Validates an entire form, setting the error field in each """
        # First performs the normal valuation.
        for f_name, f_value in request.json.items():
            self._validate_one_field(f_name, f_value, record_id=record_id)
        # If an additional validation function is specified, uses it.
        if self.validate is not None:
            self.validate(self.fields)
        return not any([ff["error"] for ff in self.fields.values()])

    def post(self):
        """Processes the form submission. The return value is the same as for get.
        This function should be over-ridden.
        """
        if not self.validate_form():
            return self.get()
        else:
            return dict(redirect_url=URL(self.redirect_url))


class InsertForm(VueForm):
    """This subclass of VueForm generates a form to insert a record in a table."""

    def __init__(
        self, path, session, dbtable, validate=None, redirect_url=None, auth=None
    ):
        """fields_or_table is a list of Fields from DAL, or a table.
        If a table is passed, the fields that are marked writable
        (or readable, if readonly=True) are included.
        session is used to sign the URLs.
        The other parameters are optional, and are used only
        if they will be needed to process the get and post metods.
        @param session: session, used to validate access and sign.
        @param db: database.  This is used also so that the transaction
            is committed.
        @param dbtable: database table into which to do the insertions.
        @param redirect_url: redirect URL used after successful submission.
        @param validate: A function that takes as arguments the dictionary of
            fields, and performs any desired extra validation.  If an error is
            set, then the form is not acted upon, and the error is shown to the user.

        """
        super().__init__(
            path,
            session,
            dbtable,
            validate=validate,
            db=dbtable._db,
            redirect_url=redirect_url,
            auth=auth,
        )
        # We need to store the db table so we can perform the inserts later.
        self.dbtable = dbtable

    def post(self):
        if not self.validate_form():
            # Returns the values with the errors.
            values = {n: f["validated_value"] for n, f in self.fields.items()}
            fs = self._get_fields_for_web(values)
            return dict(fields=list(fs.values()), readonly=self.readonly)
        # Performs the insertion.
        d = {n: f["validated_value"] for n, f in self.fields.items()}
        self.dbtable.insert(**d)
        # Redirects to the desired URL.
        return dict(redirect_url=URL(self.redirect_url))


class TableForm(VueForm):
    """This subclass of VueForm generates a form to insert or edit
    a record in a table."""

    def __init__(
        self, path, session, dbtable, validate=None, redirect_url=None, auth=None
    ):
        """fields_or_table is a list of Fields from DAL, or a table.
        If a table is passed, the fields that are marked writable
        (or readable, if readonly=True) are included.
        session is used to sign the URLs.
        The other parameters are optional, and are used only
        if they will be needed to process the get and post metods.
        @param session: session, used to validate access and sign.
        @param db: database.  This is used also so that the transaction
            is committed.
        @param dbtable: database table into which to do the insertions.
        @param redirect_url: redirect URL used after successful submission.
        @param validate: A function that takes as arguments the dictionary of
            fields, and performs any desired extra validation.  If an error is
            set, then the form is not acted upon, and the error is shown to the user.
        """
        super().__init__(
            path,
            session,
            dbtable,
            db=dbtable._db,
            validate=validate,
            redirect_url=redirect_url,
            url_params=["<id>"],
            auth=auth,
        )
        # We need to store the db table so we can perform the inserts later.
        self.dbtable = dbtable

    def __call__(self, id=None):
        """This method returns the element that can be included in the page.
        @param id: if an id is specified, the form is an update form for the
        specified record id."""
        return XML(VueForm.FORM.format(url=self.url(id), check_url=self.check_url(id)))

    def url(self, id):
        return URL(self.path_form, id, signer=self.signer)

    def check_url(self, id):
        return URL(self.path_check, id, signer=self.signer)

    def _get_values(self, id):
        """The function must return the data to fill the form.
        This must return a dictionary mapping each field name to a field value.
        This function should be over-ridden.
        """
        values = {}
        if id != "None":
            row = self.db(self.dbtable.id == id).select().first()
            if row is not None:
                for f in self.fields.values():
                    ff = f["field"]
                    values[ff.name] = ff.formatter(row.get(ff.name))
        return values

    def get(self, id):
        """Returns the info necessary to dispay the form: a list of fields,
        filled with values."""
        # Gets the values from the fields.
        values = self._get_values(int(id))
        fields = self._get_fields_for_web(values)
        response = []
        for n, f in fields.items():
            f["value"] = values.get(n)
            response.append(f)
        return dict(fields=response, readonly=self.readonly)

    def post(self, id):
        if not self.validate_form(record_id=id):
            # Returns the values with the errors.
            values = {n: f["validated_value"] for n, f in self.fields.items()}
            fs = self._get_fields_for_web(values)
            return dict(fields=list(fs.values()), readonly=self.readonly)
        d = {n: f["validated_value"] for n, f in self.fields.items()}
        # We do not want to overwrite the record id.
        if "id" in d:
            del d["id"]
        if id == "None":
            # Performs the insertion.
            self.dbtable.insert(**d)
        else:
            # Performs the update.
            self.db(self.dbtable.id == int(id)).update(**d)
        # Redirects to the desired URL.
        return dict(redirect_url=URL(self.redirect_url))
