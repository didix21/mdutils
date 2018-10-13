# Python
#
# This module implements tests for Header class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll

from unittest import TestCase
from mdutils.tools.tools import Link


class TestLink(TestCase):
    def test_new_link(self):
        a_link = "https://github.com/didix21/mdutils"
        title = "Github Didac"
        reference = "Reference Style"
        global_references = {}

        expected_inline_style = '[' + title + '](' + a_link + ')'
        actual_inline_style = Link(title, a_link, "inline", global_references)
        self.assertEqual(expected_inline_style, actual_inline_style.new_link())

        expected_reference_style = '[' + title +'][' + reference + ']'
        actual_reference_style = Link(title, a_link, "reference-Reference Style", global_references)
        self.assertEqual(expected_reference_style, actual_reference_style.new_link())

        global_references = actual_reference_style.get_global_references()
        self.assertEqual({reference: a_link}, global_references)




