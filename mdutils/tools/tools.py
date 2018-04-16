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
        return '\n# ' + title + '\n'

    @staticmethod
    def atx_level_2(title):
        return '\n## ' + title + '\n'

    @staticmethod
    def atx_level_3(title):
        return '\n### ' + title + '\n'

    @staticmethod
    def atx_level_4(title):
        return '\n#### ' + title + '\n'

    @staticmethod
    def atx_level_5(title):
        return '\n##### ' + title + '\n'

    @staticmethod
    def atx_level_6(title):
        return '\n###### ' + title + '\n'

    # ********************************************************************
    # *                          Setext-Style                            *
    # ********************************************************************
    @staticmethod
    def setext_level_1(title):
        return '\n' + title + '\n' + ''.join(['=' for _ in title]) + '\n'

    @staticmethod
    def setext_level_2(title):
        return '\n' + title + '\n' + ''.join(['-' for _ in title]) + '\n'

    @staticmethod
    def header_anchor(text, link=""):
        """Creates an internal link of a defined Header level 1 or level 2 in the markdown file.

        Giving a text string an text link you can create an internal link of already existing header. If the ``link``
        string does not contain '#', it will creates an automatic link of the type ``#title-1``.

        :param text: it is the text that will be displayed.
        :param link: it is the internal link.
        :return: ``'[text](#link)'``
        :type text: str
        :type link: str
        :rtype: string

        **Example:** [Title 1](#title-1)
        """
        if link:
            if link[0] != '#':
                link = link.lower().replace(' ', '-')
            else:
                link = '#' + link
        else:
            link = '#' + text.lower().replace(' ', '-')

        return '[' + text + '](' + link + ')'

    def choose_header(self, level, title, style='atx'):
        # noinspection SpellCheckingInspection
        """ This method choose the style and the header level.

                    :Examples:
                    >>> from mdutils.tools.tools import Header
                    >>> createHeaders = Header()
                    >>> createHeaders.choose_header(level=1, title='New Header', style='atx')
                    '\n# New Header\n'

                    >>> createHeaders.choose_header(level=2, title='Another Header 1', style='setext')
                    '\nAnother Header 1\n----------------\n'

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
        """Method that go through a list of elements that contain strings and other list and return a string.

        The returned string is ready to be written inside a markdown file in order to create a table of contents.

        :param elements: contain all the headers defined on the main class.
        :param tab: Inserts tabulations.
        :type elements: list
        :type tab: str
        :rtype: str
        """
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
        table_of_contents += '\n'

        return table_of_contents


class Table(object):

    def __init__(self):
        self.rows = 0
        self.columns = 0

    @staticmethod
    def _align(columns, text_align):
        """ This private method it is in charfe of aligning text of a table.

        - notes: more information about `text_align`

        :param columns: it is the number of columns.
        :param text_align: it is a string giving information about the alignment that is wanted.  text_align can take
                           the following parameters: ``'center'``, ``'right'`` and ``'left'``.
        :return: returns a string of type ``'| :---: | :---: | :---: |'``.
        :type columns: int
        :type text_align: str
        :rtype: str

        .. note:
        """

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
        table = '\n'
        column_align_string = self._align(columns, text_align)
        index = 0
        for r in range(rows + 2):
            if r == 1:
                table += column_align_string                    # Row align, Example: '| :---: | :---: | ... | \n'
            else:
                table += '|'
                for c in range(columns):
                    table += text[index] + '|'
                    index += 1

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
        """Using this method can change text color.

        :param text: it is the text that will be changed its color.
        :param color: it is the text color: ``'orange'``, ``'blue'``, ``'red'``...
        :return: ``'<font color='color'> 'text' </font>'``
        :type text: str
        :type color: str
        :rtype: string
        """

        return '<font color="' + color + '"> ' + text + ' </font>'

    @staticmethod
    def text_external_link(text, link=''):
        """ Using this method can be created an external link of a file or a web page.

        :param text: Text to be displayed.
        :type text: str
        :param link: External Link.
        :type link: str
        :return: return a string like this: ``'[Text to be shown](https://write.link.com)'``
        :rtype: str"""

        return '[' + text + '](' + link + ')'

    def text_format(self, text, bold_italics_code='', color='black'):
        """Text format helps to write multiple text format such as bold, italics and color.

        :param text: it is a string in which will be added the mew format
        :param bold_italics_code: using `'b'`: **bold**, `'i'`: _italics_ and `'c'`: `inline_code`.
        :param color: Can change text color. For example: 'red', 'green, 'orange'...
        :return: return a string with the new text format.
        :type text: str
        :type bold_italics_code: str
        :type color: str

        :Example:

        >>> from mdutils.tools import tools.TextUtils
        >>> textUtils = TextUtils()
        >>> textUtils.text_format(text='Some Text Here', bold_italics_code='bi', color='red')
        '_**<font color='red'> Some Text Here </font>**_'
        """
        if color != 'black':
            new_text_format = self.text_color(text, color)
        else:
            new_text_format = text

        if bold_italics_code:
            for i in range(len(bold_italics_code)):
                char = bold_italics_code[i]
                if char == 'b':
                    new_text_format = self.bold(new_text_format)
                elif char == 'c':
                    new_text_format = self.inline_code(new_text_format)
                elif char == 'i':
                    new_text_format = self.italics(new_text_format)

        return new_text_format

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
