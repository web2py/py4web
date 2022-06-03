from yatl.helpers import DIV

from py4web import Field, action
from py4web.utils.form import Form

from ..common import flash


@action("mycomponent.load", method=["GET", "POST"])
@action.uses(flash)
def mycomponent():
    flash.set("Welcome")
    form = Form([Field("your_name")])
    return DIV("Hello " + request.forms["your_name"] if form.accepted else form).xml()


# a py4web component loader is a page that loads page parts via ajax
@action("component_loader")
@action.uses("component_loader.html", flash)
def component_loader():
    return dict()
