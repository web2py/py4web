from .common import unauthenticated


@unauthenticated.get()  # exposed as /hello_world/<msg>
def hello_world_msg(msg):
    return dict(msg=msg)
