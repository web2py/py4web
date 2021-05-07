=====
Forms
=====

WORK IN PROGRESS

Just know that ``py4web.utils.form.Form`` is a pretty much equivalent to
web2py’s ``SQLFORM``.

The ``Form`` constructor accepts the following arguments:

.. code:: python

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

Where:

-  ``table``: a DAL table or a list of fields (equivalent to old
   SQLFORM.factory)
-  ``record``: a DAL record or record id
-  ``readonly``: set to True to make a readonly form
-  ``deletable``: set to False to disallow deletion of record
-  ``formstyle``: a function that renders the form using helpers
   (FormStyleDefault)
-  ``dbio``: set to False to prevent any DB writes
-  ``keep_values``: if set to true, it remembers the values of the
   previously submitted form
-  ``form_name``: the optional name of this form
-  ``hidden``: a dictionary of hidden fields that is added to the form
-  ``before_validate``: an optional validator.

Example
-------

Here is a simple example of a custom form not using database access. We
declare an endpoint ``/form_example``, which will be used both for the
GET and for the POST of the form:

.. code:: python

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

The form can be displayed in the template simply using ``[[=form]]``.

Form validation
---------------

The validation of form input can be done in two ways. One can define
``requires`` attributes of ``Field``, or one can define explicitly a
validation function. To do the latter, we pass to ``validate`` a
function that takes the form and returns a dictionary, mapping field
names to errors. If the dictionary is non-empty, the errors will be
displayed to the user, and no database I/O will take place.

Here is an example:

.. code:: python

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

Form Structure Manipulation
---------------------------

Like in web2py, in py4web a form is rendered by helpers. Unlike web2py, it uses yatl helpers. This means the tree structure of a form can be manilupated before the form is serialized in HTML. For example:

.. code:: python

    db.define_table('paint', Field('color'))
    form = Form(db.paint)
    form.structure.find('[name=color]')[0]['_class'] = 'my-class'

Notice that a form does not make an HTML tree until form structure is accessed. Once accessed you can use `.find(...)` to find matching elements. The argument of `find` is a string following the filter syntax of jQuery. In the above case there is a single match `[0]` and we modify the `_class` attribute of that element. Attribute names of HTML elements must be preceded by an underscore.
