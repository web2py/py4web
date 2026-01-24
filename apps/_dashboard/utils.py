# -*- coding: utf-8 -*-

"""
| This file is part of the py4web Web Framework
| Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
| License: "BSDv3" (https://opensource.org/licenses/BSD-3-Clause)

File operations
---------------
"""

import glob
import gzip
import logging
import os
import re
import shutil
import subprocess
import tarfile
import datetime

from py4web import URL
from yatl.helpers import A

__all__ = (
    "safe_join",
    "list_dir",
    "recursive_unlink",
    "tar",
    "untar",
    "pack",
    "unpack",
    "create_app",
    "make_safe",
    "run",
    "get_commits",
    "get_branches",
    "is_git_repo",
    "make_admin_reference_represent",
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
    for root, dirs, files in os.walk(path, topdown=True):
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
    """Deletes `f`. If it's a folder, also its contents will be deleted"""
    if os.path.isdir(path):
        for s in os.listdir(path):
            recursive_unlink(os.path.join(path, s))
        os.rmdir(path)
    elif os.path.isfile(path):
        os.unlink(path)


def _extractall(filename, path=".", members=None):
    tar = tarfile.TarFile(filename, "r")
    tar.extractall(path, members)
    tar.close()


def tar(file, dir, expression="^.+$", filenames=None, exclude=None):
    """Tars dir into file, only tars file that match expression"""
    tar = tarfile.TarFile(file, "w")
    try:
        if filenames is None:
            filenames = list_dir(dir, expression, add_dirs=True, exclude=exclude)
        for file in filenames:
            tar.add(os.path.join(dir, file), file, False)
    finally:
        tar.close()


def untar(file, dir):
    """Untar file into dir"""
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


def make_safe(db):
    def make_safe_field(func):
        def wrapper():
            try:
                return func()
            except Exception as exp:
                print(exp)
                print("Warning: _dashboard trying to access a forbidden method of app")
                return None

    for table in db:
        for field in table:
            if callable(field.default):
                field.default = make_safe_field(field.default)
            if callable(field.update):
                field.update = make_safe_field(field.update)


def run(command, cwd="."):
    """for runing git commands inside an app (project)"""
    return subprocess.check_output(command.split(), cwd=cwd).decode(errors="ignore")


def get_commits(project, cwd="."):
    """List of git commits for the project"""
    output = run("git log", cwd=cwd)
    commits = []
    for line in output.split("\n"):
        if line.startswith("commit "):
            commit = {"code": line[7:], "message": "", "author": "", "date": ""}
            commits.append(commit)
        elif line.startswith("Author: "):
            commit["author"] = line[8:]
        elif line.startswith("Date: "):
            commit["date"] = datetime.datetime.strptime(
                line[6:].strip(), "%a %b %d %H:%M:%S %Y %z"
            )
        else:
            commit["message"] += line.strip() + "\n"
    return commits


def get_branches(cwd="."):
    """Dictionary of git local branches for the project"""
    output = run("git branch", cwd=cwd)
    branches = {"current": "", "other": []}
    for line in output.split("\n"):
        if line.startswith("* "):
            branches["current"] = line[2:]
        elif not line == "":
            branches["other"].append(line[2:])
    return branches


def is_git_repo(cwd="."):
    """Checks if the cwd is a git repo"""
    return os.path.exists(os.path.join(cwd, ".git/config"))


def fieldformat(table, row):
    """
    Given a table and a record, returns a string representation for the record
    Compatible with pydal.helpers.methods._fieldformat
    """
    format = getattr(table, "_format", None)
    if format:
        if isinstance(format, str):
            return table._format % row
        elif callable(table._format):
            return table._format(row)
        else:
            raise NotImplementedError
    return str(row.id)


# Create a custom represent function that returns a clickable link
def make_admin_reference_represent(app_name, db_name, db, field):
    def represent(value, _):
        if not value:
            return ""
        ref_table = field.referenced_table()
        ref_row = ref_table(value)
        if not ref_row:
            return f"#{value}(missing)"
        # Create text to be displayed
        display_text = fieldformat(ref_table, ref_row)
        # Create link to the referenced record's table
        link_url = URL(
            "dbadmin", app_name, db_name, ref_table._tablename, vars=dict(id=value)
        )
        return A(display_text, _href=link_url)

    return represent
