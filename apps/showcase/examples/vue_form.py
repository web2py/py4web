import datetime

from pydal.validators import IS_IN_SET

from py4web import Field, action

from ..common import session
from ..components.vueform import VueForm

myform = VueForm(
    "test_form",
    session,
    [
        Field("name", default="Luca"),
        Field("last_name", default="Smith", writable=False),
        Field("read", "boolean", default=True),
        Field(
            "animal",
            requires=IS_IN_SET(["cat", "dog", "bird"]),
            default="dog",
            writable=False,
        ),
        Field(
            "choice",
            requires=IS_IN_SET({"c": "cat", "d": "dog", "b": "bird"}),
            default="d",
        ),
        Field("arrival_time", "datetime", default=datetime.datetime.utcnow),
        Field("date_of_birth", "date"),
        Field("narrative", "text"),
    ],
    readonly=False,
    redirect_url="index",
)


@action("vue_form", method=["GET"])
@action.uses("vueform.html", myform)
def vue_form():
    return dict(form=myform())
