# Python
#
# This module implements tests for Header class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll

from unittest import TestCase
from mdutils.tools.Header import Header


class TestHeader(TestCase):

    def test_atx_level_1(self):
        title = "Text Title Atx 1"
        header_id = "myheader"
        result = '\n# ' + title + '\n'
        result2 = '\n# ' + title + ' {#myheader}' + '\n'
        self.assertEqual(Header().atx_level_1(title), result)
        self.assertEqual(Header().atx_level_1(title, header_id), result2)

    def test_atx_level_2(self):
        title = "Text Title Atx 2"
        header_id = "myheader"
        result = '\n## ' + title + '\n'
        result2 = '\n## ' + title + ' {#myheader}' + '\n'
        self.assertEqual(Header().atx_level_2(title), result)
        self.assertEqual(Header().atx_level_2(title, header_id), result2)

    def test_atx_level_3(self):
        title = "Text Title Atx 3"
        header_id = "myheader"
        result = '\n### ' + title + '\n'
        result2 = '\n### ' + title + ' {#myheader}' + '\n'
        self.assertEqual(Header().atx_level_3(title), result)
        self.assertEqual(Header().atx_level_3(title, header_id), result2)

    def test_atx_level_4(self):
        title = "Text Title Atx 4"
        header_id = "myheader"
        result = '\n#### ' + title + '\n'
        result2 = '\n#### ' + title + ' {#myheader}' + '\n'
        self.assertEqual(Header().atx_level_4(title), result)
        self.assertEqual(Header().atx_level_4(title, header_id), result2)

    def test_atx_level_5(self):
        title = "Text Title Atx 5"
        header_id = "myheader"
        result = '\n##### ' + title + '\n'
        result2 = '\n##### ' + title + ' {#myheader}' + '\n'
        self.assertEqual(Header().atx_level_5(title), result)
        self.assertEqual(Header().atx_level_5(title, header_id), result2)

    def test_atx_level_6(self):
        title = "Text Title Atx 6"
        header_id = "myheader"
        result = '\n###### ' + title + '\n'
        result2 = '\n###### ' + title + ' {#myheader}' + '\n'
        self.assertEqual(Header().atx_level_6(title), result)
        self.assertEqual(Header().atx_level_6(title, header_id), result2)

    def test_setext_level_1(self):
        title = "Text Title Setext 1"
        result = '\n' + title + '\n' + ''.join(['=' for _ in title]) + '\n'
        self.assertEqual(Header().setext_level_1(title), result)

    def test_setext_level_2(self):
        title = "Text Title Setext 2"
        result = '\n' + title + '\n' + ''.join(['-' for _ in title]) + '\n'
        self.assertEqual(Header().setext_level_2(title), result)

    def test_choose_header(self):
        header = Header()
        func_list = [header.atx_level_1('Atx Example'), header.atx_level_2('Atx Example'),
                     header.atx_level_3('Atx Example'), header.atx_level_4('Atx Example'),
                     header.atx_level_5('Atx Example'), header.atx_level_6('Atx Example'),
                     header.setext_level_1('Setext Example'), header.setext_level_2('Setext Example')]
        for x in range(8):
            if x < 6:
                title = 'Atx Example'
                chosen_header = header.choose_header(level=x + 1, title=title, style='atx')
            else:
                title = 'Setext Example'
                chosen_header = header.choose_header(level=x - 5, title=title, style='setext')
            self.assertEqual(chosen_header, func_list[x])
