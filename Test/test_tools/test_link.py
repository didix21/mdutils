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
        expected = '[' + title + '](' + a_link + ')'

        actual = Link(title, a_link, style="inline")

        self.assertEqual(expected, actual.new_link())
