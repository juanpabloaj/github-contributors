import unittest
from github_contributors import generate_markdown
from github_contributors import generate_rst


class TestGenMarkdown(unittest.TestCase):

    def setUp(self):
        self.author = 'author'
        self.url = 'url'

        self.expected_string = u'[author](url)'

    def test_get_text(self):
        assert generate_markdown(self.author, self.url) == self.expected_string

    def test_is_unicode(self):
        assert type(generate_markdown(self.author, self.url)) == unicode


class TestGenRST(unittest.TestCase):

    def setUp(self):
        self.author = 'author'
        self.url = 'url'

        self.expected_string = u'`author <url>`_'

    def test_gen_text(self):
        assert generate_rst(self.author, self.url) == self.expected_string

    def test_is_unicode(self):
        assert type(generate_rst(self.author, self.url)) == unicode
