# -*- coding: utf-8 -*-

"""
| This file is part of the py4web Web Framework
| Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
| License: "BSDv3" (https://opensource.org/licenses/BSD-3-Clause)

File operations
---------------
"""

import os
import re
import tarfile
import glob
import shutil
import logging
import gzip

from py4web.utils.grid import GridClassStyle


__all__ = (
    "safe_join",
    "list_dir",
    "recursive_unlink",
    "sanitize",
    "tar",
    "untar",
    "pack",
    "unpack",
    "create_app",
    "GridClassStyleFuture"
)


def safe_join(folder, path):
    fullpath = os.path.abspath(os.path.join(folder, path))
    if not fullpath.startswith(os.path.abspath(folder) + os.sep):
        return None
    return fullpath


def list_dir(
    path,
    expression="^.+$",
    drop_prefix=True,
    add_dirs=False,
    sort=True,
    maxnum=None,
    exclude=None,
):
    """
    Like `os.listdir()` but you can specify a regex pattern to filter files.
    If `add_dirs` is True, the returned items will have the full path.
    """
    exclude = exclude or []
    if path[-1:] != os.path.sep:
        path = path + os.path.sep
    if drop_prefix:
        n = len(path)
    else:
        n = 0
    regex = re.compile(expression)
    items = []
    for (root, dirs, files) in os.walk(path, topdown=True):
        for dir in dirs[:]:
            if dir.startswith("."):
                dirs.remove(dir)
        if add_dirs:
            items.append(root[n:])
        for file in sorted(files):
            if regex.match(file) and not file.startswith("."):
                if root not in exclude:
                    items.append(os.path.join(root, file)[n:])
            if maxnum and len(items) >= maxnum:
                break
    if sort:
        return sorted(items)
    else:
        return items


def recursive_unlink(path):
    """Deletes `f`. If it's a folder, also its contents will be deleted
    """
    if os.path.isdir(path):
        for s in os.listdir(path):
            recursive_unlink(os.path.join(path, s))
        os.rmdir(path)
    elif os.path.isfile(path):
        os.unlink(path)


def sanitize(name):
    """Turns any expression/path into a valid filename. replaces / with _ and
    removes special characters.
    """
    return re.sub(r"\W", "", re.sub("[/.-]+", "_", name))


def _extractall(filename, path=".", members=None):
    tar = tarfile.TarFile(filename, "r")
    tar.extractall(path, members)
    tar.close()


def tar(file, dir, expression="^.+$", filenames=None, exclude=None):
    """Tars dir into file, only tars file that match expression
    """
    tar = tarfile.TarFile(file, "w")
    try:
        if filenames is None:
            filenames = list_dir(
                dir, expression, add_dirs=True, exclude=exclude)
        for file in filenames:
            tar.add(os.path.join(dir, file), file, False)
    finally:
        tar.close()


def untar(file, dir):
    """Untar file into dir
    """
    _extractall(file, dir)


def pack(filename, path, filenames=None, exclude=None):
    """Packs a py4web application.

    Args:
        filename(str): path to the resulting archive
        path(str): path to the application
        filenames(list): adds filenames to the archive
    """
    exclude = exclude or []
    tarname = filename + ".tar"
    tar(tarname, path, r"^[\w.-]+$", filenames=filenames, exclude=exclude)
    with open(tarname, "rb") as tarfp, gzip.open(filename, "wb") as gzfp:
        shutil.copyfileobj(tarfp, gzfp, 4194304)  # 4 MB buffer
    os.unlink(tarname)


def unpack(filename, path, delete_tar=True):
    tarname = None
    if filename.endswith(".w3p"):
        tarname = filename[:-4] + ".tar"
    if tarname is not None:
        with gzip.open(filename, "rb") as gzfp, open(tarname, "wb") as tarfp:
            shutil.copyfileobj(gzfp, tarfp, 4194304)  # 4 MB buffer
    else:
        tarname = filename
    untar(tarname, path)
    if delete_tar:
        os.unlink(tarname)


def create_app(path, model="scaffold.w3p"):
    unpack(model, path)


class GridClassStyleFuture(GridClassStyle):
    """The Grid style for Bulma"""

    classes = {
        "grid-wrapper": "grid-wrapper",
        "grid-header": "grid-header",
        "grid-new-button": "grid-new-button btn",
        "grid-search": "grid-search",
        "grid-table-wrapper": "grid-table-wrapper",
        "grid-table": "grid-table",
        "grid-sorter-icon-up": "grid-sort-icon-up fas fa-sort-up",
        "grid-sorter-icon-down": "grid-sort-icon-down fas fa-sort-down",
        "grid-thead": "",
        "grid-tr": "",
        "grid-th": "",
        "grid-td": "",
        "grid-td-buttons": "",
        "grid-button": "btn",
        "grid-details-button": "grid-details-button btn",
        "grid-edit-button": "grid-edit-button btn",
        "grid-delete-button": "grid-delete-button btn",
        "grid-search-button": "grid-search-button btn",
        "grid-clear-button": "grid-clear-button btn",
        "grid-footer": "grid-footer",
        "grid-info": "grid-info",
        "grid-pagination": "grid-pagination",
        "grid-pagination-button": "grid-pagination-button btn",
        "grid-pagination-button-current": "grid-pagination-button-current default",
        "grid-cell-type-string": "grid-cell-type-string",
        "grid-cell-type-text": "grid-cell-type-text",
        "grid-cell-type-boolean": "grid-cell-type-boolean",
        "grid-cell-type-float": "grid-cell-type-float",
        "grid-cell-type-decimal": "grid-cell-type-decimal",
        "grid-cell-type-int": "grid-cell-type-int",
        "grid-cell-type-date": "grid-cell-type-date",
        "grid-cell-type-time": "grid-cell-type-time",
        "grid-cell-type-datetime": "grid-cell-type-datetime",
        "grid-cell-type-upload": "grid-cell-type-upload",
        "grid-cell-type-list": "grid-cell-type-list",
        "grid-cell-type-id": "grid-cell-type-id",
        # specific for custom form
        "grid-search-form": "grid-search-form",
        "grid-search-form-table": "grid-search-form-table",
        "grid-search-form-tr": "grid-search-form-tr",
        "grid-search-form-td": "grid-search-form-td",
        "grid-search-boolean": "grid-search-boolean",
    }

    styles = {
        "grid-wrapper": "",
        "grid-header": "display: table; width: 100%;",
        "grid-new-button": "margin-top:4px; height:34px; line-height:34px;",
        "grid-search": "display: table-cell; float:right;",
        "grid-table-wrapper": "overflow-x: auto; width:100%;",
        "grid-table": "",
        "grid-sorter-icon-up": "",
        "grid-sorter-icon-down": "",
        "grid-thead": "",
        "grid-tr": "",
        "grid-th": "white-space: nowrap; vertical-align: middle;",
        "grid-td": "white-space: nowrap; vertical-align: middle;",
        "grid-td-buttons": "",
        "grid-button": "margin-bottom: 0;",
        "grid-details-button": "margin-bottom: 0;",
        "grid-edit-button": "margin-bottom: 0;",
        "grid-delete-button": "margin-bottom: 0;",
        "grid-search-button": "height: 34px;",
        "grid-clear-button": "height: 34px;",
        "grid-footer": "display: table; width:100%;",
        "grid-info": "display: table-cell;",
        "grid-pagination": "display: table-cell; text-align:right;",
        "grid-pagination-button": "min-width: 20px;",
        "grid-pagination-button-current": "min-width: 20px; pointer-events:none; opacity: 0.7;",
        "grid-cell-type-string": "white-space: nowrap; vertical-align: middle; text-align: left; text-overflow: ellipsis; max-width: 200px;",
        "grid-cell-type-text": "vertical-align: middle; text-align: left; text-overflow: ellipsis; max-width: 200px;",
        "grid-cell-type-boolean": "white-space: nowrap; vertical-align: middle; text-align: center;",
        "grid-cell-type-float": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-decimal": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-int": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-date": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-time": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-datetime": "white-space: nowrap; vertical-align: middle; text-align: right;",
        "grid-cell-type-upload": "white-space: nowrap; vertical-align: middle; text-align: center;",
        "grid-cell-type-list": "white-space: nowrap; vertical-align: middle; text-align: left;",
        "grid-cell-type-int": "white-space: nowrap; vertical-align: middle; text-align: right;",
        # specific for custom form
        "grid-search-form": "",
        "grid-search-form-table": "",
        "grid-search-form-tr": "border-bottom: none;",
        "grid-search-form-td": "",
        "grid-search-boolean": "",
    }
