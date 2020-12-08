import json

from py4web import action, URL, request
from yatl.helpers import XML
from py4web.utils.url_signer import URLSigner
from py4web.core import Fixture


class Grid(Fixture):
    """This is a prototype class for building paginable grids (tables)
    with content provided server-side."""

    GRID = '<grid url="{url}"></grid>'

    def __init__(
        self, path, session, search_placeholder=None, signer=None, db=None, auth=None
    ):
        """
        Displays a grid.
        :param path: Path where the grid is loaded via AJAX.
        :param session: used by the signer.
        :param signer: singer for URLs.
        :param db: specify a db if you need it added as widget.
        :param auth: specify auth if you need it added as widget.
        """
        self.path = path
        self.search_placeholder = search_placeholder
        self.signer = signer or URLSigner(session)
        # Creates an action (an entry point for URL calls),
        # mapped to the api method, that can be used to request pages
        # for the table.
        self.__prerequisites__ = [session]
        args = list(filter(None, [session, db, auth, self.signer.verify()]))
        f = action.uses(*args)(self.api)
        action(self.path, method=["GET"])(f)

    def __call__(self):
        """This method returns the element that can be included in the page."""
        return XML(Grid.GRID.format(url=self.url()))

    def url(self):
        return URL(self.path, signer=self.signer)

    def api(self):
        """The API must return the data to fill the table.
        The data is a dictionary, containing:
            - page: <integer>
            - search_placeholder: <string>
            - has_more: <boolean>
            - rows: <list of rows (see below)>
        A row is a dictionary, containing:
            - is_header: <boolean>
            - cells: <cells>
        <cells> is a list of dictionaries, containing:
            - text: <text>
            - url: <text> or None
            - is_button: <boolean>
            - sortable: <boolean> (valid only of the row is a header)
            - sort: <int> (+1 for sort up, -1 for sort down, 0 for no sort)
            - el_class: <text> or None (class of element, if needed)
        All the fields except text are optional.
        This is a sample implementation only, to test code.  You should
        over-ride the api method to provide your own input for the table.
        """
        page = request.query.get("page") or 1
        q = request.query.get("q", "")  # Query string
        sort_order = request.query.get("sort_order") or None
        header = dict(
            is_header=True,
            cells=[
                dict(text="Animal", sortable=True),
                dict(text="N. paws", sortable=True),
                dict(text="Class"),
            ],
        )
        # Copies the sort_order into the header, to reflect that the request has been
        # satisfied.  Note that we are doing server-side sorting, as the set of
        # results can be very large and the web UI may have only a small set of the results.
        # The reason why sort order is repeated in the answer is that the server might
        # want to be able to communicate to the web UI what sort order has truly been
        # used when producing the table.
        if sort_order is not None:
            for hc, so in zip(header["cells"], json.loads(sort_order)):
                hc["sort"] = so
        row1 = dict(
            cells=[
                dict(text="Cat"),
                dict(text="4"),
                dict(text="Mammal", url=URL("mammals/cat"), is_button=True),
            ]
        )
        row2 = dict(
            cells=[
                dict(text="Dog"),
                dict(text="4"),
                dict(text="Mammal", url=URL("mammals/dog"), is_button=True),
            ]
        )
        row3 = dict(
            cells=[
                dict(text="Owl"),
                dict(text="2"),
                dict(text="Bird", url=URL("bird/owl"), is_button=True),
            ]
        )
        return dict(
            page=int(page),
            search_placeholder=self.search_placeholder,
            has_more=True,
            rows=[header, row1, row2, row3],
        )
