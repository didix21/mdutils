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

    def test_new_table_of_contents(self):
        # Create headers level 1 and 2.
        md_file = MdUtils(file_name="Test_file", title="Testing table of contents")
        list_headers = ["Header 1", "Header 1.1", "Header 2", "Header 2.2", "Header 2.3"]
        table_of_content_title = MdUtils(file_name='').new_header(level=1, title='Index', style='setext')
        md_file.new_header(level=1, title=list_headers[0])
        md_file.new_header(level=2, title=list_headers[1])
        md_file.new_header(level=1, title=list_headers[2])
        md_file.new_header(level=2, title=list_headers[3])
        md_file.new_header(level=2, title=list_headers[4])

        # Testing Depth 1
        table_of_contents_result = md_file.new_table_of_contents(table_title="Index", depth=1)
        table_of_content_expected = table_of_content_title \
            + '\n* [' + list_headers[0] + '](#' + list_headers[0].lower().replace(' ', '-') \
            + ')' \
            + '\n* [' + list_headers[2] + '](#' + list_headers[2].lower().replace(' ', '-') \
            + ')\n'
        self.assertEqual(table_of_contents_result, table_of_content_expected)
        # Testing created file
        md_file.create_md_file()
        data_file_result = MdUtils('').read_md_file('Test_file')
        data_file_expected = MdUtils('').new_header(1, "Testing table of contents", 'setext') \
            + md_file.table_of_contents \
            + md_file.file_data_text
        self.assertEqual(data_file_result, data_file_expected)
        os.remove('Test_file.md')

        # Testing Depth 2
        md_file = MdUtils(file_name="Test_file", title="Testing table of contents")
        list_headers = ["Header 1", "Header 1.1", "Header 2", "Header 2.2", "Header 2.3"]
        table_of_content_title = MdUtils(file_name='').new_header(level=1, title='Index', style='setext')
        md_file.new_header(level=1, title=list_headers[0])
        md_file.new_header(level=2, title=list_headers[1])
        md_file.new_header(level=1, title=list_headers[2])
        md_file.new_header(level=2, title=list_headers[3])
        md_file.new_header(level=2, title=list_headers[4])

        table_of_contents_result = md_file.new_table_of_contents(table_title="Index", depth=2)
        table_of_content_expected = table_of_content_title
        for x in range(len(list_headers)):
            if x in (0, 2):
                table_of_content_expected += '\n* [' + list_headers[x] + '](#' \
                                             + list_headers[x].lower().replace(' ', '-') + ')'
            else:
                table_of_content_expected += '\n\t* [' + list_headers[x] + '](#' \
                                             + list_headers[x].lower().replace(' ', '-') + ')'
        table_of_content_expected += '\n'
        self.assertEqual(table_of_contents_result, table_of_content_expected)

        md_file.create_md_file()
        data_file_result = MdUtils('').read_md_file('Test_file')
        data_file_expected = MdUtils('').new_header(1, "Testing table of contents", 'setext') \
            + md_file.table_of_contents \
            + md_file.file_data_text
        self.assertEqual(data_file_result, data_file_expected)
        os.remove('Test_file.md')

    def test_create_table(self):
        self.fail()
