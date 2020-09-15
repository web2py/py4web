## Grid

**Warning: the API described in this chapter is new and subject to changes. Make sure you keep your code up to date**

py4web comes with a Grid object providing simple grid and CRUD capabilities.
#### Key Features
- Click column heads for sorting - click again for DESC
- Pagination control
- Filter Form - you supply and control filtering (remember filters between pages)
- Action Buttons - with or without text
- Full CRUD with Delete Confirmation
- Pre and Post Action (add your own buttons to each row)
- Grid dates in local format using moment.js
- Checkboxes in grid for boolean fields

#### Simple Example
In this simple example we will make a grid over the superhero table.  Since there is a foreign key defined we will
take advantage of the DAL `left` keyword to bring in the related values and allow sorting on them.

controllers.py
``
from py4web.utils.grid import Grid, get_storage_key, get_storage_value, GridDefaults, GridClassStyle
from py4web.utils.param import Param
from .settings import SESSION_SECRET_KEY

@action('companies', method=['POST', 'GET'])
@action('companies/<action>/<tablename>/<record_id>', method=['POST', 'GET'])
@action.uses(session, db, auth, 'grid.html')
def companies(**kwargs):
    #  NOTE - this would normally go in common.py and then imported to your controller
    GRID_COMMON = GridDefaults(db=db,
                               secret=SESSION_SECRET_KEY,
                               rows_per_page=5)

    storage_key = get_storage_key()
    search_filter = get_storage_value(storage_key, 'search_filter', common_settings=GRID_COMMON)

    search_form = Form([Field('search_filter',
                              length=50,
                              default=search_filter,
                              _placeholder='...search text...',
                              _title='Enter search text and click on %s' % GRID_COMMON.param.search_button_text)],
                       keep_values=True, formstyle=FormStyleGrid)

    if search_form.accepted:
        search_filter = search_form.vars['search_filter']

    queries = [(db.company.id > 0)]
    if search_filter:
        queries.append(db.company.name.contains(search_filter))

    orderby = [db.company.name]

    grid = Grid(GRID_COMMON,
                queries,
                search_form=search_form,
                storage_values=dict(search_filter=search_filter),
                orderby=orderby,
                create=True,
                details=True,
                editable=True,
                deletable=True,
                storage_key=storage_key)

    return dict(grid=grid)
``:python

grid.html
``
[[extend 'layout.html']]
<div class="container" style="padding-top: 1em;">
    [[if 'action' in request.url_args and request.url_args['action'] in ['details', 'edit']:]]
        [[form = grid.render()]]
        [[=form]]
    [[else:]]
        [[=grid.render()]]
    [[pass]]
</div>
``

#### Signature

``
class Grid:
    def __init__(self,
                 common_settings,
                 queries,
                 search_form=None,
                 storage_values=None,
                 fields=None,
                 show_id=False,
                 orderby=None,
                 left=None,
                 headings=None,
                 create=False,
                 details=False,
                 editable=False,
                 deletable=False,
                 requires=None,
                 storage_key=None,
                 pre_action_buttons=None,
                 post_action_buttons=None):
``:python

- common_settings: Params object with common settings for all grids within the application
- queries: list of queries used to filter the data
- search_form: py4web FORM to be included as the search form
- storage_values: values to save between requests
- fields: list of fields to display on the list page, if blank, glean tablename from first query and use all fields of that table
- show_id: show the record id field on list page - default = False
- orderby: pydal orderby field or list of fields
- left: if joining other tables, specify the pydal left expression here
- headings: list of headings to be used for list page - if not provided use the field label
- create: URL to redirect to for creating records - set to False to not display the button
- editable: URL to redirect to for editing records - set to False to not display the button
- deletable: URL to redirect to for deleting records - set to False to not display the button
- requires: dict of fields and their 'requires' parm for building edit pages - dict key should be tablename.fieldname
- storage_key: id of the cookie containing saved values
- pre_action_buttons: list of action_button instances to include before the standard action buttons
- post_action_buttons: list of action_button instances to include after the standard action buttons

#### Grid Defaults

``
    def __init__(self,
                 db,
                 secret,
                 token_longevity=3600,
                 rows_per_page=15,
                 include_action_button_text=True,
                 search_button_text="Filter",
                 formstyle=FormStyleDefault,
                 grid_class_style=GridClassStyle):
``:python

The GridDefaults class allows you to set app-wide grid defaults that you can use when instantiating grids.0

- db: PyDAL db instance to use within your grid
- secret: secrent encryption key used to encrypt storage values
- token_longevity: number of seconds to remember you storage values for this grid instance
- rows_per_page: number of rows to display on each grid page
- included_action_button_text: boolean telling the grid whether or not you want text on action buttons within your grid
- search_button_text: text to appear on the submit button on your search form
- formstyle: py4web Form formstyle used to style your form when automatically building CRUD forms
- grid_class_style: GridClassStyle object used to override defaults for styling your rendered grid.  Allows you to specify classes or styles to apply at certain points in the grid.

#### Searching / Filtering

You can pass a py4web Form to the grid to be used as a search form.  You are responsible for taking the values from the search form and building the queries to pass to the Grid __init__ method.

The grid provides helper functions that allow you save/retrieve filter values between page displays.

- set_storage_values
- get_storage_value

#### CRUD

The grid provide CRUD (create, read, update and delete) capabilities utilizing py4web Form.  This is disabled on the grid by default.

You can enable CRUD features by setting create/details/editable/deletable to True at instantiation.

Additionally, you can provide a separate URL to the create/details/editable/deletable parameters to bypass the auto-generated CRUD pages and handle the detail pages yourself.

#### Templates

Use the following to render your grid or CRUD forms in your templates.

Display the grid or a CRUD Form
``
[[=grid.render()]]
``

To allow for customizing CRUD form layout (like with web2py) you can use the following
``
[[form = grid.render() ]]
[[form.custom["begin"] ]]
...
[[form.custom["submit"]
[[form.custom["end"]
``

When handling custom form layouts you need to know if you're displaying the grid or a form.  Use the following to decide
``
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
``

#### Customizing Style

You can provide your own formstyle or grid classes and style to grid.

- formstyle is the same as a Form formstyle, used to style the CRUD forms.
- grid_class_style is a class that provides the classes and/or styles used for certain portions of the grid.

The default GridClassStyle - based on no.css, primarily uses styles to modify the layout of the grid
``
def GridClassStyle(element_name):
    classes = {"wrapper": "",
               "top_div": "",
               "search_form": "",
               "search_form_table": "",
               "search_form_tr": "",
               "search_form_td": "",
               "table": "",
               "thead": "",
               "th": "",
               "sorter_icon": "",
               "action_column_header": "",
               "tbody": "",
               "tr": "",
               "td": "",
               "td_date": "",
               "td_boolean": "",
               "action_column_cell": "",
               "action_button": "",
               "table_footer": "",
               "row_count": "",
               "pager": "",
               "active_page_button": "",
               "inactive_page_button": ""}

    styles = {"wrapper": "",
              "top_div": "border-bottom: 0;",
              "search_form": "float: right; border-bottom: 0; padding-bottom: 0; margin-bottom: 0;",
              "search_form_table": "margin-bottom: 0;",
              "search_form_tr": "border-bottom: 0; padding-bottom: 0;",
              "search_form_td": "border-bottom: 0; padding-bottom: 0;",
              "table": "",
              "thead": "",
              "th": "text-align: center;",
              "sorter_icon": "float: right;",
              "action_column_header": "text-align: center; width: 1px; white-space: nowrap;",
              "tbody": "",
              "tr": "",
              "td": "vertical-align: middle;",
              "td_date": "",
              "td_boolean": "",
              "action_column_cell": "text-align: center; width: 1px; white-space: nowrap; vertical-align: middle;",
              "action_button": ("border: thin solid lightgray; "
                                "color: black; "
                                "cursor: pointer; "
                                "display: inline-block; "
                                "font-size: .75rem;"
                                "min-width: 75px; "
                                "padding-right: 1rem; "
                                "padding-left: 1rem; "
                                "text-align: center; "
                                "text-decoration: none; "
                                "vertical-align: middle; "
                                "white-space: nowrap;"),
              "table_footer": "line-height: 1.8rem; padding-bottom: 20px;",
              "row_count": "float: left; line-height: 1.8rem;",
              "pager": "float: right; line-height: 1.8rem;",
              "active_page_button": "background-color: #0074d9; "
                                    "border: thin solid #0074d9; "
                                    "color: white; "
                                    "cursor: pointer; "
                                    "display: inline-block; "
                                    "font-size: .75rem;"
                                    "padding-right: .75rem; "
                                    "padding-left: .75rem; "
                                    "margin-right: .25rem; "
                                    "text-align: center; "
                                    "text-decoration: none; "
                                    "vertical-align: middle; "
                                    "white-space: nowrap;",
              "inactive_page_button": "background-color: white; "
                                      "border: thin solid #0074d9; "
                                      "color: #0074d9; "
                                      "cursor: pointer; "
                                      "display: inline-block; "
                                      "font-size: .75rem;"
                                      "padding-right: .75rem; "
                                      "padding-left: .75rem; "
                                      "margin-right: .25rem; "
                                      "text-align: center; "
                                      "text-decoration: none; "
                                      "vertical-align: middle; "
                                      "white-space: nowrap;"}

    classes_styles = {}
    if classes.get(element_name) and classes.get(element_name) != "":
        classes_styles["_class"] = classes.get(element_name)

    if styles.get(element_name) and styles.get(element_name) != "":
        classes_styles["_style"] = styles.get(element_name)

    return classes_styles
``
GridClassStyleBulma - bulma implementation
``
def GridClassStyleBulma(element_name):
    classes = {"wrapper": "field",
               "top_div": "pb-2",
               "search_form": "is-pulled-right pb-2",
               "search_form_table": "",
               "search_form_tr": "",
               "search_form_td": "pr-1",
               "table": "table is-bordered is-striped is-hoverable is-fullwidth",
               "thead": "",
               "th": "",
               "sorter_icon": "",
               "action_column_header": "has-text-centered is-narrow",
               "tbody": "",
               "tr": "",
               "td": "",
               "td_date": "has-text-centered",
               "td_boolean": "has-text-centered",
               "action_column_cell": "has-text-centered is-narrow",
               "action_button": "button is-small",
               "table_footer": "",
               "row_count": "is-pulled-left",
               "pager": "is-pulled-right",
               "active_page_button": "button is-primary is-small",
               "inactive_page_button": "button is-small"}

    styles = {"wrapper": "",
              "top_div": "",
              "search_form": "",
              "search_form_table": "",
              "search_form_tr": "",
              "search_form_td": "",
              "table": "",
              "thead": "",
              "th": "",
              "sorter_icon": "",
              "action_column_header": "",
              "tbody": "",
              "tr": "",
              "td": "",
              "td_date": "",
              "td_boolean": "",
              "action_column_cell": "",
              "action_button": "",
              "table_footer": "",
              "row_count": "",
              "pager": "",
              "active_page_button": "",
              "inactive_page_button": ""}

    classes_styles = {}
    if classes.get(element_name) and classes.get(element_name) != "":
        classes_styles["_class"] = classes.get(element_name)

    if styles.get(element_name) and styles.get(element_name) != "":
        classes_styles["_style"] = styles.get(element_name)

    return classes_styles
``

#### Custom Action Buttons

As with web2py, you can add additional buttons to each row in your grid.  You do this by providing pre_action_buttons or post_action_buttons to the Grid __init__ method.

- pre_action_buttons - list of action_button instances to include before the standard action buttons
- post_action_buttons - list of action_button instances to include after the standard action buttons

#### Action Button Signature

``
def __init__(self,
             url,
             text,
             icon="fa-calendar",
             additional_classes=None,
             message=None,
             append_id=False,
             append_storage_key=False,
             append_page=False):
``
- url: the page to navigate to when the button is clicked
- text: text to display on the button
- icon: the font-awesome icon to display before the text
- additional_classes: a space-separated list of classes to include on the button element
- message: confirmation message to display if 'confirmation' class is added to additional classes
- append_id: if True, add id_field_name=id_value to the url querystring for the button
- append_storage_key: if True, append the storage key for the grid to the url for the button
- append_page: if True, append page=`page_number` to the url querystring

Grid uses ActionButtons internally to generate the row buttons in the grid.  You can provide your own by specifying a list of ActionButtons in the pre_action_buttons and/or post_action_buttons parameter on the Grid __init__ method.

#### Reference Fields

When displaying fields in a PyDAL table, you sometimes want to display a more descriptive field than a foreign key value.  There are a couple of ways to handle that with the py4web grid.

filter_out on PyDAL field definition - here is an example of a foreign key field
``
Field('company', 'reference company',
      requires=IS_NULL_OR(IS_IN_DB(db, 'company.id',
                                   '%(name)s',
                                   zero='..')),
      filter_out=lambda x: x.name if x else ''),
``
This will display the company name in the grid instead of the company ID

The downfall of using this method is that sorting and filtering are based on the company field in the employee table and not the name of the company

left join and specify fields from joined table - specified on the left parameter of Grid instantiation
``
db.company.on(db.employee.company == db.company.id)
``

You can specify a standard PyDAL left join, including a list of joins to consider.

Now the company name field can be included in your fields list can be clicked on and sorted.

Now you can also specify a query such as:
``
queries.append((db.employee.last_name.contains(search_text)) | (db.employee.first_name.contains(search_text)) | db.company.name.contains(search_text)))
``

This method allows you to sort and filter, but doesn't allow you to combine fields to be displayed together as the filter_out method would

You need to determine which method is best for your use case understanding the different grids in the same application may need to behave differently.
