import mimetypes
import os
import re
import shutil

from pydal.exceptions import NotAuthorizedException, NotFoundException
from pydal.helpers.regex import REGEX_UPLOAD_PATTERN

from py4web import HTTP, request, response
from py4web.core import bottle

# extensions that are safe to display inline in the browser: they cannot run
# scripts in the app origin. Anything else (html, svg, xml, js, pdf, ...) is
# always sent as an attachment, else an uploaded file could be stored XSS.
SAFE_INLINE_EXTENSIONS = {
    "png", "jpg", "jpeg", "gif", "webp", "bmp", "ico", "avif",
    "mp3", "ogg", "oga", "wav", "flac", "m4a",
    "mp4", "webm", "ogv", "mov",
    "txt",
}

# headers added to every download
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "Content-Security-Policy": "default-src 'none'; sandbox",
}


def downloader(
    db, path, filename, download_filename=None, inline_extensions=None
):
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

    Only files whose extension is in inline_extensions (default
    SAFE_INLINE_EXTENSIONS) are displayed inline, all others are downloaded.
    """
    if inline_extensions is None:
        inline_extensions = SAFE_INLINE_EXTENSIONS

    items = re.match(REGEX_UPLOAD_PATTERN, filename)
    if not items:
        raise HTTP(404)
    tablename = items.group("table")
    fieldname = items.group("field")
    try:
        field = db[tablename][fieldname]
        path = field.uploadfolder or path

        # Functionality to handle uploadseparate Field declaration.
        if field.uploadseparate:
            uuidname = items.group("uuidkey")
            path = os.path.join(path, *[f"{tablename}.{fieldname}", uuidname[:2]])

    except (AttributeError, KeyError):
        raise HTTP(404)
    try:
        (original_name, stream) = field.retrieve(filename, path, nameonly=True)
        extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
        inline = extension in inline_extensions
        fullpath = os.path.join(path, filename)
        if not os.path.exists(fullpath) and hasattr(stream, "read"):
            # file stored in the database
            mimetype = mimetypes.guess_type(filename)[0]
            response.headers["Content-Type"] = (
                mimetype if inline and mimetype else "application/octet-stream"
            )
            if not inline or request.query.get("attachment"):
                name = (download_filename or original_name or filename).replace('"', "")
                response.headers["Content-Disposition"] = f'attachment; filename="{name}"'
            response.headers.update(SECURITY_HEADERS)
            return stream.read()
    except NotAuthorizedException:
        raise HTTP(403)
    except NotFoundException:
        raise HTTP(404)
    except IOError:
        raise HTTP(404)
    if inline and not request.query.get("attachment"):
        download_filename = None
    elif not download_filename:
        download_filename = original_name or filename
    res = bottle.static_file(filename, root=path, download=download_filename)
    res.headers.update(SECURITY_HEADERS)
    return res
