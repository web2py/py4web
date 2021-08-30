from py4web.core import Fixture, request, response, HTTP

class CORS(Fixture):
    """
    Fixture helper for sharing web service avoiding cross origin resource sharing problems
    """

    def __init__(self,
                 age=86400,
                 origin="*",
                 headers="*",
                 methods="*"):
        Fixture.__init__(self)

        self.age = age
        self.origin = origin
        self.headers = headers
        self.methods = methods

    def on_request(self):
        response.headers["Access-Control-Allow-Origin"] = self.origin
        response.headers["Access-Control-Max-Age"] = self.age
        response.headers["Access-Control-Allow-Headers"] = self.headers
        response.headers["Access-Control-Allow-Methods"] = self.methods
        response.headers["Access-Control-Allow-Credentials"] = "true"
        if request.method == "OPTIONS":
            raise HTTP(200)
