import unittest

from web3py import request, response, Session, DAL
from web3py.utils.dbstore import DBStore

class TestSession(unittest.TestCase):

    def test_session(self):
        request.app_name = 'myapp'
        session = Session(secret="a", expiration=10)
        session.on_request()
        session['key'] = 'value'
        session.on_success()
        cookie_name = session.local.session_cookie_name 

        a,b = str(response._cookies)[len('Set-Cookie: '):].split(';')[0].split('=', 1)
        request.cookies[a] = b
        request.cookies = response._cookies
        session.local.data.clear()

        session = Session(secret="b", expiration=10)
        session.on_request()
        self.assertEqual(session.get('key'), None)

        session = Session(secret="a", expiration=10)
        session.on_request()
        self.assertEqual(session.get('key'), 'value')

    def test_session_in_db(self):
        request.app_name = 'myapp'
        db = DAL('sqlite:memory')
        session = Session(secret="a", expiration=10, storage=DBStore(db))
        session.on_request()
        session['key'] = 'value'
        session.on_success()
        cookie_name = session.local.session_cookie_name 

        a,b = str(response._cookies)[len('Set-Cookie: '):].split(';')[0].split('=', 1)
        request.cookies[a] = b
        request.cookies = response._cookies
        session.local.data.clear()

        session = Session(expiration=10, storage=DBStore(db))
        session.on_request()
        self.assertEqual(session.get('key'), 'value')

        request.cookies[a] = 'wrong cookie'
        session = Session(expiration=10, storage=DBStore(db))
        session.on_request()
        self.assertEqual(session.get('key'), None)


