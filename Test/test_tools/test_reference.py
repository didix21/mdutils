from unittest import TestCase
from mdutils.tools.tools import Reference


class ReferenceBasicTest(TestCase):

    def __init__(self, *args, **kwargs):
        super(ReferenceBasicTest, self).__init__(*args, **kwargs)

    def setUp(self):
        super(ReferenceBasicTest, self).setUp()

    def tearDown(self):
        super(ReferenceBasicTest, self).tearDown()


class TestReference(ReferenceBasicTest):

    def __init__(self, *args, **kwargs):
        super(TestReference, self).__init__(*args, **kwargs)
        self.global_references = {}
        self.link = "https://github.com/didix21/mdutils"
        self.github_link_key = "github_link"

    def test_add_new_reference_to_global_references(self):

        actual = Reference(self.global_references, self.link, self.github_link_key)
        expected = {self.github_link_key: self.link}

        self.assertEqual(expected, actual.get_global_references_updated())

    def test_add_new_reference_if_exist(self):

        self.global_references = {self.github_link_key: self.link}

        actual = Reference(self.global_references, self.link, self.github_link_key)
        expected = {'github_link': self.link, 'github_link1': self.link}

        self.assertEqual(expected, actual.get_global_references_updated())

