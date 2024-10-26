class JsonRpc:
    """implements the jsonrpc server 2.0 protocol"""

    def __init__(self):
        self.methods = {}

    def __call__(self, data):
        """
        this function implements the jsonrpc server protocol, do not edit
        client example:
        import jsonrpc.proxy
        p = jsonrpc.proxy.JSONRPCProxy("http://127.0.0.1:8000", "/examples/rpc")
        assert p.add(1,2) == 3
        assert p.add(x=1, y=2) == 3
        """
        if not data or data.get("jsonrpc") != "2.0":
            return {
                "id": None,
                "jsonrpc": "2.0",
                "error": {"code": -32600, "message": "Invalid Request"},
            }
        rid = data.get("id")
        method = data.get("method")
        params = data.get("params")
        if None in (rid, method) or not isinstance(params, (list, dict)):
            return {
                "id": None,
                "jsonrpc": "2.0",
                "error": {"code": -32600, "message": "Invalid Request"},
            }
        func = self.methods.get(method)
        if not func:
            return {
                "rid": None,
                "jsonrpc": "2.0",
                "error": {"code": -32601, "message": "Method not found"},
            }
        try:
            result = func(*params) if isinstance(params, list) else func(**params)
            return {"result": result, "id": rid, "jsonrpc": "2.0"}
        except Exception as err:
            return {
                "rid": None,
                "jsonrpc": "2.0",
                "error": {"code": -32603, "message": "Internal error", "data": err},
            }
