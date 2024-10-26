import os
import signal
import tempfile
import unittest

from click.testing import CliRunner

from py4web.core import cli


def run_cli():
    dirpath = tempfile.mkdtemp()
    dir = os.path.join(dirpath, "apps")
    runner = CliRunner()

    testargs = ["setup", dir]
    res = runner.invoke(cli, testargs, input="y")
    if res.exception:
        raise res.exception

    testargs = ["run", "-d", "demo", dir]
    res = runner.invoke(cli, testargs)
    if res.exception:
        raise res.exception


class MainTest(unittest.TestCase):
    def test_main(self):
        def handler(signum, frame):
            raise KeyboardInterrupt

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(10)
        try:
            run_cli()
        except KeyboardInterrupt:
            pass
