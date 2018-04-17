from unittest import TestCase
from mdutils.mdutils import MdUtils

from pathlib import Path
import os

class TestMdUtils(TestCase):
    def test_create_md_file(self):
        md_file = MdUtils("Test_file")
        md_file.create_md_file()
        md_file_expect = Path('Test_file.md')
        if md_file_expect.is_file():
            os.remove('Test_file.md')
            pass
        else:
            self.fail()

    def test_new_header(self):
        file_name = 'Test_file'
        md_file = MdUtils(file_name)
        string_headers_expected = "\n# Header 0\n\n## Header 1\n\n### Header 2\n\n#### Header 3\n\n" \
                                  "##### Header 4\n\n###### Header 5\n"
        string_headers = ""
        for x in range(6):
            string_headers += md_file.new_header(level=(x + 1), title='Header ' + str(x), style='atx')

        self.assertEqual(string_headers, string_headers_expected)
        md_file.create_md_file()
        file_result = md_file.read_md_file(file_name)
        self.assertEqual(file_result, '\n\n\n' + string_headers_expected)
        os.remove(file_name + '.md')

    def test__add_new_item_table_of_content(self):
        self.fail()

    def test_new_table_of_contents(self):
        self.fail()

    def test_create_table(self):
        self.fail()
