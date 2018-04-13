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

The different features availables are:
    * Create Heades, Til 6 sub-lvels.
    * Auto generate a table of contents.
    * Create List and sub-list.
    * Create paragraph.
    * Generate tables of different sizes.
    * Insert Links.
    * Insert Images.
    * Insert Code.
"""
from mdutils.fileutils.fileutils import NewFile
from mdutils.tools.tools import Header
from mdutils.tools.tools import TableOfContents
from mdutils.tools.tools import Table


class MdUtils:
    """This class give some basic methods that helps the creation of Markdown files.

    Long description will be written.

    """
    def __init__(self, file_name, title="", author=""):
        self.file_name = file_name
        self.title = title
        self.author = author
        self.header = Header()
        self.markdown_file = self.create_md_file()
        self._table_titles = []

    def create_md_file(self):
        """ It creates a new Markdown file"""
        md_file = NewFile(self.file_name)
        md_file.rewrite_all_file(data=self.header.choose_header(level=1, title=self.title, style='setext'))
        return md_file

    def new_header(self, level, title, style='atx'):
        """ Add a new header to the Markdown file.
            **Examples:**
            ``new_header(level=2, title='Header Title', style='atx')``
            This will write a new level 2 Atx-style header on file_name.md:
                * ## Header Title
            ``new_header(level=2, title='Header Title', style='setext)``
            This will write a new level 2 Setext-style header on file_name.md:
                * Header Title
                '-------------'

        :param level: Header level
        :param title: Header title
        :param style: Header style, could be ``'atx'`` or ``'setext'``. By default **atx* style is chosen.
        """
        self._add_new_item_table_of_content(level, title)
        self.markdown_file.append_end(self.header.choose_header(level, title, style))

    def _add_new_item_table_of_content(self, level, item):
        if level == 1:
            self._table_titles.append(item)
            self._table_titles.append([])
        elif level == 2:
            self._table_titles[-1].append(item)
            self._table_titles[-1].append([])
        # elif level == 3:
        #     self._table_titles[-1][-1].append(item)
        #     self._table_titles[-1][-1].append([])
        # elif level == 4:
        #     self._table_titles[-1][-1][-1].append(item)
        #     self._table_titles[-1][-1][-1].append([])
        # elif level == 5:
        #     self._table_titles[-1][-1][-1][-1].append(item)

    def new_table_of_contents(self):
        """ Add a table of contents of the Header Levels 2, 3 and 4."""
        table = TableOfContents().create_table_of_contents(self._table_titles)
        self.markdown_file.append_after_second_line(table)

    def create_table(self, columns, rows, text, text_align='center'):
        new_table = Table()
        text_table = new_table.create_table(columns, rows, text, text_align)
        self.markdown_file.append_end(text_table)


if __name__ == '__main__':
    heeader = Header()
