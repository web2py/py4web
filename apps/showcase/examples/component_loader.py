from yatl.helpers import DIV

from py4web import Field, action, request
from py4web.utils.form import Form

from .common import flash


@action("mycomponent.load", method=["GET", "POST"])
@action.uses(flash)
def mycomponent():
    # create a form object
    form = Form([Field("your_name")])
    # if the form is not submmitted show a welcome flash message
    if not request.forms:
        flash.set("Welcome")
    # if the form is submitted and accepted display another message
    elif form.accepted:
        flash.set("Welcome " + request.forms["your_name"])
    # return the form if it has not already been submitted and accepted
    return DIV(form if not form.accepted else "done!").xml()


# a page that loads the above compnent via ajax
@action("component_loader")
@action.uses("examples/component_loader.html", flash)
def component_loader():
    return dict()
