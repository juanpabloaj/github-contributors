import unittest
from github_contributors import generate_markdown


class TestGenMarkdown(unittest.TestCase):

    def setUp(self):
        self.author = 'author'
        self.url = 'url'

        self.expected_string = u'[author](url)'

    def test_get_text(self):
        assert generate_markdown(self.author, self.url) == self.expected_string

    def test_is_unicode(self):
        assert type(generate_markdown(self.author, self.url)) == unicode
