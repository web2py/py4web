from py4web import HTTP, URL, Field, abort, action, redirect, request
from py4web.utils.form import Form, FormStyleDefault

from .common import session


@action("tagsinput_form", method=["GET", "POST"])
@action.uses("examples/tagsinput_form.html", session)
def tagsinput_form():
    form = Form([Field("colors", "list:string")], keep_values=True)
    return dict(form=form)
