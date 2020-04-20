# Python
#
# This module implements a text class that allows to modify and create text on Markdown files.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2020 Dídac Coll


class Table:

    def __init__(self):
        self.rows = 0
        self.columns = 0

    @staticmethod
    def _align(columns, text_align):
        """ This private method it's in charge of aligning text of a table.

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
        """This method takes a list of strings and creates a table.

            Using arguments ``columns`` and ``rows`` allows to create a table of *n* columns and *m* rows.
            The ``columns * rows`` operations has to correspond to the number of elements of ``text`` list argument.

        :param int columns: number of columns of the table.
        :param int rows: number of rows of the table.
        :param text: a list of strings.
        :type text: list of str
        :param str text_align: text align argument. Values available are: ``'right'``, ``'center'``, and ``'left'``.
        :return: a markdown table.
        :rtype: str


        :Example:
        >>> from mdutils.tools.Table import Table
        >>> text_list = ['List of Items', 'Description', 'Result', 'Item 1', 'Description of item 1', '10', 'Item 2', 'Description of item 2', '0']
        >>> table = Table().create_table(columns=3, rows=3, text=text_list, text_align='center')
        >>> print(repr(table))
        '\\n|List of Items|Description|Result|\\n| :---: | :---: | :---: |\\n|Item 1|Description of item 1|10|\\n|Item 2|Description of item 2|0|\\n'


            .. csv-table:: **Table result on Markdown**
               :header: "List of Items", "Description", "Results"

               "Item 1", "Description of Item 1", 10
               "Item 2", "Description of Item 2", 0


        """
        self.columns = columns
        self.rows = rows
        table = '\n'
        column_align_string = self._align(columns, text_align)
        index = 0
        if columns * rows == len(text):
            if text_align.lower() in ('right', 'center', 'left'):
                for r in range(rows + 1):
                    if r == 1:
                        table += column_align_string  # Row align, Example: '| :---: | :---: | ... | \n'
                    else:
                        table += '|'
                        for c in range(columns):
                            table += text[index] + '|'
                            index += 1

                    table += '\n'

                return table

            else:
                raise ValueError("text_align's expected value: 'right', 'center' or 'left', but text_align = "
                                 + text_align.lower())
        else:
            raise ValueError("columns * rows is not equal to text length")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
