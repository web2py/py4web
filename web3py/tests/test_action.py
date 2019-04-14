import unittest

from web3py import action

os.environ['WEB2PY_APPLICATIIONS'] = 'applications'


@action('/index')
def index():
    return 'ok'


class CacheAction(unittest.TestCase):

    def test_action(self):
        pass
