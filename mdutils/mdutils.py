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

    The different __init__ variables are:

    - **file_name:** it is the name of the Markdown file.
    - **author:** it is the author fo the Markdown file.
    - **header:** it is an instance of Header Class.
    - **textUtils:** it is an instance of TextUtils Class.
    - **title:** it is the title of the Markdown file. It is written with Setext-style.
    - **table_of_contents:** it is the table of contents, it can be optionally created.
    - **file_data_text:** contains all the file data that will be written on the markdown file.
    """

    def __init__(self, file_name, title="", author=""):
        """

        :param file_name: it is the name of the Markdown file.
        :param title: it is the title of the Markdown file. It is written with Setext-style.
        :param author: it is the author fo the Markdown file.
        """
        self.file_name = file_name
        self.author = author
        self.header = tools.Header()
        self.textUtils = tools.TextUtils()
        self.title = self.header.choose_header(level=1, title=title, style='setext')
        self.table_of_contents = ""
        self.file_data_text = ""
        self._table_titles = []

    def create_md_file(self):
        """It creates a new Markdown file.
        :return: return an instance of a NewFile."""
        md_file = NewFile(self.file_name)
        md_file.rewrite_all_file(data=self.title + self.table_of_contents + self.file_data_text)
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
        self.file_data_text += self.header.choose_header(level, title, style)
        return self.header.choose_header(level, title, style)

    def _add_new_item_table_of_content(self, level, item):
        if level == 1:
            self._table_titles.append(item)
            self._table_titles.append([])
        elif level == 2:
            self._table_titles[-1].append(item)
            self._table_titles[-1].append([])

    def new_table_of_contents(self, table_title="Table of contents", depth=1, marker=''):
        """Table of contents can be created if Headers of 'atx' style have been defined.

        This method allows to create a table of contents and define a title for it. Moreover, `depth` allows user to
        define if headers of level 1 and 2 or only level 1 have to be placed on the table of contents.

        :param table_title: The table content's title, by default "Table of contents"
        :type table_title: str
        :param depth: allows to include Headers 1 and 2 or only Headers of level 1. Possibly values 1 or 2.
        :type depth: int
        :param marker: allows to place the table of contents using a marker.
        :type marker: str
        :return: a string with the data is returned.
        :rtype: str
        """

        if marker:
            self.table_of_contents = ""
            marker_table_of_contents = self.header.choose_header(level=1, title=table_title, style='setext')
            marker_table_of_contents += tools.TableOfContents().create_table_of_contents(self._table_titles, depth)
            self.file_data_text = self.place_text_using_marker(marker_table_of_contents, marker)
        else:
            marker_table_of_contents = ""
            self.table_of_contents += self.header.choose_header(level=1, title=table_title, style='setext')
            self.table_of_contents += tools.TableOfContents().create_table_of_contents(self._table_titles, depth)

        return self.table_of_contents + marker_table_of_contents

    def create_table(self, columns, rows, text, text_align='center', marker=''):
        new_table = tools.Table()
        text_table = new_table.create_table(columns, rows, text, text_align)
        if marker:
            self.file_data_text = self.place_text_using_marker(text_table, marker)
        else:
            self.file_data_text += text_table

        return text_table

    def add_new_paragraph(self, text='', bold_italics_code='', color='black', align=''):
        """ Add a new paragraph to Markdown file. The text is saved to the global class variable file_data_text.

        :param text: is a string containing the paragraph text. Optionally, the paragraph text is returned.
        :type text: str
        :param bold_italics_code: bold_italics_code: using `'b'`: **bold**, `'i'`: _italics_ and `'c'`: `inline_code`.
        :type bold_italics_code: str
        :param color: Can change text color. For example: 'red', 'green, 'orange'...
        :type color: str
        :param align: Using this parameter you can align text.
        :type align: str
        :return: return a string '\n' + text + '\n'. Not necessary to take it, if only has to be written to the file.
        """
        if bold_italics_code or color != 'black' or align:
            self.file_data_text += '\n\n' + self.textUtils.text_format(text, bold_italics_code, color, align)
        else:
            self.file_data_text += '\n\n' + text

        return self.file_data_text

    def create_marker(self, text_marker):
        """This will add a marker to file_data_text in order to add after some text.

        :param text_marker: marker name.
        :type text_marker: str
        :return return the marker.
        :rtype: str
        """

        new_marker = '##--[' + text_marker + ']--##'
        self.file_data_text += new_marker
        return new_marker

    def place_text_using_marker(self, text, marker):
        """It replace a previous marker created with ``create_marker`` with a text string.

        :param text: the new string that will replace the marker.
        :type text: str
        :param marker: the marker that has to be replaced.
        :type marker: str
        :return: return a new file_data_text with the replace marker.
        :rtype: str
        """
        return self.file_data_text.replace(marker, text)


if __name__ == '__main__':
    header = tools.Header()
