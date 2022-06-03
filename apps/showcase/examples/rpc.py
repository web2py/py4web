from py4web import action, request
from py4web.utils.jsonrpc import JsonRpc

obj = JsonRpc()


def add(a, b):
    return a + b


# register your functions
obj.methods["add"] = add

# this is a standard handler that implements the protocol
@action("rpc", method="POST")
def rpc():
    return obj(request.json)
