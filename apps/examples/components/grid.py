from py4web import action, URL, request
from yatl.helpers import XML
from py4web.utils.url_signer import URLSigner
from py4web.core import Fixture

class Grid(Fixture):
    """This is a prototype class for building paginable grids (tables)
    with content provided server-side."""

    GRID = '<grid url="{url}"></grid>'

    def __init__(self, path, session, signer=None, db=None, auth=None):
        """
        Displays a grid.
        :param path: Path where the grid is loaded via AJAX.
        :param session: used by the signer.
        :param signer: singer for URLs.
        :param db: specify a db if you need it added as widget.
        :param auth: specify auth if you need it added as widget.
        """
        self.path = path
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
            - has_more: <boolean>
            - rows: <list of rows (see below)>
        A row is a dictionary, containing:
            - is_header: <boolean>
            - cells: <cells>
        <cells> is a list of dictionaries, containing:
            - text: <text>
            - url: <text> or None
            - is_button: <boolean>
            - el_class: <text> or None (class of element, if needed)
        All the fields except text are optional.
        This is a sample implementation only, to test code.  You should
        over-ride the api method to provide your own input for the table.
        """
        page = request.query.get('page') or 1
        row0 = dict(
            is_header=True,
            cells=[dict(text="Animal"), dict(text="N. paws"), dict(text="Class")])
        row1 = dict(cells=[
            dict(text="Cat"), dict(text="4"),
            dict(text="Mammal", url=URL('mammals/cat'), is_button=True)])
        row2 = dict(cells=[
            dict(text="Dog"), dict(text="4"),
            dict(text="Mammal", url=URL('mammals/dog'), is_button=True)])
        row3 = dict(cells=[
            dict(text="Owl"), dict(text="2"),
            dict(text="Bird", url=URL('bird/owl'), is_button=True)])
        return dict(
            page=int(page),
            has_more=True,
            rows = [row0, row1, row2, row3]
        )
