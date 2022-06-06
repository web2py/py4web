from py4web import action

from .common import flash, session


@action("flash_example_naive")
@action.uses("examples/flash_example.html")
def flash_example_naive():
    return dict(flash={"message": "hello", "class": "error"})
