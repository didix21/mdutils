# Python
#
# This module implements tests for MdUtils class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2020 Dídac Coll

from unittest import TestCase
from mdutils.fileutils import MarkDownFile
import tempfile
import os


class TestMarkdownFile(TestCase):

    def test_create_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            file = MarkDownFile('Test_file')
            self.assertEqual(file.file_name, 'Test_file.md')

    def test_create_file_case_0(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            file = MarkDownFile('Test_filemd')
            self.assertEqual(file.file_name, 'Test_filemd.md')

    def test_create_file_case_1(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            file = MarkDownFile('Test_file.md')
            self.assertEqual(file.file_name, 'Test_file.md')

    def test_rewrite_all_file(self):
        expected_content = "Write some content"
        file_name = 'Test_file.md'
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            file = MarkDownFile(file_name)
            file.rewrite_all_file(expected_content)
            with open(file_name, 'r') as actual_md:
                self.assertEqual(actual_md.read(), expected_content)

    def test_append_end(self):
        expected_content = "Write some content and some data"
        file_name = 'Test_file.md'
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            file = MarkDownFile(file_name)
            file.rewrite_all_file("Write some content")
            file.append_end(" and some data")
            with open(file_name, 'r') as actual_md:
                self.assertEqual(actual_md.read(), expected_content)

    def test_append_second_line(self):
        expected_content = "This is the 1st line\nThis is the 2nd line\nThis is the 3th line\nThis is the 4th line"
        file_name = 'Test_file.md'
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            file = MarkDownFile(file_name)
            file.rewrite_all_file("This is the 1st line\nThis is the 2nd line\nThis is the 4th line")
            file.append_after_second_line("This is the 3th line")
            with open(file_name, 'r') as actual_md:
                self.assertEqual(actual_md.read(), expected_content)

    def test_read(self):
        expected_content = "This is the expected content after reading the file"
        file_name = 'Test_file.md'
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            with open(file_name, 'w') as file:
                file.write(expected_content)

            self.assertEqual(MarkDownFile.read_file(file_name), expected_content)
