import unittest

from requests_oauthlib import OAuth1Session
from unplag.file import File

#   Initialize empty file entity
file = File(OAuth1Session('key', 'secret'), 'https://unplag.com')


class TestFullFileEntity(unittest.TestCase):
    def test_file_abstract(self):
        self.assertIsInstance(file, File)
        self.assertIsInstance(file.oauth_session, OAuth1Session)
        self.assertEqual(file.server, 'https://unplag.com')


if __name__ == "__main__":
    unittest.main()