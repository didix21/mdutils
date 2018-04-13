# Python
#
# This module implements a text class that allows to modify and create text on Markdown files.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# (C) 2018 Dídac Coll
#
# SPDX-License-Identifier:   BSD-3-Clause


# noinspection SpellCheckingInspection
class Header(object):
    """Contain the main methods to define Headers on a Markdown file.

    """

    # ********************************************************************
    # *                             Atx-Style                            *
    # ********************************************************************
    @staticmethod
    def atx_level_1(title):
        return '\n\n# ' + title

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
        # noinspection SpellCheckingInspection
        """ This method choose the style and the header level.

                    :Examples:
                    >>> from mdutils.tools.tools import Header
                    >>> createHeaders = Header()
                    >>> createHeaders.choose_header(level=1, title='New Header', style='atx')
                    "# New Header"

                    >>> createHeaders.choose_header(level=1, title='Another Header 1', style='setext')
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
    def _loop_through(self, elements, tab=''):
        """Method that go trough a list of elements that contain strings and other list and return a string \
        reade to be written inside a markdown file in order to create a table of contents.

        - **elements**: contain all the headers defined on the main class.
        - **tab:** Inserts tabulations."""
        elements_to_string = ""
        for item in elements:
            if isinstance(item, list):
                if item:
                    if tab == '\t':
                        elements_to_string += self._loop_through(item, tab='\t\t')
                    else:
                        elements_to_string += self._loop_through(item, tab='\t')
            else:
                elements_to_string += '\n' + tab + '* [' + item + '](#' + item.lower().replace(' ', '-') + ')'

        return elements_to_string

    def create_table_of_contents(self, array_of_title_contents):
        table_of_contents = ""
        table_of_contents += self._loop_through(array_of_title_contents)

        return table_of_contents


class Table(object):

    def __init__(self):
        self.rows = 0
        self.columns = 0

    @staticmethod
    def _align(columns, text_align):

        column_align_string = ''

        if text_align == 'center':

            column_align_string = '|' + ''.join([' :---: |' for _ in range(columns)])

        elif text_align == 'left':

            column_align_string = '|' + ''.join([' :--- |' for _ in range(columns)])

        elif text_align == 'right':

            column_align_string = '|' + ''.join([' ---: |' for _ in range(columns)])

        return column_align_string

    def create_table(self, columns, rows, text, text_align='center'):
        self.columns = columns
        self.rows = rows
        table = ''
        column_align_string = self._align(columns, text_align)
        n_row = 0                                               # New Row, its value is 1 when is set row align
        for r in range(rows):
            if r == 1:
                table += column_align_string                    # Row align, Example: '| :---: | :---: | ... | \n'
                n_row = 1
            else:
                table += '|' + ''.join([text[c + r + n_row] + '|' for c in range(columns)])
            table += '\n'

        return table


class TextUtils(object):
    """This class helps to create bold, italics and change color text.

    """

    @staticmethod
    def bold(text):
        return '**' + text + '**'

    @staticmethod
    def italics(text):
        return '_' + text + '_'

    @staticmethod
    def inline_code(text):
        return '`' + text + '`'

    @staticmethod
    def text_color(text, color="black"):
        return '<font color="' + color + '">' + text + '</font>'
