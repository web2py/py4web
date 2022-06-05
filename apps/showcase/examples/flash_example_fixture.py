from py4web import action, redirect

from .common import flash, session


@action("flash_example_fixture")
@action.uses(flash)
def flash_example_fixture():
    flash.set("you have been redirected <test!>", sanitize=True)
    redirect("flash_next")


@action("flash_next")
@action.uses("examples/flash_example_next.html", flash)
def flash_example_next():
    return dict()
