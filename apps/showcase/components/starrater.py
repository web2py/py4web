from yatl.helpers import XML

from py4web import URL, action, request
from py4web.core import Fixture
from py4web.utils.url_signer import URLSigner


class StarRater(Fixture):

    STARRATER = '<starrater url="{url}"></starrater>'

    def __init__(self, path, session, signer=None, db=None, auth=None):
        """
        :param path: path at which the star rating does the AJAX calls
        :param session: session, used to validate access and sign.
        :param signer: A URL signer, or else one is created.
        :param db: Used in case db should be one of the widgets.
        :param auth: Used in case auth should be one of the widgets.
        """
        self.path = path
        self.signer = signer or URLSigner(session)
        # Creates an action (an entry point for URL calls),
        # mapped to the api method, that can be used to request pages
        # for the table.
        self.__prerequisites__ = [self.signer]
        args = list(filter(None, [session, db, auth, self.signer.verify()]))
        f = action.uses(*args)(self.get_stars)
        action(self.path + "/<id>", method=["GET"])(f)
        f = action.uses(*args)(self.set_stars)
        action(self.path + "/<id>", method=["POST"])(f)

    def __call__(self, id=None):
        """This method returns the element that can be included in the page.
        @param id: id of the file uploaded.  This can be useful if there are
        multiple instances of this form on the page."""
        return XML(StarRater.STARRATER.format(url=self.url(id=id)))

    def url(self, id=None):
        return URL(self.path, id, signer=self.signer)

    def get_stars(self, id=None):
        """Gets the number of stars for a given id."""
        # This is a test implementation; it should be over-ridden.
        # 0 means no stars set.
        return dict(num_stars=0)

    def set_stars(self, id=None):
        """Sets the number of stars."""
        # This is a test implementation that should be over-ridden.
        print("Number of stars set to:", id, int(request.json["num_stars"]))
        return "ok"
