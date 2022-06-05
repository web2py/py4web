from .common import unauthenticated


@unauthenticated.get()  # exposed as /hello_world
def hello_world():
    return dict()
