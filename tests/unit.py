import unittest
from requests_oauthlib import OAuth1Session

from unplag import Unplag
from unplag.connection import Connection
from unplag.check import Check


class TestUnplagEntity(unittest.TestCase):
    def test_unplag_auth(self):
        with self.assertRaises(Exception):
            Unplag('test_key', 'test_secret', server='http://unplag.com')


class TestConnectionEntity(unittest.TestCase):
    def test_connection(self):
        conn = Connection('test_key', 'test_secret', 'http://unplag.com')
        conn.create()
        self.assertIsNotNone(conn.oauth_session)
        self.assertIsInstance(conn.oauth_session, OAuth1Session)
        with self.assertRaises(Exception):
            conn.ping()


class TestCheckEntity(unittest.TestCase):
    def test_check_create(self):
        check = Check(None, None)
        with self.assertRaises(Exception):
            check.create(1, "web", 1, 1)

if __name__ == "__main__":
    unittest.main()