# Python
#
# This module implements tests for TableOfContents class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll

from unittest import TestCase
from mdutils.tools.tools import TableOfContents

__author__ = 'didix21'
__project__ = 'MdUtils'


class TestTableOfContents(TestCase):

    def test_create_table_of_contents(self):
        array_of_contents = ['Results Tests', [], 'Test Details', ['Test 1', [], 'Test 2', [],
                                                                   'Test 3', [], 'Test 4', []]]
        result = '\n* [Results Tests](#results-tests)\n' \
                 '* [Test Details](#test-details)\n\t' \
                 '* [Test 1](#test-1)\n\t' \
                 '* [Test 2](#test-2)\n\t' \
                 '* [Test 3](#test-3)\n\t' \
                 '* [Test 4](#test-4)\n'

        table_of_contents = TableOfContents()
        self.assertEqual(table_of_contents.create_table_of_contents(array_of_contents, depth=2), result)
