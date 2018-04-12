# Python
#
# This module implements a main class that allows to create markdown files, write in them or read.
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


class Header(object):
    """Contain the main methods to define Headers on a Markdown file.

    """
    # ********************************************************************
    # *                             Atx-Style                            *
    # ********************************************************************
    @staticmethod
    def atx_level_1(title):
        return '# ' + title

    @staticmethod
    def atx_level_2(title):
        return '\n\n## ' + title

    @staticmethod
    def atx_level_3(title):
        return '\n\n### ' + title

    @staticmethod
    def atx_level_4(title):
        return '\n\n#### ' + title

    @staticmethod
    def atx_level_5(title):
        return '\n\n##### ' + title

    @staticmethod
    def atx_level_6(title):
        return '\n\n###### ' + title

    # ********************************************************************
    # *                          Setext-Style                            *
    # ********************************************************************
    @staticmethod
    def setext_level_1(title):
        return title + '\n' + ''.join(['=' for _ in title])

    @staticmethod
    def setext_level_2(title):
        return title + '\n' + ''.join(['-' for _ in title])

    def choose_header(self, level, title, style='atx'):
        """ This method choose the style and the header level.

            :Examples:
            >>> import Header
            >>> createHeaders = Header()
            >>> createHeaders.choose_header(level=1, title='New Header', style='atx')
            "# New Header"

            >>> createHeaders.choose_header(level=1, title='Another Header 1', style=setext)
            "Another Header 1\\n----------------"

        :param level: Header Level, For Atx-style 1 til 6. For Setext-style 1 and 2 header levels.
        :param title: Header Title.
        :param style: Header Style atx or setext.
        :return:
        """
        if style.lower() == 'atx':
            if level == 1:
                return self.atx_level_1(title)
            elif level == 2:
                return self.atx_level_2(title)
            elif level == 3:
                return self.atx_level_3(title)
            elif level == 4:
                return self.atx_level_4(title)
            elif level == 5:
                return self.atx_level_5(title)
            elif level == 6:
                return self.atx_level_6(title)
        elif style.lower() == 'setext':
            if level == 1:
                return self.setext_level_1(title)
            elif level == 2:
                return self.setext_level_2(title)


class TableOfContents(object):
    def _loop_trought(self, elements, tab=''):
        """Method that go trough a list of elements that contain strings and other list and return a string \
        reade to be written inside a markdown file in order to create a table of contents.

        - **elements**: contain all the headers defined on the main class.
        - **tab:** Inserts tabulations."""
        elements_to_string = ""
        for item in elements:
            if isinstance(item, list):
                if item != []:
                    if tab == '\t':
                        elements_to_string += self._loop_trought(item, tab='\t\t')
                    else:
                        elements_to_string += self._loop_trought(item, tab='\t')
            else:
                elements_to_string += '\n' + tab + '* [' + item + '](#' + item.lower().replace(' ', '-') + ')'

        return elements_to_string

    def create_table_of_contents(self, array_of_title_contents):
        table_of_contents = ""
        table_of_contents += self._loop_trought(array_of_title_contents)

        return table_of_contents


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
        md_file.rewrite_all_file(data=self.header.choose_header(level=1, title=self.title))
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
        if level == 2:
            self._table_titles.append(item)
            self._table_titles.append([])
        elif level == 3:
            self._table_titles[-1].append(item)
            self._table_titles[-1].append([])
        elif level == 4:
            self._table_titles[-1][-1].append(item)
            self._table_titles[-1][-1].append([])
        elif level == 5:
            self._table_titles[-1][-1][-1].append(item)
            self._table_titles[-1][-1][-1].append([])
        elif level == 6:
            self._table_titles[-1][-1][-1][-1].append(item)

    def new_table_of_contents(self):
        """ Add a table of contents of the Header Levels 2, 3 and 4."""
        table = TableOfContents().create_table_of_contents(self._table_titles)
        self.markdown_file.append_after_first_line(table)


if __name__ == '__main__':
    heeader = Header()
