import os
import unittest
from py4web.core import get_error_snapshot


class ErrorTest(unittest.TestCase):
    def test_get_error_snapshot(self):
        try:
            1 / 0
        except Exception:
            snapshot = get_error_snapshot()
            keys = list(sorted(snapshot.keys()))
        self.assertEqual(
            keys,
            [
                "exception_type",
                "exception_value",
                "os_environ",
                "platform_info",
                "python_version",
                "stackframes",
                "timestamp",
                "traceback",
            ],
        )
