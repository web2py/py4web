from py4web import action, Field
from py4web.utils.grid import Grid
from py4web.core import DAL
from .common import session

# Import TailwindCSS for Grid and Form
from py4web.utils.form import FormStyleTailwind
from py4web.utils.grid import GridClassStyleTailwind

# Define a persistent SQLite database
db = DAL("sqlite://storage_tailwindcss.sqlite")


# Define the products table
def define_tables():
    # Only define if it doesn't exist
    if not hasattr(db, "products"):
        db.define_table(
            "products",
            Field("name", "string"),
            Field("category", "string"),
            Field("price", "float"),
            migrate=True,
        )
    return db.products


# Initialize the products table
products = define_tables()


def initialize_data():
    if db(db.products).select().first() is None:  # Check if table is empty
        db.products.bulk_insert(
            [
                {"name": "Laptop", "category": "Electronics", "price": 999.99},
                {"name": "Desk Chair", "category": "Furniture", "price": 149.99},
                {"name": "Coffee Maker", "category": "Appliances", "price": 79.99},
            ]
        )
        db.commit()


# Initialize data after table creation
initialize_data()


@action("page_with_tailwindcss", method=["POST", "GET"])
@action("page_with_tailwindcss/<path:path>", method=["POST", "GET", "DELETE"])
@action.uses("examples/page_with_tailwindcss.html", session, db)
def page_with_tailwindcss(path=None):
    """Creates a simple Grid with TailwindCSS."""
    p = db.products
    grid = Grid(
        path,
        query=(p.id > 0),
        columns=[p.name, p.category, p.price],
        headings=["Name", "Category", "Price"],
        search_queries=[
            ("Search by Name", lambda val: p.name.contains(val)),
            ("Search by Category", lambda val: p.category.contains(val)),
        ],
        orderby=[p.name],
        formstyle=FormStyleTailwind,
        grid_class_style=GridClassStyleTailwind,
    )
    return dict(grid=grid)


if False:
    # How FormStyleTailwind and GridClassStyleTailwind are defined in py4web/utils/form.py and py4web/utils/grid.py
    from py4web.utils.grid import GridClassStyle
    from py4web.utils.form import FormStyleFactory

    FormStyleTailwind = FormStyleFactory()
    FormStyleTailwind.classes.update(
        {
            "outer": "mb-4",
            "inner": "w-full flex flex-col space-y-1",
            "label": "block text-gray-700 font-medium",
            "info": "text-gray-500 text-sm",
            "error": "text-red-600 text-sm mt-1",
            "submit": "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition",
            "input": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "input[type=text]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "input[type=date]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "input[type=time]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "input[type=datetime-local]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "input[type=radio]": "form-radio h-5 w-5 text-blue-600",
            "input[type=checkbox]": "form-checkbox h-5 w-5 text-blue-600",
            "input[type=submit]": "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition",
            "input[type=password]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "input[type=file]": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm",
            "select": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "textarea": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
        }
    )

    FormStyleTailwind.class_inner_exceptions = {"select": "w-full"}

    class GridClassStyleTailwind(GridClassStyle):
        classes = {
            "grid-wrapper": "grid-wrapper space-y-4 bg-white shadow-md rounded-lg p-4",
            "grid-header": "grid-header flex justify-between items-center pb-4 border-b border-gray-300",
            "grid-new-button": "grid-new-button px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600",
            "grid-search": "grid-search flex items-center gap-2",
            "grid-table-wrapper": "grid-table-wrapper overflow-x-auto",
            "grid-table": "grid-table w-full border-collapse bg-white shadow-md rounded-lg overflow-hidden",
            "grid-sorter-icon-up": "grid-sort-icon-up fas fa-sort-up text-gray-600",
            "grid-sorter-icon-down": "grid-sort-icon-down fas fa-sort-down text-gray-600",
            "grid-thead": "bg-gray-200 text-gray-700",
            "grid-tr": "border-b border-gray-300",
            "grid-th": "px-4 py-2 text-left font-semibold",
            "grid-td": "px-4 py-2 text-gray-700",
            "grid-td-buttons": "px-4 py-2 flex gap-2",
            "grid-button": "px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 shadow",
            "grid-details-button": "px-3 py-1 bg-gray-500 text-white rounded hover:bg-gray-600 shadow",
            "grid-edit-button": "px-3 py-1 bg-yellow-500 text-white rounded hover:bg-yellow-600 shadow",
            "grid-delete-button": "px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600 shadow",
            "grid-search-button": "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition",
            "grid-clear-button": "px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600 transition",
            "grid-footer": "grid-footer flex justify-between items-center pt-4 border-t border-gray-300",
            "grid-info": "grid-info text-gray-600",
            "grid-pagination": "grid-pagination flex gap-2",
            "grid-pagination-button": "px-3 py-1 bg-gray-200 rounded hover:bg-gray-300",
            "grid-pagination-button-current": "px-3 py-1 bg-blue-500 text-white rounded",
            # Cell styling
            "grid-cell-type-string": "text-left",
            "grid-cell-type-text": "text-left",
            "grid-cell-type-boolean": "text-center",
            "grid-cell-type-float": "text-right",
            "grid-cell-type-decimal": "text-right",
            "grid-cell-type-int": "text-right",
            "grid-cell-type-date": "text-center",
            "grid-cell-type-time": "text-center",
            "grid-cell-type-datetime": "text-center",
            "grid-cell-type-upload": "text-center",
            "grid-cell-type-list": "text-left",
            "grid-cell-type-id": "text-center",
            # Search form
            "grid-search-form": "flex flex-wrap gap-2 items-center border p-2 rounded-lg bg-gray-100",
            "grid-search-form-table": "w-full",
            "grid-search-form-tr": "border-b border-gray-300",
            "grid-search-form-td": "p-2",
            "grid-search-form-input": "px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 w-full",
            "grid-search-form-select": "px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 w-full",
            "grid-search-boolean": "form-checkbox h-5 w-5 text-blue-600",
            "grid-header-element": "px-3 py-1 bg-gray-500 text-white rounded hover:bg-gray-600",
            "grid-footer-element": "px-3 py-1 bg-gray-500 text-white rounded hover:bg-gray-600",
        }
