# Python
#
# This module implements the Main Markdown class.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll

"""Module **mdutils**

The available features are:
    * Create Headers, Til 6 sub-levels.
    * Auto generate a table of contents.
    * Create List and sub-list.
    * Create paragraph.
    * Generate tables of different sizes.
    * Insert Links.
    * Insert Code.
    * Place text anywhere using a marker.
"""
from mdutils.fileutils.fileutils import MarkDownFile
from mdutils.tools import tools


class MdUtils:
    """This class give some basic methods that helps the creation of Markdown files while you are executing a python
    code.

    The ``__init__`` variables are:

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
        :type file_name: str
        :param title: it is the title of the Markdown file. It is written with Setext-style.
        :type title: str
        :param author: it is the author fo the Markdown file.
        :type author: str
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
        :return: return an instance of a MarkDownFile."""
        md_file = MarkDownFile(self.file_name)
        md_file.rewrite_all_file(data=self.title + self.table_of_contents + self.file_data_text)
        return md_file

    def read_md_file(self, file_name):
        """Reads a Markdown file and save it to global class `file_data_text`.

        :param file_name: Markdown file's name that has to be read.
        :type file_name: str
        :return: optionally returns the file data content.
        :rtype: str
        """
        file_data = MarkDownFile().read_file(file_name)
        self.file_data_text += file_data

        return file_data

    def new_header(self, level, title, style='atx'):
        """ Add a new header to the Markdown file.

        :param level: Header level. *atx* style can take values 1 til 6 and *setext* style take values 1 and 2.
        :type level: int
        :param title: Header title.
        :type title: str
        :param style: Header style, can be ``'atx'`` or ``'setext'``. By default ``'atx'`` style is chosen.
        :type style: str


        The example below consist in creating two types Headers examples:

        :Example:
        >>> mdfile = MdUtils("Header_Example")
        >>> print(mdfile.new_header(level=2, title='Header Level 2 Title', style='atx'))
        '\\n## Header Level 2 Title\\n'
        >>> print(mdfile.new_header(level=2, title='Header Title', style='setext'))
        '\\nHeader Title\\n-------------\\n'

        The previous example generates a markdown file with the following content:

        Header Level 2 Title
        --------------------

        Header Title
        ------------
        """

        self._add_new_item_table_of_content(level, title)
        self.file_data_text += self.header.choose_header(level, title, style)
        return self.header.choose_header(level, title, style)

    def _add_new_item_table_of_content(self, level, item):
        """Automatically add new atx headers to the table of contents.

        :param level: add til 2 levels. Only can take 1 or 2.
        :type level: int
        :param item: items to add.
        :type item: list or str
        """
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
        If no marker is defined, the table of contents will be placed automatically after the file's title.

        :param table_title: The table content's title, by default "Table of contents"
        :type table_title: str
        :param depth: allows to include Headers 1 and 2 or only Headers of level 1. Possible values 1 or 2.
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

    def new_table(self, columns, rows, text, text_align='center', marker=''):
        """This method takes a list of strings and creates a table.

            Using arguments ``columns`` and ``rows`` allows to create a table of *n* columns and *m* rows. The
            ``columns * rows`` operations has to correspond to the number of elements of ``text`` list argument.
            Moreover, ``argument`` allows to place the table wherever you want from the file.

        :param columns: this variable defines how many columns will have the table.
        :type columns: int
        :param rows: this variable defines how many rows will have the table.
        :type rows: int
        :param text: it is a list containing all the strings which will be placed in the table.
        :type text: list
        :param text_align: allows to align all the cells to the ``'right'``, ``'left'`` or ``'center'``.
                            By default: ``'center'``.
        :type text_align: str
        :param marker: using ``create_marker`` method can place the table anywhere of the markdown file.
        :type marker: str
        :return: can return the table created as a string.
        :rtype: str

        :Example:
        >>> from mdutils.tools.tools import Table
        >>> text_list = ['List of Items', 'Description', 'Result', 'Item 1', 'Description of item 1', '10', 'Item 2', 'Description of item 2', '0']
        >>> table = Table().new_table(columns=3, rows=3, text=text_list, text_align='center')
        >>> print(repr(table))
        '\\n|List of Items|Description|Result|\\n| :---: | :---: | :---: |\\n|Item 1|Description of item 1|10|\\n|Item 2|Description of item 2|0|\\n'


            .. csv-table:: **Table result on Markdown**
               :header: "List of Items", "Description", "Results"

               "Item 1", "Description of Item 1", 10
               "Item 2", "Description of Item 2", 0
        """

        new_table = tools.Table()
        text_table = new_table.create_table(columns, rows, text, text_align)
        if marker:
            self.file_data_text = self.place_text_using_marker(text_table, marker)
        else:
            self.file_data_text += text_table

        return text_table

    def new_paragraph(self, text='', bold_italics_code='', color='black', align=''):
        """Add a new paragraph to Markdown file. The text is saved to the global variable file_data_text.

        :param text: is a string containing the paragraph text. Optionally, the paragraph text is returned.
        :type text: str
        :param bold_italics_code: bold_italics_code: using ``'b'``: **bold**, ``'i'``: *italics* and
                                    ``'c'``: ``inline_code``.
        :type bold_italics_code: str
        :param color: Can change text color. For example: ``'red'``, ``'green'``, ``'orange'``...
        :type color: str
        :param align: Using this parameter you can align text.
        :type align: str
        :return:  ``'\\n\\n' + text``. Not necessary to take it, if only has to be written to
                    the file.
        :rtype: str
        """

        if bold_italics_code or color != 'black' or align:
            self.file_data_text += '\n\n' + self.textUtils.text_format(text, bold_italics_code, color, align)
        else:
            self.file_data_text += '\n\n' + text

        return self.file_data_text

    def new_line(self, text='', bold_italics_code='', color='black', align=''):
        """Add a new line to Markdown file. The text is saved to the global variable file_data_text.

        :param text: is a string containing the paragraph text. Optionally, the paragraph text is returned.
        :type text: str
        :param bold_italics_code: bold_italics_code: using ``'b'``: **bold**, ``'i'``: *italics* and
                                    ``'c'``: ``inline_code``..
        :type bold_italics_code: str
        :param color: Can change text color. For example: ``'red'``, ``'green'``, ``'orange'``...
        :type color: str
        :param align: Using this parameter you can align text.
        :type align: str
        :return: return a string ``'\\n' + text + '\\n'``. Not necessary to take it, if only has to be written to the
                    file.
        :rtype: str
        """

        if bold_italics_code or color != 'black' or align:
            self.file_data_text += self.textUtils.text_format(text, bold_italics_code, color, align) + '  \n'
        else:
            self.file_data_text += text + '  \n'

        return self.file_data_text

    def write(self, text=''):
        """Write text in ``file_Data_text`` string.

        :param text: a text a string.
        :type text: str
        """

        self.file_data_text += text

    def create_marker(self, text_marker):
        """This will add a marker to ``file_data_text`` and returns the marker result in order to be used whenever
            you need.

            Markers allows to place them to the string data text and they can be replaced by a peace of text using
            ``place_text_using_marker`` method.

        :param text_marker: marker name.
        :type text_marker: str
        :return: return a marker of the following form: ``'##--[' + text_marker + ']--##'``
        :rtype: str
        """

        new_marker = '##--[' + text_marker + ']--##'
        self.file_data_text += new_marker
        return new_marker

    def place_text_using_marker(self, text, marker):
        """It replace a previous marker created with ``create_marker`` with a text string.

            This method is going to search for the ``marker`` argument, which has been created previously using
            ``create_marker`` method, in ``file_data_text`` string.

        :param text: the new string that will replace the marker.
        :type text: str
        :param marker: the marker that has to be replaced.
        :type marker: str
        :return: return a new file_data_text with the replace marker.
        :rtype: str
        """
        return self.file_data_text.replace(marker, text)
