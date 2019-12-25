import os
import sys
import unittest
import tempfile
import time
import signal
from multiprocessing import Process
from unittest.mock import patch
from py4web.core import main


def patched_main():
    dirpath = tempfile.mkdtemp()
    dir = os.path.join(dirpath, "apps")
    testargs = ["py4web", "-d", "demo", "-c", dir]
    with patch.object(sys, "argv", testargs):
        main()


class MainTest(unittest.TestCase):
    def test_main(self):
        class MyException(Exception):
            pass

        def handler(signum, frame):
            raise MyException

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(10)
        try:
            patched_main()
        except MyException:
            pass
