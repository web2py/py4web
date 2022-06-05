from yatl.helpers import H1, INPUT

from py4web import action


@action("example_helpers")
@action.uses("examples/generic.html")
def example_helpers():
    return dict(a=H1("I am a title"), b=2, c=dict(d=3, e=4, x=INPUT(_name="test")))
