# Python
#
# This module implements the Main Markdown class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# (C) 2018 Dídac Coll
#
# SPDX-License-Identifier:   BSD-3-Clause

"""Module **mdutils**

The available features are:
    * Create Headers, Til 6 sub-levels.
    * Auto generate a table of contents.
    * Create List and sub-list.
    * Create paragraph.
    * Generate tables of different sizes.
    * Insert Links.
    * Insert Images.
    * Insert Code.
"""
from mdutils.fileutils.fileutils import NewFile
from mdutils.tools import tools


class MdUtils:
    """This class give some basic methods that helps the creation of Markdown files.

    Long description will be written.

    """

    def __init__(self, file_name, title="", author=""):
        self.file_name = file_name

        self.author = author
        self.header = tools.Header()
        self.textUtils = tools.TextUtils()
        self.title = self.header.choose_header(level=1, title=title, style='setext')
        self.table_of_contents = ""
        self.data_text = ""
        self._table_titles = []

    def create_md_file(self):
        """ It creates a new Markdown file"""
        md_file = NewFile(self.file_name)
        md_file.rewrite_all_file(data=self.title + self.table_of_contents + self.data_text)

        return md_file

    def new_header(self, level, title, style='atx'):
        """ Add a new header to the Markdown file.
            **Examples:**
            ``new_header(level=2, title='Header Title', style='atx')``
            This will write a new level 2 Atx-style header on file_name.md:
                * ## Header Title
            ``new_header(level=2, title='Header Title', style='setext')``
            This will write a new level 2 Setext-style header on file_name.md:
                * Header Title
                '-------------'

        :param level: Header level
        :param title: Header title
        :param style: Header style, could be ``'atx'`` or ``'setext'``. By default **atx* style is chosen.
        """
        self._add_new_item_table_of_content(level, title)
        self.data_text += self.header.choose_header(level, title, style)

    def _add_new_item_table_of_content(self, level, item):
        if level == 1:
            self._table_titles.append(item)
            self._table_titles.append([])
        elif level == 2:
            self._table_titles[-1].append(item)
            self._table_titles[-1].append([])

    def new_table_of_contents(self, table_title="Table of contents"):
        """ Add a table of contents of the Header Levels 2, 3 and 4."""
        self.table_of_contents += self.header.choose_header(level=1, title=table_title, style='setext')
        self.table_of_contents += tools.TableOfContents().create_table_of_contents(self._table_titles)

        return self.table_of_contents

    def create_table(self, columns, rows, text, text_align='center'):
        new_table = tools.Table()
        text_table = new_table.create_table(columns, rows, text, text_align)
        self.data_text += text_table

        return text_table

    def add_new_paragraph(self, text=''):
        self.data_text += '\n' + text + '\n'
        return self.data_text


if __name__ == '__main__':
    header = tools.Header()
