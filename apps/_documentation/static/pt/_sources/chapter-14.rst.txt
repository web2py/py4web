====
Grid
====

py4web comes with a Grid object providing simple grid and CRUD
capabilities.

Key Features
------------

-  Click column heads for sorting - click again for DESC
-  Pagination control
-  Built in Search (can use search_queries OR search_form)
-  Action Buttons - with or without text
-  Full CRUD with Delete Confirmation
-  Pre and Post Action (add your own buttons to each row)
-  Grid dates in local format
-  Default formatting by type plus user overrides

Basic Example
-------------

In this simple example we will make a grid over the company table.

controllers.py

.. code:: python

   from functools import reduce
   from py4web.utils.grid import Grid
   from py4web import action
   from .common import db, session, auth

   @action('companies', method=['POST', 'GET'])
   @action('companies/<path:path>', method=['POST', 'GET'])
   @action.uses(session, db, auth, 'grid.html')
   def companies(path=None):
       grid = Grid(path,
                   query=reduce(lambda a, b: (a & b), [db.company.id > 0]),
                   orderby=[db.company.name],
                   search_queries=[['Search by Name', lambda val: db.company.name.contains(val)]])

       return dict(grid=grid)

grid.html

::

   [[extend 'layout.html']]
   [[=grid.render()]]

Signature
---------

.. code:: python

   class Grid:
       def __init__(
           self,
           path,
           query,
           search_form=None,
           search_queries=None,
           fields=None,
           show_id=False,
           orderby=None,
           left=None,
           headings=None,
           create=True,
           details=True,
           editable=True,
           deletable=True,
           pre_action_buttons=None,
           post_action_buttons=None,
           auto_process=True,
           rows_per_page=15,
           include_action_button_text=True,
           search_button_text="Filter",
           formstyle=FormStyleDefault,
           grid_class_style=GridClassStyle,
       ):

-  path: the route of this request
-  query: pydal query to be processed
-  search_form: py4web FORM to be included as the search form. If
   search_form is passed in then the developer is responsible for
   applying the filter to the query passed in. This differs from
   search_queries.
-  search_queries: list of query lists to use to build the search form.
   Ignored if search_form is used. Format is
-  fields: list of fields to display on the list page, if blank, glean
   tablename from first query and use all fields of that table
-  show_id: show the record id field on list page - default = False
-  orderby: pydal orderby field or list of fields
-  left: if joining other tables, specify the pydal left expression here
-  headings: list of headings to be used for list page - if not provided
   use the field label
-  details: URL to redirect to for displaying records - set to True to
   automatically generate the URL - set to False to not display the
   button
-  create: URL to redirect to for creating records - set to True to
   automatically generate the URL - set to False to not display the
   button
-  editable: URL to redirect to for editing records - set to True to
   automatically generate the URL - set to False to not display the
   button
-  deletable: URL to redirect to for deleting records - set to True to
   automatically generate the URL - set to False to not display the
   button
-  pre_action_buttons: list of action_button instances to include before
   the standard action buttons
-  post_action_buttons: list of action_button instances to include after
   the standard action buttons
-  auto_process: Boolean - whether or not the grid should be processed
   immediately. If False, developer must call grid.process() once all
   params are setup
-  rows_per_page: number of rows to display per page. Default 15
-  include_action_button_text: boolean telling the grid whether or not
   you want text on action buttons within your grid
-  search_button_text: text to appear on the submit button on your
   search form
-  formstyle: py4web Form formstyle used to style your form when
   automatically building CRUD forms
-  grid_class_style: GridClassStyle object used to override defaults for
   styling your rendered grid. Allows you to specify classes or styles
   to apply at certain points in the grid.

Searching / Filtering
---------------------

There are two ways to build a search form.

-  Provide a search_queries list
-  Build your own custom search form

If you provide a search_queries list to grid, it will:

-  build a search form. If more than one search query in the list, it
   will also generate a dropdown to select which search field to search
   agains
-  gather filter values and filter the grid

However, if this doesn’t give you enough flexibility you can provide
your own search form and handle all the filtering (building the queries)
by yourself.

CRUD
----

The grid provides CRUD (create, read, update and delete) capabilities
utilizing py4web Form.

You can turn off CRUD features by setting
create/details/editable/deletable during grid instantiation.

Additionally, you can provide a separate URL to the
create/details/editable/deletable parameters to bypass the
auto-generated CRUD pages and handle the detail pages yourself.

Using templates
---------------

Use the following to render your grid or CRUD forms in your templates.

Display the grid or a CRUD Form

::

   [[=grid.render()]]

To allow for customizing CRUD form layout (like with web2py) you can use
the following

::

   [[form = grid.render() ]]
   [[form.custom["begin"] ]]
   ...
   [[form.custom["submit"]
   [[form.custom["end"]

When handling custom form layouts you need to know if you are displaying
the grid or a form. Use the following to decide

::

   [[if 'action' in request.url_args and request.url_args['action'] in ['details', 'edit']:]]
       #  Display the custom form
       [[form = grid.render() ]]
       [[form.custom["begin"] ]]
       ...
       [[form.custom["submit"]
       [[form.custom["end"]
   [[else:]]
       [[grid.render() ]]
   [[pass]]

Customizing Style
-----------------

You can provide your own formstyle or grid classes and style to grid.

-  formstyle is the same as a Form formstyle, used to style the CRUD
   forms.
-  grid_class_style is a class that provides the classes and/or styles
   used for certain portions of the grid.

The default GridClassStyle - based on no.css, primarily uses styles to
modify the layout of the grid

.. code:: python

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
           "grid-th-action-button": "grid-col-action-button",
           "grid-td-action-button": "grid-col-action-button",
           "grid-tr": "",
           "grid-th": "",
           "grid-td": "",
           "grid-details-button": "grid-details-button info",
           "grid-edit-button": "grid-edit-button info",
           "grid-delete-button": "grid-delete-button info",
           "grid-footer": "grid-footer",
           "grid-info": "grid-info",
           "grid-pagination": "grid-pagination",
           "grid-pagination-button": "grid-pagination-button info",
           "grid-pagination-button-current": "grid-pagination-button-current default",
           "grid-cell-type-string": "grid-cell-type-string",
           "grid-cell-type-text": "grid-cell-type-text",
           "grid-cell-type-boolean": "grid-cell-type-boolean",
           "grid-cell-type-float": "grid-cell-type-float",
           "grid-cell-type-int": "grid-cell-type-int",
           "grid-cell-type-date": "grid-cell-type-date",
           "grid-cell-type-time": "grid-cell-type-time",
           "grid-cell-type-datetime": "grid-cell-type-datetime",
           "grid-cell-type-upload": "grid-cell-type-upload",
           "grid-cell-type-list": "grid-cell-type-list",
           # specific for custom form
           "search_form": "search-form",
           "search_form_table": "search-form-table",
           "search_form_tr": "search-form-tr",
           "search_form_td": "search-form-td",
       }

       styles = {
           "grid-wrapper": "",
           "grid-header": "display: table; width: 100%",
           "grid-new-button": "display: table-cell;",
           "grid-search": "display: table-cell; float:right",
           "grid-table-wrapper": "overflow-x: auto; width:100%",
           "grid-table": "",
           "grid-sorter-icon-up": "",
           "grid-sorter-icon-down": "",
           "grid-th-action-button": "",
           "grid-td-action-button": "",
           "grid-tr": "",
           "grid-th": "white-space: nowrap; vertical-align: middle",
           "grid-td": "white-space: nowrap; vertical-align: middle",
           "grid-details-button": "margin-bottom: 0",
           "grid-edit-button": "margin-bottom: 0",
           "grid-delete-button": "margin-bottom: 0",
           "grid-footer": "display: table; width:100%",
           "grid-info": "display: table-cell;",
           "grid-pagination": "display: table-cell; text-align:right",
           "grid-pagination-button": "min-width: 20px",
           "grid-pagination-button-current": "min-width: 20px; pointer-events:none; opacity: 0.7",
           "grid-cell-type-string": "white-space: nowrap; vertical-align: middle; text-align: left; text-overflow: ellipsis; max-width: 200px",
           "grid-cell-type-text": "vertical-align: middle; text-align: left; text-overflow: ellipsis; max-width: 200px",
           "grid-cell-type-boolean": "white-space: nowrap; vertical-align: middle; text-align: center",
           "grid-cell-type-float": "white-space: nowrap; vertical-align: middle; text-align: right",
           "grid-cell-type-int": "white-space: nowrap; vertical-align: middle; text-align: right",
           "grid-cell-type-date": "white-space: nowrap; vertical-align: middle; text-align: right",
           "grid-cell-type-time": "white-space: nowrap; vertical-align: middle; text-align: right",
           "grid-cell-type-datetime": "white-space: nowrap; vertical-align: middle; text-align: right",
           "grid-cell-type-upload": "white-space: nowrap; vertical-align: middle; text-align: center",
           "grid-cell-type-list": "white-space: nowrap; vertical-align: middle; text-align: left",
           # specific for custom form
           "search_form": "",
           "search_form_table": "",
           "search_form_tr": "",
           "search_form_td": "",
       }

       @classmethod
       def get(cls, element):
           """returns a dict with _class and _style for the element name"""
           return {
               "_class": cls.classes.get(element),
               "_style": cls.styles.get(element),
           }

GridClassStyleBulma - bulma implementation

.. code:: python

   class GridClassStyleBulma(GridClassStyle):
       classes = {
           "grid-wrapper": "grid-wrapper field",
           "grid-header": "grid-header pb-2",
           "grid-new-button": "grid-new-button button",
           "grid-search": "grid-search is-pulled-right pb-2",
           "grid-table-wrapper": "grid-table-wrapper table_wrapper",
           "grid-table": "grid-table table is-bordered is-striped is-hoverable is-fullwidth",
           "grid-sorter-icon-up": "grid-sort-icon-up fas fa-sort-up is-pulled-right",
           "grid-sorter-icon-down": "grid-sort-icon-down fas fa-sort-down is-pulled-right",
           "grid-th-action-button": "grid-col-action-button is-narrow",
           "grid-td-action-button": "grid-col-action-button is-narrow",
           "grid-tr": "",
           "grid-th": "",
           "grid-td": "",
           "grid-details-button": "grid-details-button button is-small",
           "grid-edit-button": "grid-edit-button button is-small",
           "grid-delete-button": "grid-delete-button button is-small",
           "grid-footer": "grid-footer",
           "grid-info": "grid-info is-pulled-left",
           "grid-pagination": "grid-pagination is-pulled-right",
           "grid-pagination-button": "grid-pagination-button button is-small",
           "grid-pagination-button-current": "grid-pagination-button-current button is-primary is-small",
           "grid-cell-type-string": "grid-cell-type-string",
           "grid-cell-type-text": "grid-cell-type-text",
           "grid-cell-type-boolean": "grid-cell-type-boolean has-text-centered",
           "grid-cell-type-float": "grid-cell-type-float",
           "grid-cell-type-int": "grid-cell-type-int",
           "grid-cell-type-date": "grid-cell-type-date",
           "grid-cell-type-time": "grid-cell-type-time",
           "grid-cell-type-datetime": "grid-cell-type-datetime",
           "grid-cell-type-upload": "grid-cell-type-upload",
           "grid-cell-type-list": "grid-cell-type-list",
           # specific for custom form
           "search_form": "search-form is-pulled-right pb-2",
           "search_form_table": "search-form-table",
           "search_form_tr": "search-form-tr",
           "search_form_td": "search-form-td pr-1",
       }

       styles = {
           "grid-wrapper": "",
           "grid-header": "",
           "grid-new-button": "",
           "grid-search": "",
           "grid-table-wrapper": "",
           "grid-table": "",
           "grid-sorter-icon-up": "",
           "grid-sorter-icon-down": "",
           "grid-th-action-button": "",
           "grid-td-action-button": "",
           "grid-tr": "",
           "grid-th": "text-align: center; text-transform: uppercase;",
           "grid-td": "",
           "grid-details-button": "",
           "grid-edit-button": "",
           "grid-delete-button": "",
           "grid-footer": "padding-top: .5em;",
           "grid-info": "",
           "grid-pagination": "",
           "grid-pagination-button": "margin-left: .25em;",
           "grid-pagination-button-current": "margin-left: .25em;",
           "grid-cell-type-string": "",
           "grid-cell-type-text": "",
           "grid-cell-type-boolean": "",
           "grid-cell-type-float": "",
           "grid-cell-type-int": "",
           "grid-cell-type-date": "",
           "grid-cell-type-time": "",
           "grid-cell-type-datetime": "",
           "grid-cell-type-upload": "",
           "grid-cell-type-list": "",
           # specific for custom form
           "search_form": "",
           "search_form_table": "",
           "search_form_tr": "",
           "search_form_td": "",
       }

You can build your own class_style to be used with the css framework of
your choice.

Custom Action Buttons
---------------------

As with web2py, you can add additional buttons to each row in your grid.
You do this by providing pre_action_buttons or post_action_buttons to
the Grid **init** method.

-  pre_action_buttons - list of action_button instances to include
   before the standard action buttons
-  post_action_buttons - list of action_button instances to include
   after the standard action buttons

You can build your own Action Button class to pass to pre/post action
buttons based on the template below (this is not provided with py4web)

Sample Action Button Class
--------------------------

.. code:: python

   def __init__(self,
                url,
                text,
                icon="fa-calendar",
                additional_classes=None,
                message=None,
                append_id=False):

-  url: the page to navigate to when the button is clicked
-  text: text to display on the button
-  icon: the font-awesome icon to display before the text
-  additional_classes: a space-separated list of classes to include on
   the button element
-  message: confirmation message to display if ‘confirmation’ class is
   added to additional classes
-  append_id: if True, add id_field_name=id_value to the url querystring
   for the button

Reference Fields
----------------

When displaying fields in a PyDAL table, you sometimes want to display a
more descriptive field than a foreign key value. There are a couple of
ways to handle that with the py4web grid.

filter_out on PyDAL field definition - here is an example of a foreign
key field

.. code:: python

   Field('company', 'reference company',
         requires=IS_NULL_OR(IS_IN_DB(db, 'company.id',
                                      '%(name)s',
                                      zero='..')),
         filter_out=lambda x: x.name if x else ''),

This will display the company name in the grid instead of the company ID

The downfall of using this method is that sorting and filtering are
based on the company field in the employee table and not the name of the
company

left join and specify fields from joined table - specified on the left
parameter of Grid instantiation

.. code:: python

   db.company.on(db.employee.company == db.company.id)

You can specify a standard PyDAL left join, including a list of joins to
consider.

Now the company name field can be included in your fields list can be
clicked on and sorted.

Now you can also specify a query such as:

.. code:: python

   queries.append((db.employee.last_name.contains(search_text)) | (db.employee.first_name.contains(search_text)) | db.company.name.contains(search_text)))

This method allows you to sort and filter, but doesn’t allow you to
combine fields to be displayed together as the filter_out method would

You need to determine which method is best for your use case
understanding the different grids in the same application may need to
behave differently.
