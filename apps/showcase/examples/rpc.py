import requests

from py4web import action, request
from py4web.utils.jsonrpc import JsonRpc


# define a function you want to expose
def add(x, y):
    return x + y


# register your functions
service = JsonRpc()
service.methods['add'] = add


# expose the server
@action("rpc", method=["GET", "POST"])
def rpc():
    return service(request.query or request.json)


# example of a client
def example_jsonrpc():
    import jsonrpc.proxy                                                    
    p = jsonrpc.proxy.JSONRPCProxy(URL('rpc'))
    assert p.add(1,2) == 3                                                  
    assert p.add(x=1, y=2) == 3
