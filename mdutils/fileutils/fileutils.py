# Python
#
# This module implements a main class that allows to create markdown files, write in them or read.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# (C) 2018 Dídac Coll
#
# SPDX-License-Identifier:   BSD-3-Clause


class NewFile(object):
    """NewFile class creates a new file of MarkDown extension.

    Features available are:
    - Create a file.
    - Rewrite all the file with new data.
    - Write at the end of the file."""

    def __init__(self, name):
        self.file_name = name + '.md'
        self.file = open(self.file_name, 'w+', encoding='UTF-8')
        self.file.close()

    def rewrite_all_file(self, data):
        """Rewrite all the data of a Markdown file by ``data``.

        - **data:** is a string containing all the data that is written in the markdown file."""
        with open(self.file_name, 'w', encoding='utf-8') as self.file:
            self.file.write(data)

    def append_end(self, data):
        """Write at the last position of a Markdown file.

        - **data:** is a string."""
        with open(self.file_name, 'a') as self.file:
            self.file.write(data)


if __name__ == '__main__':
    new_file = NewFile('Example')
    new_file.rewrite_all_file(data="# Some Text Example")
