import os
import sys
import unittest
import tempfile
import time
import signal
from multiprocessing import Process
from unittest.mock import patch
from py4web.core import cli


def patched_cli():
    dirpath = tempfile.mkdtemp()
    dir = os.path.join(dirpath, "apps")
    testargs = ["py4web", "run", "-d", "demo", dir]
    with patch.object(sys, "argv", testargs):
        cli()


class MainTest(unittest.TestCase):
    def test_main(self):
        class MyException(Exception):
            pass

        def handler(signum, frame):
            raise MyException

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(10)
        try:
            patched_cli()
        except MyException:
            pass
