
class P4WException(BaseException):
    pass


class HTTP(P4WException):
    """Our HTTP exception does not delete cookies and headers like the bottle.HTTPResponse does;
    since it is considered a success, not a failure"""

    def __init__(self, status, *, is_error = False):
        self.status = status
        self.is_error = is_error
