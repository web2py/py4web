import unittest

from web3py import request, response, Session


class TestSession(unittest.TestCase):

    def test_session(self):
        request.app_name = 'myapp'
        session = Session(secret="a", expiration=10)
        session.on_request()
        session['key'] = 'value'
        session.on_success()
        cookie_name = session.local.session_cookie_name 

        a,b = str(response._cookies)[len('Set-Cookie: '):].split('=')
        request.cookies[a] = b
        request.cookies = response._cookies
        session.local.data.clear()

        session = Session(secret="b", expiration=10)
        session.on_request()
        self.assertEqual(session.get('key'), None)

        session = Session(secret="a", expiration=10)
        session.on_request()
        self.assertEqual(session.get('key'), 'value')
