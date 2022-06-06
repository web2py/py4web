# Generic grid.

import json
from collections import namedtuple

from yatl.helpers import XML

from py4web import URL, action, request
from py4web.core import Fixture
from py4web.utils.url_signer import URLSigner

Req = namedtuple("Req", ["page", "search_args", "query"])


class Grid(Fixture):
    """This is a prototype class for building paginable grids (tables)
    with content provided server-side."""

    GRID = '<grid url="{url}"></grid>'

    def __init__(
        self,
        path,
        session,
        use_id=False,
        search_placeholder=None,
        signer=None,
        db=None,
        sort_fields=None,
        default_sort=None,
        auth=None,
        page_size=20,
    ):
        """
        Displays a grid.
        :param path: Path where the grid is loaded via AJAX.
        :param session: used by the signer.
        :param signer: singer for URLs.
        :param use_id: does the AJAX call come with an id?
        :param db: specify a db if you need it added as widget.
        :param sort_fields: list of fields that are sortable.  If a
            field is not sortable, use None.  E.g.:
            [db.user.name, None, db.user.email]
        :param default_sort: array that indicates the default sorting order.
        :param auth: specify auth if you need it added as widget.
        """
        assert session is not None, "You must provide a session."
        self.path = path
        self.search_placeholder = search_placeholder
        self.signer = signer or URLSigner(session)
        # Creates an action (an entry point for URL calls),
        # mapped to the api method, that can be used to request pages
        # for the table.
        self.use_id = use_id
        self.__prerequisites__ = [self.signer]
        args = list(filter(None, [session, db, auth, self.signer.verify()]))
        f = action.uses(*args)(self.api)
        p = "/".join([self.path, "<id>"]) if use_id else self.path
        action(p, method=["GET"])(f)
        # Some defaults.  Over-ride them in subclasses.
        self.sort_fields = sort_fields
        self.default_sort = default_sort
        self.page_size = page_size

    def __call__(self, id=None):
        """This method returns the element that can be included in the page."""
        return XML(Grid.GRID.format(url=self.url(id=id)))

    def url(self, id=None):
        return URL(*filter(None, [self.path, id]), signer=self.signer)

    def is_empty(self, id=None):
        """You can use this to decide if the grid should be displayed or not."""
        return False

    def _get_request_params(self, header):
        """Helper that returns relevant portions of the request,
        pre-processed."""
        # Gets the query if any.
        query = request.query.get("q")
        # Computes sort_array and sort_order.
        so = request.query.get("sort_order")
        sort_array = self.default_sort if so is None else json.loads(so)
        sort_order = None
        if self.sort_fields is not None:
            for i, a in enumerate(sort_array):
                if a == 1:
                    sort_order = self.sort_fields[i]
                elif a == -1:
                    sort_order = ~self.sort_fields[i]
        # Computes the kwargs.
        try:
            page = int(request.query.get("page", 1))
        except:
            page = 1
        search_args = {}
        if sort_order is not None:
            search_args["orderby"] = sort_order
        row_range = ((page - 1) * self.page_size, page * self.page_size + 1)
        search_args["limitby"] = row_range
        # Fixes the header.
        if sort_order is not None:
            for hc, so in zip(header["cells"], sort_array):
                hc["sort"] = so
        # Returns the parameters.
        req = Req(query=query, page=page, search_args=search_args)
        return req

    def _has_more(self, rows):
        """Helper for the has_more field."""
        has_more = False
        if len(rows) > self.page_size:
            has_more = True
            result_rows = rows[: self.page_size]
        else:
            result_rows = rows
        return has_more, result_rows

    def api(self, id=None):
        """The API must return the data to fill the table.
        The data is a dictionary, containing:
            - page: <integer>
            - search_placeholder: <string>
            - has_more: <boolean>
            - has_delete: <boolean> ; indicates some row can be deleted.
            - rows: <list of rows (see below)>
        A row is a dictionary, containing:
            - is_header: <boolean>
            - cells: <cells>
        <cells> is a list of dictionaries, containing:
            - raw_html: <content>; takes precedence over other types.
            - text: <text>
            - url: <text> or None
            - is_button: <boolean>; buttonizes the text or URL.
            - sortable: <boolean> (valid only of the row is a header)
            - sort: <int> (+1 for sort up, -1 for sort down, 0 for no sort)
            - el_class: <text> or None (class of element, if needed)
            - delete: set this to a URL that will cause deletion if called
                via GET, if you want the raw to be deletable.
        All the fields except text are optional.
        This is a sample implementation only, to test code.  You should
        over-ride the api method to provide your own input for the table.
        """
        page = int(request.query.get("page", 1))
        query = request.query.get("q", "")
        sort_order = json.loads(request.query.get("sort_order", "[]"))
        print(repr(sort_order))
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
            for hc, so in zip(header["cells"], sort_order):
                hc["sort"] = so
        rows = [
            dict(
                cells=[
                    dict(text="Cat"),
                    dict(text="4"),
                    dict(text="Mammal", url="javascript:alert('mammal/cat')", is_button=True),
                ]
            ),
            dict(
                cells=[
                    dict(text="Dog"),
                    dict(text="4"),
                    dict(text="Mammal", url="javascript:alert('mammal/dog')", is_button=True),
                ],
                has_delete=True,
            ),
            dict(
                cells=[
                    dict(text="Owl"),
                    dict(text="2"),
                    dict(text="Bird", url="javascript:alert('bird/owl')", is_button=True),
                ]
            )
        ]
        if query:
            rows = [row for row in rows if query.lower() in row["cells"][0]["text"].lower()]
        for k, sign in enumerate(sort_order):
            if sign != 0:
                rows.sort(key=lambda row: row["cells"][k]["text"], reverse=(sign<0))
        return dict(
            page=int(page),
            has_search=True,
            has_delete=True,  # TODO: put this in each row.
            search_placeholder=self.search_placeholder,
            has_more=True,
            rows=[header] + rows,
        )
