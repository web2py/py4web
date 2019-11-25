WORK IN PROGRESS

Just know that ``py4web.utils.form.Form`` is a pretty much equivalent to web2py's ``SQLFORM``.

Form will accept the following:
    - table: a DAL table or a list of fields (equivalent to old SQLFORM.factory)
    - record: a DAL record or record id
    - readonly: set to True to make a readonly form
    - deletable: set to False to disallow deletion of record
    - formstyle: a function that renders the form using helpers (FormStyleDefault)
    - dbio: set to False to prevent any DB writes
    - keep_values: if set to true, it remembers the values of the previously submitted form
    - form_name: the optional name of this form
