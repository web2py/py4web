import os
import re
import shutil
import urllib
from bottle import static_file
from py4web import request, HTTP
from pydal.exceptions import NotAuthorizedException, NotFoundException
from pydal.helpers.regex import REGEX_UPLOAD_PATTERN


def downloader(db, path, filename, download_filename=None):

    """
    Given a db, and filesystem path, and the filename of an uploaded file,
    it retrieves the file, checks permission, and returns or stream its.
    Optionally as an attachment if the URL contains attachment=true
    If the file is not in the filesystem, it gets copied into the path folder
    before being returned for speed.

    To be used as follows:

    @action('download/<filename>')
    @action.uses(db)
    def download(filename):
        return downloader(db, PATH, filename)

    PATH is the fullpath to where uploaded files are normally stored.
    """

    items = re.match(REGEX_UPLOAD_PATTERN, filename)
    if not items:
        raise HTTP(404)
    tablename = items.group("table")
    fieldname = items.group("field")
    try:
        field = db[tablename][fieldname]

        # Functionality to handle uploadseparate Field declaration.
        if field.uploadseparate:
            uuidname = items.group("uuidkey")
            path = os.path.join(path, *[f"{tablename}.{fieldname}", uuidname[:2]])

    except (AttributeError, KeyError):
        raise HTTP(404)
    try:
        (original_name, stream) = field.retrieve(filename, path, nameonly=True)
        fullpath = os.path.join(path, filename)
        if not os.path.exists(fullpath) and hasattr(stream, "read"):
            with open(fullpath, "wb") as fp:
                shutil.copyfile(fp, stream)
    except NotAuthorizedException:
        raise HTTP(403)
    except NotFoundException:
        raise HTTP(404)
    except IOError:
        raise HTTP(404)
    if not request.query.get("attachment"):
        download_filename = None
    elif not download_filename:
        download_filename = original_name
    return static_file(filename, root=path, download=download_filename)
