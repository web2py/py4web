WORK IN PROGRESS

Just know that ``py4web.utils.form.Form`` is a pretty much equivalent to web2py's ``SQLFORM``.

The `Form` constructor accepts the following arguments:

``
Form(self,
     table,
     record=None,
     readonly=False,
     deletable=True,
     formstyle=FormStyleDefault,
     dbio=True,
     keep_values=False,
     form_name=False,
     hidden=None,
     before_validate=None):
``:python

Where:

- `table`: a DAL table or a list of fields (equivalent to old SQLFORM.factory)
- `record`: a DAL record or record id
- `readonly`: set to True to make a readonly form
- `deletable`: set to False to disallow deletion of record
- `formstyle`: a function that renders the form using helpers (FormStyleDefault)
- `dbio`: set to False to prevent any DB writes
- `keep_values`: if set to true, it remembers the values of the previously submitted form
- `form_name`: the optional name of this form
- `hidden`: a dictionary of hidden fields that is added to the form
- `before_validate`: an optional validator.

## Example

Here is a simple example of a custom form not using database access.
We declare an endpoint `/form_example`, which will be used both for the GET and for the POST of the form:

``
from py4web import Session, redirect, URL
from py4web.utils.dbstore import DBStore
from py4web.utils.form import Form, FormStyleBulma

db = DAL('sqlite:memory')
session =  Session(storage=DBStore(db))

@action('form_example', method=['GET', 'POST'])
@action.uses('form_example.html', session)
def form_example():
    form = Form([
        Field('product_name'),
        Field('product_quantity', 'integer')],
        formstyle=FormStyleBulma)
    if form.accepted:
        # Do something with form.vars['product_name'] and form.vars['product_quantity']
        redirect(URL('index'))
    return dict(form=form)
``:python

The form can be displayed in the template simply using `[[=form]]`.

## Form validation

The validation of form input can be done in two ways.  One can define `requires` attributes of `Field`, or one can define explicitly a validation function.  To do the latter, we pass to `validate` a function that takes the form and returns a dictionary, mapping field names to errors.  If the dictionary is non-empty, the errors will be displayed to the user, and no database I/O will take place.

Here is an example:

``
from py4web import Field
from py4web.utils.form import Form, FormStyleBulma
from pydal.validators import IS_INT_IN_RANGE

def check_nonnegative_quantity(form):
    if not form.errors and form.vars['product_quantity'] % 2:
        form.errors['product_quantity'] = T('The product quantity must be even')

@action('form_example', method=['GET', 'POST'])
@action.uses('form_example.html', session)
def form_example():
    form = Form([
        Field('product_name'),
        Field('product_quantity', 'integer', requires=IS_INT_IN_RANGE(0,100))],
        validation=check_nonnegative_quantity,
        formstyle=FormStyleBulma)
    if form.accepted:
        # Do something with form.vars['product_name'] and form.vars['product_quantity']
        redirect(URL('index'))
    return dict(form=form)
``:python
