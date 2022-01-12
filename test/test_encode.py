from unittest.case import TestCase
from flask.typing import StatusCode
from flask.wrappers import Request
import sys, os

from werkzeug.wrappers import response

sys.path.append("./src")
import unittest
from src.EncodeDecode import EncodeDecode
from src import tinyurl


class test_encode(unittest.TestCase):
    def setUp(self):
        self.tiny_url = tinyurl.tinyurl
        self.client = self.tiny_url.test_client()

    def test_index(self):

        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_content(self):
        """
        Test that urls get shorter
        """
        url = "http://www.example.com/jkhkjshdfjhdjsfhdjfhdjh"
        # check = tinyurl.test_client()
        link = EncodeDecode()
        l = link.encode(url)
        self.assertLess(len(l), len(url))

    def test_redirect_to_url(self):
        url = "http://www.example.com/jkhkjshdfjhdjsfhdjfhdjh"
        # check = tinyurl.test_client()
        link = EncodeDecode()
        l = link.encode(url)

    def test_post_route(self):

        url = "http://www.example.com/jkhkjshdfjhdjsfhdjfhdjh"
        # check = tinyurl.test_client()
        link = EncodeDecode()
        l = link.encode(url)
        response = self.client.post(
            "/encode_url", data=dict(original_url=url), follow_redirects=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertIn(l, response.content)

    def test_404(self):
        response = self.client.get("/failed_url")
        self.assertEquals(response.status_code, 404)


if __name__ == "__main__":

    unittest.main()
