from py4web import action

from .common import session
from .components.fileupload import FileUpload

file_uploader = FileUpload("upload_api", session)


@action("vue_file_uploader", method=["GET"])
@action.uses("vue/file_uploader.html", file_uploader)
def vue_file_uploader():
    return dict(uploader=file_uploader(id=1))
