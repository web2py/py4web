from yatl.helpers import XML

from py4web import URL, action, request
from py4web.core import Fixture
from py4web.utils.url_signer import URLSigner


class FileUpload(Fixture):
    FILE_UPLOAD = '<fileupload url="{url}"></fileupload>'

    def __init__(self, path, session, signer=None, db=None, auth=None):
        self.path = path
        self.signer = signer or URLSigner(session)
        # Creates an action (an entry point for URL calls),
        # mapped to the api method, that can be used to request pages
        # for the table.
        self.__prerequisites__ = [self.signer]
        args = list(filter(None, [session, db, auth, self.signer.verify()]))
        f = action.uses(*args)(self.api)
        action(self.path + "/<id>", method=["POST"])(f)

    def __call__(self, id=None):
        """This method returns the element that can be included in the page.
        @param id: id of the file uploaded.  This can be useful if there are
        multiple instances of this form on the page."""
        return XML(FileUpload.FILE_UPLOAD.format(url=self.url(id=id)))

    def url(self, id=None):
        return URL(self.path, id, signer=self.signer)

    def api(self, id=None):
        """This API receives the file upload and does something with it.
        @param id: id of the file uploaded.  This can be useful if the uploader
        is used in multiple places in the page.
        """
        f = request.files.get("file")
        if f is None:
            print("No file")
        else:
            print("Received file:", f.filename)
            print("Content:", f.file.read())
